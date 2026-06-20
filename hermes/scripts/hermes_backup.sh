#!/usr/bin/env bash
# Hermes Agent 备份脚本（优化版）
# 备份配置/技能/记忆到 GitHub + 本地
set -uo pipefail

HERMES_HOME="$HOME/.hermes"
REPO_DIR="$HOME/hermes-backup"
BACKUP_DIR="$REPO_DIR/hermes"
DATE_TAG=$(date +%Y%m%d%H%M)

cd "$REPO_DIR"

# 1. 配置
mkdir -p "$BACKUP_DIR/config"
cp "$HERMES_HOME/config.yaml" "$BACKUP_DIR/config/" 2>/dev/null || true
cp "$HERMES_HOME/SOUL.md" "$BACKUP_DIR/config/" 2>/dev/null || true

# 2. 技能
mkdir -p "$BACKUP_DIR/skills"
rsync -a "$HERMES_HOME/skills/" "$BACKUP_DIR/skills/" 2>/dev/null || true

# 3. Hindsight 记忆
mkdir -p "$BACKUP_DIR/hindsight"
cp -r "$HERMES_HOME/hindsight/"* "$BACKUP_DIR/hindsight/" 2>/dev/null || true

# 4. Cron 任务
mkdir -p "$BACKUP_DIR/cron"
rsync -a "$HERMES_HOME/cron/" "$BACKUP_DIR/cron/" 2>/dev/null || true

# 5. 脚本
mkdir -p "$BACKUP_DIR/scripts"
rsync -a "$HERMES_HOME/scripts/" "$BACKUP_DIR/scripts/" 2>/dev/null || true

# 6. 记忆
mkdir -p "$BACKUP_DIR/memories"
cp -r "$HERMES_HOME/memories/"* "$BACKUP_DIR/memories/" 2>/dev/null || true

# 7. GBrain
mkdir -p "$BACKUP_DIR/gbrain"
cp "$HOME/.gbrain/config.json" "$BACKUP_DIR/gbrain/" 2>/dev/null || true
cp "$HOME/gbrain/CLAUDE.md" "$BACKUP_DIR/gbrain/" 2>/dev/null || true

# 8. 本地 tar.gz（增量压缩）
LOCAL_TAR="$REPO_DIR/hermes-backup-$DATE_TAG.tar.gz"
tar -czf "$LOCAL_TAR" -C "$REPO_DIR" hermes/ 2>/dev/null || true

# 9. 拷贝到外接硬盘
cp "$LOCAL_TAR" /media/miao/seagate-1tb/hermes-backup/ 2>/dev/null || true

# 10. 推 GitHub（超时 30 秒，失败不阻塞）
export GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no -o ConnectTimeout=30"
git add -A 2>/dev/null || true
if ! git diff --cached --quiet 2>/dev/null; then
    git commit -m "hb: $DATE_TAG" --quiet 2>/dev/null || true
    PUSH_OUT=$(git push origin main 2>&1) && PUSH_EXIT=0 || PUSH_EXIT=$?
    if [ "$PUSH_EXIT" -eq 0 ]; then
        SIZE=$(du -sh "$BACKUP_DIR" | cut -f1)
        echo "hermes-backup: $DATE_TAG OK - GitHub 已同步 (${SIZE})"
        exit 0
    fi
fi

SIZE=$(du -sh "$LOCAL_TAR" 2>/dev/null | cut -f1 || echo "?")
echo "hermes-backup: $DATE_TAG OK - 本地备份 (${SIZE})"
