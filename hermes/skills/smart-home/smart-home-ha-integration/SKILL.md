---
name: smart-home-ha-integration
description: Home Assistant 多平台智能家居集成方案 — 研究、规划、安装、接入的完整工作流。覆盖小米/华为/海尔/美的/追觅/晶御等国内主流平台。
version: 1.0.0
---

## Trigger

当用户提出以下需求时加载此技能：
- 将多个智能家居平台统一接入 Home Assistant
- 调研某个品牌/平台的 HA 集成可行性
- 规划 HA + Hermes 统一管理架构
- 在基地（M710q Ubuntu）上安装/恢复 HA 环境
- **HA 设备实体大量 unavailable 的故障修复**（如凭据过期、集成报错）
- **微信/飞书中任何智能家居控制指令**（温度查询、扫地机控制、窗帘/灯光/空调操作等）— 无论当前 profile 是谁，自动切入 HA 模式执行

## 核心架构

```
Hermes Agent (ha_* 工具, WebSocket)
    ↓ HASS_TOKEN
Home Assistant (Docker, 基地 :8123)
    ↓ HACS + 官方集成
各平台设备 (小米/追觅/美的/海尔/晶御/华为...)
```

**关键认知**：
1. Hermes 对 HA 有原生支持 — 四个内置工具（ha_get_state, ha_call_service, ha_list_entities, ha_list_services）+ WebSocket 事件订阅，只需配置 `HASS_TOKEN` 即可自动启用
2. HA 装在基地 M710q 上用 Docker Compose，不装 HA OS（基地还有其他服务）
3. 所有品牌通过 HACS 插件或 HA 官方集成接入，非逆向/非破解

## 工作流

### Phase 1 — 环境准备
1. 检查基地 Docker 状态：`docker --version`
2. 若未安装：`sudo apt install docker.io docker-compose-v2 -y`
3. 确认系统资源（内存 >= 4GB，磁盘 >= 20GB）
4. docker-compose.yml 部署 HA + Mosquitto MQTT（可选）

### Phase 2 — 平台调研（核心步骤）
1. **加载 anysearch skill**，用 batch_search 并行查询各平台接入方案
2. 查询维度：官方集成 → HACS 插件 → GitHub Stars/活跃度 → 社区讨论（hassbian.com）
3. 输出对比表：平台名 | 接入方式 | 插件名 | Stars | 可靠性评分 | 备注
4. 对不可直连的平台（如华为），列出替代路线
5. **参考 `references/platforms.md`** 获取已知平台的调研结论，避免重复搜索

### Phase 3 — 安装实施
1. Docker Compose 启动 HA
2. 安装 HACS（`hacs.xyz` 一键脚本）
3. 按难度升序接入各平台（先官方后社区）
4. 每个平台接入后验证：实体出现在 HA → 可读取状态 → 可执行控制
5. 配置 HASS_TOKEN，在 Hermes `.env` 中填入，重启 Gateway

### Phase 4 — 验证
1. 确认 Hermes Gateway 日志显示 HA 平台已连接
2. 测试 ha_list_entities 能列出设备
3. 测试 ha_call_service 能控制设备
4. 配置微信通知：HA 事件 → Hermes → WeChat 推送

## 支持文件

| 文件 | 用途 |
|------|------|
| `references/platforms.md` | 六大平台详细调研（安装方式、插件、风险、注意事项） |
| `references/dreame-credential-refresh.md` | 追觅凭据过期刷新的完整流程、API 端点、故障排除 |
| `templates/docker-compose.yml` | HA + Mosquitto + Node-RED 的 Docker Compose 模板 |

## 已知平台集成状态

详见 `references/platforms.md`，摘要如下：

| 平台 | 评分 | 关键插件 |
|------|:----:|---------|
| 小米米家 | ⭐⭐⭐⭐⭐ | 官方 Xiaomi Home + 社区 Miot Auto |
| DREAME 追觅 | ⭐⭐⭐⭐ | Tasshack/dreame-vacuum (2K⭐) |
| 美的美居 | ⭐⭐⭐⭐ | hasscc/meiju + midea_ac_lan |
| 晶御智能 | ⭐⭐⭐⭐ | HA 官方 Home Connect |
| 海尔智家 | ⭐⭐⭐ | banto6/haier (有 DMCA 历史) |
| 华为智慧生活 | ⭐ | 无成熟方案，需逐设备评估 |

