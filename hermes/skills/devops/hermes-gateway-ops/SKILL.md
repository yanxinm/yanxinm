---
name: hermes-gateway-ops
description: Hermes Gateway 运维操作——健康检查、故障诊断、服务恢复及平台连通性验证。覆盖 Gateway、Web UI、Dashboard、TDAI Memory Gateway 以及微信/飞书等消息通道的全链路检测。
tags: [gateway, ops, monitoring, health-check, wechat, feishu, recovery]
---

# Hermes Gateway 运维操作技能

> **⚠️ 机器端口差异：** 以下文档描述了两套部署拓扑。
> - **Ethan 笔记本 (WSL2)**：Dashboard 独立在端口 **9119**，Web UI 在 8648
> - **基地 M710q (Linux 物理机)**：Dashboard 集成在 Web UI 中，统一端口 **8648**，无独立 9119 服务
> 
> 操作前先确认当前主机，用 `ss -tlnp | grep -E '8642|8648|8420|9119'` 查看实际监听端口。

## 触发条件

- 用户要求检查服务是否正常
- 用户反馈微信/飞书消息无响应
- 怀疑 Gateway 进程崩溃
- 系统启动后需要验证全链路连通性
- Web UI 或 Dashboard 访问失败
- Desktop 远程后端显示“网关断开”或任务跑着跑着失联
- Desktop 反复“提示词发送失败”或“代理 1 个失败”，但 `9119/8642/8648/8420` 端口看似都在线
- 设置开机自启、保活、常年挂机（systemd / 任务计划程序）

## 一、全链路健康检查步骤

### 1.1 检查 Hermes Gateway 进程

```bash
hermes gateway status
```

- ✅ `✓ Gateway is running (PID: XXX)` → 进程存在
- ❌ `✗ Gateway is not running` → 需要重启

**⚠️ 陷阱一：进程存在 ≠ 运行正常。Gateway 可能在启动后立刻崩溃，但 hermes gateway status 误报。**
**解决方案：同时检查 gateway.log 的时间戳是否在持续更新，并用 `ss -tlnp` 确认所有端口都在监听。**
**⚠️ 陷阱二：`hermes gateway status` 可能在上次正常运行时缓存了状态，再次调用时已变 `✗ Gateway is not running`。如果第一次返回 running 但几分钟后检查又显示 not running，说明 Gateway 在悄悄崩溃。**

### 1.2 检查 Gateway 日志验证平台连接

```bash
# 检查最近一次启动是否完成了所有平台连接
tail -30 ~/.hermes/logs/gateway.log | grep -E 'running with|connected'

# 预期输出示例（3 个平台）：
# ✓ api_server connected
# ✓ feishu connected
# ✓ weixin connected
# Gateway running with 3 platform(s)
```

**关键信号：**
- 日志末尾看到 `Gateway running with X platform(s)` → 启动完成
- 日志末尾停留在启动过程（无 `running with` 行）→ Gateway 启动被中断或崩溃
- 缺少 `✓ weixin connected` → 微信平台连接失败
- 缺少 `✓ feishu connected` → 飞书连接失败

### 1.3 检查 Web UI (8648) 和 Dashboard

**⚠️ 端口因机器而异：** Ethan (WSL2) 上 Dashboard 为 9119，基地 M710q 上 Dashboard 集成在 Web UI 8648。

```bash
# 通用检查 — 看实际监听哪些端口
ss -tlnp | grep -E '8648|9119'
```

验证 Web UI：
```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8648
```

验证 Dashboard（如果独立存在）：
```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:9119
```

- HTTP 200 + 端口在监听 → 正常
- HTTP 000 → 服务未运行，需要启动

### 1.4 检查 TDAI Memory Gateway (8420)

```bash
ss -tlnp | grep 8420
```

TDAI Memory Gateway 是 Node.js 进程，在端口 8420 监听。它是独立于 Hermes Gateway 的组件。

### 1.5 验证消息通道（微信 + 飞书）

```bash
# 查看可用消息目标
send_message list
```

然后发送测试消息：

```bash
# 发送测试消息到微信
send_message target=weixin:USER_ID message="测试消息"
```

**⚠️ 超级陷阱：send_message 在 Gateway 已死时仍返回 success=true！**

这是本会话发现的最危险的坑。即使 `hermes gateway status` 后来显示 `✗ Gateway is not running`，在此之前调用 `send_message` 依然返回 `success=true + mirrored=true`。

**根因：** send_message 工具通过 socket 连接失败后可能从缓存/内存返回假阳性结果，不验证 Gateway 进程实际存活状态。

**三层验证法：**
1. 第一步：执行 `hermes gateway status` 确认 Gateway 进程存活
2. 第二步：调用 `send_message` 发送测试
3. 第三步：等待 3-5 秒，检查 `gateway.log` 确认有 `Sending response` 日志条目

```bash
# 正确的验证流程
hermes gateway status  # 第1步：确认进程
send_message target=weixin:USER_ID message="test"  # 第2步：发送
sleep 5
tail -5 ~/.hermes/logs/gateway.log | grep 'Sending response'  # 第3步：确认送达日志
```

**注意：** 三步缺一不可。只做第2步（send_message 返回 success）没有任何可靠性。**

## 二、服务恢复步骤

### 2.1 重启 Hermes Gateway

#### 标准路径（systemd）

```bash
sudo systemctl restart hermes-gateway
```

#### 无 sudo / systemctl 不可用时

**方法 A — 杀旧进程让 systemd 自动重启：**

```bash
kill $(pgrep -f "hermes gateway run")
# systemd 检测到进程退出后会在 10-15 秒内自动拉起新进程
sleep 15
hermes gateway status
```

**方法 B — 手动前台启动（Agent terminal 中）：**

```bash
# 在 background=true 的 terminal 中执行
# 先 kill 旧进程
kill $(pgrep -f "hermes gateway run")
sleep 2
# 启动新 Gateway
cd ~/.hermes/hermes-agent && source venv/bin/activate && hermes gateway run --replace
```

**⚠️ 注意：** `hermes gateway restart` 可能要求 sudo。`systemctl --user restart` 在 DBUS 未配置时不可用。方法 A 最稳健——利用 systemd 的 `Restart=always` 自动恢复。

**启动后等待 15-20 秒让所有平台完成连接。**

### 2.2 验证启动完成

```bash
# 等待平台连接完成
sleep 15
tail -10 ~/.hermes/logs/gateway.log | grep 'Gateway running with'
```

### 2.3 启动 Gateway（必须先启动）

Web UI 和 Dashboard 都依赖 Gateway 的 API server。**必须先启动 Gateway**，再启动 Web UI/Dashboard。

```bash
cd ~/Hermes-Agent && source venv/bin/activate && nohup hermes gateway run --replace > ~/.hermes/logs/gateway.log 2>&1 &
```

等待 15-20 秒确认所有平台连接完成。

### 2.4 启动 Web UI

```bash
# 使用 npm 全局安装的 hermes-web-ui CLI
# 端口在 hermes-web-ui 配置中指定，无需传参（默认 8648）
hermes-web-ui start
```

如需后台启动（推荐在 Agent terminal 中操作）：
```bash
nohup /home/yanxin/.npm-global/bin/hermes-web-ui start > /dev/null 2>&1 &
```

### 2.5 启动 Dashboard

```bash
hermes dashboard --port 9119 --host 127.0.0.1 --no-open
```

后台启动方式：
```bash
nohup /home/yanxin/.local/bin/hermes dashboard --port 9119 --host 127.0.0.1 --no-open > /dev/null 2>&1 &
```

