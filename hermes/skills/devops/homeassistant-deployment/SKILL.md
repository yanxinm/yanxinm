---
name: homeassistant-deployment
description: 在 M710q Ubuntu 基地上部署 Home Assistant（Docker 方案）并通过 Tailscale Funnel 远程访问。涵盖 HACS 安装、自定义集成部署（国内网络方案）、Hermes 对接、常见兼容性坑位。
---

## 触发条件

当用户需要在基地上安装/配置/管理 Home Assistant，或接入新的智能家居平台时加载。

## 架构概览

```
Docker (docker.io from Ubuntu repo)
  └── homeassistant (ghcr.io/home-assistant/home-assistant:stable)
       network_mode: host  ← 关键，设备发现需要
       port 8123
       config volume: /home/miao/docker/ha/config

Tailscale Funnel
  └── https://miao-thinkcentre-m710q-n080.tail589fe7.ts.net
       /     → localhost:8123  (HA must be at root path)
       /dash → 127.0.0.1:9119 (Hermes Dashboard)
```

## 安装步骤

### 1. Docker 安装

国内直接用 Ubuntu 官方源（不需要添加 docker.com 源）：

```bash
sudo apt-get install -y docker.io docker-compose-v2
sudo usermod -aG docker $USER
# 新 shell 后生效，或用 sg docker -c "command"
```

### 2. docker-compose.yml

放在 `/home/miao/docker/ha/docker-compose.yml`：

```yaml
services:
  homeassistant:
    container_name: homeassistant
    image: ghcr.io/home-assistant/home-assistant:stable
    network_mode: host
    restart: unless-stopped
    volumes:
      - /home/miao/docker/ha/config:/config
      - /etc/localtime:/etc/localtime:ro
      - /run/dbus:/run/dbus:ro
    environment:
      - TZ=Asia/Shanghai
```

⚠️ 不要加 `devices` 段，除非真有 USB dongle 插着，否则容器启动失败。

### 3. 防火墙

```bash
sudo ufw allow 8123/tcp comment 'Home Assistant'
```

### 4. Tailscale Funnel（远程访问）

```bash
# 先设 operator 免 sudo
sudo tailscale set --operator=$USER

# HA 必须占根路径 /（子路径 /ha 会导致 400 Bad Request）
sudo tailscale funnel --bg --https=443 --set-path=/ http://localhost:8123

# Hermes Dashboard 放子路径
sudo tailscale funnel --bg --https=443 --set-path=/dash http://127.0.0.1:9119
```

### 5. HA 反向代理配置

Funnel 代理请求从 127.0.0.1 来，HA 默认拒绝。在 `configuration.yaml` 加：

```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 127.0.0.1
```

### 6. HACS 安装

脚本方式在 Docker 下不好用，手动装：

```bash
# 获取最新版本
VERSION=$(curl -s https://api.github.com/repos/hacs/integration/releases/latest | jq -r .tag_name)
wget "https://github.com/hacs/integration/releases/download/${VERSION}/hacs.zip" -O /tmp/hacs.zip
sudo mkdir -p /home/miao/docker/ha/config/custom_components/hacs
sudo unzip -qo /tmp/hacs.zip -d /home/miao/docker/ha/config/custom_components/hacs
docker restart homeassistant
```

## 自定义集成安装（国内网络）

### 方式 A：HACS（可能失败，GitHub 直连不稳）

HACS → Explore & Download → 搜索

### 方式 B：手动 via ghproxy（推荐）

```bash
# 下载
wget "https://ghproxy.net/https://github.com/OWNER/REPO/archive/refs/heads/BRANCH.zip" -O /tmp/xxx.zip

# 如果 zip 下载超时，换 git clone
git clone --depth 1 "https://ghproxy.net/https://github.com/OWNER/REPO" /tmp/xxx_repo

# 安装
sudo cp -r /tmp/xxx_repo/custom_components/yyy /home/miao/docker/ha/config/custom_components/
docker restart homeassistant
```

### 配置文件权限

Docker 创建的 config 目录属主是 root。两种操作方式：

```bash
# 方式 1：sudo
sudo tee -a /home/miao/docker/ha/config/configuration.yaml << 'EOF'
...
EOF

# 方式 2：docker exec（推荐，不用 sudo 密码）
sg docker -c "docker exec homeassistant sh -c 'cat >> /config/configuration.yaml << EOF
...
EOF'"
```

## 平台兼容性速查

| 平台 | HA 集成 | 方式 | 兼容性 |
|------|---------|------|:---:|
| 小米 | Xiaomi Miot Auto | HACS / 手动 | ✅ v1.1.4 |
| 追觅 | Dreame Vacuum | HACS / 手动 | ⚠️ 待验证 |
| 美的 | Midea AC LAN v0.3.22 | 手动 | ⚠️ HA 2026.6 兼容问题 |
| 海尔 | Haier (banto6) | 手动 | ⚠️ 待验证 |
| 晶御 | Home Connect（官方） | 内置，自动发现 | ✅ |
| 树新风 | Treeow Home | 手动 | ⚠️ 待验证 |
| 华为 | ❌ 不可接入 | — | 封闭协议 |

## 已知坑位

### HA 2026.6.x 太新
2026年6月版 HA 很新，许多自定义集成的 config_flow 不兼容，报 `"Invalid handler specified"`。
→ 降级到旧版集成（如 midea_ac_lan v0.3.22），或用官方内置集成。

### meiju 集成已死
hasscc/meiju 使用 `hass.helpers` API，HA 2026.6 已移除。→ 换成 midea_ac_lan。

### Funnel 子路径 HA 400
HA 不支持反向代理子路径。→ 让 HA 占 Funnel 根路径 `/`。

### Tailscale 笔记本直连基地不通
笔记本 ping 基地超时但基地 ping 笔记本通 → DERP 中继单向问题。用 Funnel（走 443）绕过。

### Docker config 文件权限
容器内进程以 root 运行，创建的配置文件宿主也是 root。修改用 `docker exec` 或 `sudo`。

## 参考

- HA 文档: https://www.home-assistant.io/installation/linux/
- HACS: https://hacs.xyz/
- 各平台 GitHub 仓库: 见 `references/platforms.md`
