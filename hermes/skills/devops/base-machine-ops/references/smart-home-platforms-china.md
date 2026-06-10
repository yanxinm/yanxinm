# 中国主流智能家居平台 Home Assistant 集成调研

> 调研日期：2026-06-09 | 更新：2026-06-09（实战验证）| 用途：老缪全屋智能统一管理

## 六大平台 HA 接入情况

| 平台 | 接入方式 | 关键插件/项目 | 可靠性 | 实战备注 |
|------|---------|--------------|:------:|------|
| **小米米家** | HA 官方集成 + HACS | `Xiaomi Miot Auto`（al-one，推荐首选）> `Xiaomi Home`（官方） | ⭐⭐⭐⭐⭐ | 官方集成登录频繁失败，**优先用 Xiaomi Miot Auto** |
| **DREAME 追觅** | HACS | `Tasshack/dreame-vacuum`（2000+⭐） | ⭐⭐⭐⭐ | 完整替代APP，含地图、分区清扫 |
| **美的美居** | HACS | `hasscc/meiju`（云API）+ `georgezhao2010/midea_ac_lan`（本地） | ⭐⭐⭐⭐ | 双方案互补 |
| **晶御智能** | HA 官方集成 | `Home Connect`（官方，HA启动时自动发现） | ⭐⭐⭐⭐ | 博世/西门子/嘉格纳家电，有国内特殊配置 |
| **海尔智家** | HACS | `banto6/haier` | ⭐⭐⭐ | 可用，曾有DMCA风险但持续维护中 |
| **华为智慧生活** | ❌ 不可直连 | — | ⭐ | 封闭协议，无成熟方案 |
| **树新风 Treeow** | HACS | `hlhk2017/treeow-homeassistant`（社区，测过 T2Pro） | ⭐⭐⭐ | 空气净化器/加湿器/净水器 |

## 安装顺序（已验证）

1. HA 初始引导 → 创建管理员账户
2. **HACS 激活**：设置 → 设备与服务 → 添加集成 → 搜 `HACS` → GitHub 授权 → 全部确认勾选 → 跳过区域分配 → 完成
3. **晶御智能**：HA 自动发现，在初始引导时就出现了，点「完成」即可
4. **小米**：HACS → Explore & Download → 搜 `Xiaomi Miot Auto` → 下载 → 重启 HA → 添加集成用小米账号登录
5. **追觅**：HACS → 搜 `Dreame Vacuum`
6. **美的**：HACS → 搜 `Midea` 或 `Meiju`
7. **海尔**：HACS → 搜 `Haier`
8. **树新风**：HACS → 搜 `Treeow`（找不到则手动装，见下方「HACS 下载失败兜底」）

## 美的美居（Meiju）YAML 配置 ⚠️

**重要**：HACS 安装的 `hasscc/meiju` 集成**不支持 UI 添加**！在「添加集成」中搜到 Meiju 后会提示"此设备无法通过用户界面添加"。必须在 `configuration.yaml` 中手动配置：

```yaml
meiju:
  accounts:
    - username: "你的美的手机号"
      password: "你的美的密码"
```

写入后重启 HA 生效。代用方案：HACS 里的 `Midea AC LAN`（33368 下载、1676⭐）支持 UI 配置，且走本地控制（不依赖美的云），可作为主方案。`Midea Auto Cloud`（231⭐）也支持 UI 添加但走云端。

## Xiaomi Home 官方集成登录问题

⚠️ **实战踩坑**：官方 `Xiaomi Home` 集成尝试多次登录均失败（"无法登录 Xiaomi Home，请检查凭据"），即使账号密码正确、服务器选 `cn`。不要浪费时间排查——直接用 `Xiaomi Miot Auto`（社区方案更稳，覆盖设备更广）。

备选：旧的 `Xiaomi Miio` 集成需要手动填设备 IP + 32位 API Token，门槛高且仅支持单设备，不推荐。

## 华为设备详情

### AGS-Q10 智能门锁
- **协议**：华为私有，HarmonyOS Connect
- **Matter**：不支持
- **HA 接入**：❌ 无任何可行方案
- **建议**：独立运行，如需门开合检测可用 Aqara 门窗传感器（Zigbee, ¥49）做物理层绕过

## HA 反向代理信任（Tailscale Funnel 必配）

HA 在 Tailscale Funnel 后面时，必须在 `configuration.yaml` 中添加：

```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 127.0.0.1
```

不加此配置 → Funnel 访问返回 `400 Bad Request`。HA 日志会明确提示 `A request from a reverse proxy was received from 127.0.0.1, but your HTTP integration is not set-up for reverse proxies`。

## Tailscale Funnel 路由

HA **不支持子路径**（`/ha` → 400），必须放 Funnel 根路径 `/`：
- `https://<host>.ts.net/` → HA
- `https://<host>.ts.net/dash` → Hermes Dashboard

非标准端口（8443）可能在笔记本端被拦截，优先用标准 443。

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

## HACS 下载失败兜底 — 命令行手动安装 custom_components

**问题**：HACS 在 HA Web UI 中下载 GitHub 插件时，因国内网络环境经常失败（`Could not download, see log for details`）。

**解决**：在基地命令行用 ghproxy 镜像下载 zip，手动解压到 custom_components。

### 方法 A：wget + unzip（适合大多数仓库）

```bash
# 批量下载（以 xiaomi_miot、dreame、meiju 为例）
wget -q "https://ghproxy.net/https://github.com/al-one/hass-xiaomi-miot/archive/refs/heads/master.zip" -O /tmp/xiaomi_miot.zip
wget -q "https://ghproxy.net/https://github.com/Tasshack/dreame-vacuum/archive/refs/heads/master.zip" -O /tmp/dreame.zip
wget -q "https://ghproxy.net/https://github.com/hasscc/meiju/archive/refs/heads/master.zip" -O /tmp/meiju.zip

# 逐个安装
for f in xiaomi_miot dreame meiju; do
  rm -rf /tmp/${f}_extract
  unzip -qo /tmp/${f}.zip -d /tmp/${f}_extract
  # zip 内结构: <repo>-<branch>/custom_components/<name>/
  dir=$(ls /tmp/${f}_extract | head -1)
  sudo cp -r /tmp/${f}_extract/${dir}/custom_components/* /home/miao/docker/ha/config/custom_components/
done
sg docker -c "docker restart homeassistant"
```

### 方法 B：git clone via ghproxy（wget 超时时用）

```bash
git clone --depth 1 https://ghproxy.net/https://github.com/banto6/haier /tmp/haier_repo
sudo cp -r /tmp/haier_repo/custom_components/haier /home/miao/docker/ha/config/custom_components/
```

⚠️ Docker volume 挂载的 `/config` 属主为 root，所有写入操作需 `sudo`。
⚠️ 部分仓库的 `custom_components` 目录名可能与 HACS slug 不同（如 `treeow_home`），需 `ls` 确认后再 cp。
