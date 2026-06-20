# 六大智能家居平台 Home Assistant 集成矩阵

调研时间：2026-06-09 | 来源：AnySearch 多轮搜索 + GitHub/社区交叉验证

## 总览

| 平台 | 集成方式 | 最优插件 | 可靠性 | 接入难度 |
|------|---------|-----------|:-----:|:------:|
| 小米米家 | HA 官方集成 | `Xiaomi Home`（官方）/ `hass-xiaomi-miot`（al-one） | ⭐⭐⭐⭐⭐ | 极易 |
| 追觅 DREAME | HACS | `Tasshack/dreame-vacuum` (2000+⭐) | ⭐⭐⭐⭐ | 容易 |
| 美的美居 | HACS | `hasscc/meiju` + `georgezhao2010/midea_ac_lan` | ⭐⭐⭐⭐ | 容易 |
| 晶御智能 | HA 官方 | `Home Connect` | ⭐⭐⭐⭐ | 极易 |
| 海尔智家 | HACS | `banto6/haier` | ⭐⭐⭐ | 中等 |
| 华为智慧生活 | ❌ | 无可用方案 | ⭐ | 不可行 |

## 小米米家 — 最强支持

**双轨制**：
1. **官方集成 `Xiaomi Home`**：小米官方维护，GitHub `Xiaomi/HA_Xiaomi_Home`，支持本地+云端双模式
2. **社区 `hass-xiaomi-miot`**（al-one）：长期主力方案，覆盖面最广

官方集成要求：HA Core ≥ 2024.4.4, OS ≥ 13.0

接入后可用实体类型：switch、light、sensor、binary_sensor、climate、cover、fan、media_player、camera

## 追觅 DREAME — 完整替代 APP

**`Tasshack/dreame-vacuum`** (GitHub, 2000+ Stars)

功能：
- 实时地图（多楼层支持）
- 分区/房间清扫
- 虚拟墙
- 障碍物照片
- 清扫历史
- 云端+本地地图备份

此外还有 `genericJE/ha-dreame-cloud`（纯云端）和 `foXaCe/dreame-vacuum`（性能优化 fork）。

## 美的美居 — 双方案

1. **`hasscc/meiju`**：云端 API 接入，通过美的美居账号登录，自动发现设备
2. **`georgezhao2010/midea_ac_lan`**：本地局域网控制，适合空调等设备，不依赖云端

备选路线：美的设备也可通过易微联（eWeLink）桥接 → eWeLink HA 集成 → 间接控制。

## 晶御智能（Home Connect）— 博世/西门子/嘉格纳

这是博西家电集团（BSH）的智能家居平台，品牌包括：
- 博世（Bosch）
- 西门子（Siemens）
- 嘉格纳（Gaggenau）

HA 官方集成 `Home Connect`，支持国内服务器（有特殊配置需求，参考 `community.home-assistant.io/t/home-connect-special-setiings-for-china/508494`）。

备选 HACS 插件：`ekutner/home-connect-hass`（可选本地服务器）。

## 海尔智家 — 谨慎可用

**`banto6/haier`** (GitHub)

- 通过 HACS 安装，输入海尔智家账号密码
- 支持设备类型：Switch、Number、Select、Sensor、Binary Sensor、Climate

⚠️ 风险提示：
- 2024年初曾收到海尔 DMCA 通知（下架了另一个叫 `hon` 的集成），`banto6/haier` 仍在维护
- 依赖云端 API，海尔可能随时封禁

## 华为智慧生活 — 不可接入

华为 HiLink/鸿蒙智家是封闭私有协议：

- ❌ 无可用 HA 集成
- ❌ 不支持 Matter（大部分设备）
- ❌ 不支持 Zigbee/Z-Wave 标准协议

已知华为 AGS-Q10 智能门锁：HarmonyOS 5.0.0.1，只联动华为生态内设备（智慧屏画中画等），完全无法接入 HA。

### 替代思路

1. **Matter 兼容设备**：极少数新款华为设备可能支持 Matter，可逐个确认
2. **物理传感器绕过**：如需要门锁联动，门上贴 Aqara 门窗传感器（Zigbee，约 ¥49）
3. **eWeLink 桥接**：部分华为设备可能同时绑定了易微联
4. **接受现状**：少量华为设备手动操作，主力迁移到米家等开放生态

## Hermes-HA 集成详情

Hermes 原生支持 HA，只需配置 `HASS_TOKEN`。详情参见主 SKILL.md 第六步。

4 个内置工具：
- `ha_list_entities` — 按 domain/area 列出实体
- `ha_get_state` — 获取实体状态和属性
- `ha_list_services` — 列出可用服务
- `ha_call_service` — 控制设备（turn_on/off、set_temperature 等）