**⚠️ Dashboard 启动卡在构建循环的修复：** 若 Dashboard 启动后长时间无端口监听（`ss -tlnp | grep 9119` 无输出），可能是 Web UI 构建因 TypeScript 类型检查失败（如 lucide-react 导出不兼容）导致 `tsc -b && vite build` 死循环。跳过类型检查直接构建：

```bash
# 如果 node_modules 不存在（新装/首次），先安装依赖
cd ~/HERMES_PROJECT/web && npm install
# 跳过 tsc 类型检查，直接 vite build
cd ~/HERMES_PROJECT/web && npx vite build
# 构建成功输出: ../hermes_cli/web_dist/
```

> `HERMES_PROJECT` 通常为 `~/.hermes/hermes-agent` 或 `~/Hermes-Agent`，取决于安装方式。用 `hermes --version` 输出的 `Project:` 行确认。

然后重新启动 Dashboard **必须加 `--skip-build`**，否则 Dashboard 会再次尝试 `tsc -b && vite build`，结果变为端口监听但 HTTP 请求超时（HTTP 000 / curl timeout）：

```bash
hermes dashboard --port 9119 --host 127.0.0.1 --no-open --skip-build
```

验证：`curl -s --max-time 3 http://localhost:9119 | head -3` 应返回 HTML。

**⚠️ 绑定 0.0.0.0 需要 --insecure：** Dashboard 绑定非 loopback 地址时会触发 OAuth 认证门控。如需从 Windows 直连 WSL IP 访问：

```bash
hermes dashboard --port 9119 --host 0.0.0.0 --insecure --no-open
```

### 2.6 验证全部就绪

```bash
# 检查所有端口
ss -tlnp | grep -E '8642|8648|9119'

# 检查 Web UI 响应
curl -s http://localhost:8648 | head -3

# 检查 Dashboard 响应
curl -s http://localhost:9119 | head -3

# 检查 Gateway 端口和健康
curl -s http://127.0.0.1:8642/health
```

## 三、故障诊断

### 3.1 Gateway 崩溃检测

**信号：** `hermes gateway status` 显示 running，但 gateway.log 最后时间戳停滞在几分钟前。

**诊断命令：**
```bash
# 查看日志最后更新时间
tail -1 ~/.hermes/logs/gateway.log

# 查看 exit-diag 日志了解崩溃原因
# ⚠️ 注意：外部 SIGTERM 杀进程（非 --replace 更替）时 exit-diag.log 可能无记录
# 详见 references/gateway-external-sigterm-pattern.md
tail -50 ~/.hermes/logs/gateway-exit-diag.log

# 检查进程实际存活
ps aux | grep 'hermes gateway' | grep -v grep
```

### 3.2 微信 iLink 连接问题

**信号：** `✓ weixin connected` 出现，但 iLink token 过期。

**日志关键词：** `weixin: restored 0 context token(s)` — 表示没有有效的 iLink 上下文令牌。
需要重新扫码登录。

**解决：** 手动重启并跟随二维码登录流程。

### 3.3 飞书 WebSocket 断开

**信号：** 飞书消息无响应。

**日志关键词：** `feishu` 相关 error 行。

### 3.4 TDAI Gateway EPIPE 崩溃

**信号：** 微信/飞书消息可达 Hermes，但 Gateway 在回复后崩溃。

**日志关键词（tdai-gw.log）：**
```
Error: write EPIPE
    at Socket._writeGeneric (node:net:971:11)
```

**根因：** TDAI Gateway 通过 IPC socket (`/tmp/hermes-agent-bridge.sock`) 连接到 Hermes Agent bridge。当 bridge 重启或 socket 被重建时，TDAI Gateway 持有的是已关闭的旧 socket 文件描述符，写入时触发 EPIPE 崩溃。

**这是单点故障** — TDAI Gateway 没有掉线重连机制，一旦 IPC 管道断开就崩溃退出。

**解决方案：**
1. 使用 watchdog 脚本每 2 分钟检测端口 8420 是否仍在监听
2. 检测到端口消失 → 自动重启 TDAI Gateway
3. 同时检测 `hermes gateway run` 进程是否存活

### 3.6 iLink 静默断开 / WeChat 消息可达但回复不达

**信号**：Gateway 日志显示 `Sending response (X chars) to o9cq801d...`，但用户微信收不到回复。Gateway 状态仍显示 `weixin: connected`。

**常见原因（按频率排序）：**
1. **iLink 隐式限流** — 短时间内发送多条长回复触发，但不在 Gateway 日志留下 `rate limited` 关键词（区别于 3.5 节显式限流）
2. **iLink session 过期 / WebSocket 静默断开** — 令牌在 Gateway 端仍然有效但服务端已拒绝推送，连接的 WebSocket 被静默关闭（无 disconnect 日志）。这是最常见的形式：**Gateway 显示 connected，日志最后一条 inbound 停留在几分钟前，用户后续消息永远到不了**。
3. **IPC socket 重建** — 参见 3.4 节 TDAI Gateway EPIPE 模式，Hermes Agent bridge 重启导致 TDAI Gateway 与 Hermes 的通信管道断裂

**排查步骤（按可靠性排序）：**

**方法 A（推荐 — 最可靠）：检查 gateway.log 最后 inbound 时间戳**
```bash
# 查看最后一条 WeChat 入站消息的时间
grep "inbound from=o9cq801d" ~/.hermes/logs/gateway.log | tail -1

# 查看最后一条已发送的响应
grep "Sending response.*o9cq801d" ~/.hermes/logs/gateway.log | tail -1

# 对比当前时间。如果最后 inbound 是几分钟前且没有新的，说明连接已死
date '+%Y-%m-%d %H:%M:%S'
```
判定规则：
- 最后 inbound < 30 秒前 → 连接正常
- 最后 inbound > 2 分钟前 + Gateway 进程健康 + 用户确认发了消息 → 静默断开，必须重启
- 最后 inbound > 2 分钟前 + Gateway 还在处理（日志有后续 activity） → 正常，只是用户没发新消息

**方法 B（备选）：检查 gateway_state.json 的 weixin.updated_at**
```bash
cat ~/.hermes/gateway_state.json 2>/dev/null | python3 -m json.tool 2>/dev/null | grep -A2 weixin
```
⚠️ **陷阱：gateway_state.json 可能不存在**（Hermes 新版本会写入 state.db 而非 JSON 文件）。不存在时退回到方法 A。

**方法 C：检查 Gateway 进程的日志文件描述符**
```bash
# 确认 Gateway 实际写日志的位置
ls -la /proc/$(pgrep -f "hermes.*gateway.*run" | head -1)/fd/ 2>/dev/null | grep log
```
- 如果有 log FD → 知道日志文件路径
- 如果 stdout/stderr 指向 socket（systemd 管理时常见） → 日志可能在 systemd journal 或 Web UI bridge 管理中

**日志位置注意事项：**
- **systemd 管理的 Gateway**（基地 M710q）：日志写入 `~/.hermes/logs/gateway.log`（默认 profile）
- **profile 环境运行的 Gateway**（`hermes gateway run --profile xxx`）：日志写入 `~/.hermes/profiles/<profile>/logs/gateway.log`
- 排查时先确认 Gateway 是用 systemd 启动的还是 profile 启动的。systemd 管理的版本**不会**向 profile-specific 日志写内容。

**修复：**
```bash
# 标准修复：重启 Gateway 重建所有平台连接
# 方法 A — 利用 systemd 自动重启（推荐，无需 sudo kill 具体 PID）
kill $(pgrep -f "hermes gateway run")
sleep 20
# 验证重连
tail -5 ~/.hermes/logs/gateway.log | grep 'Gateway running with'
```
等待 10-15 秒后验证日志中出现 `Gateway running with 3 platform(s)` 且 `weixin: connected`。


**信号：** Gateway 日志显示 `Sending response (X chars) to o9cq801d...`，但用户收不到微信回复。

**日志关键词：**
```
ERROR gateway.platforms.weixin: [Weixin] send failed to=o9cq801d: iLink sendmessage rate limited: ret=-2 errcode=None errmsg=rate limited
```

**常见原因：**
- iLink 短时间发送过多消息触发限流（10 秒内多条长回复）
- iLink 账号 session 过期但门控状态仍显示 `connected`
- iLink WebSocket 连接被静默关闭（无 disconnect 日志）

**排查步骤：**
1. 检查 `gateway.log` 是否有 `rate limited` 日志
2. 检查 `gateway_state.json` 中 `weixin` 的 `updated_at` 时间戳是否较新
3. 如果时间戳已停滞→重启 gateway

**修复：** `hermes gateway run --replace` 强制重新连接所有平台。

### 3.7 API Server 认证问题

**3.7a — API_SERVER_KEY 强制要求（v0.16+）**

新版 Hermes（v0.16+）**强制要求** API_SERVER_KEY，即使绑定 127.0.0.1 也要。

**信号：** Gateway 日志显示 `Gateway running with 2 platform(s)` 而不是 3，且日志中出现：
```
ERROR gateway.platforms.api_server: [Api_Server] Refusing to start: API_SERVER_KEY is required for the API server, including loopback-only binds on 127.0.0.1.
WARNING gateway.run: ✗ api_server failed to connect
INFO gateway.run: Starting reconnection watcher for 1 failed platform(s): api_server
```

此时 Web UI（8648）虽然能打开页面，但聊天功能完全不可用——用户输入消息后报 `Error: API Error 500: Internal Server Error`。

**原因：** `.env` 中的 `API_SERVER_KEY` 被删除或未设置。Gateway 的重连 watcher 只检查 `.env`，不检查 `config.yaml`。用 `hermes config set platforms.api_server.key xxx` 写入 config.yaml **无法生效**，必须写入 `.env`。

**修复：**
```bash
# 设置 API_SERVER_KEY（写入 .env）
echo 'API_SERVER_KEY=your-key-here' >> ~/.hermes/.env

# 重启 Gateway
sudo systemctl restart hermes-gateway.service

# 验证（应看到 3 platform(s)）
tail -5 ~/.hermes/logs/gateway.log | grep 'running with'
```

如果没有 systemd：
```bash
# 停旧进程
kill $(pgrep -f "hermes gateway run")
# 启动新进程
cd ~/.hermes/hermes-agent && source venv/bin/activate && hermes gateway run --replace
```

**3.7b — Web UI 报 500 实际是 Gateway API 401**

**信号：** Web UI 登录正常（能打开页面、输入 token），但发送聊天消息后显示 `Error: API Error 500: Internal Server Error`。Gateway 日志中有：
```
WARNING gateway.platforms.api_server: API server rejected invalid API key: remote='127.0.0.1'
```

**根因：** Web UI 向 Gateway 的 API Server（8642）发起 chat 请求时没带正确的 API Key。Gateway 返回 401，Web UI 把 401 包装成 500 展示给用户。

**排查：**
```bash
# 确认 API Server 是否在拒绝请求
grep 'rejected invalid API key' ~/.hermes/logs/gateway.log | tail -5

# 确认 API_SERVER_KEY 是否配置
grep 'API_SERVER_KEY' ~/.hermes/.env
```

**修复：** 确保 `.env` 中有 `API_SERVER_KEY`，且 Gateway 重启后 api_server 平台连接成功（3/3 platforms）。

启动脚本位于 `C:\Tools\hermes-gateway-start.bat`，由任务计划程序 `Hermes Gateway` 在登录时触发。

**⚠️ 致命陷阱：多个独立 `wsl.exe` 调用会创建互相隔离的 WSL 会话。** 前一个 `wsl.exe` 退出时，WSL 会回收该会话内所有 `nohup &` 后台进程。只有最后一个保持前台阻塞的 `wsl.exe` 中的进程能存活。4 个独立 `wsl.exe` 调用的脚本模式在重启后必定丢失前 3 个服务。

**v2 修复（2026-06-02）：** 合并为单个 `wsl.exe` 调用，所有服务在同一 WSL 会话内启动。Gateway 放在最后前台阻塞以保持 WSL 存活。

```
wsl.exe -d Ubuntu -u yanxin bash -lc "
  export PATH=\"\$HOME/.npm-global/bin:\$HOME/.local/bin:\$PATH\"

  nohup hermes-web-ui start > /dev/null 2>&1 &
  sleep 3

  nohup bash -c 'cd ~/.memory-tencentdb && node ...' > /dev/null 2>&1 &
  sleep 3

  nohup hermes dashboard --port 9119 --host 127.0.0.1 --no-open > /dev/null 2>&1 &
  sleep 8

  # 端口验证
  ss -tlnp | grep -E '8648|8420|9119'

  # Gateway 最后，前台阻塞保持 WSL 存活
  cd /home/yanxin/Hermes-Agent && source venv/bin/activate && hermes gateway run --replace
"
```

**关键点：**
- 单次 `wsl.exe` 调用内串行启动全部 4 个服务
- 显式 `export PATH` 避免 `bash -lc` 非交互模式缺失 `~/.npm-global/bin` 和 `~/.local/bin`
- 每步之间 `sleep` 让服务有时间完成初始化
- Gateway 必须最后启动且前台运行（阻塞 `wsl.exe`），这是 WSL 会话存活的锚点

## 四-B、Linux systemd 自启（无显示器/常年挂机）

适用场景：Linux 物理机/虚拟机，需要开机自动拉起全部 4 个服务，无需用户登录。

> 详细 systemd unit 文件模板见 `references/systemd-auto-start.md`。

### 服务列表与启动顺序

| 序号 | 服务 | 端口 | Type | 依赖 |
|------|------|------|------|------|
| 1 | hermes-tdai | 8420 | simple | network-online |
| 2 | hermes-web-ui | 8648 | forking | network-online |
| 3 | hermes-dashboard | 9119 | simple | web-ui (可选) |
| 4 | hermes-gateway | 8642 | simple | tdai + web-ui + dashboard |

Gateway 必须在最后启动，且 `After=` 声明对前三个的依赖。

### 快速部署

```bash
# 1. 创建 4 个 service 文件到 /etc/systemd/system/
#    模板见 references/systemd-auto-start.md

# 2. 重载并启用
sudo systemctl daemon-reload
sudo systemctl enable hermes-tdai hermes-web-ui hermes-dashboard hermes-gateway

# 3. 停掉手动启动的旧进程（如有），再启动 systemd 版
sudo systemctl start hermes-tdai hermes-web-ui hermes-dashboard hermes-gateway

# 4. 验证
sudo systemctl status hermes-tdai hermes-web-ui hermes-dashboard hermes-gateway --no-pager
ss -tlnp | grep -E '8420|8642|8648|9119'
```

### 关键配置要点

- **User=** 设为主机用户名（如 `miao`），不要用 root
- **ExecStart=** 使用绝对路径。hermes 在 venv 中：`/home/<user>/.hermes/hermes-agent/venv/bin/hermes`；hermes-web-ui 的绝对路径通过 `npm config get prefix` 确认
- **Restart=always + RestartSec=10~15s**：进程崩溃自动复活
- **WantedBy=multi-user.target**：系统启动时自动拉起，无需用户登录
- **TDAI 的 ExecStart**：`node --import tsx/esm node_modules/@tencentdb-agent-memory/memory-tencentdb/src/gateway/server.ts`，WorkingDirectory 为 `~/.memory-tencentdb/`

