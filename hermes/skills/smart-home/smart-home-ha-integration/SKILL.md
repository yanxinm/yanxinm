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
