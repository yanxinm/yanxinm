---
name: base-machine-ops
description: M710q Ubuntu 基地运维——远程访问（Tailscale/Funnel/SSH隧道）、网络诊断、GitHub被墙下载、端口管理、pnpm环境。
category: devops
tags: [基地, Tailscale, Funnel, 远程访问, GitHub加速, 端口管理]
---

# 基地运维（Base Machine Ops）

M710q Ubuntu 基地（`miao-thinkcentre-m710q-n080`）的远程访问、网络诊断、软件安装等运维操作。

## 触发条件

任何涉及基地远程访问、Tailscale 连接、端口暴露、GitHub 被墙下载等任务。

---

## 一、远程访问方案

### 方案 A：Tailscale Funnel（推荐，免费 HTTPS 公网，不依赖 Tailscale 客户端）

**一次性启用**（老缪在 Admin 面板操作）：
1. 基地执行 `tailscale funnel --help` 获取 node link -> 或在 Admin 面板直接启用 Funnel
2. 老缪浏览器打开链接，点「启用漏斗」
3. 基地执行：`sudo tailscale funnel --bg <port>`
4. 获得 `https://<hostname>.tail<xxx>.ts.net/` 公网地址

**新版 Funnel 语法**（v1.80+，`tailscale funnel <target>` 替代旧的 `funnel on`）：
```bash
sudo tailscale funnel --bg 9119             # 主 Funnel：Hermes Dashboard（443→9119）
sudo tailscale funnel --bg --https=8443 http://localhost:8123  # HA 面板（公网 8443→本地 8123）
tailscale serve status                       # 查看 serve/funnel 状态
sudo tailscale funnel --https=8443 off       # 关闭
```

**旧版语法（已废弃，但 `tailscale serve status` 仍显示 `Funnel on/off`）：**
```bash
tailscale funnel on   # 旧版启用
tailscale funnel off  # 旧版关闭
```

### 方案 A-2：Funnel 指向选择

| 端口 | 服务 | 适用场景 | 注意事项 |
|------|------|----------|----------|
| 8648 | Node SPA (Hermes Studio) | 完整 Web UI 聊天界面 | Node 代理不转发 `X-Hermes-Session-Token`，API 返回 401 |
| 9119 | Python Dashboard | API 访问 + 基础 Web UI + Desktop 远程后端 | 需 `--insecure --host 0.0.0.0`，直接支持 token 认证 |

---

## 一之补充：Hermes Desktop 远程后端

基地可作为 Hermes Desktop 的远程后端。笔记本安装 Hermes Desktop 后选 **Remote** 模式连接。

### 基地配置步骤

```bash
# 1. 设置固定 session token（否则每次重启会变）
echo "HERMES_DASHBOARD_SESSION_TOKEN=$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))')" >> ~/.hermes/.env

# 2. 停止旧 dashboard，用 0.0.0.0 + --insecure 重启
hermes dashboard --stop
hermes dashboard --port 9119 --host 0.0.0.0 --insecure --no-open --skip-build &

# 3. Funnel 指向 Dashboard（注意：不能指 Node SPA 8648，它不转发 auth header）
sudo tailscale funnel --bg 9119

# 4. 验证（从公网）
TOKEN=*** ~/.hermes/.env | grep DASHBOARD_SESSION | cut -d= -f2)
curl -s https://<hostname>.tail<xxx>.ts.net/api/status \
  -H "X-Hermes-Session-Token: $TOKEN"
```

### 笔记本配置

Hermes Desktop → Settings → Gateway → **Remote** 模式：
- 地址：`https://<hostname>.tail<xxx>.ts.net`
- 认证：Token
- Token：`<从 .env 取的 HERMES_DASHBOARD_SESSION_TOKEN>`

### 架构说明

```
笔记本浏览器/Desktop ──HTTPS──> Tailscale Funnel ──> 127.0.0.1:9119 (Python Dashboard)
                                                        ↑ --insecure --host 0.0.0.0
                                                        ↑ auth_required=False
                                                        ↑ X-Hermes-Session-Token 认证
```

**为什么不能指 8648（Node SPA）**：Funnel → Node(8648) → Python(9119) 这条链路中，Node 代理会丢弃 `X-Hermes-Session-Token` 请求头，导致 Python Dashboard 的 `auth_middleware` 返回 401。直接指 9119 绕过此问题。

详细认证架构见 [`references/hermes-remote-backend-auth.md`](references/hermes-remote-backend-auth.md)。

### Token 提取技巧

```bash
# 当前运行 token（从 dashboard HTML 注入中提取）
curl -s http://127.0.0.1:9119/ | sed -n 's/.*HERMES_SESSION_TOKEN__="\([^"]*\).*/\1/p'
```

