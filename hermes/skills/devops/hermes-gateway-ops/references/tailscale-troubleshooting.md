# Tailscale 故障诊断

## 单向 DERP 阻断（一台设备通，另一台不通）

**症状**：两台设备都在 Tailscale admin 中显示 Connected/Active，但从 A→B 通而 B→A 不通。

**诊断**：在两端分别执行：

```bash
tailscale ping <对方IP>
```

- A 通、B 超时 → 单向阻断
- 两端都通 → 连接正常，问题在其他层面（端口、防火墙）

**常见原因**：单位防火墙只放行入站 DERP 而阻断出站 DERP。

**修复**：
1. 退出 Tailscale（任务栏图标右键 → Exit）
2. 重新打开 Tailscale
3. 等待连接后重新 `tailscale ping` 验证

**注意**：新版 Tailscale（v1.80+）已移除 TCP 模式选项（`--tcp=true`），无法通过配置绕行。

## 显示 Connected 但实际不通

**持续修复不奏效时**：重启笔记本通常能解决（重建所有网络栈和防火墙规则）。

## SSH 隧道作为备用方案

当 Tailscale 不稳定时，SSH 隧道提供更可靠的连接：

```bash
ssh -L 8648:127.0.0.1:8648 miao@100.86.13.11
```

SSH 通过 Tailscale 或直连 IP 建立，TCP keepalive 保证连接持续。浏览器访问 `http://127.0.0.1:8648`。

## Funnel 多路径路由：顺序陷阱

**核心规则：先设全部 serve 路径，最后启用 funnel。**

### 错误顺序（导致路由被覆盖）

```bash
tailscale funnel --bg 9119                    # ✅ / → :9119, funnel on
tailscale serve --bg --set-path /ha :8123     # ❌ 覆盖！funnel 被重置为 tailnet-only
```

`tailscale serve --bg --set-path` 会重写 serve 配置，**同时清掉 funnel 公开状态**，公网域名降级为 tailnet-only。

### 正确顺序

```bash
# 1. 先清掉旧配置
tailscale serve --https=443 off

# 2. 设置所有路径（顺序无关）
tailscale serve --bg --set-path / http://127.0.0.1:9119
tailscale serve --bg --set-path /ha http://localhost:8123

# 3. 最后一步：启用 funnel 公开
tailscale funnel --bg 9119

# 验证
tailscale serve status   # 应显示 (Funnel on) + 所有路径
```

### 语法变更（v1.80+）

- ❌ 旧：`tailscale funnel on` / `tailscale funnel off`
- ✅ 新：`tailscale funnel --bg <port>` / `tailscale funnel --https=443 off`
