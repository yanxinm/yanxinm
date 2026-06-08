#!/usr/bin/env bash
# Hermes Agent 全量灾备脚本（安全版）
# 只备份不含密钥的核心配置/技能/记忆
# 每天凌晨3:00执行
set -euo pipefail

HERMES_HOME="$HOME/.hermes"
REPO_DIR="$HOME/hermes-backup"
BACKUP_DIR="$REPO_DIR/hermes"
DATE_TAG=$(date +%Y%m%d%H%M)

cd "$REPO_DIR"
# 保持 HTTPS（通过 ghproxy.net 代理），不切 SSH
# SSH 在墙内经常不通，HTTPS + ghproxy 更可靠

# 清理上次备份
rm -rf "$BACKUP_DIR"

# 1. 核心配置文件（不含 .env / auth.json）
mkdir -p "$BACKUP_DIR/config"
cp "$HERMES_HOME/config.yaml" "$BACKUP_DIR/config/" 2>/dev/null || true
cp "$HERMES_HOME/SOUL.md" "$BACKUP_DIR/config/" 2>/dev/null || true

# 2. 技能 - 最重要的资产（你的所有技能）
mkdir -p "$BACKUP_DIR/skills"
rsync -a --delete "$HERMES_HOME/skills/" "$BACKUP_DIR/skills/" 2>/dev/null || true

# 3. Hindsight 记忆系统配置
mkdir -p "$BACKUP_DIR/hindsight"
cp -r "$HERMES_HOME/hindsight/"* "$BACKUP_DIR/hindsight/" 2>/dev/null || true

# 4. Cron 定时任务定义
mkdir -p "$BACKUP_DIR/cron"
rsync -a --delete "$HERMES_HOME/cron/" "$BACKUP_DIR/cron/" 2>/dev/null || true

# 5. 自定义脚本
mkdir -p "$BACKUP_DIR/scripts"
rsync -a --delete "$HERMES_HOME/scripts/" "$BACKUP_DIR/scripts/" 2>/dev/null || true

# 6. 持久记忆文件
mkdir -p "$BACKUP_DIR/memories"
cp -r "$HERMES_HOME/memories/"* "$BACKUP_DIR/memories/" 2>/dev/null || true

# 7. GBrain 配置
mkdir -p "$BACKUP_DIR/gbrain"
cp "$HOME/.gbrain/config.json" "$BACKUP_DIR/gbrain/" 2>/dev/null || true
cp "$HOME/gbrain/CLAUDE.md" "$BACKUP_DIR/gbrain/" 2>/dev/null || true

# 8. 心智配置文件
mkdir -p "$BACKUP_DIR/config"
cp "$HERMES_HOME/.hermes_history" "$BACKUP_DIR/config/" 2>/dev/null || true

# 9. 本地备份保存（不依赖网络）
# 当 GitHub 不可达时，纯本地 tar 兜底
LOCAL_TAR="$REPO_DIR/hermes-backup-$DATE_TAG.tar.gz"
tar -czf "$LOCAL_TAR" -C "$REPO_DIR" hermes/ 2>/dev/null

# 尝试 git 推送（最佳努力）
echo "hermes/skills/guizang-ppt-skill/" > "$REPO_DIR/.gitignore" 2>/dev/null || true
git add -A 2>/dev/null
if ! git diff --cached --quiet 2>/dev/null; then
    git commit -m "hb: $DATE_TAG" --quiet 2>/dev/null || true
    PUSH_OUT=$(git push origin main 2>&1) && PUSH_EXIT=0 || PUSH_EXIT=$?
    if [ "$PUSH_EXIT" -eq 0 ]; then
        echo "hermes-backup: $DATE_TAG OK — GitHub 已同步 ($(du -sh $BACKUP_DIR | cut -f1))"
        exit 0
    fi
fi

echo "hermes-backup: $DATE_TAG OK — 本地备份 ($(du -sh "$LOCAL_TAR" | cut -f1))"
