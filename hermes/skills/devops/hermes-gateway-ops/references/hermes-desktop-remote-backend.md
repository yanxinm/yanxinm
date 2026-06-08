# Hermes Desktop 远程后端：笔记本连接基地

> 2026-06-08 实战验证。适用于：笔记本安装 Hermes Desktop → 通过 Tailscale Funnel 连接基地 Dashboard 作为远程后端。

## 架构

```
笔记本 Hermes Desktop ──HTTPS──▶ Tailscale Funnel (TS.net 域名)
                                        │
                                        ▼
                                基地 Python Dashboard (:9119)
                                 --host 0.0.0.0 --insecure
                                        │
                                        ▼
                                基地 Gateway (:8642) → 微信/飞书
```

**关键区别**：Desktop 远程模式连接的是 **Python Dashboard（9119）**，不是 Node SPA（8648）。两者端口不同，认证机制也不同。

## 认证机制

Dashboard 使用 **Session Token** 认证（不是 API_SERVER_KEY）：

- Token 在 Dashboard 启动时生成：`secrets.token_urlsafe(32)` 或从环境变量 `HERMES_DASHBOARD_SESSION_TOKEN` 读取
- 注入到 Dashboard HTML 中：`HERMES_SESSION_TOKEN__="<token>"`
- 客户端通过 Header 传递：`X-Hermes-Session-Token: <token>`
- 也支持 Bearer 方式：`Authorization: Bearer <token>`

**中间件链**（请求处理顺序）：
1. `host_header_middleware` — 拒绝 Host 不匹配的请求
2. `_dashboard_auth_gate` — OAuth 门控（`--insecure` 时跳过）
3. `auth_middleware` — Session Token 校验（OAuth 门控激活时跳过）

## 配置步骤

### 1. 基地：Dashboard 绑定 0.0.0.0 + --insecure

```bash
# 停止 gateway 自动管理的 dashboard（如有）
kill $(pgrep -f "hermes dashboard")

# 用 0.0.0.0 + insecure 启动
hermes dashboard --port 9119 --host 0.0.0.0 --insecure --no-open --skip-build
```

**为什么必须 `--host 0.0.0.0`**：Funnel 转发请求时 Host header 是 TS.net 域名。Dashboard 的 `host_header_middleware` 会拒绝 Host 与 bound_host 不匹配的请求。绑定 0.0.0.0 时该中间件放行所有 Host。

**为什么必须 `--insecure`**：绑定非 loopback 地址时，`should_require_auth()` 返回 True，触发 OAuth 门控。`--insecure` 强制 `auth_required=False`，回退到 Session Token 校验。

### 2. 固化 Session Token

Dashboard 每次重启生成新 token。固定它避免 Desktop 反复配置：

```bash
echo 'HERMES_DASHBOARD_SESSION_TOKEN=<固定token>' >> ~/.hermes/.env
```

生成随机 token：
```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 3. 配置 Tailscale Funnel 指向 Dashboard

```bash
# 新版 Tailscale 语法（v1.80+）
sudo tailscale funnel --bg 9119

# 验证
tailscale serve status
# 预期：Funnel on → proxy http://127.0.0.1:9119
```

### 4. 笔记本 Desktop 配置

| 配置项 | 值 |
|--------|-----|
| 模式 | Remote / 远程后端 |
| 地址 | `https://<machine>.tail<xxx>.ts.net` |
| 认证方式 | Token |
| Token | `<固定token>` |

## ⚠️ 关键陷阱

### 陷阱 1：Node SPA 不转发认证头

Funnel 指向 Node SPA（8648）时，`X-Hermes-Session-Token` 不会被转发到 Python Dashboard。即使 token 正确，也返回 401。

**修复**：Funnel 必须直接指向 Python Dashboard（9119），绕过 Node SPA。

### 陷阱 2：Host header 校验拒绝

Dashboard 绑定 `127.0.0.1` 时，`host_header_middleware` 拒绝 Funnel 转发的 TS.net Host header，返回 400 "Invalid Host header"。

**修复**：Dashboard 绑定 `0.0.0.0`（非 loopback）。

### 陷阱 3：Gateway 自动重启 Dashboard

Gateway 检测到 Dashboard 进程退出后会自动重启，但用的是原始参数（`--host 127.0.0.1`），覆盖手动启动的 `0.0.0.0` 版本。

