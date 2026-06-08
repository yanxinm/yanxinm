# Cron-pkill 自毁模式 (2026-05-24)

## 事故

自检脚本 v1 在 18:00 第一次运行时，检测 Gateway 后执行了自杀式操作。

## 事件时间线

1. **初始检查** (≈07:39): `hermes gateway status` 返回 `✓ Gateway is running (PID: 25595, 25582)`
2. **Gateway 持续运行**直到 18:00 自检 cron 触发
3. **18:00:18**: 自检脚本发现 Gateway "not running"（假阴性）
4. 脚本执行 `pkill -f "hermes gateway run"` — 杀死了运行中的 Gateway 进程
5. Gateway 收到 SIGTERM，主动向微信发送关机通知，清理断开所有平台连接
6. **18:00:20**: 脚本启动新 Gateway，但旧 Gateway 的日志和新 Gateway 的初始化日志交错，第二个 Gateway 也异常退出（exit code -15）
7. Gateway 彻底下线，直到人工介入重启

## 根因：三层故障叠加

### 1. `hermes gateway status` 在 cron 环境假阴性

Cron 作业通过 `no_agent=true` 的脚本执行，其 shell 环境（无 TTY、无 XDG 会话、无登录 shell）导致 `hermes gateway status` 无法找到 PID 文件或通信 socket，返回了 `✗ Gateway is not running`——尽管 Gateway 进程实际存活、端口正常监听。

**规避 (v2)**: 不再依赖 `hermes gateway status` 命令，改用 `pgrep -f "python.*hermes.*gateway.*run"` 直接检测 Python 进程，配合 `ps -o etime=` 检查进程运行时长排除启动瞬态。

### 2. `pkill -f "hermes gateway run"` 的模糊匹配

`pkill -f "hermes gateway run"` 匹配所有包含 `hermes gateway run` 字符串的命令行——包括整个进程树。它不仅匹配：
- 实际的 Gateway Python 进程 (`python3 ... hermes gateway run --replace`)
- 包裹 Gateway 的 bash 启动脚本 (`/usr/bin/bash -lic ... hermes gateway run --replace`)

而且此模式不区分是目标进程还是脚本自身进程树的父/子/兄弟进程。

**规避 (v2)**: 
- ❌ 不再使用 `pkill -f`
- ✅ 改用 `pgrep -f` 获取精确 PID，再用 `kill $PID` 逐个清理
- ✅ Dashboard 也同理：`pgrep -f "hermes.*dashboard.*9119" | head -1` + `kill`

### 3. Gateway 日志交错导致误判

旧 Gateway 关闭时的日志（`[Weixin] Disconnected`, `Cron ticker stopped`, `Exiting with code 1`）和新 Gateway 启动的日志（`restored 1 context token`, `Gateway running with 3 platform(s)`）在日志文件中交错出现，使得事后排查时需要仔细辨别两条进程的各自时间线。

## 教训：cron 自检脚本 Iron Rules

1. **永不使用 `pkill -f` 杀本家进程** —— `pkill -f "hermes gateway run"` 是自残行为
2. **永不只依赖 CLI 自检命令** —— `hermes gateway status` 在 cron 环境不可靠
3. **永远三重检测进程存活**：`pgrep` 查 PID → `ps` 查运行时长 → `ss` 查端口
4. **杀死旧进程时用精确 PID**，不模糊匹配
5. **重启后等待足够时间**（Gateway 至少 10s + 5s 平台握手，共 15s）