### 迁移旧进程到 systemd

如果服务已在手动运行，切换到 systemd 时注意端口冲突：

```bash
# 1. 停旧进程（TDAI 和 Web UI 需要手动 kill，因为它们不是 systemd 管的）
sudo systemctl stop hermes-gateway    # 如果已在 systemd
kill $(ss -tlnp | grep 8648 | grep -oP 'pid=\K\d+')  # Web UI
kill $(ss -tlnp | grep 8420 | grep -oP 'pid=\K\d+')  # TDAI
# 2. 等端口释放
sleep 3
# 3. 启动 systemd 版
sudo systemctl start hermes-tdai hermes-web-ui hermes-dashboard hermes-gateway
```

**⚠️ 陷阱：** 如果在旧 Gateway 进程存活时启动 systemd 版，新 Gateway 会因为端口 8642 已被占用而无法绑定。必须先停旧的。

### Headless sudo

无显示器主机执行 `sudo` 命令（安装软件、启停服务），将密码写入 `~/.hermes/.env`：

```bash
echo 'SUDO_PASSWORD=*** >> ~/.hermes/.env
```

Hermes 的 terminal 工具自动读取。不要用 `echo password | sudo -S cmd`——会被安全策略拦截。详见 `references/headless-sudo.md`。

## 五、常见陷阱汇总

