---
name: tailscale-networking
description: Tailscale 网络诊断与故障排除，覆盖基地与笔记本之间的 DERP 中继问题、连接验证、稳定性优化
triggers:
  - tailscale 不通
  - ping 超时
  - SSH 连不上
  - 笔记本换网络后断连
  - DERP relay
---

# Tailscale 网络诊断与故障排除

基地 miao-thinkcentre-m710q-n080 (100.86.13.11) 与笔记本 ethan (100.86.148.56) 之间的 Tailscale 连接，
在中国企业网络环境下常出现间歇性中断。

## 快速诊断流程

1. **基地侧**：`tailscale status` — 确认两台设备都在线
2. **基地 → 笔记本**：`tailscale ping 100.86.148.56` — 验证出站
3. **笔记本 → 基地**：`tailscale ping 100.86.13.11` — 验证入站

## 常见故障模式

### 单向下行通（基地能 ping 笔记本，反向超时）
- **根因**：笔记本出站 DERP 被单位防火墙阻断
- **修复**：笔记本退出 Tailscale 后重新打开（不必重启系统）

### 单向上行通（笔记本能 ping 基地，反向超时）⚠️ 最常被误判
- **现象**：基地 `tailscale status` 显示 `active; relay "sfo", tx 2184 rx 0`（tx 有数据、rx 为 0）
- **本质**：基地发出的包能到笔记本，笔记本的回应回不来 — Tailscale 层单向
- **误判风险**：从基地 `tailscale ping ethan` 通了≠笔记本能访问基地。必须双向验证。
- **诊断**：笔记本端也跑 `tailscale status` — 看对方的 tx/rx，两边对比
- **修复**：笔记本重启 Tailscale（右键任务栏图标 → Exit → 重新打开）

### 笔记本→基地 ping 不通但 `tailscale status` 显示对方 online
- **诊断步骤**：
  1. 基地 `tailscale ping ethan` — 如果通，说明基地→笔记本 OK
  2. 笔记本 `Test-NetConnection 100.86.13.11 -Port <port>` — 确认 TCP 层
  3. 笔记本 `tailscale status` — 确认从笔记本视角看基地状态、tx/rx 计数器
- **常见根因**：笔记本 Tailscale 半挂（服务运行但路由表/中继异常），外观 online 但实际不转发流量
- **修复**：笔记本重启 Tailscale，重新建立 DERP 中继

### 双向都不通但显示 Connected
- **现象**：`tailscale status` 显示两台在线，但 ping 全丢包
- **修复**：两台设备都重启 Tailscale

### DERP 中继正常但特定端口 TCP 超时

**症状**：`tailscale ping` 双向通，但浏览器访问 `http://100.86.13.11:<port>` 超时（ERR_CONNECTION_TIMED_OUT）

**优先排查 ufw**（基地防火墙默认 DROP INPUT，新服务端口需显式放行）：

```bash
sudo ufw status                    # 看当前规则
sudo iptables -L ufw-user-input -n -v  # 检查是否有对应端口的 ACCEPT 规则
sudo ufw allow <port>/tcp          # 放行
```

⚠️ `tailscale status` 和 `tailscale ping` 通了只说明 Tailscale 层没问题。TCP 连接是 OS 层，ufw 挡了就是挡了。**这是常见坑：Tailscale 通了就以为万事大吉，忘了 ufw。**

### Funnel 访问 HA 返回 400 Bad Request

**症状**：Funnel URL 能打开（说明 Funnel 本身通），但访问 HA 返回 `400: Bad Request`。

**根因**：HA 收到来自反向代理（Tailscale Funnel 从 127.0.0.1 转发）的请求，但未配置信任代理。HA 日志显示：
```
ERROR: A request from a reverse proxy was received from 127.0.0.1, 
but your HTTP integration is not set-up for reverse proxies
```

**修复**：在 HA `configuration.yaml` 中添加：
```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 127.0.0.1
```

若 config 文件属主为 root（Docker volume 默认），可用 `docker exec` 写入：
```bash
sg docker -c "docker exec homeassistant sh -c 'cat >> /config/configuration.yaml' << 'EOF'
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 127.0.0.1
EOF"
sg docker -c "docker restart homeassistant"
```

### Funnel 路径路由与子路径兼容性问题

**症状**：把应用挂到 Funnel 子路径（如 `/ha`），应用返回 400/404。

**根因**：很多 Web 应用（如 Home Assistant）假定自己运行在根路径 `/`，不认子路径前缀。

**解决**：互换主次——让需要根路径的应用占 `/`，把其他服务挪到子路径。