**修复**：先 `kill` 旧进程再启动 `0.0.0.0` 版本，两个 Dashboard 会端口冲突——先启动的抢到端口。

### 陷阱 4：sudo 需要终端

`sudo tailscale funnel --bg 9119` 在非 PTY 环境下会因密码提示失败。Hermes terminal 工具需用 `pty=true`。

## 验证

```bash
# 端到端测试（公网）
curl -s https://<machine>.tail<xxx>.ts.net/api/status \
  -H "X-Hermes-Session-Token: <token>" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['version'], d['gateway_state'])"

# 预期输出：0.16.0 running
```

## 笔记本 Windows Desktop 安装（国内环境）

在国内网络环境下安装 Hermes Desktop 需要配置多个镜像源。**按顺序执行，缺一不可：**

### 前置配置（新开 cmd 窗口，逐条执行）

```cmd
:: 1. GitHub 代理（git clone 走 ghproxy.net）
git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"

:: 2. npm 国内镜像
npm config set registry https://registry.npmmirror.com

:: 3. Electron 镜像（否则 npm install 卡在 electron 二进制下载）
setx ELECTRON_MIRROR "https://npmmirror.com/mirrors/electron/"

:: 4. Playwright Chromium 镜像（否则 Installing Node.js dependencies 卡 30+ 分钟）
setx PLAYWRIGHT_DOWNLOAD_HOST "https://npmmirror.com/mirrors/playwright/"
```

> ⚠️ `setx` 只对新开的 cmd/PowerShell 窗口生效。执行完后必须重新打开终端再装。

### PowerShell 执行策略

如果 PowerShell 报 `npm.ps1` 无法加载：
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
输入 `Y` 确认。

### 常见安装失败

| 错误 | 原因 | 修复 |
|------|------|------|
| `git fetch failed (exit 128)` | GitHub 被墙，未配代理 | `git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"` |
| `npm install failed (exit -4082)` / `EBUSY` | `node_modules\electron` 被 Windows 安全软件锁定 | 任务管理器结束 `node.exe` 进程 → 重启电脑 → 重装 |
| `apps/desktop build failed (exit 1)` | Electron 编译环境问题 | 以管理员身份运行安装程序，或关闭杀毒软件实时防护 |
| npm 卡 30+ 分钟不动 | Playwright Chromium (~400MB) 走境外 CDN | 设 `PLAYWRIGHT_DOWNLOAD_HOST` |
| Electron 下载卡 10+ 分钟 | Electron 二进制走 GitHub Releases 直连 | 设 `ELECTRON_MIRROR` |

### 安装路径

Windows 安装位置：`C:\Users\<用户>\AppData\Local\hermes\`

如果多次安装失败、文件锁残留，删掉整个目录重来：
```cmd
rmdir /s /q C:\Users\<用户>\AppData\Local\hermes
```

## Desktop 远程模式已知限制

Desktop 远程模式下，**模型设置页（提供方/模型选择）可能不可用**，报 `Error invoking remote method 'hermesapi': Timed out connecting to Hermes backend after 15000ms`。这是 Desktop 通过 Electron IPC 调用本地方法但远程后端不支持导致的。

**绕过方法**：跳过模型设置页，直接进入「对话」（Chat）。对话功能走 WebSocket (`/api/ws`)，正常工作。模型配置保留基地本地设置即可。

## 诊断速查

| 症状 | 原因 | 修复 |
|------|------|------|
| 401 Unauthorized | Funnel 指向 Node SPA（8648），认证头未转发 | Funnel 指向 Dashboard（9119） |
| 400 Invalid Host header | Dashboard 绑定 127.0.0.1 | 绑定 0.0.0.0 |
| 401（token 正确） | Dashboard 重启导致 token 变更 | 固化 `HERMES_DASHBOARD_SESSION_TOKEN` |
| Funnel 不通 | sudo 需要密码 | `pty=true` 或用交互终端 |
| 两个 Dashboard 进程 | Gateway 自动重启抢了端口 | 先 kill 再启 0.0.0.0 版 |
| Desktop 模型页 `hermesapi` 超时 | 远程模式不支持 Electron IPC 方法 | 跳过模型设置页，直接进对话页 |
