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

## Home Assistant on the base

When operating the base-machine Home Assistant Docker stack, use the following reference. HA Docker/compose shape, API proxy pattern, Bluetooth/AppArmor fix (`privileged: true` + D-Bus mount), HA token/auth pitfalls, and config-flow inspection commands.

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

## 一之补充 A：Tailscale Funnel 路径路由最佳实践\n\n### HA 与 Hermes Dashboard 共存\n\n**问题**：HA 不支持子路径（`/ha` 会 400 Bad Request）。Funnel 路径代理到 HA 根路径时，HA 收到的是 `/ha/xxx` 而非 `/xxx`，导致路由失败。\n\n**解决方案**：把 HA 放 Funnel 根路径 `/`，其他服务放子路径：\n\n```bash\n# HA → 根路径（必须）\nsudo tailscale funnel --bg --https=443 --set-path=/ http://localhost:8123\n# Hermes Dashboard → /dash（Dashboard 对子路径容忍度高）\nsudo tailscale funnel --bg --https=443 --set-path=/dash http://127.0.0.1:9119\n```\n\n结果：\n- `https://<host>.ts.net/` → HA\n- `https://<host>.ts.net/dash` → Hermes Dashboard\n\n### 端口选择\n\n⚠️ Funnel 支持的标准端口是 443。非标准端口（8443、10000）**可能在笔记本端被防火墙/代理拦截**，表现为 `ERR_CONNECTION_TIMED_OUT`。优先用 443。\n\n### 笔记本 Tailscale 单向不通排查\n\n症状：基地→笔记本通，笔记本→基地不通（`ping 100.86.13.11` 超时）。\n\n```bash\n# 基地查状态\ntailscale status  # 看 ethan 是否 active; relay \"tok/sfo\" 正常\n# 笔记本查状态  \ntailscale status  # 确认基地显示 active; tx/rx 有数据说明链路在走\n```\n\n如果 `tailscale status` 两端都显示 active 且 tx/rx 有非零值，但 TCP 连接仍不通：\n1. **检查 Funnel 端口**：笔记本可能只放行 443，非标端口被拦\n2. **检查 ufw**：基地 `sudo ufw status`，确认目标端口已放行\n3. **重启笔记本 Tailscale**：退出重开客户端\n4. **终极方案**：用 Funnel 443 代替 Tailscale 直连 IP\n\n---\n\n## 一之补充 B：Hermes Desktop 远程后端

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
| ping 通但 TCP 全部超时（SSH/SMB/HTTP） | **DERP 中继不转发 TCP**（已验证：双向 SSH/22、SMB/445、HTTP/18888 全超时，防火墙关闭也不行） | 必须等两台机器直连（同一局域网），走中继时跳过同步 |
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

Home Assistant 相关部署细节、蓝牙 Docker 修复、Xiaomi Miot 验证流排查见 [`references/home-assistant-m710q.md`](references/home-assistant-m710q.md)。

| 端口 | 服务 | 绑定 | 说明 |
|------|------|------|------|
| 8123 | Home Assistant | 0.0.0.0 | 智能家居控制面板 |
| 8080 | HA API Proxy | 0.0.0.0 | 注入令牌的 HA 代理，无需认证即可调用 API |
| 8648 | Hermes Web UI / Studio (Node SPA) | 0.0.0.0 | Vue 版完整聊天界面，但不能用于 Desktop 远程后端 |
| 9119 | Hermes Dashboard (Python) | 0.0.0.0 | API 服务 + 基础 Web UI，Desktop 远程后端口。`--insecure --host 0.0.0.0` |
| 8642 | Hermes Gateway API | 127.0.0.1 | 仅本地 |
| 8420 | Gateway 内部 | 127.0.0.1 | 仅本地 |
| 3071 | html-video Studio | 0.0.0.0 | 需先 patch 绑定地址 |
| 8123 | Home Assistant Web UI/API | host 网络 | HA Docker 本体；网页登录/集成配置走此端口 |
| 8080 | HA API Proxy | 0.0.0.0 | `/home/miao/ha_proxy.py` 注入 HA 长期令牌后转发到 8123；供脚本/API/Tailscale 调用 |
| 22 | SSH | 0.0.0.0 | 远程管理 |
| 8123 | Home Assistant | 0.0.0.0 | HA 网页后台，仅在本地/内网直接访问 |
| 8080 | HA API Proxy | 0.0.0.0 | Token 注入代理，Tailscale `http://100.86.13.11:8080/api/` |
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
    privileged: true          # ⚠️ 蓝牙需要！否则 AppArmor 阻止 D-Bus → setup_retry
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

### HACS 下载失败 → 命令行兜底安装 custom_components

当 HACS 在 HA Web UI 中下载 GitHub 插件失败（`Could not download, see log for details`），在基地命令行用 ghproxy 镜像手动安装：

**方法 A：wget zip（标准）**
```bash
# 示例：批量下载三个插件
wget -q "https://ghproxy.net/https://github.com/al-one/hass-xiaomi-miot/archive/refs/heads/master.zip" -O /tmp/xiaomi_miot.zip
wget -q "https://ghproxy.net/https://github.com/Tasshack/dreame-vacuum/archive/refs/heads/master.zip" -O /tmp/dreame.zip
wget -q "https://ghproxy.net/https://github.com/hasscc/meiju/archive/refs/heads/master.zip" -O /tmp/meiju.zip

# 逐个解压安装（zip 内结构: <repo>-<branch>/custom_components/<name>/）
for f in xiaomi_miot dreame meiju; do
  rm -rf /tmp/${f}_extract
  unzip -qo /tmp/${f}.zip -d /tmp/${f}_extract
  dir=$(ls /tmp/${f}_extract | head -1)
  sudo cp -r /tmp/${f}_extract/${dir}/custom_components/* /home/miao/docker/ha/config/custom_components/
done
sg docker -c "docker restart homeassistant"
```

**方法 B：git clone via ghproxy（wget 超时时）**
```bash
git clone --depth 1 https://ghproxy.net/https://github.com/banto6/haier /tmp/haier_repo
sudo cp -r /tmp/haier_repo/custom_components/haier /home/miao/docker/ha/config/custom_components/
```

⚠️ 部分仓库 `custom_components` 目录名与 HACS slug 不同（如 `treeow_home`），需 `ls` 确认后再 cp。
⚠️ 所有写入 `/config` 的操作需 `sudo`（Docker volume 属主为 root）。

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

### 蓝牙集成 — 需要 privileged 模式

**症状**：蓝牙集成状态 `setup_retry`，日志报：
```
Failed to start Bluetooth: [org.freedesktop.DBus.Error.AccessDenied] 
An AppArmor policy prevents this sender...
```

**根因**：Docker 的 AppArmor 默认策略阻止容器通过 D-Bus 访问蓝牙硬件。

**修复**：在 `docker-compose.yml` 中加 `privileged: true`，然后重建容器：
```bash
sg docker -c "docker compose -f /home/miao/docker/ha/docker-compose.yml down"
sg docker -c "docker compose -f /home/miao/docker/ha/docker-compose.yml up -d"
```

⚠️ 数据不受影响（`/config` 是 bind mount volume）。重建容器约 30 秒。

当无法通过 Web UI 创建长期令牌时，可手动操作 HA 的 auth 存储。详见：
- [`references/ha-auth-token-creation.md`](references/ha-auth-token-creation.md) — auth 存储结构、JWT 签发方法、关键坑点
- [`references/ha-gen-token.py`](references/ha-gen-token.py) — 宿主机上执行的令牌生成脚本（操作 bind mount 路径，需先 `docker stop`）
- [`references/ha-proxy-notes.md`](references/ha-proxy-notes.md) — ha_proxy.py 代理方案说明

⚠️ 核心坑：**HA 启动后会用内存数据覆盖 auth 文件**。修改 auth 存储前必须先 `docker stop homeassistant`。

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

## 七、Home Assistant Docker on 基地

HA 在基地用 Docker Compose 运行时，详见 [`references/home-assistant-docker-ops.md`](references/home-assistant-docker-ops.md)。该参考包含：HA/proxy 验证命令、`privileged: true` 修复蓝牙 AppArmor/D-Bus、HA 长期令牌代理模式、HA 本地密码 hash 的 base64(bcrypt) 格式、Xiaomi Miot 登录排障，以及已检测到的自定义集成清单。

---

## 七、Home Assistant on Base Machine