### 方案 B：SSH 隧道

笔记本 PowerShell（需 Tailscale 双向通）：
```powershell
ssh -L 8648:127.0.0.1:8648 miao@100.86.13.11
```
浏览器访问 `http://127.0.0.1:8648`。

### 方案 C：Tailscale 直连

笔记本浏览器 `http://100.86.13.11:8648`，前提 `tailscale ping` 通。

---

## 二、Tailscale 网络诊断

```bash
tailscale status                              # 所有设备
tailscale ping 100.86.148.56                 # 基地→笔记本
```

**常见问题与修复**：

| 症状 | 原因 | 修复 |
|------|------|------|
| 基地→笔记本通，笔记本→基地不通 | 单位防火墙阻出站 DERP | 笔记本重启 Tailscale |
| 两边显示在线但 ping 不通 | DERP 中继失效 | 重启两端 Tailscale |
| headless 认证 | 无浏览器 | Admin→Keys→Generate auth key，`sudo tailscale up --auth-key=<key> --accept-routes` |

---

## 三、GitHub 被墙应对

基地网络：`github.com` 超时，`api.github.com` 可达。

### 3.1 Git 全局代理（推荐，一劳永逸）

```bash
# ghproxy.net 已验证可用，ghproxy.com 已失效
git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"
# 此后所有 git clone 自动走代理，无需手动加前缀
# 恢复直连：git config --global --unset url."https://ghproxy.net/https://github.com/".insteadOf
```

### 3.2 其他方案

```bash
# tarball 下载（绕过 git clone）
curl -L -o /tmp/repo.tar.gz "https://api.github.com/repos/<owner>/<repo>/tarball/main"
mkdir -p /path/to/dest && tar xzf /tmp/repo.tar.gz -C /path/to/dest --strip-components=1

# GHProxy 直连（手动前缀）
git clone https://ghproxy.net/https://github.com/<owner>/<repo>.git

# 依赖下载失败时跳过 postinstall
pnpm install --ignore-scripts
```

### 3.3 Windows / 笔记本同理

```cmd
git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"
```

---

## 四、基地关键端口

| 端口 | 服务 | 绑定 | 说明 |
|------|------|------|------|
| 8123 | Home Assistant | 0.0.0.0 | 智能家居控制面板 |
| 8648 | Hermes Web UI / Studio (Node SPA) | 0.0.0.0 | Vue 版完整聊天界面，但不能用于 Desktop 远程后端 |
| 9119 | Hermes Dashboard (Python) | 0.0.0.0 | API 服务 + 基础 Web UI，Desktop 远程后端口。`--insecure --host 0.0.0.0` |
| 8642 | Hermes Gateway API | 127.0.0.1 | 仅本地 |
| 8420 | Gateway 内部 | 127.0.0.1 | 仅本地 |
| 3071 | html-video Studio | 0.0.0.0 | 需先 patch 绑定地址 |
| 22 | SSH | 0.0.0.0 | 远程管理 |
| 1883 | Mosquitto MQTT (预留) | — | 未来可选 |

---

## 五、pnpm / Node 环境

```bash
# pnpm 在 Hermes node 目录下，需每次 export
export PATH="/home/miao/.hermes/node/bin:$PATH"
```

---

## 六、Docker 安装（国内环境）

### 优先使用 Ubuntu 官方源

Docker 官方源 `download.docker.com` 在国内经常被墙，**Ubuntu 22.04 官方仓库自带 docker.io**，直接用：

```bash
sudo apt-get install -y docker.io docker-compose-v2
# 版本：docker.io 29.1.x, compose v2.40.x — 完全够用
sudo usermod -aG docker $USER
sudo systemctl enable docker --now
# 新 shell 验证: docker version
```

⚠️ 不要折腾清华/阿里 Docker CE 源——GPG key 下载和 sudo 密码交互在 Hermes terminal 工具里容易连环失败。Ubuntu 官方 `docker.io` 包一行搞定。

### 无需 sudo 运行 Docker

```bash
# 加组后需新 shell 生效；Hermes terminal 里用 sg 临时切组：
sg docker -c "docker ps"
sg docker -c "docker compose up -d"
sg docker -c "docker compose -f /home/miao/docker/ha/docker-compose.yml pull"
sg docker -c "docker restart homeassistant"
```

⚠️ `sg docker -c "..."` 是 Hermes terminal 工具的关键技巧：每行 terminal 调用是独立 shell，`newgrp` 无效，`sg` 是正确姿势。不加 `sg` 会导致 `permission denied while trying to connect to the docker API`。

## 七、Home Assistant Docker 部署

