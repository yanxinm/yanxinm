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

```bash
# Funnel 指向 Dashboard 端口
sudo tailscale funnel --bg 9119

# 验证
tailscale serve status
# 应显示：Funnel on → proxy http://127.0.0.1:9119
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

| 现象 | 原因 | 解决 |
|------|------|------|
| Desktop 测试远程超时 | Funnel 指向了 8648（Node SPA） | 切到 9119（Dashboard） |
| Funnel 测试返回 401 | Dashboard 绑定了 127.0.0.1，Host 校验拒绝 | 用 `--host 0.0.0.0` 重启 |
| 模型页超时 "hermesapi" | Dashboard 没以 `--insecure` 启动或绑定不对 | 检查进程参数 `pgrep -af dashboard` |
| 切 Funnel 端口后 serve 配置丢失 | 新版 tailscale 语法变化 | 用 `sudo tailscale funnel --bg <port>` |
| Dashboard 自动回退到 127.0.0.1 | Gateway 检测到 dashboard 挂了就自动重启 | 先启 0.0.0.0 版本占住端口，gateway 重启的会绑定失败 |
| 笔记本浏览器能打开但 Desktop 超时 | DNS/网络问题 | 切手机热点测试；确认 URL 完整无截断 |

## 与 Web UI 的关系

如果需要同时保留 Web UI（Hermes Studio，8648端口）和远程 Desktop 访问：
- Funnel 只能指一个端口
- 选 Desktop 路线：Funnel → 9119（Dashboard），Web UI 仅本地访问
- 选 Web UI 路线：Funnel → 8648（Node SPA），Desktop 远程不可用
- 高级方案：Nginx/Caddy 反代，按路径分流（`/api/*` → 9119，`/` → 8648）
