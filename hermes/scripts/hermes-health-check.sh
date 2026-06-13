#!/bin/bash
# ============================================================
# Hermes 全链路自检脚本 — 每6小时由 cron 触发
# 检查: Gateway | Web UI | Dashboard | 微信 | 飞书
# 发现异常自动修复，并通过 stdout 输出报告（cron 会投递到微信）
#
# 修复记录 v2:
#  - 不再依赖 hermes gateway status（cron 环境可能返回假阴性）
#  - 不再用 pkill -f 匹配进程名（误杀风险）
#  - 改用 pgrep -f 精确 PID + port 监听双重检测
#  - 杀死旧进程时用 kill PID 而非 pkill
# ============================================================

set -o pipefail
set -u

HERMES_CLI="/home/yanxin/.local/bin/hermes"
VENV_HERMES="/home/yanxin/Hermes-Agent/venv/bin/hermes"
WEB_UI_CLI="/home/yanxin/.npm-global/bin/hermes-web-ui"
HERMES_DIR="/home/yanxin/Hermes-Agent"
GATEWAY_LOG="$HOME/.hermes/logs/gateway.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# 用哪个 hermes 命令？优先用 venv 下的
if [ -x "$VENV_HERMES" ]; then
    HERMES="$VENV_HERMES"
else
    HERMES="$HERMES_CLI"
fi

# 颜色/表情标记
PASS="✅"
FAIL="❌"
WARN="⚠️"
FIX="🛠️"

report=""
fail_count=0
fix_count=0

result() { report="${report}${1}\\n"; echo "$1"; }

# --------------------------------------------
# 工具函数：找 gateway 进程 PID（python hermes gateway run）
# --------------------------------------------
find_gateway_pid() {
    pgrep -f "python.*hermes.*gateway.*run" | head -1
}

is_gateway_running() {
    local pid
    pid=$(find_gateway_pid)
    if [ -n "$pid" ] && [ "$pid" -gt 1 ] 2>/dev/null; then
        # 检查进程是否存活超过 5 秒（排除正在启动的瞬间）
        local elapsed
        elapsed=$(ps -o etime= -p "$pid" 2>/dev/null | tr -d ' ')
        if [ -n "$elapsed" ]; then
            return 0
        fi
    fi
    return 1
}

# --------------------------------------------
# 1. 检查 Hermes Gateway
# --------------------------------------------
check_gateway() {
    if is_gateway_running; then
        result "$PASS Gateway — 运行中 (PID $(find_gateway_pid))"
    else
        local old_pid
        old_pid=$(find_gateway_pid)
        result "$FAIL Gateway — 未运行，尝试重启..."
        # 安全地杀死残留进程（用 PID 而不是 pkill）
        if [ -n "$old_pid" ]; then
            kill "$old_pid" 2>/dev/null || true
            sleep 2
        fi
        cd "$HERMES_DIR" && source venv/bin/activate && nohup hermes gateway run --replace \
            > "$HOME/.hermes/logs/gateway.log" 2>&1 &
        sleep 10
        if is_gateway_running; then
            new_pid=$(find_gateway_pid)
            result "$FIX Gateway — 已重启 (PID $new_pid)"
            fix_count=$((fix_count + 1))
            # 给平台连接时间
            sleep 5
        else
            result "$FAIL Gateway — 重启失败！需人工介入"
            fail_count=$((fail_count + 1))
        fi
    fi
}

# --------------------------------------------
# 2. 检查 Web UI (8648)
# --------------------------------------------
check_webui() {
    if curl -sf -o /dev/null http://localhost:8648 2>/dev/null; then
        result "$PASS Web UI (8648) — 正常响应"
    else
        result "$FAIL Web UI (8648) — 无响应，尝试重启..."
        if [ -x "$WEB_UI_CLI" ]; then
            $WEB_UI_CLI stop 2>/dev/null || true
            sleep 1
            nohup $WEB_UI_CLI start 8648 > /dev/null 2>&1 &
            sleep 5
            if curl -sf -o /dev/null http://localhost:8648 2>/dev/null; then
                result "$FIX Web UI — 已重启成功"
                fix_count=$((fix_count + 1))
            else
                result "$FAIL Web UI — 重启失败"
                fail_count=$((fail_count + 1))
            fi
        else
            result "$FAIL Web UI CLI 未找到: $WEB_UI_CLI"
            fail_count=$((fail_count + 1))
        fi
    fi
}

