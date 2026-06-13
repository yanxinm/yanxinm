# 远程 Web UI 访问：多设备 Hermes 架构

## 场景

基地（固定主机）运行 Hermes Gateway + 微信 + 飞书，笔记本上的 Web UI 需要连接基地的 API Server。笔记本在局域网内和带出去后都需要可用。

## 架构

```
笔记本 Web UI (:8648) ──HTTP──▶ 基地 API Server (:8642) ──▶ Hermes Agent
                                           │
                              微信/飞书 ◀──┘ (Gateway 平台)
```

Web UI 不直接对话 Agent — 它通过 Gateway 的 API Server（`/v1/chat/completions`）转发请求。

## 配置步骤

### 1. 基地：开放 API Server 监听地址

默认 `127.0.0.1` 只能本机访问。改为 `0.0.0.0` 允许外部连接：

```bash
hermes config set platforms.api_server.extra.host 0.0.0.0
```

**配置写入 config.yaml 的路径：** `platforms.api_server.extra.host`

**前置条件：** `.env` 中必须有 `API_SERVER_KEY`（v0.16+ 强制要求）。否则 API Server 拒绝启动，即使改 bind 也无效。

### 2. 重启 Gateway 使配置生效

```bash
# 方法A（推荐）：杀旧进程，依赖 systemd Restart=always 自动拉起
kill $(pgrep -f "hermes gateway run")
sleep 15  # 等待 systemd 自动拉起+平台连接完成

# 方法B：手动前台启动（无 systemd 或 systemd 被绕过时）
hermes gateway run --replace

# 方法C：有 sudo 时
sudo systemctl restart hermes-gateway
```

**⚠️ 陷阱：手动 `hermes gateway run --replace` 的风险**

如果用 `terminal(background=true)` 启动，其父 bash 进程退出时会发 SIGTERM 给子进程。如果 systemd 也配置了 `Restart=always`，两个启动路径会互相冲突——systemd 拉起的新 Gateway 会 SIGTERM 掉手动启动的进程。推荐方法A（纯 systemd），方法B 仅在 systemd 完全停用时使用。

### 3. 验证绑定

```bash
ss -tlnp | grep 8642
# 预期：LISTEN 0.0.0.0:8642

curl -s http://192.168.1.42:8642/health
# 预期：{"status": "ok", "platform": "hermes-agent"}
```

### 4. 笔记本 Web UI 配置

Web UI 需要指向基地的 API Server：
- **API URL**: `http://<基地IP>:8642`（局域网）或 VPN IP（远程）
- **API Key**: 与基地 `.env` 中 `API_SERVER_KEY` 一致

Web UI 配置文件通常位于：
- npm 全局安装：`~/.hermes-web-ui/.env` 或启动参数
- 通过环境变量：`HERMES_API_URL` + `HERMES_API_KEY`

## 局域网访问

基地 IP 固定（如 `192.168.1.42`），笔记本在局域网内直接配置该 IP 即可。

## 远程访问（笔记本带出局域网）

### 推荐方案：Tailscale

免费（个人使用 100 设备），自动 NAT 穿透，配置一次 IP 不变。

#### 安装

```bash
# 基地和笔记本都安装
curl -fsSL https://tailscale.com/install.sh | sh
```

#### 认证方式：Auth Key（headless 机器唯一推荐方式）

**⚠️ 关键：** headless 服务器不能用 `tailscale up` + 点链接的方式 — 每次 `tailscale up` 阻塞等待浏览器认证，命令超时（10-30s）后被取消，已生成的认证链接作废，需要重新生成，陷入死循环。

**正确做法：** 在 Tailscale Admin 面板生成 auth key，一步完成：

```bash
# 1. 浏览器打开 https://login.tailscale.com/admin/settings/keys
# 2. 点 Generate auth key → 复制 key
# 3. 在 headless 机器上执行：
sudo tailscale up --auth-key=<tskey-auth-xxx> --accept-routes
```

Auth key 一步完成，无超时问题。

#### 验证

```bash
# 检查连接状态
tailscale status
# 预期输出两台机器 + IP

# 测试互通
ping -c 3 <对方机器IP>

# 测试服务可达
curl -s -o /dev/null -w "%{http_code}" http://<基地TS_IP>:8648/  # Web UI
curl -s -o /dev/null -w "%{http_code}" http://<基地TS_IP>:8642/  # API Server
```

#### 笔记本 Web UI 配置