## 注意事项

- 海尔插件的 DMCA 风险：banto6/haier 曾受 DMCA 通知，虽然目前仍有维护，但需关注替代方案
- 华为的封闭性：HiLink/鸿蒙智家无开放 API，唯一的希望是 Matter 协议兼容的新款设备
- 美的双方案：hasscc/meiju（云API）和 midea_ac_lan（本地控制）可并存，本地优先延迟低
- 晶御智能的国内特殊性：国内版 App 叫「晶御智能」，对应博世/西门子/嘉格纳家电，HA 官方集成需配置中国区服务器
- 追觅两种路线：Tasshack/dreame-vacuum（云API，含地图）vs Valetudo（需越狱，完全本地），默认推荐前者
- **追觅凭据过期**：Dreamehome 的 OAuth refresh_token 会周期性过期（全部实体 unavailable），可通过 API 直接刷新无需重装集成，详见 `references/dreame-credential-refresh.md`
- **追觅 v2.0.0b23 + HA 2026.6.x 兼容问题**：config flow 的 setup 阶段 MQTT connect 可能超时被 Cancel，绕过方案是直写 config JSON + restart HA，不走 HA UI 的 config flow

---

## HomeKit Bridge（把 HA 设备接入 Apple 家庭）

### 用途

将 HA 中已接入的所有设备（米家/追觅/海尔等）统一暴露给 Apple HomeKit，实现：
- iPhone 家庭 App 直接控制
- Siri 语音控制
- 家庭自动化场景

### 配置方法

**推荐：通过 HA UI 配置**（避免 Docker 文件权限问题）

1. 打开 HA 网页：`http://<HA_IP>:8123`
2. 设置 → 设备与服务 → 添加集成 → 搜索 "HomeKit Bridge"
3. 选择要暴露的设备域（light/switch/cover/fan/climate/sensor）
4. 保存后会生成配对码

**备选：编辑 configuration.yaml**（需处理权限）

```yaml
homekit:
  - name: 缪宅
    port: 21063
    filter:
      include_domains:
        - light
        - switch
        - cover
        - fan
        - climate
        - sensor
      include_entity_globs:
        - sensor.*temperature*
        - sensor.*humidity*
```

**权限坑**：Docker 部署的 HA，`configuration.yaml` 通常归 `root` 所有，直接编辑会报权限不足。解决方案：
1. `sudo chmod 666 /path/to/config/configuration.yaml` 再编辑
2. 或优先用 HA UI 配置（推荐）

### iPhone 配对

1. 打开「家庭」App
2. 点击 + → 添加配件 → 扫描代码
3. 输入 HA 显示的配对码
4. 按提示分配房间

### 获取配对码

**方法1：HA 通知**（首次添加集成后）
- HA 左下角通知图标 → 查看 HomeKit 配对通知

**方法2：Docker 日志**（推荐，通知可能消失）
```bash
docker logs homeassistant 2>&1 | grep -i "pin\|pairing"
```

输出示例：
```
Or enter this code in your HomeKit app on your iOS device: 906-89-047
```

**注意**：每次创建新的 HomeKit Bridge 都会生成新的配对码。如有多个 Bridge，配对时选择对应名称。

### 多个 Bridge 实例说明

添加 HomeKit Bridge 后，HA 会自动创建多个 Bridge 实例：

| Bridge 类型 | 用途 | 示例名称 |
|-------------|------|----------|
| 主 Bridge | 暴露 lights/switches/climate 等设备 | `HASS Bridge` |
| 摄像头 Bridge | 每个摄像头一个独立实例 | `Current Map`、`Saved Map` |
| 媒体播放器 Bridge | 每个电视/接收器一个实例 | 自动创建 |

**原因**：摄像头和部分媒体设备需要 accessory 模式运行，无法与其他设备共用 Bridge。

**配对时**：选择主 Bridge（如 `HASS Bridge` 或 `HASS Bridge IU`），摄像头 Bridge 可选择性添加。