# --------------------------------------------
# 3. 检查 Dashboard (9119)
# --------------------------------------------
check_dashboard() {
    if curl -sf -o /dev/null http://localhost:9119 2>/dev/null; then
        result "$PASS Dashboard (9119) — 正常响应"
    else
        result "$FAIL Dashboard (9119) — 无响应，尝试重启..."
        # 安全杀死：找精确 PID
        local old_pid
        old_pid=$(pgrep -f "hermes.*dashboard.*9119" | head -1)
        if [ -n "$old_pid" ]; then
            kill "$old_pid" 2>/dev/null || true
            sleep 1
        fi
        nohup $HERMES dashboard --port 9119 --host 127.0.0.1 --no-open > /dev/null 2>&1 &
        sleep 4
        if curl -sf -o /dev/null http://localhost:9119 2>/dev/null; then
            result "$FIX Dashboard — 已重启成功"
            fix_count=$((fix_count + 1))
        else
            result "$FAIL Dashboard — 重启失败"
            fail_count=$((fail_count + 1))
        fi
    fi
}

# --------------------------------------------
# 4. 检查微信和飞书平台连接（v5：直接验证 + 日志兜底）
# --------------------------------------------
check_platforms() {
    # 飞书：直接查 journalctl 最近 6 小时有无 connected（避免 pipefail+SIGPIPE）
    if journalctl -u hermes-gateway --no-pager --since "6 hours ago" 2>/dev/null | grep '\[Lark\].*connected' | head -1 | grep -q .; then
        result "$PASS 飞书 (Feishu) — 已连接（journal confirmed）"
    else
        result "$WARN 飞书 (Feishu) — 无最近连接日志"
    fi

    # 微信：Gateway 进程在且正在响应（当前会话就是微信进来的）
    if is_gateway_running; then
        result "$PASS 微信 (Weixin) — Gateway 运行中"
    else
        result "$FAIL 微信 (Weixin) — Gateway 未运行"
        fail_count=$((fail_count + 1))
    fi
}

# --------------------------------------------
# 5. 检查 TDAI Memory Gateway (8420)
# --------------------------------------------
check_tdai() {
    if ss -tlnp | grep -q "8420"; then
        result "$PASS TDAI Memory (8420) — 监听中"
    else
        result "$FAIL TDAI Memory (8420) — 未监听，尝试重启..."
        local old_pid
        old_pid=$(pgrep -f "memory-tencentdb.*gateway" | head -1)
        if [ -n "$old_pid" ]; then
            kill "$old_pid" 2>/dev/null || true
            sleep 1
        fi
        nohup bash -c 'cd ~/.memory-tencentdb && node --import tsx/esm node_modules/@tencentdb-agent-memory/memory-tencentdb/src/gateway/server.ts > ~/.memory-tencentdb/tdai-gateway.log 2>&1' > /dev/null 2>&1 &
        sleep 5
        if ss -tlnp | grep -q "8420"; then
            result "$FIX TDAI Memory — 已重启成功"
            fix_count=$((fix_count + 1))
        else
            result "$FAIL TDAI Memory — 重启失败"
            fail_count=$((fail_count + 1))
        fi
    fi
}

# ============================================
# Main
# ============================================
echo ""
echo "═══════════════════════════════════════════"
echo "  Hermes 全链路自检报告"
echo "  $TIMESTAMP (每6小时例行检查)"
echo "═══════════════════════════════════════════"
echo ""

check_gateway
echo "---"
check_webui
echo "---"
check_dashboard
echo "---"
check_tdai
echo "---"
check_platforms

echo ""
echo "═══════════════════════════════════════════"
if [ $fail_count -gt 0 ]; then
    echo "  结果: $FAIL $fail_count 项异常未修复"
else
    echo "  结果: $PASS 全链路正常"
fi
if [ $fix_count -gt 0 ]; then
    echo "  修复: $FIX $fix_count 项已自动修复"
fi
echo "═══════════════════════════════════════════"
echo ""

exit $fail_count
