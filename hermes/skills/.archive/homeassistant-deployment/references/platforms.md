# 智能家居平台 HA 集成详情

调研时间：2026-06-09

## 小米米家

- **官方集成**: `Xiaomi Home` — 小米官方维护，OAuth 登录，部分设备需特定服务器
- **社区集成**: `Xiaomi Miot Auto` (al-one/hass-xiaomi-miot) — 5.9K⭐, 54K 下载
  - GitHub: https://github.com/al-one/hass-xiaomi-miot
  - 安装：HACS 或手动下载 master.zip
  - 配置：小米账号+密码，UI config_flow
- **备选**: `Xiaomi Gateway 3` — 需小米网关硬件

## 追觅 Dreame

- **集成**: `Dreame Vacuum` (Tasshack/dreame-vacuum) — 2K+⭐
  - GitHub: https://github.com/Tasshack/dreame-vacuum
  - 功能：完整替代APP，含地图、分区清扫、虚拟墙
  - 社区活跃分支: foXaCe/dreame-vacuum, genericJE/ha-dreame-cloud

## 美的 Midea

- **最佳选择**: `Midea AC LAN` (georgezhao2010/midea_ac_lan) — 1676⭐, 33K 下载
  - GitHub: https://github.com/georgezhao2010/midea_ac_lan
  - 本地控制，自动发现设备
  - v0.3.22 兼容 HA 2026.6（master 可能太新）
- **备选**: `Midea Auto Cloud` — 云端 API，兼容性更好
- **已弃用**: `hasscc/meiju` — 使用已删除的 hass.helpers API，HA 2026.6 不可用

## 海尔 Haier

- **集成**: `Haier` (banto6/haier)
  - GitHub: https://github.com/banto6/haier
  - 社区维护，曾有 DMCA 风险（Haier 官方发函下架 hon 集成）
  - 支持：洗衣机、烘干机、洗碗机等
  - HACS 可安装，或手动从 main 分支下载

## 晶御智能 Home Connect

- **官方集成**: HA 内置 `Home Connect`
  - 博世/西门子/嘉格纳家电平台
  - 自动发现（mDNS），UI 配置
  - 国内有特殊配置参考：https://community.home-assistant.io/t/home-connect-special-setiings-for-china/508494
- **备选**: `Home Connect Hass` (ekutner/home-connect-hass) — 社区改良版

## 树新风 Treeow Home

- **集成**: `Treeow Home` (hlhk2017/treeow-homeassistant)
  - GitHub: https://github.com/hlhk2017/treeow-homeassistant
  - 空气净化器、加湿器、净水器
  - 测试设备：T2 Pro
  - 集成由 AI 辅助生成，功能基础但可用

## 华为智慧生活

- **状态**: ❌ 不可接入
- **原因**: HiLink/HarmonyOS Connect 为封闭私有协议
- **已测试设备**: AGS-Q10 智能门锁
- **替代方案**: 
  - Matter 兼容设备可桥接（新款华为设备）
  - eWeLink 桥接（如果设备也接入了易微联）
  - 物理传感器绕过（如 Aqara 门窗传感器检测门开合）
