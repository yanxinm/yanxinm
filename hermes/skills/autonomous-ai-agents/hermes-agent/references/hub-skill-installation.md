# Hub Skill Installation — Quick Reference

## Commands

```bash
hermes skills search <query>       # Search the skills hub
hermes skills inspect <id>         # Preview without installing
hermes skills install <id>         # Install (interactive confirmation)
hermes skills install <id> --yes   # Install (skip confirmation)
hermes skills uninstall <id>       # Remove a hub-installed skill
hermes skills browse               # Browse all available skills
```

## Identifier Format

Skills are identified by `official/<category>/<name>`:
- `official/research/scrapling`
- `official/productivity/siyuan`
- `official/creative/meme-generation`

## ClawHub Inspect/Install Gap

Some skills that can be **inspected** from ClawHub cannot be **installed by name**:

```bash
# This WORKS (inspect)
hermes skills inspect nuwa-skill           # Found in ClawHub

# This FAILS
hermes skills install nuwa-skill           # "No skill found in any source"

# Fix: install from GitHub URL instead
hermes skills install https://github.com/alchaincyf/nuwa-skill --yes
```

The root cause: ClawHub indexes some skills for browsing/inspection but doesn't host them for direct install. If a skill name is found by `inspect` but fails on `install`, try the GitHub URL directly. Repos with a root-level `SKILL.md` install cleanly.

Prefix notation (`clawhub:nuwa-skill`) also fails. Always fall back to the full GitHub URL.

## GitHub URL Installation

Skills can also be installed directly from GitHub repos:

```bash
hermes skills install https://github.com/<owner>/<repo> --yes
```

Example (installed nuwa-skill from alchaincyf/nuwa-skill, ~14K stars):
```bash
hermes skills install https://github.com/alchaincyf/nuwa-skill --yes
```

This works for any GitHub repo containing a `SKILL.md` in its root. The installer:
1. Clones the repo to `.hub/quarantine/<name>/`
2. Runs a security scan (verdict: SAFE/CAUTION/DANGEROUS)
3. Moves to `~/.hermes/skills/<name>/` on approval

**Known GitHub skill repos discovered via this method:**
- `alchaincyf/nuwa-skill` — Nuwa skill creation engine (女娲), 6-agent parallel research framework
- Any repo with a top-level `SKILL.md` can be installed this way

## Security Scan Behavior

Every hub skill goes through a security scan before installation:

| Verdict | Meaning | Action |
|---------|---------|--------|
| `SAFE` | No suspicious patterns | Installs silently with `--yes` |
| `CAUTION` | Mild concerns (network calls, pip install commands) | Installs with `--yes` (official source) |
| `DANGEROUS` | Credential handling, config file writes | Installs with `--yes` (official source) |

For **official/builtin** skills (maintained by Nous Research), CAUTION and DANGEROUS verdicts are expected — the skill writes to `.env` files or makes network calls by design. Use `--yes` to bypass the confirmation prompt.

For **community/third-party** skills, inspect the findings carefully before allowing.

## Where Skills Land

```
~/.hermes/skills/<category>/<name>/
├── SKILL.md          # Main skill file
├── EXAMPLES.md       # (optional) Examples
├── scripts/          # (optional) Executable scripts
│   ├── generate_meme.py
│   └── templates.json
├── templates/        # (optional) Boilerplate templates
└── references/       # (optional) Reference docs
```

## Known Pitfalls

- **First install requires confirmation** — unless `--yes` is passed
- **Network timeout in China**: some hub skills install additional dependencies (e.g., Playwright browsers via `scrapling install`) that download from CDNs which may be slow or timeout. Run those separately with longer timeouts.
- **Reload needed**: newly installed skills may not appear in-session until `/reload-skills` or a new session is started.

## Manual Fallback (When `hermes skills install <URL>` Fails)

When `hermes skills install` fails due to network issues (common in China), use this manual method:

```bash
# 1. Clone with depth=1 to avoid timeout on large repos
git config --global http.postBuffer 524288000
git clone --depth 1 https://github.com/<owner>/<repo>.git ~/<repo>

# 2. Copy the skill into Hermes
mkdir -p ~/.hermes/skills/<name>
cp -r ~/<repo>/SKILL.md ~/<repo>/prompts ~/<repo>/references ~/<repo>/tools ~/<repo>/README.md ~/.hermes/skills/<name>/
# (adjust which directories to copy based on what SKILL.md references)

# 3. Verify
hermes skills list | grep <name>

# 4. Clean up
rm -rf ~/<repo>
```

**When to use this:** the `hermes skills install` command clones to `.hub/quarantine/<name>/` and runs security scans, which may time out on slow connections. Manual install skips the scan — only use for repos you trust.

**Sub-skills from prototypes:** some framework skills (e.g., `master-skill`) come with pre-built prototype sub-skills in a `prototypes/` directory. Hermes auto-discovers these as separate skills when the directory is inside `~/.hermes/skills/<name>/`, but they won't show up in `skills_list` unless the repo layout matches what Hermes expects. Verify with `skills_list` after install; sub-skills may need manual symlinking if not auto-detected.