| 陷阱 | 说明 | 规避方法 |
|------|------|----------|
| **API_SERVER_KEY 强制要求（即使 loopback）** | v0.16.0+ 中 API_SERVER_KEY 对 loopback 绑定也是强制要求，缺失时 api_server 拒绝启动 | `.env` 中必须设置 `API_SERVER_KEY`；Web UI 自动从中读取 |
| send_message 假成功 | 返回 success 但 Gateway 已死，消息未实际送达 | 检查 gateway.log 确认有 Sending response 日志 |
| gateway status 误报 | 进程 zombie 但实际不可用 | 结合日志时间戳判断 |
| 微信 iLink 令牌过期 | 显示 connected 但 token 已失效 | 检查 restored context token 数量 |
| Web UI/Dashboard 未自启 | 仅 Gateway 运行，但辅助服务未启动 | 明确检查 8648/9119 两个端口 |
| **send_message 在 Gateway 已死时仍返回 success** | 这是最大陷阱：即使 Gateway 彻底挂掉，send_message 可能返回 success=true + mirrored=true | 必须三步验证：gateway status → send_message → 检查 log 的 Sending response 条目 |
| **TDAI Memory 返回 404 但不是故障** | TDAI Memory Gateway 的 GET / 返回 404 Not Found，端口实际正常 | 用 `ss -tlnp \| grep 8420` 检查端口监听，不要用 curl HTTP 状态码 |
| **cron 环境下 gateway status 假阴性** | `hermes gateway status` 在 cron shell 中可能返回 not running，即使进程正常 | 用 `pgrep -f "python.*hermes.*gateway.*run"` 直接查进程 |
| **pkill -f 自毁** | `pkill -f "hermes gateway run"` 会匹配所有包含该字符串的进程，包括被监控进程本身 | 用 `pgrep` 获取精确 PID → `kill $PID`，绝不使用 pkill -f 杀本家进程 |
| **Dashboard 构建死循环** | `lucide-react` 版本升级后 `tsc -b` TypeScript 类型检查报错（如 `PanelLeftClose` 无导出），导致 `tsc -b && vite build` 中 `vite build` 永远不执行，Dashboard 启动无限重试。2026-06-01 确认 lucide-react 0.577.0 + `verbatimModuleSyntax: true` 触发此问题。**次级症状：** 手动 `npx vite build` 后不加 `--skip-build` 重启 Dashboard，端口会监听但 HTTP 请求超时（HTTP 000）— 因为 Dashboard 再次进入构建流程卡住。 | 跳过类型检查直接构建：`cd ~/Hermes-Agent/web && npx vite build`，dist 输出到 `../hermes_cli/web_dist/`。构建完成后启动 Dashboard **必须加 `--skip-build`**：`hermes dashboard --port 9119 --host 127.0.0.1 --no-open --skip-build`。长期方案：将 `package.json` 中 `"build"` 改为 `"vite build"` 或升级 lucide-react 类型声明。 |
| **WSL 独立会话隔离导致启动脚本丢失服务** | 多个独立 `wsl.exe` 调用各自创建独立 WSL 会话，前一个 `wsl.exe` 退出时回收该会话内所有 `nohup &` 进程。4 个服务的 .bat 脚本重启后必定丢失前 3 个（只有 Gateway 因前台阻塞存活）。2026-06-02 实战确认。 | 合并为单个 `wsl.exe` 调用，所有服务在同一会话内串行启动，Gateway 最后前台阻塞。详见 §四。 |
| **WSL2 localhost 转发失效** | WSL2 重启后 localhost 从 Windows 无法访问 WSL 端口，但服务内部正常 | 用 WSL 直连 IP 作为回退：`curl -s http://$(ip addr show eth0 \| grep 'inet ' \| awk '{print $2}' \| cut -d/ -f1):8648/`。或重启 WSL：`wsl --shutdown`（PowerShell）后重新打开终端。 |
| **外部 SIGTERM 杀 Gateway 时 exit-diag 无记录** | Gateway 被 bash wrapper 等外部 SIGTERM 杀死时，gateway.log 有完整 shutdown 日志但 exit-diag.log 可能完全无对应条目 | 诊断时 gateway.log 是权威来源，exit-diag.log 是补充而非替代；详见 `references/gateway-external-sigterm-pattern.md` |
| **systemd PATH 不含用户本地 bin → Web UI 用错 Node 版本** | systemd 默认 PATH 不含 `~/.local/bin`，`hermes-web-ui start` 的 `#!/usr/bin/env node` 找到系统旧版 Node（v18），新版 Web UI（≥0.6.x）需要 `node:sqlite` 等 v22 特性 | 在 `[Service]` 段显式设置 `Environment=PATH=/home/<user>/.local/bin:/usr/local/bin:/usr/bin:/bin` |
| **hermes-web-ui 在非交互 shell 中找不到命令** | 在 systemd / cron / `terminal(background=true)` 等非交互 shell 中，`hermes-web-ui` 可能不在 PATH 中（即使用户 shell 中 `which hermes-web-ui` 能找到）。这与 `~/.npm-global/bin` 不在非交互 shell 的 PATH 中有关。 | 使用绝对路径。npm 全局 prefix 可通过 `npm config get prefix` 获取，bin 路径为 `<prefix>/bin/hermes-web-ui`。常见值：`~/.hermes/node/bin/hermes-web-ui` 或 `~/.npm-global/bin/hermes-web-ui`。 |
| **hermes-web-ui stop 不杀服务器进程** | `hermes-web-ui stop` 只杀 stop 自身 wrapper 进程，不杀实际监听的 node 服务器进程。再次 `hermes-web-ui start` 会报 `already running`。 | 用 `kill <PID>` 直接杀服务器 PID（从 `ss -tlnp | grep 8648` 获取），删除 `~/.hermes-web-ui/server.pid`，再启动。 |
| **Web UI 设置页改密码/用户名报错（v0.6.11 bug）** | `/api/auth/change-password` 和 `/api/auth/change-username` 即使携带有效 JWT 也返回 401。浏览器端报错无有用信息。 | 直接操作 SQLite 数据库修改。详见 `references/webui-user-management.md`。 |
| **API_SERVER_KEY 现在强制要求（v0.16+）** | 删除 API_SERVER_KEY 或用 config.yaml 设置后，Gateway 的 api_server 平台拒绝启动（日志：`Refusing to start: API_SERVER_KEY is required ... including loopback-only binds on 127.0.0.1`）。只有 2/3 平台在线，Web UI 聊天功能完全瘫痪。`hermes config set` 写入 config.yaml 不被 Gateway 重连 watcher 读取。 | **必须写入 .env**：`echo 'API_SERVER_KEY=xxx' >> ~/.hermes/.env`，然后重启 Gateway。 |
| **Gateway 重启无 sudo 权限** | `hermes gateway restart` 要求 sudo（系统级服务），`systemctl --user` 在 DBUS 不可用时失败。 | 方法A：`kill $(pgrep -f "hermes gateway run")` 利用 systemd `Restart=always` 自动拉起。方法B：手动 `hermes gateway run --replace`。见 §二-2.1。 |
| **API Server 绑定 127.0.0.1 外部设备无法访问** | Web UI 在另一台设备上时，默认 127.0.0.1 绑定只能本机访问。 | `hermes config set platforms.api_server.extra.host 0.0.0.0` + 重启 Gateway。详见 `references/remote-webui-access.md`。 |
| **API Server 0.0.0.0 配置重启后丢失** | 已正确设为 `0.0.0.0`，但系统重启/sytemd 重启后回退到 `127.0.0.1`。`ss -tlnp` 显示 `127.0.0.1:8642` 而非 `0.0.0.0:8642`。症状：笔记本 Tailscale IP 访问 `http://100.x.x.x:8642/health` 超时，Dashboard 显示"网关启动失败"。根因可能：(1) `hermes config set` 写到错误 profile（活跃 profile ≠ default）；(2) default config 中 `platforms.api_server` 段不存在，Gateway 无法读取配置回退到默认值。完整诊断路径见 `references/api-server-config-missing.md`。 | 重启后验证：`ss -tlnp \| grep 8642` 应显示 `0.0.0.0:8642`。若非，参照 `references/api-server-config-missing.md` 诊断 + 修复。建议在自检脚本中增加端口绑定地址检测（不仅是端口是否监听）。 |
| **hermes config set 设到错误 profile** | `hermes config set` 默认写入当前活跃 profile 的 config（可通过 `hermes config path` 确认），可能不是 default profile。2026-06-11 实战：活跃 profile 为 `jike`，config set 写入了 `~/.hermes/profiles/jike/config.yaml` 而非 `~/.hermes/config.yaml`，Gateway 读的是 default config → 修改不生效。 | 明确指定 profile：`hermes -p default config set ...`。操作前先用 `hermes config path` 确认目标文件。 |
| **Tailscale 单向 DERP（A→B 通、B→A 不通）** | 单位防火墙只放行入站 DERP，`tailscale ping` 单向超时但 admin 显示 Connected。 | 笔记本上重启 Tailscale（Exit→重新打开）。详见 `references/tailscale-troubleshooting.md`。 |
| **Node SPA 不转发认证头** | Funnel 指向 Node SPA（8648）时，`X-Hermes-Session-Token` 不会被转发到 Python Dashboard，即使 token 正确也返回 401。 | Funnel 必须直接指向 Python Dashboard（9119），绕过 Node SPA。详见 `references/hermes-desktop-remote-backend.md`。 |
| **Dashboard Host header 拒绝** | Dashboard 绑定 `127.0.0.1` 时，Funnel 转发的 TS.net Host header 被 `host_header_middleware` 拒绝（400）。 | Dashboard 必须 `--host 0.0.0.0`。详见 `references/hermes-desktop-remote-backend.md`。 |
| **Hermes Desktop 远程后端认证** | Desktop 远程模式需要 Session Token（非 API_SERVER_KEY），与 Web UI 的 API Key 认证不同。Token 每次 Dashboard 重启变化。 | 固化 `HERMES_DASHBOARD_SESSION_TOKEN` 到 `.env`，Desktop 配置 Token 模式。详见 `references/hermes-desktop-remote-backend.md`。 |
| **Desktop 发送失败不能只测 200/101** — `Dashboard 200`、`/api/ws 101`、甚至 `model.options` 成功都只能证明部分链路；Desktop 仍可能在实际 `prompt.submit` 路径失败。必须做 `/api/ws` JSON-RPC 端到端探针：`gateway.ready` → `session.create` → `prompt.submit` → `message.delta/complete`。脚本见 `hermes-base-operations` §七。若探针返回 `OK` 而 Desktop 失败，转向 Desktop 本地缓存/版本/后端地址。 | 用 `python3 ~/.hermes/skills/devops/hermes-base-operations/scripts/ws_rpc_probe.py` |
| **Tailscale Funnel 语法变更（v1.80+）** | 旧版 `tailscale funnel on` / `tailscale funnel off` 已废弃，新语法为 `tailscale funnel <port>` / `tailscale funnel --bg <port>`。 | 使用新语法。切端口：先 `tailscale funnel --https=443 off` 再 `tailscale funnel --bg <新端口>`。 |
| **Funnel 多路径覆盖陷阱** | `tailscale serve --bg --set-path` 会重置 funnel 状态，公网降级为 tailnet-only。 | 先设所有 serve 路径，最后一步启用 funnel。详见 `references/tailscale-troubleshooting.md`。 |
| **Hermes Desktop 国内安装** | Windows 国内安装需配 git/npm/electron/playwright 四个镜像，否则卡在 git fetch、npm install、Electron 下载等步骤。 | 先配置 `ghproxy.net`、`npmmirror.com`、`ELECTRON_MIRROR`、`PLAYWRIGHT_DOWNLOAD_HOST` 再安装。详见 `references/hermes-desktop-remote-backend.md`。 |
| **平台检测「状态未知」误报** | 自检脚本只 grep 最后一条 Connected/Disconnected 日志，长时间稳定连接无新日志时误报为「状态未知」，累积 fail_count。2026-06-07 实战：6AM 自检报微信/飞书双异常，实际两平台均正常。 | 平台检测改为 6 层时间窗口判定（见 §10.1 v3 增强）：优先看 30 分钟内消息往来印证连通；无日志时参考 Gateway 进程稳定性推断；「状态未知但 Gateway 稳定」不计入 fail。 |\n| **Gateway 日志写 journal 不自写文件** | `hermes update` 升级后 Gateway 日志只写 systemd journal 不写 `~/.hermes/logs/gateway.log`，旧自检脚本读空文件误报平台断开。2026-06-13 实战确认。 | 自检脚本 v5 改为直接用 `journalctl -u hermes-gateway` 查询连接状态，不依赖文件日志。飞书连接检测用 `[Lark].*connected` 模式（journal 中飞书标签为 `[Lark]` 而非 `[Feishu]`）。微信直接用 Gateway 进程存活推断。 |\n| **`set -o pipefail` + `grep -q` 导致 SIGPIPE 反向判断** | `grep -q` 找到匹配立即退出，关闭管道触发 journalctl 收到 SIGPIPE (141)，`set -o pipefail` 下 pipeline 退出码取 journalctl 的 141 而非 grep 的 0，`if` 条件反转。2026-06-13 实战：自检 v4 飞书检测明明有 connected 日志却报"无最近连接日志"。 | 避免 `grep -q` 与 pipefail 共用。改为 `grep ... | head -1 | grep -q .` 或拆分为两步（先赋值变量再 `[ -n "$var" ]`）。 |
| **灾备脚本路径硬编码** | 从旧笔记本迁移时，`$HOME/yanxinm` 在新机器上解析为 `/home/miao/yanxinm`（不存在）。脚本强切 SSH 绕过 ghproxy 代理。git push 失败时 `exit 1` 导致 cron 报错。 | 仓库路径改为 `$HOME/hermes-backup`；保持 HTTPS + ghproxy；push 失败退化为本地 tar + exit 0。详见 §十二。 |
| **git push 被墙（smart HTTP 阻断）** | 即使 ghproxy HTTPS 代理对网页/API 可用，git smart HTTP 协议（fetch-pack/push）仍会 `unexpected disconnect`。SSH over 443 同样被 DPI 阻断。 | 灾备脚本不依赖 git push：先做本地 tar 备份，git push 仅最佳努力。网络恢复后自动同步。详见 `references/github-gfw-workaround.md`。 |
| **cron_mode: deny 导致定时任务静默失败** | profile（通过 `--clone` 创建或默认）的 `approvals.cron_mode: deny` 会让 cron worker 在执行到任何需要审批的命令（terminal/write_file 等）时被直接拒绝，任务悄悄挂掉。`hermes cron list` 不显示错误——上次运行可能显示 `ok` 但实际 agent 内部已失败。症状：cron 按时触发但从未产生实际输出或副作用。 | **创建 profile 后立即改**：`sed -i 's/cron_mode: deny/cron_mode: allow/' ~/.hermes/profiles/<name>/config.yaml`。同时检查 default：`grep cron_mode ~/.hermes/config.yaml`。修改后需重启 Gateway。**注意：** `hermes config set approvals.cron_mode allow` 会写到当前活跃 profile 而非 default，务必显式指定 `-p default` 或用 sed 直接改。 |
| **`hermes update` 静默副作用** | `hermes update` 执行后可能发生：(1) Gateway 日志迁移到 systemd journal，`gateway.log` 停止更新；(2) API Server 绑定从 `0.0.0.0` 回退到 `127.0.0.1`；(3) Web UI 版本在 `~/.hermes/node/` 中未更新（需单独 copy 全局版本）；(4) cron 投递渠道可能受影响需重新确认。症状分散：自检报平台断开、笔记本连不上、定时任务产出丢失。 | 升级后立即执行：① `ss -tlnp | grep 8642` 确认 API 绑定；② `journalctl -u hermes-gateway -n 5` 确认日志写入正常；③ `cat ~/.hermes/node/lib/node_modules/hermes-web-ui/package.json | grep version` 确认 Web UI 版本；④ `hermes cron list` 确认投递渠道。 |
| **Hermes Desktop Dashboard WebSocket 卡死** | Desktop 远程后端显示“网关断开”/长任务中途断，但 `hermes-gateway` 仍 active；Dashboard `/api/status` 可能超时，`/api/ws` 断开 | 区分 messaging Gateway 与 Dashboard WebSocket；只重启卡死的 9119 Dashboard，验 `local/public 200` + `/api/ws` `101` + 模型 `OK`。如果反复“提示词发送失败”，不要继续让用户重开 Desktop，必须加每分钟 Dashboard watchdog（HTTP + WS 双检查，失败只重启 9119）。详见 `references/hermes-desktop-dashboard-ws-stall.md`。 |
| **Hermes Desktop token 与 systemd Dashboard 不一致** | `local/public 200` 和 `/api/ws 101` 看似正常，但 Desktop 反复“提示词发送失败/网关断开/代理 1 个失败”；`hermes-dashboard.service` 自动拉起无固定 token 的 9119 进程，手动固定 token 启动会因 `EADDRINUSE` 失败 | 先用 `ss -tlnp` 找 9119 真实 PID，再查 `/proc/$PID/environ` 是否有 `HERMES_DASHBOARD_SESSION_TOKEN`。若 systemd 服务未注入 token，必须先 sudo 停/禁用或 patch `/etc/systemd/system/hermes-dashboard.service`；否则 watchdog 会反复拉起错误实例。详见 `references/hermes-desktop-systemd-token-mismatch.md`。 |
| **Tailscale Funnel 多端口搭建** | 单个 Funnel 只能指向单一端口。两个 Funnel（8648 + 9119）的 DNS 名不同，Desktop 不能在同一个 Base URL 中同时使用两个端口。 | 同时需要 Web UI + Desktop 的场景，Funnel 指向 Dashboard (9119)，Web UI 通过 Tailscale IP 或内网直接访问。详见 `references/hermes-desktop-remote-backend.md`。 |

