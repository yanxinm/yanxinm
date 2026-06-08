#!/usr/bin/env python3
"""source_verifier.py — mechanical URL classifier for Phase 4 quality gate.

Classifies URLs into 5 buckets based on domain + path heuristics:

  verified_primary  Authoritative one-hand source (arXiv / DOI / official docs /
                    repo root / standard body / author's own blog / govt site).
                    Eligible to anchor a mental model claim.
  secondary         Secondhand reportage / analysis / encyclopedia / general
                    tech news. Allowed but cannot solo-anchor a claim.
  reference         Pointer-only — stack overflow answers, GH issue comments,
                    HN / Reddit threads, single tweets. Allowed as supporting
                    pointer, not as evidence.
  blacklisted       Locale-specific banned sources (zh-CN: 知乎 / 公众号 / 百度百科 /
                    CSDN / 博客园; en: G2 / Capterra / Medium-farm patterns;
                    universal: PR-wire / AI-summary auto-content).
  dead              HTTP HEAD returns 4xx/5xx or domain doesn't resolve. Only
                    checked when --check-liveness is set; otherwise unknown
                    URLs default to "secondary".

Pure stdlib. macOS python3 out-of-the-box.

Usage:
  # Single URL — exit code mirrors classification (0=primary, 1=secondary,
  # 2=reference, 3=blacklisted, 4=dead, 5=error)
  python3 source_verifier.py classify https://arxiv.org/abs/2305.12345

  # Batch a research directory's .md files, output JSON map URL→classification
  python3 source_verifier.py scan --research-dir <skill_dir>/references/research/

  # With liveness check (slower, ~1 HEAD request per URL; respects timeout)
  python3 source_verifier.py scan --research-dir <path> --check-liveness

  # Optional locale narrows the blacklist applied (default: both en + zh-CN)
  python3 source_verifier.py classify <URL> --locale zh-CN
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Classification tables. Order matters — earlier rules take priority.
# Key principle: domains-only when possible, path patterns only when domain
# is mixed-quality (e.g. youtube.com — channel root vs random video).
# ---------------------------------------------------------------------------

VerifiedPrimary = "verified_primary"
Secondary = "secondary"
Reference = "reference"
Blacklisted = "blacklisted"
Dead = "dead"
SurrogatePrimary = "surrogate_primary"  # manifest-only; never returned by classifier
Unknown = "secondary"  # default fallback

# Buckets the URL classifier can return on its own (auto). Manifests may also
# declare `surrogate_primary` per the cold-deep-mode policy in
# prompts/research/_source_id_manifest.md, but it's never auto-assigned.
AUTO_BUCKETS: tuple[str, ...] = (
    VerifiedPrimary, Secondary, Reference, Blacklisted, Dead,
)
ALL_BUCKETS: tuple[str, ...] = AUTO_BUCKETS + (SurrogatePrimary,)

EXIT_CODES = {
    VerifiedPrimary: 0,
    Secondary: 1,
    Reference: 2,
    Blacklisted: 3,
    Dead: 4,
}

# Domains that are blanket verified_primary regardless of path.
# Academic, standard bodies, government, journal publishers, well-known
# canonical channels.
PRIMARY_DOMAINS_EXACT: set[str] = {
    "arxiv.org",
    "doi.org",
    "ieeexplore.ieee.org",
    "dl.acm.org",
    "www.nature.com",
    "www.science.org",
    "www.cell.com",
    "www.thelancet.com",
    "www.nejm.org",
    "openreview.net",
    "papers.nips.cc",
    "papers.neurips.cc",
    "proceedings.mlr.press",
    "www.w3.org",
    "datatracker.ietf.org",
    "www.rfc-editor.org",
    "www.ietf.org",
    "www.iso.org",
    "www.iec.ch",
    "standards.ieee.org",
    "spec.commonmark.org",
    "www.unicode.org",
    "tc39.es",
    "schema.org",
    "developer.mozilla.org",
    "docs.python.org",
    "go.dev",
    "rust-lang.org",
    "kubernetes.io",
    "pytorch.org",
    "www.tensorflow.org",
    "huggingface.co",
    "platform.openai.com",
    "docs.anthropic.com",
    "ai.google.dev",
    "neurips.cc",
    "icml.cc",
    "iclr.cc",
    "aclanthology.org",
    "kubecon.io",
    "aaos.org",
    "aofas.org",
    "www.aofas.org",
    "www.aaos.org",
    "www.npc.gov.cn",  # 全国人大 — 立法源
    "www.court.gov.cn",  # 最高法
    "www.spp.gov.cn",  # 最高检
    "www.gov.cn",  # 中国政府门户
    "scholar.google.com",
    "semanticscholar.org",
    # Iter 26: industry standards bodies (insurance / finance) — referenced as
    # canonical sources by master-skill insurance-broker-cn run.
    "www.mdrt.org",
    "mdrt.org",
    "www.lloyds.com",
    "lloyds.com",
    "www.iso20022.org",  # finance messaging standard
    "www.bis.org",       # Bank for International Settlements
    "www.imf.org",
    "www.worldbank.org",
    # Iter 27: Chinese classics digital archives — canonical text ground truth
    # for any zh-CN classics-heavy industry (bazi-metaphysics, china-law historical
    # canon, traditional Chinese medicine, etc.).
    "ctext.org",                  # Chinese Text Project — 古籍数字化主源
    "www.guoxuedashi.net",        # 国学大师 — 综合古籍数据库
    "zh.wikisource.org",          # 中文维基文库 — 公共领域古籍
    "archive.org",                # Internet Archive — 民国整理本 PDF / 长内容档案
    "www.archive.org",
}

# Suffix patterns for primary (TLD or sub-domain end-match).
PRIMARY_DOMAIN_SUFFIXES: tuple[str, ...] = (
    ".gov",
    ".gov.cn",
    ".gov.uk",
    ".gov.hk",
    ".gov.tw",
    ".gov.jp",
    ".gov.kr",
    ".edu",
    ".edu.cn",
    ".ac.uk",
    ".ac.jp",
    ".mil",
    ".int",
    ".org.cn",  # 行业协会
    ".chinalaw.gov.cn",
)

# Known author / podcast / personal blog primaries (heuristic).
# This list is non-exhaustive — agent can extend per industry research.
PRIMARY_PERSONAL_DOMAINS: set[str] = {
    "lexfridman.com",
    "latent.space",
    "www.latent.space",
    "swyx.io",
    "simonwillison.net",
    "karpathy.ai",
    "magazine.sebastianraschka.com",
    "rachelbythebay.com",
    "danluu.com",
    "stratechery.com",
    "mattturck.com",
    "blog.replit.com",
    "anthropic.com",
    "openai.com",
    "deepmind.com",
    "deepmind.google",
}

# Substack / Beehiiv-hosted newsletters: primary IF subdomain looks like an
# author/publication name (i.e., not "www" / "help" / "discover").
NEWSLETTER_HOSTS: tuple[str, ...] = (
    "substack.com",
    "beehiiv.com",
    "ghost.io",
    "convertkit.com",
)

# zh-CN newsletter / podcast platforms (channel listings allowed; reference
# for individual posts).
ZH_NEWSLETTER_HOSTS: set[str] = {
    "xiaoyuzhoufm.com",  # 小宇宙
    "www.xiaoyuzhoufm.com",
    "podcasts.apple.com",
    "open.spotify.com",
    "music.apple.com",
}

# Repo / code hosts: github.com/{org}/{repo} root → primary. github.com/{...}/issues/N → reference.
REPO_HOSTS: set[str] = {
    "github.com",
    "gitlab.com",
    "bitbucket.org",
    "codeberg.org",
    "gitee.com",
}

# ---------------------------------------------------------------------------
# Blacklists (locale-specific)
# ---------------------------------------------------------------------------

BLACKLIST_ZH_EXACT: set[str] = {
    "www.zhihu.com",
    "zhihu.com",
    "zhuanlan.zhihu.com",
    "baike.baidu.com",
    "wenku.baidu.com",
    "jingyan.baidu.com",
    "blog.csdn.net",
    "www.csdn.net",
    "blog.51cto.com",
    "www.cnblogs.com",
    "www.jianshu.com",
    "juejin.cn",  # 掘金 — 部分原创但 SEO 农场化
    "developer.aliyun.com",  # 阿里云开发者社区 — 多为厂商 PR
    "tencent.cloud.com",
}

# 公众号 mp.weixin.qq.com: blacklisted as evidence (cannot cite content),
# but the WeChat *channel* itself is allowed in Track 05 source listings.
# We classify URL = blacklisted; agents that maintain Track 05 channel lists
# should override / annotate via meta when the URL is the channel root.
BLACKLIST_ZH_PATTERNS: tuple[str, ...] = (
    "mp.weixin.qq.com",  # 微信公众号文章
)

BLACKLIST_EN_EXACT: set[str] = {
    "www.g2.com",
    "g2.com",
    "www.capterra.com",
    "capterra.com",
    "www.gartner.com",
    "www.forrester.com",
    "www.softwareadvice.com",
    "www.trustradius.com",
    "www.businesswire.com",  # PR newswire
    "www.prnewswire.com",
    "www.globenewswire.com",
    "www.einnews.com",
}

# Medium / dev.to: hard to classify without author check. We mark as
# secondary by default; classify path /@{author}/ as secondary; specific
# known SEO-farm subdomains as blacklisted.
MEDIUM_FARM_SUBDOMAINS: set[str] = {
    "javascript.plainenglish.io",
    "betterprogramming.pub",
    "levelup.gitconnected.com",
}

# Reference-tier: forum / Q&A / aggregator hosts where typical URL is a single
# answer / comment / thread, not authoritative.
REFERENCE_DOMAINS: set[str] = {
    "stackoverflow.com",
    "superuser.com",
    "serverfault.com",
    "askubuntu.com",
    "stackexchange.com",
    "news.ycombinator.com",
    "www.reddit.com",
    "old.reddit.com",
    "twitter.com",
    "x.com",
    "mobile.twitter.com",
    "t.co",
    "v2ex.com",
    "tieba.baidu.com",
    "www.douban.com",
    "movie.douban.com",
}

SECONDARY_DOMAINS_EXACT: set[str] = {
    "en.wikipedia.org",
    "zh.wikipedia.org",
    "www.wikipedia.org",
    "en.wiktionary.org",
    "techcrunch.com",
    "www.theverge.com",
    "www.wired.com",
    "www.economist.com",
    "www.bloomberg.com",
    "www.ft.com",
    "www.nytimes.com",
    "www.wsj.com",
    "www.36kr.com",  # 36 氪 — 二手分析
    "36kr.com",
    "www.geekpark.net",
    "www.huxiu.com",
    "www.latepost.com",
    "www.caixin.com",
    "tech.sina.com.cn",
    "tech.qq.com",
    "tech.163.com",
    "www.ithome.com",
    "www.leiphone.com",
    "www.jiqizhixin.com",  # 机器之心 — 偏二手
    "medium.com",
    "dev.to",
    "hacker-news.firebaseapp.com",
}

# Canonical entity-reference hosts: pages of the form /subject/X, /album/Y,
# /book/Z, /podcast/N — these are the authoritative landing for a real-world
# entity (a book, a podcast, an album). Agents reasonably cite them as the
# primary URL for the entity even if the host itself isn't an "official source"
# in the traditional sense. Treated as verified_primary when path matches.
ENTITY_REFERENCE_HOSTS: dict[str, frozenset[str]] = {
    "book.douban.com": frozenset({"subject"}),
    "movie.douban.com": frozenset({"subject"}),
    "music.douban.com": frozenset({"subject"}),
    "www.douban.com": frozenset({"subject", "book", "movie", "music"}),
    "weread.qq.com": frozenset({"web", "bookDetail"}),  # 微信读书 book pages
    "www.ximalaya.com": frozenset({"album", "sound", "track"}),
    "ximalaya.com": frozenset({"album", "sound"}),
    "www.lizhi.fm": frozenset({"podcast"}),
    "www.acast.com": frozenset({"show"}),
    "podcasts.google.com": frozenset({"feed"}),
    "open.spotify.com": frozenset({"show", "episode"}),
}

# ---------------------------------------------------------------------------
# Core classifier
# ---------------------------------------------------------------------------


def _norm_host(url: str) -> tuple[str, str]:
    """Return (host, path) lowercased; strip default port + leading www only
    when host has no further label. e.g., www.foo.com stays as-is for matching
    in tables that include `www.`. Path is left urlencoded."""
    parsed = urllib.parse.urlsplit(url.strip())
    host = (parsed.hostname or "").lower()
    path = parsed.path or ""
    return host, path


def classify_url(url: str, locale: str = "all") -> tuple[str, str]:
    """Classify a single URL. Return (bucket, reason).

    locale:
      "all"   apply both zh-CN + en blacklists (default; safe over-rejecting)
      "zh-CN" zh-CN blacklist only
      "en"    en blacklist only
      "ja"/"ko"/... fall through to "all" (placeholder for future expansion)
    """
    if not url or not url.strip():
        return Secondary, "empty url"
    if not re.match(r"^https?://", url, re.IGNORECASE):
        return Reference, "non-http url (file? mailto?)"
    host, path = _norm_host(url)
    if not host:
        return Secondary, "no host parsed"

    # 1) Blacklists first — locale-narrow if asked, else apply both.
    apply_zh = locale in ("all", "zh-CN")
    apply_en = locale in ("all", "en")
    if apply_zh:
        if host in BLACKLIST_ZH_EXACT:
            return Blacklisted, f"zh-CN blacklist domain: {host}"
        for pat in BLACKLIST_ZH_PATTERNS:
            if pat in host:
                return Blacklisted, f"zh-CN blacklist pattern: {pat}"
    if apply_en:
        if host in BLACKLIST_EN_EXACT:
            return Blacklisted, f"en blacklist domain: {host}"
        if host in MEDIUM_FARM_SUBDOMAINS:
            return Blacklisted, f"en SEO-farm subdomain: {host}"

    # 2) Verified primary — explicit domain match.
    if host in PRIMARY_DOMAINS_EXACT:
        return VerifiedPrimary, f"primary domain (exact): {host}"
    for suffix in PRIMARY_DOMAIN_SUFFIXES:
        if host == suffix.lstrip(".") or host.endswith(suffix):
            return VerifiedPrimary, f"primary domain (suffix): {suffix}"
    if host in PRIMARY_PERSONAL_DOMAINS:
        return VerifiedPrimary, f"known personal/author primary: {host}"

    # 3) Repo hosts — root path / docs / releases → primary; issues/PRs → reference.
    if host in REPO_HOSTS:
        # github.com/{org}/{repo}     → primary (project root)
        # github.com/{org}/{repo}/...
        # github.com/{org}/{repo}/(issues|pull|discussions)/N → reference
        seg = [s for s in path.strip("/").split("/") if s]
        if len(seg) >= 3 and seg[2] in ("issues", "pull", "discussions"):
            return Reference, f"{host} thread/comment, not project root"
        if len(seg) >= 2:
            return VerifiedPrimary, f"{host} project root"
        return Secondary, f"{host} top-level / org page"

    # 4) Newsletter hosts (Substack/Beehiiv/Ghost/ConvertKit).
    for nh in NEWSLETTER_HOSTS:
        if host.endswith(nh):
            sub = host[: -len(nh)].rstrip(".")
            # Bare host (e.g. substack.com) → secondary marketing
            if not sub or sub.lower() in {"www", "help", "discover", "about"}:
                return Secondary, f"{host} root/marketing page"
            return VerifiedPrimary, f"newsletter author host: {sub}.{nh}"

    # 5) zh-CN podcast / 小宇宙 / Apple / Spotify — channel pages are primary,
    # episode play pages reference (single play vs the channel as a tracked source).
    if host in ZH_NEWSLETTER_HOSTS:
        seg_all = [s.lower() for s in path.strip("/").split("/") if s]
        if "episode" in seg_all:
            return Reference, f"{host} single episode link"
        if any(s in seg_all for s in ("podcast", "podcasts")):
            return VerifiedPrimary, f"{host} podcast channel"
        return Secondary, f"{host} unspecified path"

    # 6) Reference-tier hosts (forums / Q&A / aggregators / single tweets).
    if host in REFERENCE_DOMAINS:
        return Reference, f"forum/Q&A/aggregator: {host}"

    # 7) Wikipedia / general tech news → secondary.
    if host in SECONDARY_DOMAINS_EXACT:
        return Secondary, f"known secondary domain: {host}"

    # 7.5) Canonical entity-reference hosts (douban /subject, ximalaya /album, ...)
    # These hosts have authoritative pages for real-world entities (books, podcasts,
    # albums). Agents reasonably treat the entity-page URL as the primary citation.
    if host in ENTITY_REFERENCE_HOSTS:
        seg = [s for s in path.strip("/").split("/") if s]
        if seg and seg[0].lower() in ENTITY_REFERENCE_HOSTS[host]:
            return VerifiedPrimary, f"canonical entity reference: {host}/{seg[0]}/{seg[1] if len(seg) > 1 else ''}"
        return Secondary, f"{host} non-entity path"

    # Podcast platform fallthrough (xyzfm.space hosts independent podcasts via feeds)
    if host == "feed.xyzfm.space" or host.endswith(".xyzfm.space"):
        return VerifiedPrimary, "xyzfm podcast feed root"

    # 8) Heuristic: subdomain "blog.{company}" / "engineering.{company}" /
    # "research.{company}" / "tech.{company}" — primary when company has its
    # own .com / .io / .ai domain. Captures "blog.replit.com" etc that aren't
    # in the static list.
    if re.match(r"^(blog|engineering|research|labs?|tech|developers?|docs)\.", host):
        return VerifiedPrimary, f"engineering/blog subdomain heuristic: {host}"

    # 9) YouTube channel paths.
    if host in ("www.youtube.com", "youtube.com", "m.youtube.com"):
        seg = [s for s in path.strip("/").split("/") if s]
        if seg and (seg[0] in ("c", "channel", "user") or seg[0].startswith("@")):
            return VerifiedPrimary, f"youtube channel root: /{seg[0]}"
        return Reference, "youtube generic page"

    # 10) Content-publishing path on an unknown domain.
    # Conservative rule (iter 25 — codex P0 audit): only paths that are
    # *unambiguous* content publishing (`/podcast`, `/blog`, `/post`, `/author`,
    # `/events`, `/newsletter`) on a not-yet-seen domain are promoted to
    # verified_primary. Bare-host roots (`https://example.com/`) and
    # generic-slug articles (`https://random.com/some-cool-article`) used
    # to also be auto-promoted, which made `verified_primary` rubber-stamp
    # SEO-farm reposts. Default for those is now `secondary` — promote them
    # by adding the host to PRIMARY_DOMAINS_EXACT or PRIMARY_PERSONAL_DOMAINS
    # (allowlist), or by writing the manifest entry by hand with a reason.
    seg = [s for s in path.strip("/").split("/") if s]
    content_segments = {
        "podcast", "podcasts", "episodes", "episode",
        "blog", "blogs", "post", "posts",
        "author", "authors", "writers",
        "events", "event", "newsletter", "newsletters",
        "research", "papers", "case-studies", "casestudies",
        "talks", "writing", "essays", "notes",
        # Iter 26: corporate "about" / "team" / "leadership" pages — authoritative
        # description of the entity itself (vendor / agency / partner).
        "about", "team", "leadership", "officers",
        "products",  # vendor product pages — primary for THAT product (not generic admin)
    }
    admin_segments = {
        # iter 26: removed "products"/"product" — vendor product pages are
        # authoritative descriptions of the vendor's own product (helium10/podcast,
        # dt.com.cn/baoxianjia). Primary, not admin.
        "pricing", "buy", "shop", "cart",
        "login", "signup", "signin", "support", "help",
        "privacy", "terms", "legal",
        "contact", "careers", "jobs",
    }
    if seg:
        if seg[0].lower() in admin_segments:
            return Secondary, f"brand-domain admin path: /{seg[0]}"
        if any(s.lower() in content_segments for s in seg):
            return VerifiedPrimary, f"brand-domain content path: /{seg[0]}"

    # 11) Default: secondary. Primary requires either an allowlisted domain,
    # the engineering/blog subdomain heuristic, the YouTube/Apple-Podcast
    # channel heuristic, or an explicit content path (handled above). Bare
    # hosts and slug-style article URLs are *not* enough by themselves —
    # they need a manual manifest entry with a reason.
    return Secondary, f"unknown host (default secondary): {host}"


# ---------------------------------------------------------------------------
# Liveness check (optional, slow)
# ---------------------------------------------------------------------------


def check_liveness(url: str, timeout: float = 5.0) -> tuple[bool, int | None, str]:
    """HEAD the URL; return (alive, status_code, reason). Treats 4xx/5xx as
    dead, 2xx/3xx as alive. Falls back to GET (range bytes=0-0) if the host
    rejects HEAD with 405."""
    try:
        req = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": "master-skill-source-verifier/1.0"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            code = resp.status
            return (200 <= code < 400), code, f"HEAD {code}"
    except urllib.error.HTTPError as e:
        if e.code == 405:
            # HEAD not allowed; try GET with byte range so we don't pull body
            try:
                req = urllib.request.Request(
                    url,
                    headers={
                        "User-Agent": "master-skill-source-verifier/1.0",
                        "Range": "bytes=0-0",
                    },
                )
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    code = resp.status
                    return (200 <= code < 400), code, f"GET-range {code}"
            except Exception as e2:
                return False, getattr(e2, "code", None), f"GET-range failed: {type(e2).__name__}"
        return False, e.code, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        return False, None, f"URLError: {e.reason}"
    except Exception as e:
        return False, None, f"{type(e).__name__}: {e}"


# ---------------------------------------------------------------------------
# Batch scan
# ---------------------------------------------------------------------------

# Pull every http(s) URL out of markdown — covers `[text](url)`, `<url>`, and
# bare `https://...` forms. Trailing punctuation is stripped.
URL_RE = re.compile(r"https?://[^\s<>\)\]'\"`]+", re.IGNORECASE)


def extract_urls(text: str) -> list[str]:
    raw = URL_RE.findall(text)
    out: list[str] = []
    seen: set[str] = set()
    for u in raw:
        u = u.rstrip(".,;:!?'\")")
        if u and u not in seen:
            seen.add(u)
            out.append(u)
    return out


def scan_dir(
    research_dir: Path,
    locale: str = "all",
    check_live: bool = False,
) -> dict[str, Any]:
    """Walk *.md under research_dir, classify every URL, return aggregate dict."""
    if not research_dir.exists():
        raise FileNotFoundError(f"research dir not found: {research_dir}")
    files = sorted(research_dir.rglob("*.md"))
    by_url: dict[str, dict[str, Any]] = {}
    counts: dict[str, int] = {b: 0 for b in EXIT_CODES.keys()}
    counts.setdefault("dead", 0)
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        for u in extract_urls(text):
            if u in by_url:
                # Already classified; just record file
                by_url[u]["files"].append(str(f.relative_to(research_dir)))
                continue
            bucket, reason = classify_url(u, locale=locale)
            entry: dict[str, Any] = {
                "bucket": bucket,
                "reason": reason,
                "files": [str(f.relative_to(research_dir))],
            }
            if check_live and bucket != Blacklisted:
                alive, code, lreason = check_liveness(u)
                entry["live"] = alive
                entry["http_status"] = code
                entry["live_reason"] = lreason
                if not alive:
                    entry["bucket"] = Dead
                    entry["reason"] = f"liveness: {lreason}"
                    bucket = Dead
            counts[bucket] = counts.get(bucket, 0) + 1
            by_url[u] = entry
    total = sum(counts.values())
    primary_ratio = counts.get(VerifiedPrimary, 0) / total if total else 0.0
    return {
        "research_dir": str(research_dir),
        "locale": locale,
        "total_urls": total,
        "counts": counts,
        "verified_primary_ratio": round(primary_ratio, 4),
        "urls": by_url,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def cmd_classify(args: argparse.Namespace) -> int:
    bucket, reason = classify_url(args.url, locale=args.locale)
    if args.json:
        print(json.dumps({"url": args.url, "bucket": bucket, "reason": reason}))
    else:
        print(f"{bucket}\t{reason}\t{args.url}")
    if args.check_liveness and bucket != Blacklisted:
        alive, code, lreason = check_liveness(args.url)
        print(f"liveness: alive={alive} status={code} reason={lreason}", file=sys.stderr)
        if not alive:
            return EXIT_CODES[Dead]
    return EXIT_CODES.get(bucket, 1)


def cmd_scan(args: argparse.Namespace) -> int:
    report = scan_dir(args.research_dir, locale=args.locale, check_live=args.check_liveness)
    out: str
    if args.json:
        out = json.dumps(report, indent=2, ensure_ascii=False)
    else:
        out_lines: list[str] = [
            f"# source_verifier scan — {report['research_dir']}",
            "",
            f"locale: `{report['locale']}`  total: {report['total_urls']}",
            "",
            "counts:",
        ]
        for k, v in report["counts"].items():
            out_lines.append(f"  - {k}: {v}")
        out_lines.append("")
        out_lines.append(
            f"verified_primary_ratio: {report['verified_primary_ratio'] * 100:.1f}%"
        )
        out_lines.append("")
        out_lines.append("| bucket | url | reason |")
        out_lines.append("|--------|-----|--------|")
        for u, info in sorted(report["urls"].items(), key=lambda kv: kv[1]["bucket"]):
            out_lines.append(f"| {info['bucket']} | {u} | {info['reason']} |")
        out = "\n".join(out_lines)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(out, encoding="utf-8")
        print(f"wrote {args.output}", file=sys.stderr)
    else:
        print(out)

    # exit non-zero on hard violations:
    #   3 — at least one blacklisted source detected
    #   4 — at least one dead source detected (only meaningful with --check-liveness)
    #   1 — primary ratio under 0.5
    # Blacklist takes priority over dead because it's a content quality issue,
    # dead is fixable by URL update.
    if report["counts"].get(Blacklisted, 0) > 0:
        return 3
    if report["counts"].get(Dead, 0) > 0:
        return 4
    if report["verified_primary_ratio"] < 0.5:
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="source_verifier — classify URLs into 5 buckets for Phase 4 quality gate"
    )
    sub = p.add_subparsers(dest="action", required=True)

    pc = sub.add_parser("classify", help="classify a single URL")
    pc.add_argument("url")
    pc.add_argument("--locale", default="all", choices=["all", "zh-CN", "en", "ja", "ko"])
    pc.add_argument("--check-liveness", action="store_true",
                    help="HEAD the URL; flag dead links")
    pc.add_argument("--json", action="store_true")

    ps = sub.add_parser("scan", help="scan a research directory of markdown files")
    ps.add_argument("--research-dir", required=True, type=Path)
    ps.add_argument("--locale", default="all", choices=["all", "zh-CN", "en", "ja", "ko"])
    ps.add_argument("--check-liveness", action="store_true")
    ps.add_argument("--output", type=Path,
                    help="write scan report here (markdown or JSON per --json)")
    ps.add_argument("--json", action="store_true")

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.action == "classify":
        return cmd_classify(args)
    if args.action == "scan":
        return cmd_scan(args)
    return 99


if __name__ == "__main__":
    sys.exit(main())
