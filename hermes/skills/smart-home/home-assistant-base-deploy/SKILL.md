---
name: home-assistant-base-deploy
description: 在基地 M710q Ubuntu 上部署 Home Assistant（Docker）、安装 HACS + 社区集成、配置 Tailscale Funnel 远程访问、接入 Hermes Agent。覆盖中国网络环境下的镜像/代理方案、常见坑与修复。
version: 1.0.0
---

## Trigger

当用户需要在基地上部署、配置、维护 Home Assistant，或接入新的智能家居平台时加载本 skill。

## 架构

```
Hermes Agent (ha_get_state / ha_call_service / ...)
  │ HASS_TOKEN (REST + WebSocket)
  ▼
Home Assistant (Docker, network_mode: host, :8123)
  │
  ├─ HACS 社区商店
  ├─ Custom Components (ghproxy.net 下载)
  ├─ 官方集成 (Home Connect / Xiaomi Home)
  └─ Tailscale Funnel (HTTPS → 公网访问)
```

## 环境

| 项目 | 值 |
|------|-----|
| 主机 | M710q, i5-6600T, 15GB RAM, Ubuntu 22.04 |
| Docker | `docker.io` 从 Ubuntu 官方 apt 源安装（非 Docker 官方源，被墙） |
| HA 目录 | `/home/miao/docker/ha/` |
| HA 配置 | `/home/miao/docker/ha/config/` |
| Docker 组 | `sg docker -c "..."` 执行（非 root） |
| 国内代理 | GitHub → `ghproxy.net` 前缀 |

## 安装步骤

### 1. Docker 安装

```bash
# Ubuntu 22.04 官方源直接装，不要用 Docker 官方源（被墙）
sudo apt-get install -y docker.io docker-compose-v2
sudo usermod -aG docker $USER
```

### 2. docker-compose.yml

文件位置: `/home/miao/docker/ha/docker-compose.yml`

```yaml
services:
  homeassistant:
    container_name: homeassistant
    image: ghcr.io/home-assistant/home-assistant:stable
    network_mode: host          # 必须 host 模式，否则无法发现局域网设备
    restart: unless-stopped
    volumes:
      - /home/miao/docker/ha/config:/config
      - /etc/localtime:/etc/localtime:ro
      - /run/dbus:/run/dbus:ro
    environment:
      - TZ=Asia/Shanghai
    # devices:  # USB dongle 以后再加
```

启动:
```bash
sg docker -c "docker compose -f /home/miao/docker/ha/docker-compose.yml up -d"
```

### 3. 远程访问（Tailscale Funnel）

HA 容器使用 `network_mode: host`，监听 `0.0.0.0:8123`。

**问题**: 笔记本→基地 Tailscale 直连可能不通（单向 DERP），需要 Funnel 暴露。

**关键经验**:
- Funnel 仅 443/8443/10000 端口可用
- 笔记本端 8443 被拦 → 用 443
- HA **不支持**子路径（如 `/ha`）→ 必须放在根路径 `/`
- Hermes Dashboard 可以放子路径 `/dash`

```bash
# 配置 Funnel（需先 tailscale set --operator=$USER）
tailscale funnel --bg --https=443 --set-path=/ http://localhost:8123
tailscale funnel --bg --https=443 --set-path=/dash http://127.0.0.1:9119
```

**HA 反向代理配置** (`configuration.yaml`):
```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 127.0.0.1
```

不加会报 `reverse proxy from 127.0.0.1 but not set-up`，返回 400 Bad Request。

### 4. HACS 安装

不能用官方 `wget | bash` 脚本（找不到 HA 目录），手动安装:

```bash
# 获取最新版本
HACS_VERSION=$(curl -s https://api.github.com/repos/hacs/integration/releases/latest | grep tag_name | head -1 | sed 's/.*"\(.*\)".*/\1/')
wget "https://github.com/hacs/integration/releases/download/${HACS_VERSION}/hacs.zip" -O /tmp/hacs.zip
# 或用代理: wget "https://ghproxy.net/https://github.com/..." -O /tmp/hacs.zip

# 安装到 custom_components（需要 sudo，容器以 root 创建目录）
sudo mkdir -p /home/miao/docker/ha/config/custom_components/hacs
sudo unzip -qo /tmp/hacs.zip -d /home/miao/docker/ha/config/custom_components/hacs
```

### 5. 社区集成安装（中国网络）

HACS UI 下载 GitHub 大概率失败 → 命令行手动装:

```bash
# 方式 A: zip + ghproxy
wget "https://ghproxy.net/https://github.com/<org>/<repo>/archive/refs/heads/<branch>.zip" -O /tmp/repo.zip
unzip -qo /tmp/repo.zip -d /tmp/extract
dir=$(ls /tmp/extract | head -1)
sudo cp -r /tmp/extract/${dir}/custom_components/* /home/miao/docker/ha/config/custom_components/

# 方式 B: git clone + ghproxy（zip 下载慢时）
git clone --depth 1 "https://ghproxy.net/https://github.com/<org>/<repo>" /tmp/repo
sudo cp -r /tmp/repo/custom_components/<name> /home/miao/docker/ha/config/custom_components/
```

### 6. 操作 HA 配置文件

Config 文件属主是 root（Docker 创建），普通用户无写权限:

```bash
# 正确方式: 通过 docker exec
sg docker -c "docker exec homeassistant cat /config/configuration.yaml"
sg docker -c "docker exec homeassistant sh -c 'echo \"...\" >> /config/configuration.yaml'"

# 错误方式: 直接写文件 → Permission denied
```

## 平台集成速查

| 平台 | 集成名称 | 来源 | 安装方式 | 备注 |
|------|---------|------|---------|------|
| 小米 | Xiaomi Miot Auto | al-one/hass-xiaomi-miot | HACS / 手动 | 社区版，比官方更稳 |
| 追觅 | Dreame Vacuum | Tasshack/dreame-vacuum | HACS / 手动 | 含地图 |
| 美的 | **Midea AC LAN** | georgezhao2010/midea_ac_lan | HACS / 手动 | ⚠️ 用这个别用 meiju（不兼容新版 HA） |
| 海尔 | Haier | banto6/haier | HACS / 手动 | 曾有 DMCA 风险 |
| 晶御/BSH | Home Connect | HA 官方内置 | 自动发现 | 博世/西门子/嘉格纳 |
| 树新风 | Treeow Home | hlhk2017/treeow-homeassistant | HACS / 手动 | 空净/加湿/净水 |

## 常见坑

1. **Docker 官方源 443 被墙** → 用 Ubuntu apt 自带的 `docker.io`
2. **ghcr.io 拉镜像慢** → 耐心等，381MB 可能需要几分钟
3. **HACS 脚本找不到 HA 目录** → 手动解压 zip
4. **HACS UI 下载失败** → 命令行 ghproxy.net 下载
5. **HA Funnel 子路径 400** → HA 必须根路径，其他服务放子路径
6. **反向代理 400** → 必须加 `trusted_proxies: [127.0.0.1]`
7. **meiju 集成报 `helpers` 错误** → 改用 midea_ac_lan
8. **config 文件权限** → 用 `docker exec` 写，不能直接写宿主机文件
9. **Tailscale 笔记本→基地单向不通** → 启用 Funnel 绕行

## Hermes 接入（待完成）

配置 `~/.hermes/.env`:
```bash
HASS_TOKEN=<长期访问令牌>
HASS_URL=http://localhost:8123
```

Hermes 自动启用 `homeassistant` 工具集（ha_get_state / ha_call_service / ha_list_entities / ha_list_services）。
