# 国内智能家居平台 HA 接入调研（2026.06）

> 以下信息来自 2026年6月 实测调研，各插件状态可能随时间变化。接入前应以 HACS 实际搜索结果为准。

---

## 1. 小米米家（Xiaomi Mi Home）

- **评分**: ⭐⭐⭐⭐⭐
- **接入方式**: 双轨制 — 官方集成 + 社区插件互为备份

| 方案 | 来源 | 链接 | 特点 |
|------|------|------|------|
| Xiaomi Home（官方） | HA 官方集成 | ha_xiaomi_home | 小米官方维护，本地+云端双控，多区域多账号 |
| hass-xiaomi-miot | HACS 社区 | al-one/hass-xiaomi-miot | MIoT 协议自动发现，覆盖设备最广 |

- **安装**: HACS 搜索 `xiaomi` 或 `miot`
- **HA 版本要求**: Core ≥ 2024.4.4
- **结论**: 对标行业最强，无需担心

---

## 2. DREAME 追觅

- **评分**: ⭐⭐⭐⭐
- **接入方式**: HACS 社区插件

| 方案 | 来源 | Stars | 特点 |
|------|------|:-----:|------|
| dreame-vacuum | Tasshack/dreame-vacuum | 2000+ | 完整替代APP，含地图、分区清扫、虚拟墙 |
| dreame-vacuum (fork) | foXaCe/dreame-vacuum | — | 架构改进版，bug 修复更积极 |
| ha-dreame-cloud | genericJE/ha-dreame-cloud | — | 云 API 方案，含交互式地图卡片 |

- **安装**: HACS 搜索 `dreame`
- **注意**: 
  - Tasshack 版是主流选择，Stars 最高
  - foXaCe fork 修复了一些架构问题，可作备选
  - Valetudo 路线可完全本地化但需要刷机，不推荐小白
- **凭据过期**：Dreamehome 账号的 OAuth `auth_key`（refresh_token）会周期性过期，导致全部实体不可用。刷新流程见 [`references/dreame-credential-refresh.md`](references/dreame-credential-refresh.md)
- **已知坑**：v2.0.0b23 + HA 2026.6.1 存在 MQTT 连接超时导致 setup 被取消（`CancelledError`），建议检查 HACS 更新

---

## 3. 美的美居（Midea Meiju）

- **评分**: ⭐⭐⭐⭐
- **接入方式**: HACS 社区插件，双方案互补

| 方案 | 来源 | 方式 | 特点 |
|------|------|------|------|
| meiju | hasscc/meiju | 云 API | 通过美的美居云接口接入，免获取 token |
| midea_ac_lan | georgezhao2010/midea_ac_lan | 本地控制 | WiFi 局域网直连，延迟更低 |
| midea_smart_home | Cyborg2017/midea_smart_home | 本地控制 | 新版本地方案，自动下载 Lua 协议脚本 |

- **安装**: HACS 搜索 `midea` 或 `meiju`
- **推荐**: 优先用 midea_ac_lan/Cyborg2017 本地方案，meiju 云方案做备选
- **注意**: midea_ac_lan 在 HA 2025.1.2+ 可能需要额外配置

---

## 4. 海尔智家（Haier Smart Home）

- **评分**: ⭐⭐⭐
- **接入方式**: HACS 社区插件

| 方案 | 来源 | 特点 |
|------|------|------|
| haier | banto6/haier | 支持 Switch/Number/Select/Sensor/Climate，理论上覆盖所有海尔设备 |
| hon (已下架) | Andre0512/hon | 曾是最佳选择，2024年初收到海尔 DMCA 通知后关闭 |

- **安装**: HACS 搜索 `haier`
- **风险**:
  - hon 插件的 DMCA 事件表明海尔对第三方接入态度不友好
  - banto6/haier 目前仍在维护，但不能排除未来也被要求下架
  - 建议安装后定期备份配置
- **覆盖**: 洗衣机、烘干机、洗碗机已确认可用；空调、热水器理论上支持

---

## 5. 晶御智能（Home Connect）

- **评分**: ⭐⭐⭐⭐
- **接入方式**: HA 官方集成

| 方案 | 来源 | 特点 |
|------|------|------|
| Home Connect（官方） | HA 内置集成 | 博世/西门子/嘉格纳家电，官方 API |
| Home Connect Local | HACS (ekutner/home-connect-hass) | 本地网络方案，特定地区备选 |

- **安装**: HA 配置 → 集成 → 搜索 `Home Connect`
- **国内特殊配置**: 需要在中国区服务器配置（community.home-assistant.io 有专门讨论帖）
- **覆盖**: 洗衣机、烘干机、洗碗机、烤箱、咖啡机等白电
- **结论**: 官方集成，最稳定可靠

---

## 6. 华为智慧生活（Huawei Smart Life / 鸿蒙智家）

- **评分**: ⭐
- **接入方式**: 无成熟方案

**为什么难**：
- 华为 HiLink 是封闭私有协议，不开放本地 API
- 鸿蒙智家（HarmonyOS Smart Home）同样封闭
- HACS 社区无可用插件
- HA 官方无集成计划

**替代路线**（均不完美）：

| 路线 | 原理 | 可行性 | 限制 |
|------|------|:------:|------|
| Matter 桥接 | 新款设备支持 Matter 协议 → HA 原生 Matter 集成 | ✅ 理想 | 仅限 2023+ 新款设备 |
| eWeLink 桥接 | 设备若同时绑定易微联 → HA eWeLink 集成 | ✅ 可用 | 需设备支持 eWeLink 绑定 |
| 旧手机+通知滤盒 | 闲置安卓机运行 HA Companion + Tasker | ⚠️ | 不稳定，依赖一台常开手机 |
| 华为云空间 API | 仅能获取手机 GPS 位置/电量，不能控制设备 | ❌ 无用 | MagicStarTrace/huawei_cloud 仅定位 |

**务实建议**：
1. 先盘点家里的华为设备清单（电视？门锁？开关？灯？）
2. 逐设备检查是否支持 Matter 或 eWeLink
3. 无法接入的华为设备保持原生 App 使用
4. 未来新增设备优先选小米/米家生态（HA 支持最好）

---

## Hermes ↔ HA 集成速查

Hermes Agent 原生支持 HA，4 个内置工具：

| 工具 | 功能 | 示例 |
|------|------|------|
| `ha_list_entities` | 列出实体（可按 domain/area 过滤） | "列出客厅所有灯光" |
| `ha_get_state` | 获取单个实体详细状态 | "空调当前状态？" |
| `ha_list_services` | 列出可调用的服务 | "climate 有哪些操作？" |
| `ha_call_service` | 执行控制服务 | "关掉客厅灯" |

配置方式：在 `~/.hermes/.env` 中设置 `HASS_TOKEN` 和 `HASS_URL`，重启 Gateway 即可。

---

## 基地部署参数

| 参数 | 值 |
|------|-----|
| 机型 | Lenovo M710q |
| CPU | Intel i5-6600T @ 2.70GHz (4核) |
| 内存 | 15GB |
| 系统 | Ubuntu 22.04 x86_64 |
| Docker | 待安装 |
| HA 端口 | 8123 |
| HA 安装方式 | Docker Compose |
| 配套 | Mosquitto MQTT (可选), Node-RED (可选) |