## 六、事故复盘记录

- `references/github-gfw-workaround.md` — GitHub 被墙时通过 api.github.com tarball 下载源码的替代方案
- `references/cron-pkill-self-destruct.md` — 2026-05-24 自检脚本 v1 弑主事故分析
- `references/pipefail-grep-quiet-sigpipe.md` — `set -o pipefail` + `grep -q` SIGPIPE 反转判断根因与修复
- `references/api-server-config-missing.md` — API Server 0.0.0.0 配置丢失/回退 127.0.0.1 的诊断与修复
- `references/gateway-log-journal-migration.md` — Gateway 升级后日志迁移到 systemd journal 的适配方案
- `references/codex-bwrap-userns-fix.md` — Codex 沙箱权限：`apparmor_restrict_unprivileged_userns` 修复
- `references/wsl-service-watchdog.md` — TDAI Gateway EPIPE 崩溃根因 + CLIProxyAPI 配置 + Provider 诊断速查
- `references/hermes-full-stack-health-check.md` — 2026-05-24 全链路健康检查实战记录（含所有命令与预期输出）
- `references/chrome-user-space-install.md` — Chrome 免 sudo 用户空间安装 + Hermes browser 工具集成
- `references/scheduler-overnight-gap-detection.md` — 定时调度器过夜停顿检测模式（凌晨备份丢失的排查与加固）
- `references/gateway-external-sigterm-pattern.md` — 外部 SIGTERM 杀 Gateway 时 exit-diag.log 无记录的分析及诊断方法
- `references/tailscale-troubleshooting.md` — Tailscale DERP 单向阻断诊断与 SSH 隧道备用方案（2026-06-07）；Funnel 多路径路由顺序陷阱（2026-06-09）
- `references/ubuntu-snap-store-fix.md` — Ubuntu Software (Snap Store) 加载空白修复：dbus-x11 缺失 + apt 源被墙（2026-06-09）
- `references/hermes-desktop-remote-backend.md` — Hermes Desktop 远程后端配置：Funnel + Dashboard --insecure + Session Token 认证（2026-06-08）
- `references/hermes-desktop-dashboard-ws-stall.md` — Desktop 远程任务中途“网关断开”时，区分 Gateway 与 Dashboard WebSocket，并重启/验收 9119 的流程
- `references/hermes-desktop-systemd-token-mismatch.md` — systemd 自动拉起无固定 token 的 Dashboard，导致 Desktop 远程后端反复提示词发送失败/网关断开的诊断与修复
- `references/hermes-desktop-jsonrpc-e2e-probe.md` — Desktop 远程后端“提示词发送失败”时的 `/api/ws` JSON-RPC 端到端探针：`session.create` + `prompt.submit` 验证真实发送路径

### 6.1 调度器过夜停顿（凌晨备份丢失）

详见 `references/scheduler-overnight-gap-detection.md`。快速检测：对比 `hermes cron list` 中 `last_run_at` 是否在昨天或今天。如果在凌晨时段整段缺失，根因通常是 WSL 挂起/Gateway OOM/SSH 阻塞。加固方案：将灾备时间从凌晨 3 点改到每日简报前的 08:00，或在 watchdog.sh 中增加调度器健康自检。

