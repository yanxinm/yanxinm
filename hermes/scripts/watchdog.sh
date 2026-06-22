#!/bin/bash
# 守护脚本（基地版）：监测并自动重启 Hermes Gateway
# 由 cron 每 2 分钟调用一次，无异常时静默退出。

LOG="/tmp/hermes-watchdog.log"
TS=$(date "+%Y-%m-%d %H:%M:%S")

log() {
  echo "[$TS] $*" | tee -a "$LOG"
}

# ── 1. 检查 Hermes Gateway (systemd) ──
SERVICE="hermes-gateway"
if ! systemctl is-active --quiet "$SERVICE" 2>/dev/null; then
  log "⚠️ Hermes Gateway 未运行，正在重启..."
  systemctl restart "$SERVICE" 2>/dev/null || {
    log "❌ systemctl restart 失败"
    # 备用：直接拉起
    export PATH="/home/miao/.local/bin:/home/miao/.hermes/venv/bin:$PATH"
    cd /home/miao && nohup hermes gateway run --replace >> /home/miao/.hermes/logs/gateway.log 2>&1 &
    log "⚠️ 已尝试直接拉起（PID=$!）"
  }
  sleep 8
  if systemctl is-active --quiet "$SERVICE" 2>/dev/null || pgrep -f "hermes gateway run" > /dev/null 2>&1; then
    log "✅ Hermes Gateway 已重启"
  else
    log "❌ Hermes Gateway 重启失败"
  fi
fi

exit 0
