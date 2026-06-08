---
name: hermes-base-operations
description: Hermes 基地运维操作——远程 Desktop 连接、Tailscale Funnel 配置、安全加固、服务管理、Windows 客户端安装。
tags: [hermes, tailscale, desktop, security, devops]
---

# Hermes 基地运维

## 适用场景
基地（Linux headless 主机）上的 Hermes 运维任务：远程 Desktop 连接、网络穿透、安全加固、服务启停、Windows 客户端安装踩坑。

---

## 一、Hermes Desktop 远程连接（完整工作流）

### 背景
Hermes Desktop 支持 **Remote 模式**——笔记本 Desktop 客户端通过 HTTPS 连接基地上的后端，完全不依赖 Tailscale 客户端，任何网络环境都能用。

### 前提
- 基地已安装 Tailscale 且启用 Funnel
- 基地运行 `hermes gateway` 和 `hermes dashboard`

### 步骤

**1. 基地侧：Dashboard 绑定 0.0.0.0 + 关闭 auth gate**

```bash
# 停掉旧 Dashboard
hermes dashboard --stop

# 用 --insecure + --host 0.0.0.0 重启（关闭 OAuth gate，允许非 loopback 访问）
hermes dashboard --port 9119 --host 0.0.0.0 --insecure --no-open --skip-build
```

⚠️ 不加 `--insecure` 会导致 Host header 校验拒绝（"Invalid Host header"），因为 Funnel 进来的请求 Host 是 TS.net 域名。

**2. 固化 Session Token**

Dashboard 每次重启生成随机 token，Desktop 需要固定 token：

```bash
# 生成固定 token 写入 .env
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
# 例如：pMbaoVMiN5HU8q7xHvGzu7dRWlz_gDWYz1LvP4UbT5s

echo "HERMES_DASHBOARD_SESSION_TOKEN=<你的token>" >> ~/.hermes/.env

# 重启 Dashboard 载入
hermes dashboard --stop
hermes dashboard --port 9119 --host 0.0.0.0 --insecure --no-open --skip-build
```

验证 token 生效：
```bash
curl -s http://127.0.0.1:9119/ | grep HERMES_SESSION_TOKEN
# 应输出固定 token
```

**3. Funnel 指向 Dashboard**

```bash
# Funnel 必须指向 9119（Python Dashboard），不能指向 8648（Node SPA）
sudo tailscale funnel --bg 9119
```

⚠️ 端口选择陷阱：
| 端口 | 服务 | Desktop 远程模式 |
|------|------|:--:|
| 8648 | Node SPA / Hermes Studio | ❌ 不转发 auth header |
| 8642 | Gateway API | ❌ 缺少 `/api/model/options` 等端点 |
| **9119** | **Python Dashboard** | **✅ 正确** |

**4. Desktop 侧配置**

Settings → 网关 → 选择「远程网关」：
- 远程 URL：`https://miao-thinkcentre-m710q-n080.tail589fe7.ts.net`
- 认证方式：Token
- Token：固定 token

### 验证
```bash
curl -s https://<ts-net域名>/api/status \
  -H "X-Hermes-Session-Token: <token>"
# 应返回 200 + version/gateway_state/gateway_platforms
```

### 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| "Invalid Host header" | Dashboard 绑在 127.0.0.1，Host 不匹配 | 改绑 0.0.0.0 |
| 401 Unauthorized | Token 未注入或过期 | 固化 token 到 .env |
| "Timed out...8000ms" | Funnel 指向了 8648（Node SPA） | 改指 9119 |
| "Timed out...15000ms"（模型页） | WebSocket 端点 404 | 正常——切到对话页即可 |
| Dashboard 重启后被 Gateway 覆盖 | Gateway 自动重启 Dashboard 用原参数 | 先 gateway stop → 手动 dashboard start → gateway start |

---

## 二、基地安全加固

### 标准清单

| 步骤 | 命令 |
|------|------|
| 关 CUPS | `sudo systemctl disable --now cups` |
| 装 Fail2ban | `sudo apt install fail2ban -y`<br>`sudo systemctl enable --now fail2ban` |
| 开 UFW | `sudo ufw default deny incoming`<br>`sudo ufw allow ssh`<br>`sudo ufw allow from 100.64.0.0/10`<br>`sudo ufw enable` |
| SSH 加固 | `sudo tee /etc/ssh/sshd_config.d/99-hardening.conf << 'EOF'`<br>`PasswordAuthentication no`<br>`PermitRootLogin no`<br>`MaxAuthTries 3`<br>`EOF`<br>`sudo systemctl restart sshd` |

⚠️ 以上全部需要 **sudo 密码**。Agent terminal 无密码时命令会失败。解决方法：将密码写入 `~/.hermes/.env`（`SUDO_PASSWORD=<pw>`），Hermes terminal 工具自动读取。详见 `hermes-gateway-ops` 技能 §四-B「Headless sudo」。

### Tailscale 网段
`100.64.0.0/10` 是 Tailscale 的 CGNAT 地址空间，放行此段保证 Tailnet 内设备互通。

### 无人值守更新
```bash
systemctl is-enabled unattended-upgrades  # 确认已启用
```

---

## 三、Windows 客户端安装（国内环境）

### 必须预先配置的镜像

Hermes Desktop 安装程序从境外下载多个大型依赖，直接装必卡死。**开装前先配：**

```cmd
# npm 镜像
npm config set registry https://registry.npmmirror.com

# 环境变量（需新开 cmd 窗口生效）
setx ELECTRON_MIRROR "https://npmmirror.com/mirrors/electron/"
setx PLAYWRIGHT_DOWNLOAD_HOST "https://npmmirror.com/mirrors/playwright/"

# Git 代理
git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"

# PowerShell 执行策略（如遇 npm.ps1 禁止运行）
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 常见错误

| 错误 | 原因 | 解决 |
|------|------|------|
| `git fetch failed (exit 128)` | GitHub 被墙 | 配 git insteadOf 代理 |
| npm 卡 30 分钟不动 | npm 下载被墙 | 配 npmmirror 镜像 |
| `npm EBUSY -4082` | Windows Defender 锁 node_modules | 关杀软实时防护 / 重启后删 `node_modules` 重装 |
| `build failed (exit 1)` | Electron 二进制下载失败 | 配 `ELECTRON_MIRROR` |
| `npm.ps1 禁止运行` | PowerShell 执行策略 | `Set-ExecutionPolicy RemoteSigned` |

### 如果实在装不上
直接用浏览器打开 Funnel URL 使用 Hermes Web UI——功能和 Desktop 完全一致。

---

## 四、git clone GitHub 加速

基地和笔记本通用：

```bash
git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"
```

测试可用镜像：
```bash
for url in https://ghproxy.net https://ghproxy.com https://mirror.ghproxy.com; do
  echo -n "$url → "; curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 "$url"
  echo
done
```

⚠️ ghproxy.com 经常挂，ghproxy.net 是目前最稳定的。

---

## 五、服务管理速查

```bash
# Dashboard
hermes dashboard --status           # 查看状态
hermes dashboard --stop             # 停止
hermes dashboard --port 9119 --host 0.0.0.0 --insecure --no-open --skip-build  # 手动启动

# Gateway
hermes gateway status               # 查看状态
hermes gateway restart              # 重启

# Tailscale Funnel
tailscale serve status              # 查看
sudo tailscale funnel --bg <port>   # 切换到新端口

# 全链路自启验证
sudo reboot
# 等 2 分钟，微信发消息 → 有回复即成功
```