- **API URL**: `http://<基地 Tailscale IP>:8642`
- **API Key**: 与基地 `.env` 中 `API_SERVER_KEY` 一致

### 备选方案

| 方案 | 优势 | 劣势 |
|------|------|------|
| ZeroTier | 免费、类似 Tailscale | 配置稍复杂 |
| frp 内网穿透 | 国内成熟 | 需要公网服务器 |
| Cloudflare Tunnel | 无需客户端 | 国内访问较慢 |

## 部署实战：基地 + 笔记本双设备（2026-06-07 已验证）

### 环境

| 设备 | 名称 | OS | Tailscale IP |
|------|------|-----|-------------|
| M710q | 基地 | Ubuntu 22.04 | 100.86.13.11 |
| 笔记本 | ethan | Windows | 100.86.148.56 |

### 实际踩坑

**坑1：Tailscale 安装需要 sudo，Hermes 无法自主完成**

`curl -fsSL https://tailscale.com/install.sh | sh` 在 Ubuntu 上会调用 `sudo apt`，Hermes 没有 sudo 权限。必须由用户在终端手动执行 `sudo tailscale up` 完成认证。

**坑2：Auth key 方式 vs 交互式登录**

参考文档推荐 headless 用 auth key 一步完成。但实际场景中用户（老缪）在笔记本端安装了 Tailscale 客户端（GUI），可以直接点网页链接认证，不需要 auth key。如果基地是纯 headless 无人值守，才必须走 auth key 方式。

### 验证检查单

部署完成后逐项确认：

```bash
# 1. 基地 Tailscale 在线
tailscale status | grep -c "$(hostname)"

# 2. 笔记本可见
tailscale status | grep ethan

# 3. API Server 监听 0.0.0.0
ss -tlnp | grep 8642 | grep '0.0.0.0'

# 4. API Server 通过 Tailscale IP 可达
curl -s -o /dev/null -w "%{http_code}" http://100.86.13.11:8642/health  # 期望 200

# 5. 微信/飞书仍在 Gateway 日志中连接
tail -5 ~/.hermes/logs/gateway.log | grep -E 'weixin|feishu' | grep -i connect
```

### 三通道确认矩阵

| 通道 | 验证方式 | 关键信号 |
|------|---------|---------|
| 微信 | 手机发消息给 H，看回复 | gateway.log 有 `inbound` + `Sending response` |
| 飞书 | 飞书里 @H | gateway.log 有 feishu 连接状态 |
| Web UI | 笔记本浏览器打开 → 连基地 Tailscale IP | 能发送消息并获得 Agent 回复 |

## 安全注意事项

- 绑定 `0.0.0.0` 意味着局域网内任何设备都能访问 API Server
- 必须设置 `API_SERVER_KEY` 防止未授权访问
- 不要在公网直接暴露 8642 端口（无 HTTPS）
- 远程访问建议走 VPN（Tailscale 自动加密隧道）
- Tailscale 安装时 Hermes 无法代替用户 sudo，需用户手动执行认证步骤

## 已知坑：重启后 0.0.0.0 配置丢失

**症状：** 已正确设为 `0.0.0.0`，系统重启或 systemd 重启 Gateway 后回退到 `127.0.0.1`。`ss -tlnp | grep 8642` 显示 `127.0.0.1:8642` 而非 `0.0.0.0:8642`。笔记本通过 Tailscale IP 访问 `health` 端点超时，Dashboard 显示「网关启动失败」。

**根因：** 未完全确定。可能原因包括 config 版本迁移（_config_version 升级时丢失自定义字段）或 systemd 环境变量覆盖。

**修复：**
```bash
# 1. 确认当前绑定
ss -tlnp | grep 8642  # 若显示 127.0.0.1 则需修复

# 2. 重新设置（务必指定 -p default）
hermes -p default config set platforms.api_server.extra.host 0.0.0.0

# 3. 确认写入正确文件
hermes -p default config path  # 应为 ~/.hermes/config.yaml，不是 profiles/jike/config.yaml
grep -r '0.0.0.0' ~/.hermes/config.yaml  # 确认值存在

# 4. 重启 Gateway
kill $(pgrep -f "hermes gateway run")  # systemd 自动拉起

# 5. 验证
ss -tlnp | grep 8642  # 必须显示 0.0.0.0:8642
curl -s http://100.86.13.11:8642/health  # 必须返回 200
```

**预防：** 建议在自检脚本中增加端口绑定地址检测——不仅检查端口是否监听，还要检查绑定的是 `0.0.0.0` 还是 `127.0.0.1`。
