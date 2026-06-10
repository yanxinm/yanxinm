# HA API 代理（ha_proxy.py）

为 HA REST API 提供无认证代理层，注入长期访问令牌，使外部客户端无需 Bearer token 即可调用。

## 部署位置

基地：`/home/miao/ha_proxy.py`
令牌：`/home/miao/.ha_token`（权限 600）

## 功能

- 监听 `0.0.0.0:8080`，转发到 HA `127.0.0.1:8123`
- 自动注入 HA 长期访问令牌（从 `~/.ha_token` 读取）
- 覆盖任何客户端传入的 Authorization header
- 支持所有 HTTP 方法：GET/POST/PUT/DELETE/PATCH/OPTIONS
- CORS 全开放（`Access-Control-Allow-Origin: *`）
- 静默日志（不输出请求日志）

## 访问方式

```
# Tailscale 网络内任意设备（无需认证）：
http://100.86.13.11:8080/api/
http://100.86.13.11:8080/api/states
http://100.86.13.11:8080/api/services
```

## 启动

### 手动
```bash
cd /home/miao && python3 ha_proxy.py &
```

### 开机自启（crontab @reboot）
```bash
@reboot sleep 15 && cd /home/miao && /usr/bin/python3 /home/miao/ha_proxy.py >> /home/miao/ha_proxy.log 2>&1
```

HA Docker 容器自身已设置 `restart=unless-stopped`。

## 令牌轮换

当令牌过期或需要更换时：
1. 按 `references/ha-auth-token-creation.md` 生成新令牌
2. 新令牌已在宿主机的 `/home/miao/docker/ha/config/ha_llt_final.txt`（bind mount，容器内路径 `/config/ha_llt_final.txt`）
3. `cp /home/miao/docker/ha/config/ha_llt_final.txt /home/miao/.ha_token`
4. `chmod 600 /home/miao/.ha_token`
5. 重启 proxy：`pkill -f ha_proxy.py && cd /home/miao && python3 ha_proxy.py &`

## 注意事项

- Proxy 本身无认证——安全性依赖 Tailscale 网络的访问控制
- 如需公网暴露，建议通过 Tailscale Funnel 加 ACL 限制
- HA 的 `configuration.yaml` 已配置 `trusted_proxies: 127.0.0.1`
- ⚠️ 脚本在 Hermes profile 环境下运行时，`os.path.expanduser("~")` 可能展开到 profile 目录（如 `~/.hermes/profiles/jike/home/`）而非 `/home/miao/`。令牌路径用绝对路径 `/home/miao/.ha_token`。
