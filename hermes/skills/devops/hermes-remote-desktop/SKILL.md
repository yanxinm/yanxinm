---
name: hermes-remote-desktop
description: 将 Hermes Desktop 远程连接到另一台机器上的 Hermes 后端（基地模式）。覆盖服务端配置、网络穿透、客户端认证全链路。
category: devops
tags: [hermes, desktop, remote-backend, tailscale-funnel, dashboard]
---

# Hermes Remote Desktop — 远程后端连接

## 适用场景

用户有一台运行 Hermes 的服务器（"基地"），想在笔记本上通过 Hermes Desktop 远程连接使用，要求安全、免费、不挑网络。

## 架构原理

```
笔记本 Hermes Desktop（远程模式）
    ↓ HTTPS + Token
Tailscale Funnel（公网穿透）
    ↓ localhost:9119
基地 Dashboard（--host 0.0.0.0 --insecure）
    ↓
基地 Gateway + Agent
```

**关键认知**：Desktop 远程模式需要连接的是 **Dashboard API（9119）**，不是 Node SPA / Hermes Studio（8648）。Node SPA 不转发认证头，会导致 `/api/status` 返回 401。

## 基地端配置

### 1. 确保 Dashboard 绑定 0.0.0.0 并关闭认证门

```bash
# 先停掉旧的（gateway 自动重启的 127.0.0.1 版本）
hermes dashboard --stop

# 手动启动，绑定所有接口 + 跳过 OAuth
hermes dashboard --port 9119 --host 0.0.0.0 --insecure --no-open --skip-build &
```

⚠️ 如果 gateway 进程检测到 dashboard 没运行，会自动以 `--host 127.0.0.1` 重启它。此时需要杀掉自动重启的进程，手动启动 0.0.0.0 版本。两个进程不能同时绑定同一端口——先启动的占住端口。

### 2. 设置固定 Session Token

```bash
# 生成 token（一次性）
python3 -c "import secrets; print(secrets.token_urlsafe(32))"

# 写入 .env（持久化，避免每次重启 token 变化）
echo "HERMES_DASHBOARD_SESSION_TOKEN=<token>" >> ~/.hermes/.env
```

### 3. 配置 Tailscale Funnel 指向 Dashboard

Tailscale v1.80+ 使用了新的 serve/funnel CLI。**关键区别**：
- `tailscale funnel --bg <port>` 一键完成 HTTPS 监听 + 公网暴露
- `tailscale serve --bg --set-path /path <url>` 添加子路径路由
- **陷阱**：`tailscale serve --set-path` 会将公网暴露状态降级回 tailnet-only，之后必须重新运行 `tailscale funnel --bg <port>` 恢复

**纯 Dashboard（无其他服务）：**
```bash
tailscale funnel --bg 9119
```

**多服务共享（如 Dashboard + HomeAssistant）：**
```bash
# 1. 先用 serve 设好所有路径
tailscale serve --bg --set-path / http://127.0.0.1:9119
tailscale serve --bg --set-path /ha http://localhost:8123

# 2. 开启公网访问（选用 funnel 而非 serve，因 serve 只会 tailnet）
tailscale funnel --bg 9119
# 此时所有 serve 路径都会变为公网可访问

# 3. 验证
tailscale funnel status
# 应显示 "Funnel on" 且列出所有路径
```

**从旧版迁移：**
```bash
# 清掉旧配置
tailscale serve --https=443 off
tailscale funnel --https=443 off

# 重新按新语法配置
```

### 4. 端到端验证

```bash
curl -s https://<ts-net-hostname>/api/status \
  -H "X-Hermes-Session-Token: <token>"
# 应返回 JSON 含 version、gateway_state 等
```

## 笔记本端配置

### Windows 安装前准备（国内网络）

在 **cmd**（非 PowerShell，因执行策略限制 npm.ps1）中：

```cmd
npm config set registry https://registry.npmmirror.com
setx ELECTRON_MIRROR "https://npmmirror.com/mirrors/electron/"
setx PLAYWRIGHT_DOWNLOAD_HOST "https://npmmirror.com/mirrors/playwright/"
git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"
```

⚠️ `setx` 修改的是永久环境变量，需要**新开 cmd 窗口**才能生效。安装前逐一验证三项都输出正确值。