```bash
# 先清掉旧 Funnel
sudo tailscale funnel --https=443 off

# 把需要根路径的 HA 放 / ，Hermes Dashboard 放 /dash
sudo tailscale funnel --bg --https=443 --set-path=/ http://localhost:8123
sudo tailscale funnel --bg --https=443 --set-path=/dash http://127.0.0.1:9119

# 验证
tailscale funnel status
# 输出：
# https://xxx.ts.net (Funnel on)
# |-- /      proxy http://localhost:8123
# |-- /dash  proxy http://127.0.0.1:9119
```

> ⚠️ 交换后 Hermes Dashboard 原来的直达 URL（`/`）会跳到 HA。Desktop 远程模式不受影响（走 API 端点 `api/status`，不是根路径 HTML）。

### DERP 中继延迟正常但 TCP 连接超时（旧版记录）
- 单位防火墙可能对某些端口做 DPI 拦截
- 尝试直接使用 Tailscale 主机名而非 IP：`miao-thinkcentre-m710q-n080`

## 端口与服务

| 端口 | 服务 | 绑定 | 公网(Funnel) |
|------|------|------|:---:|
| 8123 | Home Assistant | 0.0.0.0 | 8443 (Funnel) |
| 8648 | Hermes Web UI | 0.0.0.0 | — |
| 8642 | Hermes API | 127.0.0.1 | — |
| 9119 | Hermes Dashboard | 0.0.0.0 | 443 (Funnel) |
| 3071 | html-video Studio | 0.0.0.0 | — |
| 22 | SSH | 0.0.0.0 | —

## 注意事项

- 笔记本切换网络（家→单位）后 Tailscale 需要时间重建 DERP 中继，最多等 30 秒
- 单位网络 UDP 可能受限，优先走 DERP 中继
- 直连几乎不可能建立（NAT 层数太多），全程依赖 DERP
- **Web UI 空白页**：Hermes Web UI 的 JS bundle 约 750KB，通过 DERP 中继加载可能被截断或超时，表现为 HTML 正常但页面空白。可尝试多次刷新。

### SSH 隧道不可靠（重要教训）

SSH 隧道（`ssh -L 8648:127.0.0.1:8648 miao@100.86.13.11`）**不能解决 DERP 断连问题**，因为 SSH 本身就走 Tailscale DERP。DERP 断了 SSH 也断。2026-06-07/08 实测验证：笔记本在单位网络 DERP 反复断开时，SSH 同样 connection timed out。

### Tailscale Funnel（真正的解法）

Tailscale 内置的 **Funnel** 功能可将基地服务暴露到公网 HTTPS，**不依赖笔记本侧 Tailscale 客户端**，笔记本任何网络都能直接打开。免费，自带 Let's Encrypt 证书。

**`tailscale serve` vs `tailscale funnel`**：
| 命令 | 范围 | 场景 |
|------|------|------|
| `tailscale serve` | tailnet 内 | 两台设备正常通信时使用 |
| `tailscale funnel` | 公网互联网 | 笔记本→基地直连断时兜底 |

⚠️ 如果笔记本 Funnel URL 也超时 → Tailscale 客户端本身有问题（DNS/路由），笔记本重启 Tailscale。

**启用（一次性 admin 操作）**：
1. 管理员（老缪）打开 `https://login.tailscale.com/f/funnel?node=<node-id>`（node-id 由 `tailscale funnel --bg <port>` 输出提示）
2. 按提示启用 Funnel

**基地侧启动（优先 sudo，避免 Access denied）**：
```bash
# 主 Funnel（Hermes Dashboard, 端口 443）
sudo tailscale funnel --bg 9119

# 额外服务（自定义端口，如 Home Assistant 8123 → 公网 8443）
sudo tailscale funnel --bg --https=8443 http://localhost:8123

# 查看当前 serve/funnel 状态
tailscale funnel status

# 关闭
sudo tailscale funnel --https=8443 off
```

公网地址格式：`https://miao-thinkcentre-m710q-n080.<tailnet-name>.ts.net:<port>`

⚠️ Funnel 是公网可见的，建议配合 Tailscale ACL 限制访问。生产环境可用 Cloudflare Tunnel（需域名）替代。

### `tailscale serve`（tailnet 内部，无需 Funnel）

```bash
# tailnet 内 HTTPS 代理（不暴露公网）
tailscale serve --bg --https=8123 http://localhost:8123
# 地址：https://miao-thinkcentre-m710q-n080.tail589fe7.ts.net:8123
# 仅同 tailnet 设备可访问
tailscale serve --https=8123 off   # 关闭
```

## 关联参考

- `references/html-video-setup.md` — 基地上 html-video 项目的安装记录与坑
- `references/tailscale-funnel.md` — Funnel 详细配置与安全注意事项