### 故障排除

| 问题 | 解决 |
|------|------|
| 配对码不显示 | `docker logs homeassistant 2>&1 \| grep -i "pin\|pairing"` 查日志 |
| 部分设备不显示 | 检查 `include_domains` 或在 HA UI 中单独选择 |
| iPhone 扫码/发现失败 | 1. 确保同一 WiFi（非手机热点）2. iPhone 蓝牙开启 3. 用「我没有或无法扫描代码」手动输入 |
| 配对后显示「无法接入」| 1. 检查 HA 网络模式是否为 `host` 2. `docker exec homeassistant netstat -tlnp \| grep 2106` 确认端口监听 3. 确认 avahi/mDNS 服务运行中 |
| 配对失败 | 确保iPhone和HA在同一局域网 |
| **显示「配件不可连接」** | **先检查防火墙！** 见下方防火墙配置，再考虑重置流程 |

### 防火墙配置（关键坑）

**症状**：iPhone 能发现 HomeKit Bridge，但配对时显示「配件不可连接」

**根因**：防火墙阻止了 HomeKit 端口（21064-21070/tcp）和 mDNS 发现端口（5353/udp）

**诊断命令**：
```bash
# 检查防火墙状态
sudo ufw status

# 检查 HomeKit 端口是否开放
sudo ufw status | grep 2106

# 检查 mDNS 端口
sudo ufw status | grep 5353
```

**修复命令**（ufw）：
```bash
# 开放 HomeKit Bridge 端口范围
sudo ufw allow 21064:21070/tcp comment 'HomeKit Bridge'

# 开放 mDNS/Bonjour 发现端口
sudo ufw allow 5353/udp comment 'mDNS/Bonjour'

# 重新加载防火墙
sudo ufw reload
```

**验证**：
```bash
# 确认端口监听
sudo ss -tlnp | grep 2106

# 确认 mDNS 运行
sudo ss -ulnp | grep 5353
```

**注意**：即使 HA 用 `--network host` 模式，主机防火墙仍会阻止外部访问，必须显式开放端口。

### 重置 HomeKit Bridge 配对

当配对反复失败或显示「配件不可连接」时，需重置配对状态：

**步骤1：删除配对状态文件**
```bash
docker exec homeassistant rm -f /config/.storage/homekit.*.state
```

**步骤2：重启 HA 容器**
```bash
docker restart homeassistant
```

**步骤3：等待 HomeKit 重新初始化（约30秒）**
```bash
sleep 30 && docker logs homeassistant 2>&1 | grep -i "pin\|pairing" | tail -5
```

**步骤4：获取新配对码**

输出示例：
```
Or enter this code in your HomeKit app on your iOS device: 627-57-987
Or enter this code in your HomeKit app on your iOS device: 465-41-583
```

**步骤5：iPhone 重新配对**
1. 家庭 App → + → 添加配件 → 我没有或无法扫描代码
2. 选择对应的 Bridge（如 `HASS Bridge IU`）
3. 输入新的配对码

**注意**：重置后旧的配对关系失效，需重新添加所有设备到家庭 App。

---

## 技能合并记录

本技能已吸收以下已归档技能的独特内容：

- **home-assistant-integration** — Hermes-HA token 配置、`ha_*` 工具使用、Hermes 侧集成平台矩阵
- **homeassistant-base-deployment** — REST API 诊断、token 处理技巧（`execute_code` 避免截断）
- **homeassistant-deployment** — Tailscale Funnel 根路径 `/` 要求、反向代理配置
- **home-assistant-deployment** — M710q Docker 部署细节、HACS 手动安装
- **home-assistant-base-deploy** — 国内网络代理（ghproxy.net）、HA 2026.6.x 兼容性坑

新增支持文件（从已归档技能迁入）：
- `references/home-assistant-integration-platforms.md` — Hermes-HA 工具集成指南
- `templates/docker-compose-ha-integration.yml` — 扩展 Docker Compose（含 Hermes 集成）
- `references/homeassistant-integrations.md` — 集成兼容性矩阵
- `references/homeassistant-deployment-platforms.md` — 部署平台说明
