---
name: home-assistant-integration
description: "基地部署 Home Assistant(Docker) + 多品牌智能家居接入 + Hermes 统一管理。覆盖海尔/美的/小米/华为/晶御/追觅六大平台的集成方案与实战流程。"
version: 1.0.0
author: 赫妹
metadata:
  hermes:
    tags: [Smart-Home, Home-Assistant, IoT, Docker, Multi-Brand]
triggers:
  - Home Assistant 安装/部署/接入
  - 智能家居平台统一管理
  - 多品牌智能设备接入 HA
  - Hermes 控制全屋智能
  - HACS 安装/配置
support_files:
  - references/platform-matrix.md  — 六大平台 HA 集成矩阵（调研报告）
  - templates/docker-compose.yml    — 可复制的 HA Docker Compose 模板
---

# Home Assistant 多品牌智能家居集成

在基地（M710q Ubuntu）上通过 Docker 部署 Home Assistant，用 Hermes 统一管理海尔、美的、小米、华为、晶御（博世/西门子）、追觅等品牌的智能设备。

## 触发条件

- 用户提到"装 HA"、"Home Assistant"、"智能家居统一"、"接入 HA"
- 需要调研某品牌是否支持 HA 集成
- 需要连接 Hermes 与 HA

## 架构

```
Hermes Agent (ha_get_state / ha_call_service / ...)
  │ HASS_TOKEN (REST + WebSocket 实时订阅)
  ▼
Home Assistant (Docker, network_mode: host, :8123)
  ├── 小米米家 → 官方 Xiaomi Home + 社区 Miot Auto
  ├── 追觅 DREAME → HACS: Tasshack/dreame-vacuum
  ├── 美的美居 → HACS: hasscc/meiju + midea_ac_lan
  ├── 晶御智能 → HA 官方 Home Connect
  ├── 海尔智家 → HACS: banto6/haier
  └── 华为 ⚠️  封闭协议，无可用集成
```

## 第一步：Docker 安装（Ubuntu 22.04）

```bash
# 单命令安装，用官方源免配额外源
sudo apt-get install -y docker.io docker-compose-v2

# 将用户加入 docker 组
sudo usermod -aG docker $USER
sudo systemctl enable docker --now

# 验证（需要 sg docker 或重新登录）
sg docker -c "docker version"
```

**镜像说明**：ghcr.io 在国内能直连，但较慢（HA 镜像 ~381MB，约需 5 分钟）。

## 第二步：部署 Home Assistant

创建 `/home/miao/docker/ha/docker-compose.yml`，使用 `network_mode: host`（设备发现必需）：

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
    # devices:  # 有 USB dongle 时取消注释
    #   - /dev/ttyUSB0:/dev/ttyUSB0
```

```bash
sg docker -c "docker compose -f /home/miao/docker/ha/docker-compose.yml up -d"
```

验证：
```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8123/
# 应返回 302（重定向到 onboarding）
```

## 第三步：安装 HACS

标准脚本可能找不到非标路径，推荐手动安装：

```bash
# 获取最新版本号
HACS_VERSION=$(curl -s https://api.github.com/repos/hacs/integration/releases/latest | grep '"tag_name"' | head -1 | sed 's/.*"tag_name": "\(.*\)".*/\1/')

# 下载并安装
wget -q "https://github.com/hacs/integration/releases/download/${HACS_VERSION}/hacs.zip" -O /tmp/hacs.zip
sudo mkdir -p /home/miao/docker/ha/config/custom_components/hacs
sudo unzip -qo /tmp/hacs.zip -d /home/miao/docker/ha/config/custom_components/hacs
sg docker -c "docker restart homeassistant"
```

## 第四步：HA 初始引导（用户操作）

浏览器打开 `http://<tailscale-ip>:8123`，创建管理员账户。

然后：设置 → 设备与服务 → 添加集成 → 搜 `HACS` → 安装（需 GitHub 授权）。

## 第五步：接入五大平台

参考 `references/platform-matrix.md` 的详细矩阵。

| 平台 | 接入方式 | HACS 插件 |
|------|---------|-----------|
| **小米米家** | HA 官方集成（首选）+ Miot Auto（社区备选） | — |
| **追觅 DREAME** | HACS | `Tasshack/dreame-vacuum` (2K+⭐) |
| **美的美居** | HACS | `hasscc/meiju`（云端）或 `georgezhao2010/midea_ac_lan`（本地） |
| **晶御智能** | HA 官方集成 | Home Connect（博世/西门子/嘉格纳） |
| **海尔智家** | HACS | `banto6/haier` |

### 华为设备：无法接入

华为 HiLink/鸿蒙智家使用私有封闭协议，不支持 Matter 的设备无法接入 HA。
- 方案：逐设备判断；门锁类建议独立运行
- 替代：如需开门联动，可用 Aqara 门窗传感器（Zigbee）绕开

## 第六步：接入 Hermes

### 6.1 在 HA 中创建长期访问令牌

HA Web UI → 个人资料 → 长期访问令牌 → 创建令牌（命名 "Hermes Agent"）→ 复制令牌。

### 6.2 配置 Hermes

在 `~/.hermes/.env` 中添加：

```bash
HASS_TOKEN=eyJhbGciOi...你的令牌
HASS_URL=http://localhost:8123
```

重启 Hermes Gateway：
```bash
hermes gateway restart
```

### 6.3 可用工具

设置 `HASS_TOKEN` 后自动启用 4 个工具：

| 工具 | 用途 |
|------|------|
| `ha_list_entities` | 按域/区域列出实体 |
| `ha_get_state` | 获取单个实体状态和属性 |
| `ha_list_services` | 列出可用的控制服务 |
| `ha_call_service` | 执行控制（开关灯、调温度等） |

同时通过 WebSocket 订阅 HA 事件，Hermes 可主动推送通知。

## 常见坑

### 1. Docker 配置目录权限
HA 容器以 root 运行，config/ 下的文件属主为 root。需要用 `sudo` 操作文件，或在 compose 中加 `user: 1000:1000`（不推荐，可能导致权限问题）。

### 2. 不存在的 device 引用会导致容器启动失败
`/dev/ttyUSB0` 等设备不存在时，compose 的 `devices:` 段会报错。部署时先注释掉，接入硬件时再打开。

### 3. 蓝牙错误无害
日志中的 `habluetooth` 和 `NET_ADMIN/NET_RAW` 权限错误不影响核心功能，可以忽略。如需蓝牙，在 compose 中加 `cap_add: [NET_ADMIN, NET_RAW]`。

### 4. HACS 自动脚本可能失败
`get.hacs.xyz` 的安装脚本依赖特定目录结构检测，非标准路径会报 "Could not find the directory"。手动下载 zip + unzip 更可靠。

### 5. docker compose `version` 字段已废弃
Docker Compose v2 不再需要 `version: "3.8"` 字段，会出 warning 但不影响运行。
