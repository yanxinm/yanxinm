# 中国主流智能家居平台 Home Assistant 集成调研

> 调研日期：2026-06-09 | 用途：老缪全屋智能统一管理

## 六大平台 HA 接入情况

| 平台 | 接入方式 | 关键插件/项目 | 可靠性 | 备注 |
|------|---------|--------------|:------:|------|
| **小米米家** | HA 官方集成 | `Xiaomi Home`（官方）+ `hass-xiaomi-miot`（al-one，社区） | ⭐⭐⭐⭐⭐ | 最强生态，双轨制，本地+云端 |
| **DREAME 追觅** | HACS | `Tasshack/dreame-vacuum`（2000+⭐） | ⭐⭐⭐⭐ | 完整替代APP，含地图、分区清扫 |
| **美的美居** | HACS | `hasscc/meiju`（云API）+ `georgezhao2010/midea_ac_lan`（本地） | ⭐⭐⭐⭐ | 双方案互补 |
| **晶御智能** | HA 官方集成 | `Home Connect`（官方）+ `ekutner/home-connect-hass`（备选） | ⭐⭐⭐⭐ | 博世/西门子/嘉格纳家电，有国内特殊配置 |
| **海尔智家** | HACS | `banto6/haier` | ⭐⭐⭐ | 可用，曾有DMCA风险但持续维护中 |
| **华为智慧生活** | ❌ 不可直连 | — | ⭐ | 封闭协议，无成熟方案 |

## 华为设备详情

### AGS-Q10 智能门锁
- **协议**：华为私有，HarmonyOS Connect
- **Matter**：不支持
- **HA 接入**：❌ 无任何可行方案
- **建议**：独立运行，如需门开合检测可用 Aqara 门窗传感器（Zigbee, ¥49）做物理层绕过

## Hermes ↔ HA 原生集成

Hermes Agent 原生支持 HA，配置 `HASS_TOKEN` 后自动启用 4 个工具：

| 工具 | 功能 |
|------|------|
| `ha_get_state` | 获取单个实体状态和所有属性 |
| `ha_call_service` | 调用服务控制设备（turn_on/off、set_temperature等） |
| `ha_list_entities` | 列出实体，可按 domain/area 过滤 |
| `ha_list_services` | 列出可用服务及参数 |

另通过 WebSocket 订阅实时状态变更。

配置方式：
```bash
# ~/.hermes/.env
HASS_TOKEN=<HA长期访问令牌>
HASS_URL=http://100.86.13.11:8123
```

参考文档：https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant
