# Home Assistant 基础设施搭建（基地版）

## Docker 运维

```bash
# 部署路径: /home/miao/docker/ha/
cd /home/miao/docker/ha
sudo docker compose restart homeassistant   # 重启
sudo docker compose logs --tail 50          # 日志
sudo docker ps --filter name=homeassistant  # 状态
```

## HA API Proxy

`ha_proxy.py` 监听 0.0.0.0:8080 → HA 127.0.0.1:8123，自动注入 Bearer token。

长期令牌通过 HA REST API 创建（需 HA 密码）后存 ~/.ha_token。
开机自启: crontab @reboot。
Tailscale 访问: http://100.86.13.11:8080/api/

## 旧插件 HA 2026 兼容性修复

HA 2026 移除了 TIME_DAYS / TIME_HOURS / TIME_MINUTES / TIME_SECONDS / TEMP_CELSIUS / POWER_WATT / PERCENTAGE / VOLUME_LITERS / ENERGY_KILO_WATT_HOUR / CONCENTRATION_* 等 homeassistant.const 常量。
修复：在插件文件头部自行定义这些常量（如 TIME_DAYS = "d"），并从 import 中删除。

Midea AC LAN 的 server select 表单需改为字符串 key 然后 int() 转换。

## 设备 LAN 发现

Midea: UDP 6445/20086 → TCP 6444
MiIO: UDP 54321, 报文 0x2131...
Docker 容器内广播可能不通，需在宿主机执行。

## 依赖 stub

py_mini_racer 编译慢 → 创建空桩类放在 site-packages/ 下。
