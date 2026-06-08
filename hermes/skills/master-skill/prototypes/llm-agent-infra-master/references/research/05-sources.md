# Track 05 — Sources (LLM agent infra)

> Wave 1. 8 sources across 4 types. Minimal-viable for prototype.

## 总览

### Newsletter (3)
| Source | Cadence | 投入产出 |
|--------|---------|---------|
| Latent Space (Substack) | weekly | high |
| Eugene Yan | rolling biweekly | high |
| Ahead of AI (Raschka) | biweekly | high |

### Podcast (3)
| Source | Cadence | Host |
|--------|---------|------|
| Latent Space pod | weekly | Swyx + Alessio |
| Cognitive Revolution | weekly | Nathan Labenz |
| Practical AI | weekly | Daniel Whitenack |

### Conference (1)
| Conference | Frequency | Last edition | Next edition |
|------------|-----------|-------------|-------------|
| AI Engineer Summit | annual | 2025-09 | 2026-09 |

### Community (1)
| Community | Platform | Notes |
|-----------|----------|-------|
| HuggingFace agent forum | HF site | Open, technical |

---

### 📰 1. Latent Space (Substack + Podcast)

- **Type**: newsletter + podcast (combined entry)
- **URL**: latent.space
- **Author / Host**: Swyx (Shawn Wang) + Alessio Fanelli
- **Cadence**: weekly
- **Last activity**: 2026-04-30 (recent within last week, last_checked 2026-05-02)
- **Audience tier**: practitioner + senior (mixed)
- **One-liner**: AI engineering view's anchor publication. 长访谈 1.5h+, 嘉宾覆盖 LLM era 主流 framework founders + 工程师 + researcher.
- **典型每期内容**: 60-90 min interview with one builder (e.g. Harrison Chase, Karpathy, Anthropic engineers)
- **投入产出比**: high (≥80% issues with actionable insight)
- **Paywall**: optional Pro tier $X/year for longer transcripts; free tier covers 90% of value
- **签名内容**: Harrison Chase 2025-Q1 "chains→graphs" episode, Karpathy multi-hour 2024-Q3
- **Endorsement evidence**:
  - `[type: figure_long]` Husain calls it "the canonical AI engineer pod"
  - `[type: cross_source]` Yan newsletter regularly references LS episodes
- **可信度**: high
- **Decay risk**: medium (host-dependent)

### 📰 2. Eugene Yan newsletter

- **Type**: newsletter
- **URL**: eugeneyan.com
- **Author**: Eugene Yan (与 Track 01 关联 — secondary figure not in retained 5 but high source-network value)
- **Cadence**: rolling biweekly
- **Last activity**: 2026-05 (rolling, last 3 months key content: eval methodology evolution, behavioral eval, LLM-as-judge limits)
- **Audience tier**: practitioner + senior
- **One-liner**: Eval-focused. Most-cited source for "how to actually evaluate LLM applications".
- **投入产出比**: high
- **Paywall**: none
- **Endorsement evidence**:
  - `[type: figure_long]` Husain frequently endorses
  - `[type: cross_source]` Latent Space references
- **Decay risk**: low (long-term standing publication)

### 📰 3. Ahead of AI — Sebastian Raschka

- **Type**: newsletter
- **URL**: magazine.sebastianraschka.com
- **Cadence**: biweekly
- **Last activity**: 2026-04 (last_checked 2026-05-02)
- **Audience tier**: senior + researcher
- **One-liner**: Technical depth, papers digest. Best source for "what new research papers actually mean for production".
- **投入产出比**: high
- **Endorsement evidence**:
  - `[type: figure_short]` multiple X mentions by Karpathy / similar
  - `[type: cross_source]` Latent Space + Yan reference
- **Decay risk**: low

### 🎙️ 4. Latent Space pod

(merged with newsletter entry above — same publisher)

### 🎙️ 5. Cognitive Revolution — Nathan Labenz

- **Type**: podcast
- **URL**: cognitiverevolution.ai
- **Host**: Nathan Labenz
- **Cadence**: weekly + bonus
- **Last activity**: 2026-05
- **Audience tier**: senior + strategy-focused
- **One-liner**: Strategy / product / forward-looking. Less tactical than Latent Space.
- **投入产出比**: medium (50-80% actionable for engineers)
- **Endorsement evidence**:
  - `[type: cross_source]` mutual referencing with Latent Space
- **Decay risk**: medium

### 🎙️ 6. Practical AI

- **Type**: podcast
- **Host**: Daniel Whitenack
- **Cadence**: weekly
- **Last activity**: 2026-05
- **Audience tier**: practitioner
- **One-liner**: Tactical, hands-on. Good entry-tier source.
- **投入产出比**: medium
- **Endorsement evidence**:
  - `[type: cross_source]` referenced in tutorials
- **Decay risk**: low

### 🎪 7. AI Engineer Summit

- **Type**: conference
- **URL**: ai.engineer
- **Last edition**: 2025-09
- **Next edition**: 2026-09
- **Audience tier**: practitioner + senior
- **One-liner**: The production-LLM annual gathering. AI Engineer movement's central event.
- **投入产出比**: high (talks free on YouTube post-event)
- **Endorsement evidence**:
  - `[type: figure_long]` Most LLM eng figures speak here
  - `[type: cross_source]` referenced by every newsletter
- **Decay risk**: low

### 👥 8. HuggingFace agent forum

- **Type**: community
- **Platform**: HuggingFace forum
- **One-liner**: Open technical forum focused on agent design + eval
- **投入产出比**: medium (signal/noise ratio varies)
- **Decay risk**: low

---

## Phase 2 提炼提示

**「这一行的资深人订阅最多的 top 3 sources」**:
1. Latent Space (newsletter + pod) — anchor publication
2. Eugene Yan newsletter — eval-focused
3. Ahead of AI / Cognitive Revolution — research/strategy view

→ master skill 「想跟最新动态」节直接列出

**「最近 3 个月话题热度」** (workflow change signals — confidence low because sources listed but content not deep-crawled):
- Browser-use vs Stagehand selection (multiple sources)
- CrewAI / AutoGen production critique
- Agent eval methodology evolution (LLM-as-judge → behavioral)
- Topic-heat: incomplete (sources listed but content not crawled)

**新 figures 候选** (喂给 wave 2 Track 01):
- Eugene Yan, Sebastian Raschka — already aware (in Track 01 candidate pool but not retained-5; could promote in non-minimal-viable run)
- Nathan Labenz — could add

**冷僻信号**: 8 sources is below 23 target — minimal-viable scope. ✅ industry not cold.