HA Docker / integration troubleshooting notes live in [`references/home-assistant-docker-integrations.md`](references/home-assistant-docker-integrations.md). Use this when operating the base-machine HA stack, especially for:

- HA Docker compose shape (`host` networking, D-Bus mount, `privileged: true` for Bluetooth)
- HA API proxy on port 8080 with long-lived token injection
- Xiaomi Miot account flow and `need_verify` handling
- Midea AC LAN compatibility patches for HA 2026 removed unit constants

---

## 七、Home Assistant / 智能家居运维

HA Docker、ha_proxy、蓝牙 AppArmor、Xiaomi Miot、Midea AC LAN 等故障处理见 [`references/home-assistant-ha-setup.md`](references/home-assistant-ha-setup.md)。处理第三方账号时使用 `/tmp` 临时文件，完成后删除；不要在回复中复述密码。

---

## 七、Home Assistant on 基地

HA/智能家居集成排障经验见 [`references/home-assistant-ops.md`](references/home-assistant-ops.md)。覆盖 Docker privileged 蓝牙修复、HA API proxy、Xiaomi Miot 二次验证、Midea AC LAN 在 HA 2026 的兼容补丁、Dreame Vacuum IP/token 取数注意事项，以及临时凭据清理规范。

---

## 七、Home Assistant（Docker）运维

HA v2026.6.1 跑在 Docker 里（ghcr.io/home-assistant/home-assistant:stable），docker-compose 在 /home/miao/docker/ha/。host 网络 + privileged（蓝牙）。

### 7.1 容器管理

```bash
cd /home/miao/docker/ha
sudo docker compose restart homeassistant   # 重启（~20s）
sudo docker compose down                    # 停+删
sudo docker compose up -d                   # 启动
```

### 7.2 HA API Proxy

ha_proxy.py 监听 0.0.0.0:8080，转发 8123，自动注入长期访问令牌。cron @reboot 自启。

```bash
cd /home/miao && python3 ha_proxy.py &
curl http://localhost:8080/api/            # {"message":"API running."}
curl http://100.86.13.11:8080/api/         # Tailscale
```

### 7.3 长期访问令牌

HA 2026 的长期令牌是 JWT。需在 .storage/auth 插入 token_type:long_lived_access_token 的 refresh_token（含 token、jwt_key 字段），用 jwt_key 签发 JWT(payload:iss,iat,exp)。令牌在 ~/.ha_token（600），10年有效。HA密码 ha2026!。

### 7.4 HA 关键端口/地址

| 端口 | 服务 |
|------|------|
| 8123 | HA Web UI（yanxinm/ha2026!） |
| 8080 | HA API Proxy（自动注入令牌） |

HA 网页 http://192.168.1.42:8123 ，API Proxy http://100.86.13.11:8080/api/

### 7.5 HA 自定义集成兼容修补

Midea AC LAN v0.3.22 在 HA 2026.6 上因 homeassistant.const 常量删除而无法加载配置流。修补要点：
- midea_devices.py：删除 TIME_DAYS/TIME_HOURS 等已移除常量导入，改为本地定义
- config_flow.py：登录表单 server 选项改用字符串键 "1"/"2"/"3"/"4"，提交时转 int

Dreame Vacuum 插件链式导入 map.py → py_mini_racer。若编译失败，用空桩模块绕过：`echo "class MiniRacer:..." > /usr/local/lib/python3.14/site-packages/py_mini_racer.py`

---

## 八、Windows Desktop 安装（国内环境）

## 八、Home Assistant 基础运维

基地运行 HA Docker 容器。详细设置（HA 代理搭建、插件兼容性修复（HA 2026 const 变更）、设备 LAN 发现）见 [`references/ha-infra-setup.md`](references/ha-infra-setup.md)。


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

## 八、字体管理

基地已预装公文排版和 PPT 常用中文字体，并通过 fontconfig 设置了 Windows 字体名到 Linux 字体的别名映射。

### 已安装字体

| 来源 | 许可 | 包含 |
|------|------|------|
| Fandol（CTAN） | GPL v2+ | 仿宋/宋体(Regular+Bold)/黑体(Regular+Bold)/楷体 |
| cwTeX | GPL | 仿宋體/粗黑體/楷書/明體 |
| Noto CJK Extra | SIL OFL | 思源黑体+宋体 全字重（Thin→Black） |
| 文泉驿 | GPL | 微米黑/正黑/等宽 |

