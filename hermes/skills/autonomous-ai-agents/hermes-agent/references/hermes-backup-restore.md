# Hermes Backup & Restore

Daily backup of all Hermes configuration, memory, skills, databases, and cron jobs. Enables full recovery after reinstall or migration to another machine.

## Backup Script

Location: `~/.hermes/scripts/backup.sh`

Creates timestamped backup directories in the configured backup root. Retains the last 30 days and auto-clears older backups.

### What Gets Backed Up

| Category | Files |
|----------|-------|
| Config | `config.yaml`, `.env`, `SOUL.md`, `auth.json`, `channel_directory.json`, `gateway_state.json` |
| Memory | `MEMORY.md` (persistent notes), `USER.md` (user profile), `hindsight/config.json` |
| Databases | `state.db` (~10MB), `kanban.db`, `response_store.db` + WAL files |
| Cron jobs | `cron/jobs.json` (full job config) + summary dump |
| Skills | Entire `skills/` directory as tar.gz |
| Platforms | `platforms/` directory as tar.gz |
| Scripts | `scripts/` directory as tar.gz |
| Plugins | `plugins/` directory as tar.gz |
| Logs | Last 512KB of each log file |
| Session index | Directory listing of `sessions/` |
| Restore guide | Auto-generated `RESTORE_GUIDE.md` with step-by-step recovery commands |

### Cron Job

The backup runs daily at 17:00 via a `no_agent` cron job:

```
job_id: a1698dc83d71
name: Hermes 每日备份
schedule: 0 17 * * *  (5:00 PM daily)
script: backup.sh
no_agent: true
```

Since the job is `no_agent`, the cron scheduler captures stdout and delivers it according to the job's `deliver` setting:
- **Non-empty stdout** → sent verbatim as the delivery message
- **Empty stdout** → silent (nothing delivered)

**Pitfall**: If the backup script exits silently when there are no changes (`git diff --cached --quiet`), the user receives no confirmation that the backup ran. **Fix**: Always echo a status line, even when there are no changes:

```bash
# In hermes_backup.sh — before the no-change early exit:
if git diff --cached --quiet; then
    echo "hermes-backup: $DATE_TAG OK (no changes)"   # ← was silently `exit 0`
    exit 0
fi
```

### Setting Up

```bash
# Create the script
# (script is at ~/.hermes/scripts/backup.sh)

# Make it executable
chmod +x ~/.hermes/scripts/backup.sh

# Run once to verify
bash ~/.hermes/scripts/backup.sh

# Check backup output
ls -la /mnt/e/Hermes备份/
```

## Restore Procedure

### Full Restore (new machine or after reinstall)

1. Install Hermes Agent: `git clone && pip install -e .`
2. Stop any running gateway: `hermes gateway stop`
3. Restore config files:
   ```bash
   cp backup_dir/config/config.yaml ~/.hermes/config.yaml
   cp backup_dir/config/.env ~/.hermes/.env
   cp backup_dir/config/SOUL.md ~/.hermes/SOUL.md
   cp backup_dir/config/auth.json ~/.hermes/auth.json
   ```
4. Restore memory:
   ```bash
   cp backup_dir/memories/MEMORY.md ~/.hermes/memories/MEMORY.md
   cp backup_dir/memories/USER.md ~/.hermes/memories/USER.md
   cp backup_dir/config/hindsight_config.json ~/.hermes/hindsight/config.json
   ```
5. Restore databases:
   ```bash
   cp backup_dir/databases/state.db ~/.hermes/state.db
   cp backup_dir/databases/kanban.db ~/.hermes/kanban.db
   cp backup_dir/databases/response_store.db ~/.hermes/response_store.db
   ```
6. Restore skills:
   ```bash
   tar -xzf backup_dir/skills/skills.tar.gz -C ~/.hermes/
   ```
7. Restore platforms + scripts:
   ```bash
   tar -xzf backup_dir/platforms.tar.gz -C ~/.hermes/
   tar -xzf backup_dir/scripts.tar.gz -C ~/.hermes/
   ```