## 七、Linux systemd 开机自启

**适用：** 无显示器 Linux 主机（headless），重启后自动拉起全链路 4 个服务。

完整部署指南 + 4 个 `.service` 模板 + 5 个常见陷阱详见 `references/linux-systemd-autostart.md`。

模板文件（含 `__USER__` / `__HOME__` 占位符，部署时替换）：
- `templates/hermes-tdai.service` — TDAI Memory Gateway (8420)
- `templates/hermes-web-ui.service` — Web UI (8648)
- `templates/hermes-dashboard.service` — Dashboard (9119)
- `templates/hermes-gateway.service` — Gateway (8642)

**快速部署：**
```bash
# 1. 替换模板占位符
for f in hermes-tdai hermes-web-ui hermes-dashboard hermes-gateway; do
  sed "s|__USER__|$(whoami)|g; s|__HOME__|$HOME|g" templates/$f.service > /tmp/$f.service
done

# 2. 安装启用
sudo cp /tmp/hermes-*.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable hermes-tdai hermes-web-ui hermes-dashboard hermes-gateway

# 3. 停旧进程后启动
sudo systemctl start hermes-tdai hermes-web-ui hermes-dashboard hermes-gateway
```

**启动顺序：** TDAI → Web UI → Dashboard → Gateway（Gateway 通过 `After=` + `Wants=` 声明依赖）。

**⚠️ 关键陷阱速查：**
| 陷阱 | 症状 | 修复 |
|------|------|------|
| systemd PATH 不含用户本地 bin | Web UI 启动用系统旧 Node (v18)，`ERR_UNKNOWN_BUILTIN_MODULE: node:sqlite` | `Environment=PATH=...:/home/<user>/.local/bin:...` |
| API_SERVER_KEY 缺失 | api_server 拒绝启动，Gateway 2/3 平台在线 | `.env` 中必须有 `API_SERVER_KEY` |
| Dashboard 构建死循环 | 端口监听但 HTTP 超时 | `npx vite build` → `--skip-build` |
| Web UI Type=forking 配置错误 | systemd 重启循环 | `Type=forking` + `PIDFile` |
| 旧进程占端口 | systemd 启动 EADDRINUSE | 先 `kill` 旧进程 |

## 九、远程访问方案总览

基地运行 Gateway + 微信/飞书，笔记本（不同网络）需要远程使用 Hermes。有以下方案：

### 方案对比

| 方案 | 客户端 | 认证 | 适用场景 |
|------|--------|------|----------|
| SSH 隧道 + Web UI | 浏览器 | API_SERVER_KEY | 临时使用、轻量 |
| Tailscale Funnel + Web UI | 浏览器 | 无（公开） | 简单快速 |
| **Tailscale Funnel + Desktop** | Hermes Desktop | Session Token | 日常主力、全功能 |
| API Server 0.0.0.0 + Tailscale | 浏览器/Desktop | API_SERVER_KEY | 内网 + VPN |

### 9.A Hermes Desktop 远程后端（推荐）

笔记本安装 Hermes Desktop，配置 Remote 模式通过 Tailscale Funnel 连接基地 Dashboard。**不依赖 Tailscale 客户端、不挑网络环境、任何能上网的地方都能用。**

> 完整配置指南详见 `references/hermes-desktop-remote-backend.md`。

快速配置步骤：
1. 基地 Dashboard 启动：`hermes dashboard --port 9119 --host 0.0.0.0 --insecure`
2. 固化 Token：`HERMES_DASHBOARD_SESSION_TOKEN=<token>` 写入 `.env`
3. Funnel 指向 Dashboard：`sudo tailscale funnel --bg 9119`
4. Desktop 填入 Funnel 域名 + Token

### 9.B SSH 隧道（最稳定，推荐）

适用于 Tailscale DERP 不稳定或单位防火墙干扰的场景。无需修改任何绑定或 API Server 配置。

```bash
# 笔记本 PowerShell：
ssh -L 8648:127.0.0.1:8648 miao@100.86.13.11
```

隧道建立后，笔记本浏览器访问 `http://127.0.0.1:8648` 即 Web UI。走 SSH 加密隧道，TCP keepalive 保活，不依赖 Tailscale DERP。

- ✅ 不需要开放 API Server 到 0.0.0.0
- ✅ 加密传输，跨任意网络
- ⚠️ 需保持 SSH 终端窗口不关
- ⚠️ 首次连接需输入 yes 确认主机指纹

如需默认免密码登录，将笔记本 SSH 公钥添加到基地 `~/.ssh/authorized_keys`。

### 9.3 Tailscale + API Server 0.0.0.0（日常远程访问，最简方案）

基地 API Server 绑定 `0.0.0.0`，笔记本通过 Tailscale 虚拟 IP 直接连接。**不需要 Funnel、不需要额外开放端口**，只需两台设备都装 Tailscale 并登录同一账号。

#### 部署步骤

```bash
# 1. 基地：API Server 绑定 0.0.0.0
hermes config set platforms.api_server.extra.host 0.0.0.0

# 2. 确认 API_SERVER_KEY 已设置
grep 'API_SERVER_KEY' ~/.hermes/.env

# 3. 基地：安装 Tailscale
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up  # 登录同一账号

# 4. 记下基地 Tailscale IP
tailscale ip -4  # 如 100.86.13.11

# 5. 重启 Gateway 使 0.0.0.0 绑定生效
kill $(pgrep -f "hermes gateway run")  # systemd 自动拉起

# 6. 验证 Tailscale IP 可达
curl -s http://100.86.13.11:8642/health  # 预期 {"status":"ok"}
```

#### 笔记本端

```bash
# Windows: 下载安装 https://tailscale.com/download/windows
# 登录同一账号 → 自动获得 100.x.x.x 虚拟 IP

# 验证连通
ping 100.86.13.11

# Web UI 配置
API URL: http://100.86.13.11:8642
API Key: hermes-fix-2026
```

#### 特点
- ✅ 两台设备装 Tailscale + 同一账号 → 零配置
- ✅ Tailscale IP 永久不变，笔记本带出去也不需改配置
- ✅ 不需要 Funnel、SSH 隧道或公网 IP
- ⚠️ Tailscale 依赖 DERP 中继（国内可能降级但通常可用）

## 十、每6小时定时自检

本系统配置了 cron 自检任务，自动维护全链路连通性。

### 10.1 自检脚本

完整脚本位于技能目录下：

```
scripts/hermes-health-check.sh
```

并同步到 `~/.hermes/scripts/hermes-health-check.sh` 供 cron 调度器使用。

该脚本检查以下6项并自动修复：
1. Hermes Gateway — 进程存活（`pgrep` + `ps etime`）+ 端口
2. Web UI (8648) — HTTP GET
3. Dashboard (9119) — HTTP GET
4. TDAI Memory (8420) — 端口监听
5. 微信 (Weixin) — 6 层判定（见下方 v3 增强）
6. 飞书 (Feishu) — 同上

**v5 平台检测重写 (2026-06-13)：** 旧版（v3/v4）通过合并文件日志 + journalctl 并统一格式解析，因 journalctl 格式（`6月 13 07:40:08 ... [Lark] [2026-...`）与文件日志格式（`2026-06-07 10:16:30,281 ...`）差异过大，sed 转换链条脆弱。v5 改为**直接验证法**：

| 平台 | 检测方式 | 备注 |
|------|---------|------|
| 飞书 | `journalctl -u hermes-gateway --since "6 hours ago" \| grep '[Lark].*connected'` | journal 中飞书标签为 `[Lark]` 非 `[Feishu]` |
| 微信 | `is_gateway_running` → 进程存续即通过 | 用户当前会话经由微信，Gateway 存活=微信通 |

