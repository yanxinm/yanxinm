#!/bin/bash
# 守护脚本：监测并自动重启 TDAI Gateway 和 Hermes Gateway
# 由 cron 每 2 分钟调用一次，无异常时静默退出。
# 路径: ~/.hermes/scripts/watchdog.sh (cron 引用)
# 镜像: ~/.hermes/skills/devops/hermes-gateway-ops/scripts/watchdog.sh (skill 副本)

LOG="/tmp/hermes-watchdog.log"
TS=$(date "+%Y-%m-%d %H:%M:%S")

log() {
  echo "[$TS] $*" | tee -a "$LOG"
}

# ── 1. 检查 TDAI Gateway (端口 8420) ──
if ! ss -tlnp | grep -q ":8420 "; then
  log "⚠️ TDAI Gateway 端口 8420 未监听，正在重启..."
  cd /home/yanxin/.memory-tencentdb || { log "❌ 无法进入 ~/.memory-tencentdb"; exit 1; }
  nohup node --import tsx/esm node_modules/@tencentdb-agent-memory/memory-tencentdb/src/gateway/server.ts \
    >> /tmp/tdai-gw.log 2>&1 &
  TD_PID=$!
  sleep 5
  if ss -tlnp | grep -q ":8420 "; then
    log "✅ TDAI Gateway 已重启 (PID=$TD_PID)"
  else
    log "❌ TDAI Gateway 启动失败"
  fi
fi

# ── 2. 检查 Hermes Gateway ──
if ! pgrep -f "hermes gateway run" > /dev/null 2>&1; then
  log "⚠️ Hermes Gateway 未运行，正在重启..."
  cd /home/yanxin/Hermes-Agent || { log "❌ 无法进入 Hermes-Agent"; exit 1; }
  source venv/bin/activate
  nohup hermes gateway run --replace >> /home/yanxin/.hermes/logs/gateway.log 2>&1 &
  HG_PID=$!
  sleep 8
  if pgrep -f "hermes gateway run" > /dev/null 2>&1; then
    log "✅ Hermes Gateway 已重启 (PID=$HG_PID)"
    echo "[$TS] Watchdog: Hermes Gateway restarted (PID=$HG_PID)" >> /home/yanxin/.hermes/logs/gateway.log
  else
    log "❌ Hermes Gateway 启动失败"
  fi
fi

exit 0
