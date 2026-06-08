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
# 确保使用 SSH remote（HTTPS 在墙内可能被阻断）
CURRENT_REMOTE=$(git remote get-url origin 2>/dev/null || echo "")
if echo "$CURRENT_REMOTE" | grep -q "^https"; then
  git remote set-url origin "git@github.com:yanxinm/yanxinm.git"
fi

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

# 9. Git 提交
git add -A
if git diff --cached --quiet; then
    echo "hermes-backup: $DATE_TAG OK (no changes)"
    exit 0
fi

git commit -m "hb: $DATE_TAG" --quiet

PUSH_OUT=$(git push origin main 2>&1) && PUSH_EXIT=0 || PUSH_EXIT=$?

if [ "$PUSH_EXIT" -ne 0 ]; then
    # 过滤掉 GitHub 的远程提示行，保留关键错误
    ERROR_MSG=$(echo "$PUSH_OUT" | grep -v "^remote:" | grep -v "^$" | head -5)
    echo "hermes-backup: $DATE_TAG ERROR — push 失败"
    echo "hermes-backup: $ERROR_MSG"
    exit 1
fi

echo "hermes-backup: $DATE_TAG OK ($(du -sh $BACKUP_DIR | cut -f1))"