### docker-compose.yml（network_mode: host）

```yaml
services:
  homeassistant:
    container_name: homeassistant
    image: ghcr.io/home-assistant/home-assistant:stable
    network_mode: host        # 必须 host 模式 — mDNS/UPnP 发现设备
    restart: unless-stopped
    volumes:
      - /home/miao/docker/ha/config:/config
      - /etc/localtime:/etc/localtime:ro
      - /run/dbus:/run/dbus:ro
    environment:
      - TZ=Asia/Shanghai
```

⚠️ `network_mode: host` 时不要配 `ports`（会报错）。HA 直接监听宿主机 8123。

### 部署命令

```bash
mkdir -p /home/miao/docker/ha
# 写入上述 compose 文件
sg docker -c "docker compose -f /home/miao/docker/ha/docker-compose.yml pull"
sg docker -c "docker compose -f /home/miao/docker/ha/docker-compose.yml up -d"
```

⚠️ 镜像 ~380MB，ghcr.io 拉取可能很慢（5-10分钟），属正常。

### HACS 手动安装

官方 `wget -O - https://get.hacs.xyz | bash -` 脚本在 Docker 环境下可能找不到 HA 目录。手动安装：

```bash
HACS_VERSION=$(curl -s https://api.github.com/repos/hacs/integration/releases/latest | grep '"tag_name"' | head -1 | sed 's/.*"tag_name": "\(.*\)".*/\1/')
wget -q "https://github.com/hacs/integration/releases/download/${HACS_VERSION}/hacs.zip" -O /tmp/hacs.zip
sudo mkdir -p /home/miao/docker/ha/config/custom_components/hacs
sudo unzip -qo /tmp/hacs.zip -d /home/miao/docker/ha/config/custom_components/hacs
sg docker -c "docker restart homeassistant"
# 之后在 HA Web UI 中：设置 → 设备与服务 → 添加集成 → 搜 HACS → 安装
```

⚠️ Docker 创建的 `/config` 目录属主是 root，所以需要 `sudo`。

### HA 反向代理信任配置（Funnel 必配）

HA 在 Tailscale Funnel 后面时，需要信任来自 127.0.0.1 的反向代理请求，否则返回 400：

```yaml
# 添加到 /config/configuration.yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 127.0.0.1
```

### 写入 root 属主配置文件

当 `sudo` 密码不可用（Hermes terminal 工具 sudo 交互不稳定）时，用 `docker exec` 在容器内写入：

```bash
# 追加配置到 HA 的 configuration.yaml
sg docker -c "docker exec homeassistant sh -c 'cat >> /config/configuration.yaml' << 'EOF'
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 127.0.0.1
EOF"
sg docker -c "docker restart homeassistant"
```

### 防火墙 — ufw 放行 8123

HA 在 `network_mode: host` 下监听 0.0.0.0:8123，但 ufw 默认 DROP INPUT。**Tailscale ping 通但 TCP 不通时，优先检查 ufw**：

```bash
sudo ufw allow 8123/tcp comment 'Home Assistant'
sudo ufw status | grep 8123   # 确认
```

### 中国智能家居平台接入参考

见 [`references/smart-home-platforms-china.md`](references/smart-home-platforms-china.md) — 六大平台（小米/追觅/美的/晶御/海尔/华为）HA 集成方案与可靠性评估。

## 八、html-video 项目

### 启动 Studio

```bash
cd /home/miao/html-video && \
  export PATH="/home/miao/.hermes/node/bin:$PATH" && \
  node packages/cli/dist/bin.js studio --port 3071
```

### 已踩坑

- **Studio 默认绑定 127.0.0.1**：需 patch `packages/cli/dist/studio-server.js`，将 `server.listen(port, '127.0.0.1',...)` 改为 `'0.0.0.0'`
- **pnpm 不在默认 PATH**：路径在 `/home/miao/.hermes/node/bin/pnpm`
- **onnxruntime-node 下载被墙**：用 `pnpm install --ignore-scripts` 跳过
- **Playwright 安装**：`--ignore-scripts` 跳过后，需手动用 playwright binary 执行 `install chromium`

---

## 九、Hermes Profiles 管理

### 创建 Profile 时 `--clone` 失败

**症状**：`hermes profile create <name> --clone` 报错 `shutil.Error: [('/home/miao/.hermes/skills/xxx', ...)]`

**根因**：`~/.hermes/skills/` 目录下有断开的符号链接，`shutil.copytree` 无法处理。

**修复**：
```bash
# 找到并删除所有断链
find ~/.hermes/skills -xtype l
# 确认后删除
find ~/.hermes/skills -xtype l -delete

# 如有部分创建的 profile 残骸也清掉
rm -rf ~/.hermes/profiles/<name>

# 重新创建
hermes profile create <name> --clone
```