### 验证别名映射

```bash
fc-match "仿宋_GB2312"      # → FandolFang-Regular.otf
fc-match "方正小标宋_GBK"    # → FandolSong-Bold.otf
fc-match "黑体"              # → FandolHei-Bold.otf
fc-match "微软雅黑"          # → Noto Sans CJK SC Regular
fc-match "Times New Roman"   # → Liberation Serif Regular
```

### 添加新字体

```bash
# 用户字体目录
mkdir -p ~/.local/share/fonts/
cp *.ttf *.otf ~/.local/share/fonts/
fc-cache -fv

# 系统字体目录（需要 sudo）
sudo cp *.otf /usr/local/share/fonts/
sudo fc-cache -fv
```

### fontconfig 配置路径

⚠️ **Hermes 修改了 `$HOME`**，实际 HOME 为 `/home/miao/.hermes/profiles/jike/home/`。fontconfig 用户配置文件 `~/.config/fontconfig/fonts.conf` 必须放在此路径下才能被加载。

也可使用系统级路径 `/etc/fonts/conf.d/99-*.conf`（需 sudo）。

---

## 八、字体管理

基地已预装公文排版和 PPT 常用中文字体，并通过 fontconfig 设置了 Windows 字体名到 Linux 字体的别名映射。

### 已安装字体

| 来源 | 许可 | 包含 |
|------|------|------|
| Fandol（CTAN） | GPL v2+ | 仿宋/宋体(Regular+Bold)/黑体(Regular+Bold)/楷体 |
| cwTeX | GPL | 仿宋體/粗黑體/楷書/明體 |
| Noto CJK Extra | SIL OFL | 思源黑体+宋体 全字重（Thin→Black） |
| 文泉驿 | GPL | 微米黑/正黑/等宽 |

### 别名映射（`~/.config/fontconfig/fonts.conf`）

```bash
# 验证映射
fc-match "仿宋_GB2312"      # → FandolFang-Regular.otf
fc-match "方正小标宋_GBK"    # → FandolSong-Bold.otf
fc-match "黑体"              # → FandolHei-Bold.otf
fc-match "微软雅黑"          # → Noto Sans CJK SC Regular
fc-match "Times New Roman"   # → Liberation Serif Regular
```

### 添加新字体

```bash
# 用户字体目录
mkdir -p ~/.local/share/fonts/
cp *.ttf *.otf ~/.local/share/fonts/
fc-cache -fv

# 系统字体目录（需要 sudo）
sudo cp *.otf /usr/local/share/fonts/
sudo fc-cache -fv
```

### 字体别名配置

配置路径：`$HOME/.config/fontconfig/fonts.conf`
（⚠️ Hermes 修改了 `$HOME`，实际路径为 `/home/miao/.hermes/profiles/jike/home/.config/fontconfig/fonts.conf`）

或在系统级目录：`/etc/fonts/conf.d/99-*.conf`（需要 sudo）

---

## 十一、基地路径差异（与笔记本 WSL 的区别）

基地是独立 Ubuntu 机器（M710q），**没有 WSL 层**。笔记本上的 Hermes 运行在 WSL 中，可通过 `/mnt/c/`、`/mnt/e/` 访问 Windows 盘符。基地上 `/mnt/` 为空目录，没有这些挂载点。

### 常见陷阱

| 笔记本 WSL 路径 | 基地是否可用 | 说明 |
|-----------------|-------------|------|
| `/mnt/e/百度云同步盘/工作台账/` | ❌ 不可用 | 独立 Ubuntu 无 Windows 盘符挂载 |
| `/mnt/c/Users/yanxi/...` | ❌ 不可用 | 同上 |
| `~/` 下的文件 | ✅ 可用 | 但内容可能不同（不同机器） |
| Tailscale IP 挂载 | ✅ 可用 | 需先配置网络共享 |

### 迁移时需检查的 cron 任务

从笔记本迁移到基地后，需验证每个 cron 任务中的路径是否在基地上可达。特别注意：
- 脚本中的硬编码路径（`weekly_scan.py` SRC 等）
- prompt 中引用的文件夹路径
- 外部依赖（gbrain、convert_docs.py）是否已同步安装

验证命令：`ls <路径> 2>&1` 直接测试。