8. Restore cron jobs: Use `cronjob` tool or manually re-create from `backup_dir/cron/jobs.json`
9. Restart gateway: `hermes gateway restart`

### Partial Restore (single file)

```bash
# Just restore config
cp backup_dir/config/config.yaml ~/.hermes/config.yaml

# Just restore memory
cp backup_dir/memories/MEMORY.md ~/.hermes/memories/MEMORY.md
```

## Remote Backup to GitHub

In addition to local backup, the Hermes config/skills/memory can be pushed to a GitHub repository for disaster recovery. The backup runs daily at 3:00 AM via a `no_agent` cron job.

### What Gets Backed Up (GitHub-safe subset)

| Category | Files | Excluded (secret scanning risk) |
|----------|-------|--------------------------------|
| Config | `config.yaml`, `SOUL.md` | `.env`, `auth.json` |
| Skills | Entire `skills/` directory | — |
| Hindsight | `hindsight/config.json` | — |
| Cron | `cron/jobs.json` | — |
| Scripts | `scripts/` directory | — |
| Memories | `memories/` files | — |
| GBrain config | `~/.gbrain/config.json` | — |

**Never push to GitHub**: `sessions/` (contain API keys from conversations), `state.db` (full session DB), `auth.json`, `.env`, `logs/`. GitHub's Push Protection scans for secrets and blocks commits containing API keys, tokens, and passwords.

### Setup

```bash
# 1. Clone the target repo
cd ~ && git clone https://github.com/YOUR_USER/YOUR_REPO.git

# 2. Create .gitignore in the repo root
echo "hermes/state.*" >> .gitignore
echo "hermes/sessions/" >> .gitignore
echo "**/.env" >> .gitignore
echo "**/auth.json" >> .gitignore
echo "**/logs/" >> .gitignore
git add .gitignore && git commit -m "init" && git push

# 3. Create backup script at ~/.hermes/scripts/hermes_backup.sh
# (copies essential files to repo, excludes secrets)

# 4. Create cron job (no_agent, mechanical)
cronjob_create(name="每日灾备", schedule="0 3 * * *",
               script="hermes_backup.sh", no_agent=true, deliver="local")
```

### China Network: HTTPS → SSH Workaround

From within mainland China, HTTPS connections to `github.com` (port 443) are frequently blocked (GnuTLS recv error, connection timeout, TLS reset). SSH (port 22) generally works. The backup script now auto-detects and switches to SSH:

```bash
# In ~/.hermes/scripts/hermes_backup.sh (at the top, before any git operation):
CURRENT_REMOTE=$(git remote get-url origin 2>/dev/null || echo "")
if echo "$CURRENT_REMOTE" | grep -q "^https"; then
  git remote set-url origin "git@github.com:${USER}/${REPO}.git"
fi
```

