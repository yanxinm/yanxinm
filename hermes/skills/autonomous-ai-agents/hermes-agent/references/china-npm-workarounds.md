# China Network Workarounds for npm/Node Operations

## Problem

From mainland China, `npm install` from the default registry (`registry.npmjs.org`) is extremely slow (30s+ per package) or times out entirely. The Hermes gateway or CLI session may appear to hang or disconnect during npm-dependent installs.

## Solution: Use npmmirror

```bash
npm install --registry=https://registry.npmmirror.com
```

For persistent use:

```bash
npm config set registry https://registry.npmmirror.com
```

### What works
- `npm install --registry=https://registry.npmmirror.com` — reliable, ~2min for 104 packages (vs timeout on official registry)
- `npm pack <package>` on npmmirror — works with `--registry` flag
- `npx` commands — use `npx --registry=https://registry.npmmirror.com <cmd>`

### What doesn't
- `npm rebuild better-sqlite3` — still compiles from source on Node 25+; no prebuilt binaries. This is expected and slow (~30-60s).

## Gateway Crash During Plugin Installs

Some install scripts (e.g., MemOS memos-local-plugin) contain:

```bash
pkill -f "/bin/hermes"
```

This kills **all** Hermes processes matching `/bin/hermes` in their cmdline — including the gateway process serving the current chat session. The gateway service will eventually restart but the **current session drops immediately**.

### Workaround: Manual install
Instead of running the install script directly, decompose it into steps that don't kill Hermes:

1. Check if the script has a `pkill` / `kill` command targeting hermes
2. If so, manually run the install steps:
   - Download/extract the package
   - Install dependencies (with `--registry` flag if needed)
   - Configure symlinks/paths
   - Patch config.yaml
   - Start any daemon processes in background mode

### Workaround: Systemd mode
If Hermes runs as a systemd service (`systemctl --user`), the service auto-restarts after being killed. On WSL without systemd, gateway runs via `nohup` and does NOT auto-restart.

## Large Downloads That Timeout

| Package | Size | Timeout Likely? | Workaround |
|---------|------|-----------------|------------|
| Playwright Chromium | 167 MB | ✅ Yes | Core download; required for browser-based skills |
| npm dependencies (large projects) | 50-200 MB | ⚠️ Sometimes | Use npmmirror |

For Playwright specifically:
```bash
# After npm install via mirror:
npx playwright install chromium
# Or set mirror env:
export PLAYWRIGHT_DOWNLOAD_HOST=https://npmmirror.com/playwright
```

## Verifying npm Mirror

```bash
npm config get registry
# Expected: https://registry.npmmirror.com (if set globally)
```
