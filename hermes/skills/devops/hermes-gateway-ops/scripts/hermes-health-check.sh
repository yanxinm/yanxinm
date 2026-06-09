#!/bin/bash
# ============================================================
# Hermes 全链路自检脚本 — 每6小时由 cron 触发
# 位置: ~/.hermes/skills/devops/hermes-gateway-ops/scripts/hermes-health-check.sh
# cron 引用: ~/.hermes/scripts/hermes-health-check.sh (自动同步)
# 使用: 通过 cron job 以 no_agent=true 方式运行
# 检查: Gateway | Web UI | Dashboard | TDAI Memory | 微信 | 飞书
# 发现异常自动修复，输出报告通过 cron deliver 投递到渠道
#
# v2 关键修复 (2026-05-24):
#  - 不再依赖 hermes gateway status（cron 环境可能返回假阴性）
#  - 不再用 pkill -f 模糊匹配进程名（曾误杀运行中的 Gateway + Dashboard）
#  - 改用 pgrep -f 精确 PID + kill PID 安全清理
#  - Gateway 检测改为直接查 python 进程存活 + ps 运行时长双重验证
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

PASS="✅"
FAIL="❌"
WARN="⚠️"
FIX="🛠️"

report=""
fail_count=0
fix_count=0

result() { report="${report}${1}\\n"; echo "$1"; }

# ---- 工具: 安全地找 Gateway 进程 PID (python hermes gateway run) ----
find_gateway_pid() {
    pgrep -f "python.*hermes.*gateway.*run" | head -1
}

is_gateway_running() {
    local pid
    pid=$(find_gateway_pid)
    if [ -n "$pid" ] && [ "$pid" -gt 1 ] 2>/dev/null; then
        local elapsed
        elapsed=$(ps -o etime= -p "$pid" 2>/dev/null | tr -d ' ')
        if [ -n "$elapsed" ]; then
            return 0
        fi
    fi
    return 1
}

# ---- 1. Gateway ----
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
            sleep 5  # 给平台连接时间
        else
            result "$FAIL Gateway — 重启失败！需人工介入"
            fail_count=$((fail_count + 1))
        fi
    fi
}

# ---- 2. Web UI ----
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

# ---- 3. Dashboard ----
check_dashboard() {
    if curl -sf -o /dev/null http://localhost:9119 2>/dev/null; then
        result "$PASS Dashboard (9119) — 正常响应"
    else
        result "$FAIL Dashboard (9119) — 无响应，尝试重启..."
        # 安全杀死：找精确 PID 再 kill
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

# ---- 4. TDAI Memory (port check, not HTTP check - returns 404 on GET /) ----
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

# ---- 5. 微信 & 飞书平台连接（v3：时间窗口+消息印证+进程推断）----
check_platforms() {
    if [ ! -f "$GATEWAY_LOG" ]; then
        result "$WARN 平台 — 无法读取 gateway 日志"
        fail_count=$((fail_count + 1))
        return
    fi

    local now_epoch cutoff_epoch
    now_epoch=$(date +%s)
    cutoff_epoch=$((now_epoch - 1800))  # 30分钟窗口

    # 辅助：日志行是否在时间窗口内
    log_line_in_window() {
        local line="$1"
        local ts
        ts=$(echo "$line" | sed -n 's/^\([0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\} [0-9]\{2\}:[0-9]\{2\}:[0-9]\{2\}\).*/\1/p')
        if [ -z "$ts" ]; then return 1; fi
        local line_epoch
        line_epoch=$(date -d "$ts" +%s 2>/dev/null || echo 0)
        [ "$line_epoch" -ge "$cutoff_epoch" ]
    }

    check_one_platform() {
        local tag="$1" name="$2"
        local connected disconnected recent_conn recent_disc recent_msg

        connected=$(grep -E "\[$tag\] Connected" "$GATEWAY_LOG" 2>/dev/null | tail -1)
        disconnected=$(grep -E "\[$tag\] Disconnected" "$GATEWAY_LOG" 2>/dev/null | tail -1)

        recent_conn=$(grep -E "\[$tag\] Connected" "$GATEWAY_LOG" 2>/dev/null | tail -1)
        [ -n "$recent_conn" ] && ! log_line_in_window "$recent_conn" && recent_conn=""
        recent_disc=$(grep -E "\[$tag\] Disconnected" "$GATEWAY_LOG" 2>/dev/null | tail -1)
        [ -n "$recent_disc" ] && ! log_line_in_window "$recent_disc" && recent_disc=""

        recent_msg=$(grep -E "\[$tag\] (inbound|Sending response)" "$GATEWAY_LOG" 2>/dev/null | tail -1)
        [ -n "$recent_msg" ] && ! log_line_in_window "$recent_msg" && recent_msg=""

        # a. 30分钟内 Connected → ✅
        if [ -n "$recent_conn" ] && [ -z "$recent_disc" ]; then
            result "$PASS $name ($tag) — 已连接（最近确认）"; return
        fi
        # b. 30分钟内 Disconnected → ❌
        if [ -n "$recent_disc" ]; then
            result "$FAIL $name ($tag) — 最近断开"; fail_count=$((fail_count + 1)); return
        fi
        # c. 30分钟内有消息 → ✅
        if [ -n "$recent_msg" ]; then
            result "$PASS $name ($tag) — 活跃中（有消息往来）"; return
        fi
        # d. 历史 Connected + Gateway 正常 → ✅
        if [ -n "$connected" ] && [ -z "$disconnected" ]; then
            result "$PASS $name ($tag) — 已连接（历史确认，Gateway正常）"; return
        fi
        # e. Connected vs Disconnected 时间戳比较
        if [ -n "$connected" ] && [ -n "$disconnected" ]; then
            local conn_ts disc_ts
            conn_ts=$(echo "$connected" | sed -n 's/^\([0-9-]* [0-9:]*\).*/\1/p')
            disc_ts=$(echo "$disconnected" | sed -n 's/^\([0-9-]* [0-9:]*\).*/\1/p')
            if [ -n "$conn_ts" ] && [ -n "$disc_ts" ] && [[ "$conn_ts" > "$disc_ts" ]]; then
                result "$PASS $name ($tag) — 已连接（已恢复）"; return
            elif echo "$disconnected" | grep -q "Disconnected" && [ -z "$recent_msg" ]; then
                result "$FAIL $name ($tag) — 已断开，无恢复迹象"; fail_count=$((fail_count + 1)); return
            fi
        fi
        # f. Gateway 稳定但无日志 → ⚠️ 轻度警告
        if is_gateway_running; then
            local gw_pid gw_uptime
            gw_pid=$(find_gateway_pid)
            gw_uptime=$(ps -o etime= -p "$gw_pid" 2>/dev/null | tr -d ' ')
            if echo "$gw_uptime" | grep -qE ':[0-9]{2}|[0-9]+-'; then
                result "$WARN $name ($tag) — 状态未知，但Gateway稳定运行中"; return
            fi
        fi
        # g. 彻底未知
        result "$WARN $name ($tag) — 状态未知（无日志）"
    }

    check_one_platform "Weixin" "微信"
    check_one_platform "Feishu" "飞书"
}

# ====== Main ======
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