### 诊断技巧：排除 Windows 防火墙干扰

当 Tailscale TCP 不通时，Windows 防火墙是主要嫌疑。排除法：

```powershell
# 1. 临时全关防火墙（诊断用，测完立即恢复）
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False

# 2. 从基地测试 TCP 连接
#    （如 SSH/curl 测试）

# 3. 立即恢复防火墙
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
```

- 关了防火墙仍不通 → 问题不在防火墙，在 Tailscale 中继（DERP 不转发 TCP）或网络层面
- 关了防火墙能通 → 问题在防火墙规则，需精确添加 RemoteAddress 规则

⚠️ **关键发现**：Tailscale DERP 中继**双向 TCP 全不通**（已验证：SMB/445、SSH/22、HTTP/18888 全部超时，即使 Windows 防火墙完全关闭）。`tailscale ping` 能通但那是 Tailscale 自有协议，与 TCP 无关。**文件同步只能依赖 Tailscale 直连**（两台机器在同一局域网时）。

#### 方案：SSH + rsync（仅直连时执行）

**前提**：
- 笔记本启用 OpenSSH Server 并配置免密登录
- 两台机器在同一局域网（Tailscale 显示 `direct` 而非 `relay "xxx"`）

**笔记本端配置**：
```powershell
# 笔记本管理员 PowerShell
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType Automatic
New-NetFirewallRule -DisplayName "SSH for Tailscale" -Direction Inbound -Protocol TCP -LocalPort 22 -RemoteAddress 100.64.0.0/10 -Action Allow

# 添加基地公钥（从基地 cat ~/.ssh/id_ed25519.pub 获取）
mkdir C:\Users\yanxi\.ssh -Force
Add-Content C:\Users\yanxi\.ssh\authorized_keys "<基地公钥>"
```

**基地端同步脚本** `~/.hermes/scripts/sync_taizhang.sh`：
- 先通过 `tailscale status --json` 检测是否直连（非直连直接退出）
- 直连时执行 `rsync -av` 增量拉取文档（仅 .docx/.xlsx/.pdf/.txt/.md）
- 仅拉取不删除，本地副本不丢历史

**中继检测技巧**：
```bash
# 从 tailscale status JSON 提取中继信息
RELAY=$(tailscale status --json | python3 -c "
import json,sys
d=json.load(sys.stdin)
for p in d.get('Peer',{}).values():
    if p.get('HostName')=='ethan':
        print(p.get('Relay',''))
        break
")
# 空串 = 直连；非空 = 走中继，跳过同步
```

**定时任务**：
- `5323ccd7cf51`「周末台账同步」：周六+周日 12:00，no_agent 跑 `sync_taizhang.sh`
- `dfdd687d1890`「工作台账扫描」：周一 9:00，LLM 加载 markitdown 扫描本地 `~/工作台账/`

**同步参数说明**：
| 选项 | 值 | 说明 |
|------|-----|------|
| 文件类型 | docx, xlsx, pdf, txt, md | 排除 PPT（3.7GB）和视频 |
| 总量 | ~3700 文件, 2.5GB | rsync 首次 3-4 分钟，后续增量秒级 |
| 调度 | 周六+周日 12:00 | 双保险，命中周末在家的概率 |
| 容错 | 中继时静默跳过 | 不报错，等下一轮直连 |

## 十二、aria2c 后台下载注意事项

aria2c 后台下载 BT 种子时，`process poll` 可能泄漏二进制垃圾（tracker 响应中的非 UTF-8 数据）和大量 ANSI 进度条刷屏。**必须**加 `--console-log-level=warn` 和 `2>/dev/null`，poll 时只取最后一行。详见 [`references/aria2c-background-binary-garbage.md`](references/aria2c-background-binary-garbage.md)。

**死种判断**：运行 3 分钟以上 CN:0 SD:0 DL:0B → 死种，终止下载。有 peer 但速度 < 100 KiB/s 且 ETA > 100 小时 → 种子极度不活跃，告知用户。

**连续死种优化**：连续 2 个以上死种时，第 2 个就主动告知用户，第 3 个起跳过等待直接判断（aria2c 对死种的 CN/SD/DL 输出几乎即时可见），建议用户换 BT 站重新搜。

## 十三、第三方 Skill 安装

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
