# WeChat iLink 静默断开实战复盘（2026-06-10）

## 场景

用户通过微信对 Agent 说话，Agent 无响应。用户反馈"跟你说话没反应啊"。

## 初始伪装

- `hermes gateway status` — 虽然命令在 PATH 外无法直接调用，但端口检查显示 Gateway (8642) 监听正常
- 进程列表显示 `hermes gateway run --replace` (PID 176716) 存活，已运行 4 小时
- 健康检查 `curl http://127.0.0.1:8642/health` → `{"status": "ok"}`

## 关键发现

### 1. 日志时间戳揭示真实状态

检查 `~/.hermes/logs/gateway.log` 发现：

```
最后 inbound: 14:30:30 — 用户发"我们用方案一，这个任务记住，我回家可以操作时再继续"
最后 response: 14:30:49 — Gateway 发送了 126 字符回复
之后 → 完全静默（无新 inbound、无 poll 事件、无 error）
```

用户反馈"没反应"时的时间是 14:38。Gateway 进程健康但没有收到新消息。

### 2. gateway_state.json 不存在

`~/.hermes/gateway_state.json` 文件不存在。较新的 Hermes 版本用 `state.db` (SQLite) 存储状态，不写 JSON 文件。所以依赖 `gateway_state.json` 的排障步骤失效。

### 3. 日志位置因启动方式而异

检查结果：
- **systemd 启动的 Gateway** → 日志在 `~/.hermes/logs/gateway.log`（默认 profile）
- **profile 模式启动** → 日志在 `~/.hermes/profiles/<profile>/logs/gateway.log`
- 本例中使用 systemd 启动，日志在默认位置

### 4. systemd Gateway 的 FD 结构

```
/proc/176716/fd/
  fd 0 → /dev/null
  fd 1 → socket (stdout 走 socket，非日志文件)
  fd 2 → socket (stderr 走 socket)
  没有 log 文件 FD
```
这是因为 systemd 接管了 stdout/stderr，不向文件写日志。

## 诊断流程（已验证可行）

```bash
# 1. 确认 Gateway 进程存活
ps aux | grep "hermes gateway run" | grep -v grep

# 2. 找到正确的日志文件（systemd 启动 → 默认位置）
LOG=~/.hermes/logs/gateway.log

# 3. 检查最后 inbound 消息
echo "最后 inbound: $(grep 'inbound from=o9cq801d' $LOG | tail -1)"
echo "最后 response: $(grep 'Sending response.*o9cq801d' $LOG | tail -1)"
echo "当前时间: $(date '+%Y-%m-%d %H:%M:%S')"

# 4. 判断：如果最后 inbound 在几分钟前且无新消息 → 静默断开
```

## 修复

利用 systemd 的 `Restart=always` 自动重新拉起：

```bash
kill $(pgrep -f "hermes gateway run")
# systemd 检测到退出 → 10-15 秒内自动重启
sleep 20
# 验证 3 个平台全部连线
tail -5 ~/.hermes/logs/gateway.log | grep 'Gateway running with'
```

预期输出：
```
✓ api_server connected
✓ feishu connected
✓ weixin connected
Gateway running with 3 platform(s)
```

## 经验教训

1. **「Gateway 显示 connected ≠ 实际可收发」** — iLink WebSocket 可以静默断开而不在日志留下错误。唯一靠谱的指标是最后 inbound 时间戳。
2. **gateway_state.json 不可靠** — 新版本可能没有这个文件。用 gateway.log 时间戳代替。
3. **pkill -f 自毁** — `pkill -f "hermes gateway"` 会杀死所有匹配进程（Gateway + TUI slash workers + 可能的 Agent 进程）。用 `kill $(pgrep -f)` 更安全，尽管 skill 已经记录了这个陷阱，实际操作中还是容易犯。当 terminal 命令被 `exit -15`（SIGTERM）终止时，就是自毁了。
4. **systemd 重启有 10-15 秒间隙** — 重启期间 WeChat 消息无法到达，但重启完成后自动恢复。
