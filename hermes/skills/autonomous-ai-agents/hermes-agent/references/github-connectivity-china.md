# GitHub Connectivity from China

From mainland China, direct HTTPS connections to `github.com` (port 443) are frequently blocked or timeout due to GFW restrictions. This reference documents workarounds tested on this setup (WSL2 Ubuntu, China network, Alibaba DNS 223.5.5.5).

## Common Failure Modes

| Error | Likely Cause |
|-------|-------------|
| `GnuTLS recv error (-110): The TLS connection was non-properly terminated` | HTTPS connection reset by GFW |
| `Failed to connect to github.com port 443: Timeout was reached` | TCP connection dropped |
| `Recv failure: Connection reset by peer` (on ghproxy.com) | Proxy mirror also blocked or unstable |

## Verified Working: SSH (Port 22)

SSH port 22 to GitHub **usually works** when HTTPS is blocked.

### Quick Test
```bash
ssh -T -o ConnectTimeout=10 git@github.com
# Expect: "Permission denied (publickey)" — confirms TCP connectivity
```

### Setup Steps

1. **Generate an SSH key** (ed25519):
   ```bash
   ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -C "your-label@host"
   ```

2. **Add public key to GitHub**:
   - Web: https://github.com/settings/keys → "New SSH key"
   - Or via API (requires a PAT with `admin:public_key` scope):
     ```bash
     curl -X POST https://api.github.com/user/keys \
       -H "Authorization: token $GH_TOKEN" \
       -d '{"title":"key-name","key":"'"$(cat ~/.ssh/id_ed25519.pub)"'"}'
     ```

3. **Switch repo remote to SSH**:
   ```bash
   git remote set-url origin git@github.com:user/repo.git
   ```

## Proxy Mirrors (Unreliable)

These mirrors sometimes work, sometimes don't:

| Mirror | URL Prefix | Status |
|--------|-----------|--------|
| ghproxy.com | `https://ghproxy.com/https://github.com/...` | Intermittent |
| mirror.ghproxy.com | `https://mirror.ghproxy.com/https://github.com/...` | Intermittent |

Both are unreliable for pushes. HTTPS proxies also carry security implications.

## Backup Script Pitfall: Silent Failure

Scripts that mask git push errors with `|| true` will **silently fail**:
```bash
git push origin main 2>&1 | grep -v "^$" || true  # BAD: swallows errors
```

**Always check exit codes** or store the result:
```bash
if ! git push origin main 2>&1; then
  echo "BACKUP_PUSH_FAILED=true" >> /tmp/backup_status
fi
```

For cron jobs, use `deliver: origin` instead of `deliver: local` so failures are reported to the user.

## Downloading Release Binaries (Assets) via Mirrors

Unlike git operations, downloading release assets (`.exe`, `.AppImage`, `.dmg`, `.deb`, `.rpm`) from `https://github.com/…/releases/download/…` requires an HTTPS proxy mirror because:

- **SSH is not an option** — release downloads only work over HTTPS
- **Direct `curl` to `github.com`** reliably times out from China after ~2 min

### Strategy: Mirror Fallback Chain

Test each mirror in sequence until one returns a valid file (>10 KB to rule out 404/error pages). Cache the working mirror address for future downloads in the same session.

| Mirror | URL Pattern | Reliability |
|--------|------------|-------------|
| `ghproxy.net` | `https://ghproxy.net/https://github.com/…` | ✅ Best (worked May 2026) |
| `gh.api.99988866.xyz` | `https://gh.api.99988866.xyz/https://github.com/…` | ⚠️ Intermittent |
| `github.moeyy.xyz` | `https://github.moeyy.xyz/https://github.com/…` | ⚠️ Intermittent |
| `mirror.ghproxy.com` | `https://mirror.ghproxy.com/https://github.com/…` | ❌ Often blocked |

### Implementation Pattern

```bash
REPO="fathah/hermes-desktop"
TAG="v0.4.3"
ASSET="hermes-desktop-0.4.3-setup.exe"
OUTPUT="/mnt/c/Users/yanxi/Downloads/$ASSET"

MIRRORS=(
  "https://ghproxy.net/https://github.com/$REPO/releases/download/$TAG/$ASSET"
  "https://gh.api.99988866.xyz/https://github.com/$REPO/releases/download/$TAG/$ASSET"
  "https://github.moeyy.xyz/https://github.com/$REPO/releases/download/$TAG/$ASSET"
)

for URL in "${MIRRORS[@]}"; do
  echo "Trying: $URL"
  curl -L --max-time 120 -o "$OUTPUT" "$URL" 2>&1
  if [ -f "$OUTPUT" ] && [ "$(stat -c%s "$OUTPUT" 2>/dev/null)" -gt 10000 ]; then
    echo "✓ SUCCESS! $(stat -c%s "$OUTPUT") bytes"
    break
  else
    echo "✗ Failed, trying next..."
    rm -f "$OUTPUT"
  fi
done
```

### Pitfalls

- **`ghproxy.com` and `mirror.ghproxy.com` are unreliable** — `ghproxy.net` (different TLD) worked more consistently in testing.
- **Always validate file size** — a mirror returning a 404 HTML page as "success" is common. Check `stat -c%s` > 10 KB.
- **Set `--max-time`** — default curl timeout is 0 (infinite). 120s per mirror is reasonable for a 100 MB binary.
- **Verify file type** — after download, confirm it's an executable:
  ```bash
  file "$OUTPUT"
  # Expected: "PE32 executable (GUI) Intel 80386, for MS Windows"
  ```

## Large Clone Timeout Workaround

When cloning large repositories (especially with long history), HTTPS timeouts are common:

| Symptom | Error |
|---------|-------|
| Hangs mid-transfer | `fetch-pack: unexpected disconnect while reading sideband packet` |
| Slow start | Cloning hangs for 30+ seconds before disconnecting |

**Workaround:** use shallow clone + increased buffer size:

```bash
git config --global http.postBuffer 524288000   # 512 MB buffer
git clone --depth 1 https://github.com/<owner>/<repo>.git
```

`http.postBuffer` prevents the HTTP connection from idling long enough for the GFW to reset it. `--depth 1` reduces data volume, keeping the single TCP connection open for less time.

If even the shallow clone fails, fall back to SSH (port 22).

## WSL-Specific Notes

- DNS resolver: Alibaba DNS (223.5.5.5) is reliable from China
- IPv6 may not be available; ensure IPv4 fallback
- Windows host may have different network conditions — test directly from WSL
- The `.git-credentials` file (`~/.git-credentials`) may store HTTPS credentials that won't help if HTTPS is blocked