### 安装 Hermes Desktop

下载地址：https://hermes-agent.nousresearch.com/desktop

常见安装失败及处理：
- **npm install 卡 30 分钟** → 设 npm 国内镜像
- **git fetch failed (exit 128)** → 设 git 代理 ghproxy.net
- **build failed (exit -4082 EBUSY)** → 杀毒软件锁了 electron 文件，关实时防护或重启后重试
- **electron 下载卡** → 设 ELECTRON_MIRROR

### 连接远程后端

1. 启动后跳过 provider 设置（"I'll choose a provider later"——基地已配好）
2. Settings → 网关 → 选「远程网关」
3. 填入：
   - 远程 URL：`https://<ts-net-hostname>`
   - 认证方式：Token
   - Token：基地 `.env` 中的 `HERMES_DASHBOARD_SESSION_TOKEN`
4. 点「测试远程」→ 确认无报错 → 「保存并重连」

## 故障排查

更细的 Desktop 模型切换/发送失败排查清单见 `references/desktop-model-switch-send-fail.md`。

| 现象 | 原因 | 解决 |
|------|------|------|
| Desktop 断开（所有服务正常） | Funnel 路由被其他服务挤占（如 HA 占了 `/`） | 重新配置 Funnel 恢复 Dashboard 到根路径 |
| Desktop 已连接但发送失败/模型切换失败 | Dashboard 会话 token/前后端状态不同步，或 Desktop 调旧模型接口 | 重启 9119 Dashboard，Desktop 完全退出重开，新建会话测试 |
| Funnel 状态显示 "tailnet only" | 添加子路径后公网被降级 | 重新运行 `tailscale funnel --bg 9119` |
| Funnel 显示 443 端口冲突 | 已有 serve/funnel 监听 | 先 `tailscale funnel --https=443 off` 清旧配置 |
| 切 Funnel 端口后 serve 配置丢失 | 新版 tailscale 语法变化 | 用 `tailscale funnel --bg <port>`（非 `sudo tailscale serve`） |

## 与 Web UI 的关系

如果需要同时保留 Web UI（Hermes Studio，8648端口）和远程 Desktop 访问：
- Funnel 只能指一个端口
- 选 Desktop 路线：Funnel → 9119（Dashboard），Web UI 仅本地/内网访问
- 选 Web UI 路线：Funnel → 8648（Node SPA），Desktop 远程不可用
- 高级方案：Nginx/Caddy 反代，按路径分流（`/api/*` → 9119，`/` → 8648）
- 推荐方案：Funnel → Dashboard 9119，Web UI 通过 Tailscale IP 直连 `http://100.86.13.11:8648`

## Desktop 失败时的回退方案

当 Desktop 持续"提示词发送失败"或显示"Hermes couldn't start"时，按以下顺序排查：

### 第1步：确认基地端是否正常

通过微信让 H 检查：
- Dashboard HTTP `200` + WebSocket `101` + 模型实发 `OK`
- Gateway 所有平台在线

### 第2步：用浏览器 Dashboard 聊天作为临时替代（立即可用）

Desktop 后端地址（Funnel URL）的浏览器本身就是 Dashboard 的 Web 聊天界面。直接打开 Funnel 地址（如 `https://miao-thinkcentre-m710q-n080.tail589fe7.ts.net`），点左侧 "Chat" 即可打字发提示词。这是最快的临时替代方案，不需要安装任何东西。

### 第3步：排查 Desktop 本地问题

- Desktop 端后端地址改成 Tailscale 直连 `http://100.86.13.11:9119`（局域网内更稳）
- 或手机热点测试确认单位防火墙是否拦截 WebSocket
- 彻底退出 Desktop（托盘也退出），重开新建会话
- 如果始终不行，卸载重装 Desktop 客户端

### Web UI 后台"未连接"修复

Web UI（8648）页面显示"未连接"但服务 active：
1. 进程和端口正常时，重启 Web UI 即可恢复 bridge 连接
2. 通过 `kill $(pgrep -f 'hermes-web-ui/dist/server')` 触发 systemd 自动重启（无需 sudo）
3. 等 15-30 秒后刷新页面
