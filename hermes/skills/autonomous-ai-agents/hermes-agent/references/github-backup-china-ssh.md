# GitHub Backup via SSH from China

When running Hermes Agent from mainland China, **HTTPS connections to GitHub (port 443) are frequently blocked** by the GFW. However, **SSH connections (port 22) to GitHub usually work**.

This document describes the workaround: using SSH instead of HTTPS for automated git-based backup.

## Diagnosis

When backup fails, you'll typically see one of these:

```
# HTTPS: TLS connection timeout
fatal: unable to access 'https://github.com/...': GnuTLS recv error (-110): The TLS connection was non-properly terminated.

# HTTPS: Connection timeout  
fatal: unable to access 'https://github.com/...': Failed to connect to github.com port 443: Timeout was reached

# Proxy mirrors also fail
fatal: unable to access 'https://ghproxy.com/...': Recv failure: Connection reset by peer
```

## Verification

**Step 1: Test HTTPS** (will likely fail from China):
```bash
curl -v --connect-timeout 10 https://github.com
```

**Step 2: Test SSH** (usually works):
```bash
ssh -o ConnectTimeout=10 -T git@github.com
# Expected: "Permission denied (publickey)." ← this is OK, means SSH TCP works
```

## Solution: Switch to SSH

### 1. Generate an SSH Key (one-time)

```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -C "hermes-backup@wsl"
cat ~/.ssh/id_ed25519.pub
```

### 2. Add the Public Key to GitHub

Send the output of the `cat` command to the user and ask them to:
1. Open https://github.com/settings/keys
2. Click "New SSH key"
3. Paste the public key, title it (e.g., "hermes-backup-wsl")
4. Click "Add SSH key"

### 3. Update the Backup Script

The backup script should auto-detect HTTPS vs SSH and switch:

```bash
cd "$HOME/yanxinm"
CURRENT_REMOTE=$(git remote get-url origin 2>/dev/null || echo "")
if echo "$CURRENT_REMOTE" | grep -q "^https"; then
  git remote set-url origin "git@github.com:yanxinm/yanxinm.git"
fi
```

### 4. Verify the Push

```bash
cd ~/yanxinm
git push origin main
# Expected: "xxx..yyy  main -> main"
```

## Backup Script Pitfalls

- **Silent error swallowing**: If the backup script uses `|| true` after git push, failures are masked. Remove `|| true` or capture the exit code explicitly.
- **Local-only delivery**: Set `deliver: origin` in the cron job to push results to the user, not just save to `local`.
- **GitHub mirror proxies** (ghproxy.com, mirror.ghproxy.com) may also be unreliable from China — SSH is more consistent.
- **No SSH key = cannot push**: The user MUST complete the SSH key addition. Generate it, show the public key, and wait for confirmation before switching the remote.

## Complete hermes_backup.sh Template

```bash
#!/usr/bin/env bash
set -euo pipefail

HERMES_HOME="$HOME/.hermes"
BACKUP_DIR="$HOME/yanxinm/hermes"
DATE_TAG=$(date +%Y%m%d%H%M)

cd "$HOME/yanxinm"

# Ensure SSH remote (HTTPS is blocked in China)
CURRENT_REMOTE=$(git remote get-url origin 2>/dev/null || echo "")
if echo "$CURRENT_REMOTE" | grep -q "^https"; then
  git remote set-url origin "git@github.com:yanxinm/yanxinm.git"
fi

# Clean previous backup
rm -rf "$BACKUP_DIR"

# Backup core config
mkdir -p "$BACKUP_DIR/config"
cp "$HERMES_HOME/config.yaml" "$BACKUP_DIR/config/" 2>/dev/null || true

# Backup skills
mkdir -p "$BACKUP_DIR/skills"
rsync -a --delete "$HERMES_HOME/skills/" "$BACKUP_DIR/skills/" 2>/dev/null || true

# Backup hindsight config
mkdir -p "$BACKUP_DIR/hindsight"
cp -r "$HERMES_HOME/hindsight/"* "$BACKUP_DIR/hindsight/" 2>/dev/null || true

# Backup cron definitions
mkdir -p "$BACKUP_DIR/cron"
rsync -a --delete "$HERMES_HOME/cron/" "$BACKUP_DIR/cron/" 2>/dev/null || true

# Backup scripts
mkdir -p "$BACKUP_DIR/scripts"
rsync -a --delete "$HERMES_HOME/scripts/" "$BACKUP_DIR/scripts/" 2>/dev/null || true

# Backup memories
mkdir -p "$BACKUP_DIR/memories"
cp -r "$HERMES_HOME/memories/"* "$BACKUP_DIR/memories/" 2>/dev/null || true

# Git commit and push
git add -A
if git diff --cached --quiet; then
    echo "hermes-backup: $DATE_TAG no changes"
    exit 0
fi

git commit -m "hb: $DATE_TAG" --quiet
if git push origin main 2>&1; then
    echo "hermes-backup: $DATE_TAG OK ($(du -sh $BACKUP_DIR | cut -f1))"
else
    echo "hermes-backup: $DATE_TAG FAILED (push error)"
    exit 1
fi
```

## Cron Job Configuration

```bash
# Set delivery to WeChat (origin) instead of local-only
hermes cron update JOB_ID --deliver origin
```

The cron schedule `0 3 * * *` (daily at 3:00 AM) is recommended — avoids interfering with daytime operations.

## exclusions

Backup should exclude:
- `~/.hermes/.env` (API keys)
- `~/.hermes/auth.json` (OAuth tokens)
- `~/.hermes/sessions/` (conversation transcripts — may contain keys)
- `~/.hermes/logs/` (logs — large, transient)
- `node_modules/` (large, reproducible)