v5 移除了 v3 的 6 层时间窗口判定（日志行时间戳解析），改为直接查询 systemd journal。关键教训：**Gateway 升级后日志只写 journal，健康检查脚本必须适配此变化。**

**⚠️ v2 关键安全更新（2026-05-24）：**

| 问题 | v1 做法 | 事故后果 | v2 修复 |
|------|---------|----------|---------|
| Gateway 检测 | `hermes gateway status` | cron 环境假阴性，误报"not running" | 改用 `pgrep -f "python.*hermes.*gateway.*run"` + `ps -o etime=` 双重确认 |
| 进程清理 | `pkill -f "hermes gateway run"` | 杀死正在运行的 Gateway + bash wrapper | 用 `pgrep` 获取精确 PID → `kill $PID` |
| Dashboard 清理 | `pkill -f "hermes dashboard"` | 同上一并杀死 | `pgrep -f "hermes.*dashboard.*9119"` → `kill` |
| 平台验证 | `send_message` 返回 success | Gateway 已死但返回假阳性 | 检查 gateway.log 中是否有 `Sending response` 日志条目 |

**事故复盘：** `cron-pkill-self-destruct.md` 记录了完整的故障分析。

### 10.2 Cron 配置

```bash
# 创建方式（通过 Agent 的 cronjob 工具）：
cronjob action=create name="Hermes 全链路自检 (每6小时)" \
    schedule="0 0,6,12,18 * * *" \
    script="hermes-health-check.sh" \
    no_agent=true \
    deliver=all
```

- **时间**：北京时间 00:00 / 06:00 / 12:00 / 18:00
- **模式**：`no_agent=true` — 直接运行脚本，输出报告，不经过 LLM 处理
- **投递**：`deliver=all` — 报告推送到所有已连接的渠道（微信 + 飞书）
- **异常处理**：脚本 exit code > 0 时，cron 额外发送错误告警

### 10.3 Cron 投递渠道切换

切换已有 cron 的投递渠道（如飞书→微信）：

```bash
# 获取 cron ID
hermes cron list | grep -B1 "Name:"

# 修改投递
hermes cron edit <id> --deliver weixin
# 可选值: weixin, feishu, all, origin, local
```

**注意**：profile 隔离 — `hermes cron list` 只显示当前活跃 profile 的 cron。用 `hermes -p <name> cron list` 查看其他 profile。

**`cron_mode: deny` 陷阱**：profile 的 `approvals.cron_mode: deny` 会让定时任务中任何需要审批的命令被直接拒绝，任务静默失败（`hermes cron list` 可能显示 `ok` 但实际 agent 内部已失败）。创建 profile 后立即改为 `allow`：
```bash
sed -i 's/cron_mode: deny/cron_mode: allow/' ~/.hermes/profiles/<name>/config.yaml
grep cron_mode ~/.hermes/config.yaml  # 同时检查 default
```

### 7.5 服务守护 watchdog（每 2 分钟检测）

**用途：** 补充每 6 小时自检的盲区 — 在自检间隔内快速恢复 TDAI Gateway 和 Hermes Gateway 的崩溃。

**脚本路径：** `~/.hermes/scripts/watchdog.sh`（主脚本）+ `scripts/watchdog.sh`（skill 镜像副本）

**检测内容：**
1. TDAI Gateway — 端口 8420 是否监听，未监听时自动重启
2. Hermes Gateway — `pgrep -f "hermes gateway run"` 进程是否存活，未存活时自动重启

**Cron 配置（通过 Agent 的 cronjob 工具）：**
```bash
cronjob action=create name="服务守护" schedule="every 2m" script="watchdog.sh" no_agent=true deliver=local
```

**特性：**
- 正常时完全静默（无 stdout 输出），不打扰用户
- 崩溃重启时输出一行通知（含时间戳 + 原因）
- 日志路径：`/tmp/hermes-watchdog.log`
- 使用 no_agent=true 确保即使 Agent 不可用，cron 也能直接运行脚本

```bash
# 手动跑一次
bash ~/.hermes/skills/devops/hermes-gateway-ops/scripts/hermes-health-check.sh

# 查看所有 cron 任务
cronjob action=list
```

### 7.4 重要：TDAI Memory 检测特殊处理

TDAI Memory Gateway 的 HTTP 根路径返回 404（这是正常的），不能用 `curl GET /` 判断存活。
必须用 `ss -tlnp | grep 8420` 检查端口是否在监听。健康检查脚本已内置此逻辑。

完成全部恢复操作后，输出以下格式的验收报告：

| 组件 | 状态 | 备注 |
|------|------|------|
| Hermes Gateway | ✅/❌ | PID + 启动时间 |
| TDAI Memory (8420) | ✅/❌ | 监听状态 |
| Web UI (8648) | ✅/❌ | HTTP 状态码 |
| Dashboard (9119) | ✅/❌ | HTTP 状态码 |
| 微信 (Weixin) | ✅/❌ | 最近活跃时间 + 平台连接状态 |
| 飞书 (Feishu) | ✅/❌ | 平台连接状态 |

## 十一、Node.js 升级

基地的 Node.js 通过 `n` 版本管理器（`npx n`）管理，安装在用户本地 `~/.local/bin/`。

```bash
# 升级到最新 LTS（n 自动处理下载 + 替换 symlink）
# N_PREFIX 指向 node 的安装根目录（~/.local）
N_PREFIX=/home/miao/.local npx -y n lts

# 验证
node --version  # 如 v24.16.0

# ⚠️ 运行中的 Node 进程（TDAI, Web UI）仍用旧版本
# 重启后自动切到新版本
```

**注意：** systemd 服务的 `Environment=PATH` 必须包含 `~/.local/bin`，否则找到系统旧 Node。

## 十二、每日灾备

cron 定时任务（每天 08:10）自动备份 Hermes 核心配置到 `~/hermes-backup/`，并尝试推送到 GitHub 仓库 `yanxinm/yanxinm`。脚本位于 `~/.hermes/scripts/hermes_backup.sh`。

### 备份内容

| 目录 | 内容 |
|------|------|
| `config/` | config.yaml, SOUL.md |
| `skills/` | 全部技能 |
| `scripts/` | 自定义脚本 |
| `cron/` | 定时任务定义 |
| `memories/` | 持久记忆 |
| `hindsight/` | 记忆系统配置 |

**不备份密钥：** `.env`、`auth.json` 不包含在备份中。

### 工作原理

1. 复制所有文件到 `~/hermes-backup/hermes/`
2. 本地打包为 `hermes-backup-<timestamp>.tar.gz`
3. 尝试 `git push` 到 GitHub（最佳努力）
4. GitHub 不可达时仅保留本地 tar，不报错（exit 0）

### 迁移陷阱

从旧笔记本迁移到基地时，脚本中的路径 `$HOME/yanxinm` 硬编码导致 `cd` 失败。修复方法：
- 仓库路径改为 `$HOME/hermes-backup`
- 删除强制切 SSH 的逻辑（绕过 ghproxy 代理）
- push 失败时退化为本地 tar，不再 `exit 1`

### GitHub 认证

基地的 SSH 公钥需添加到 GitHub → https://github.com/settings/keys：
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBoGROVU5D4FY04HiAHRtTM7tHCO/l7Yfj5fjyJ2BMhU hermes-base-m710q
```

网络通畅时，备份自动推送到 `git@github.com:yanxinm/yanxinm.git`。被墙时仅本地保存，待网络恢复后自动同步（git push 在下次成功执行时会推送所有积压提交）。