**One-time SSH key setup:**
1. Generate key: `ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -C "hermes-backup@wsl"`
2. Add public key (`cat ~/.ssh/id_ed25519.pub`) at [GitHub Settings > SSH Keys](https://github.com/settings/keys)
3. Title it descriptively (e.g., "hermes-backup-wsl")
4. Grant **Read/Write** access — needed for push

### Delivery Notification

The GitHub backup cron job should use `deliver: "weixin"` (or whichever platform the user uses for daily checks) so the user receives a brief push notification at 3:00 AM when the backup completes. If using WeChat via iLink, keep output concise (≤3 lines) to avoid iLink rate limiting.

**no_agent output rule**: non-empty stdout → delivered verbatim; empty stdout → silent.

### Recovery

```bash
git clone git@github.com:YOUR_USER/YOUR_REPO.git ~/hermes-restore
cp -r ~/hermes-restore/hermes/config/config.yaml ~/.hermes/
cp -r ~/hermes-restore/hermes/skills/* ~/.hermes/skills/
cp -r ~/hermes-restore/hermes/hindsight/* ~/.hermes/hindsight/
# ... restore .env and auth.json from local backup (never on GitHub)
```

### GitHub Secret Scanning Pitfall

GitHub's Push Protection scans every pushed commit for secrets (API keys, tokens, passwords). Two common sources of false/failed pushes:

#### Source 1: Session files with API keys

If a commit inadvertently contains session files (which include API keys from conversations), GitHub's Push Protection will block the push:

```
remote: - GITHUB PUSH PROTECTION
remote:   - Push cannot contain secrets
remote:   —— OpenRouter API Key ————————————————————————————————
remote:     path: hermes/sessions/session_xxx.json:288
remote:   —— GitHub Personal Access Token ——————————————————————
remote:     path: hermes/sessions/session_yyy.json:2724
```

**Fix**: Remove the offending files from git history, add them to `.gitignore`, and force-push a clean history:
```bash
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch hermes/sessions/*' \
  --prune-empty --tag-name-filter cat -- --all
git push origin --force --all
```
Or simply reset and start fresh if no important history:
```bash
git checkout --orphan clean-branch
git rm -rf .
# add only safe files, commit, push -f
```

#### Source 2: API keys hardcoded in skill markdown files

Skill files (`SKILL.md`, `references/*.md`) under `~/.hermes/skills/` are **backed up to GitHub** by the backup script. If any skill contains a hardcoded API key (e.g., `r8_...` for Replicate, or any inline token), it will be flagged by GitHub secret scanning on push.

**Prevention (always)**:
- Store all API keys in `~/.hermes/.env` (protected from direct file tools), **never** in skill markdown files
- When documenting a model/API, use placeholder text: `已申请，存储于 ~/.hermes/.env`
- After adding a new skill or reference, scan for secrets before the next backup:
  ```bash
  grep -rPn 'r8_|sk-[a-zA-Z0-9]|ghp_|gho_' ~/.hermes/skills/ | grep -v '.git/' || echo "✅ Clean"
  ```

**Fix (push already blocked)**:
1. Remove the key from the source skill files
2. Rewrite git history in the backup repo to purge the offending commit:
   ```bash
   cd ~/yanxinm  # your backup repo
   git rebase -i <parent-of-secret-commit>  # drop the secret commit
   # OR: hard-reset to before the secret commit
   git reset --hard <clean-commit>
   ```
3. Re-run backup: `bash ~/.hermes/scripts/hermes_backup.sh`
4. Verify push succeeded: check `git status` shows `up to date with 'origin/main'`

### Backup Script Push Verification

The backup script's git push command may use `|| true` to suppress error output:
```bash
git push origin main 2>&1 | grep -v "^$" | grep -v "^remote:" || true
```
This causes the script to always report "OK" even when GitHub rejects the push (e.g., due to secret scanning). An `OK` from the script does NOT guarantee the remote is updated.

**Detection**: Check the backup repo's status to verify remote sync:
```bash
cd ~/yanxinm && git status
# "Your branch is up to date with 'origin/main'" → clean sync
# "Your branch is ahead of 'origin/main' by N commits" → push failed
```
Or check the last backup report against `git log` output.

**Recommended fix**: Remove the `|| true` tail so push failures propagate, or add explicit verification:
```bash
git push origin main 2>&1 || { echo "PUSH FAILED"; exit 1; }
```

## Pitfalls

1. On old machine: run the backup script one final time `bash ~/.hermes/scripts/backup.sh`
2. Copy the latest backup directory to the new machine's `E:/Hermes备份/` or equivalent
3. Follow the Full Restore procedure above
4. The cron jobs.json contains all job configs — use `hermes cron create` for each

## Pitfalls

- **Secrets in .env**: The `.env` file contains all API keys. Keep backups in a secure location. On the backup destination, chmod 600 the files.
- **Job IDs change**: Cron job `job_id` values are generated at creation time. `jobs.json` is informational for re-creating jobs, not for direct import. The old job_ids won't exist on the new machine.
- **Hindsight memory**: The hindsight daemon stores its index in `state.db`. Restoring this database should restore hindsight recall capabilities. If the hindsight config file is restored too, the daemon should reconnect automatically.
- **State.db is large**: ~10MB. Backup times are fast (~2s) because it's a single file copy.
- **Windows path for backup**: The backup root `E:/Hermes备份` has a Chinese character in the folder name. Make sure the WSL mount supports UTF-8 filenames (standard for /mnt/e/).