### 查看 Profile 配置
```bash
hermes profile list              # 所有 profile 及状态
hermes profile show <name>       # 查看详情
```

---

## 十、Windows Desktop 安装（国内环境）

在笔记本（Windows）上安装 Hermes Desktop 时遇到的坑和解决方案。

### 下载地址

<https://hermes-agent.nousresearch.com/desktop>

### 常见问题

| 症状 | 原因 | 修复 |
|------|------|------|
| `npm.ps1 无法加载，禁止运行脚本` | PowerShell 执行策略 | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`（管理员 PS） |
| `Installing Node.js dependencies` 卡 30 分钟+ | npm 下载被墙 | `npm config set registry https://registry.npmmirror.com` |
| Playwright Chromium 下载慢 | 境外 CDN | `setx PLAYWRIGHT_DOWNLOAD_HOST "https://npmmirror.com/mirrors/playwright/"`（管理员 cmd，**需新开窗口生效**） |
| `Building desktop app` 卡 10 分钟+ / `build failed` | Electron 二进制下载被墙 | `setx ELECTRON_MIRROR "https://npmmirror.com/mirrors/electron/"`（管理员 cmd，**需新开窗口生效**） |
| `git fetch failed (exit 128)` | Git 克隆 GitHub 被墙 | `git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"`（cmd） |
| `EBUSY resource busy or locked` | 杀毒软件锁 `node_modules\electron` | 重试（锁通常自动释放），或删除 `AppData\Local\hermes\hermes-agent\node_modules` 重装 |
| `apps/desktop build failed (exit 1)` | electron 编译失败 | 管理员运行安装程序、关闭实时防护、或干脆用 Web UI 代替 |

### 建议

国内环境安装 Hermes Desktop 坑较多。**安装前先在 cmd（管理员）一次性配好所有镜像**：

```cmd
npm config set registry https://registry.npmmirror.com
setx ELECTRON_MIRROR "https://npmmirror.com/mirrors/electron/"
setx PLAYWRIGHT_DOWNLOAD_HOST "https://npmmirror.com/mirrors/playwright/"
git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"
```

⚠️ `setx` 修改的是永久环境变量，需要**新开一个 cmd 窗口**才能生效。配完验证：

```cmd
echo %ELECTRON_MIRROR%
echo %PLAYWRIGHT_DOWNLOAD_HOST%
git config --global --list | findstr ghproxy
```

如果 `%PLAYWRIGHT_DOWNLOAD_HOST%` 输出为空，说明还在旧窗口——关掉重开一个 cmd 再验证。

如果遇到 `EBUSY` 文件锁（杀毒软件锁 electron），删 `node_modules` 重试；还不行就**重启电脑**最快。如果 `build failed` 持续出现，**Web UI（浏览器打开 Funnel URL）是完整替代方案**。

---

## 十一、第三方 Skill 安装

Hermes 会自动发现 `~/.hermes/skills/<name>/` 下任何包含 `SKILL.md` 的目录，无需手动注册。

### 安装流程

```bash
# 1. 下载（国内走 ghproxy 镜像）
curl -L -o /tmp/skill.zip \
  "https://ghproxy.net/https://github.com/<owner>/<repo>/archive/refs/heads/main.zip"

# 2. 解压并移入 skills 目录
unzip /tmp/skill.zip
mv <repo>-main ~/.hermes/skills/<skill-name>

# 3. （可选）创建 runtime.conf 指定运行时，避免每次检测
cat > ~/.hermes/skills/<skill-name>/runtime.conf << 'EOF'
RUNTIME=python3
CLI_PATH=scripts/cli.py
EOF

# 4. 验证安装
python3 ~/.hermes/skills/<skill-name>/scripts/cli.py doc  # 或对应入口命令

# 5. 确认 Hermes 已识别
# 用 skill_view('<skill-name>') 检查，readiness_status 应为 "available"
```

### 已验证案例：AnySearch

| 项目 | 值 |
|------|-----|
| 仓库 | `anysearch-ai/anysearch-skill` |
| 安装目录 | `~/.hermes/skills/anysearch/` |
| 运行时 | Python 3 (CLI: `scripts/anysearch_cli.py`) |
| API Key | 可选（匿名模式可用，1000次/天） |
| 官网 | https://anysearch.com |
| 文档 | https://anysearch.com/docs |

AnySearch 提供 `search`、`batch_search`、`extract`、`get_sub_domains` 四个命令，覆盖通用搜索（含中文）、16 个垂直领域（金融/旅行/代码/学术等）、并行批量搜索和网页内容提取。
