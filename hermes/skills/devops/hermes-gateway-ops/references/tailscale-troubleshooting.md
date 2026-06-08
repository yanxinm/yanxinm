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
