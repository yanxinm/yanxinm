#!/bin/bash
# sync_taizhang.sh — SSH+rsync 从笔记本拉取工作台账增量到基地本地副本
# 参考脚本，实际部署在 ~/.hermes/scripts/sync_taizhang.sh
# 仅 Tailscale 直连时执行；中继时静默跳过
#
# 配套定时任务：
#   5323ccd7cf51「周末台账同步」：周六+周日 12:00，no_agent
#   dfdd687d1890「工作台账扫描」：周一 9:00，LLM 扫描本地副本

set -e

SSH_HOST="100.86.148.56"
SSH_USER="yanxi"
SRC="E:/百度云同步盘/工作台账/"
LOCAL="/home/miao/工作台账"
LOG_TAG="[$(date '+%Y-%m-%d %H:%M')]"

echo "$LOG_TAG 开始同步..."

# ===== 连通检测：检查 Tailscale 是否直连 =====
# DERP 中继不转发 TCP，只能在直连时同步
RELAY=$(tailscale status --json 2>/dev/null | python3 -c "
import json,sys
d=json.load(sys.stdin)
for p in d.get('Peer',{}).values():
    if p.get('HostName')=='ethan':
        print(p.get('Relay',''))
        break
" 2>/dev/null)

if [ -n "$RELAY" ]; then
    echo "$LOG_TAG Tailscale 走中继('$RELAY')，跳过同步（等待直连）"
    exit 0
fi

echo "$LOG_TAG Tailscale 直连已建立，开始 rsync..."

# ===== rsync 增量同步（仅文档类，排除 PPT 和媒体）=====
rsync -av --timeout=120 \
    --include='*.docx' --include='*.doc' \
    --include='*.xlsx' --include='*.xls' \
    --include='*.pdf' --include='*.txt' --include='*.md' \
    --include='*/' --exclude='*' \
    -e "ssh -o ConnectTimeout=15 -o StrictHostKeyChecking=no" \
    "$SSH_USER@$SSH_HOST:'$SRC'" "$LOCAL/"

# ===== 统计 =====
FILE_COUNT=$(find "$LOCAL" -type f | wc -l)
TOTAL_SIZE=$(du -sh "$LOCAL" | cut -f1)
echo "$LOG_TAG 同步完成 — 文件数: $FILE_COUNT, 总量: $TOTAL_SIZE"
