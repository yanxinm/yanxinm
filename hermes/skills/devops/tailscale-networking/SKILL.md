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

### 双向都不通但显示 Connected
- **现象**：`tailscale status` 显示两台在线，但 ping 全丢包
- **修复**：两台设备都重启 Tailscale

### DERP 中继延迟正常但 TCP 连接超时
- 单位防火墙可能对某些端口做 DPI 拦截
- 尝试直接使用 Tailscale 主机名而非 IP：`miao-thinkcentre-m710q-n080`

## 端口与服务

| 端口 | 服务 | 绑定 |
|------|------|------|
| 8648 | Hermes Web UI | 0.0.0.0 |
| 8642 | Hermes API | 127.0.0.1（需对外开放时用 socat 转发）|
| 3071 | html-video Studio | 0.0.0.0（需手动 patch studio-server.js）|
| 22 | SSH | 0.0.0.0 |

## 注意事项

- 笔记本切换网络（家→单位）后 Tailscale 需要时间重建 DERP 中继，最多等 30 秒
- 单位网络 UDP 可能受限，优先走 DERP 中继
- 直连几乎不可能建立（NAT 层数太多），全程依赖 DERP
- **Web UI 空白页**：Hermes Web UI 的 JS bundle 约 750KB，通过 DERP 中继加载可能被截断或超时，表现为 HTML 正常但页面空白。可尝试多次刷新。

### SSH 隧道不可靠（重要教训）

SSH 隧道（`ssh -L 8648:127.0.0.1:8648 miao@100.86.13.11`）**不能解决 DERP 断连问题**，因为 SSH 本身就走 Tailscale DERP。DERP 断了 SSH 也断。2026-06-07/08 实测验证：笔记本在单位网络 DERP 反复断开时，SSH 同样 connection timed out。

### Tailscale Funnel（真正的解法）

Tailscale 内置的 **Funnel** 功能可将基地服务暴露到公网 HTTPS，**不依赖笔记本侧 Tailscale 客户端**，笔记本任何网络都能直接打开。免费，自带 Let's Encrypt 证书。

**启用（一次性 admin 操作）**：
1. 管理员（老缪）打开 `https://login.tailscale.com/f/funnel?node=<node-id>`（node-id 由 `tailscale funnel --bg <port>` 输出提示）
2. 按提示启用 Funnel

**基地侧启动**：
```bash
sudo tailscale funnel --bg 8648   # 暴露 Hermes Web UI
```

公网地址格式：`https://miao-thinkcentre-m710q-n080.<tailnet-name>.ts.net`

⚠️ Funnel 是公网可见的，建议配合 Tailscale ACL 限制访问。生产环境可用 Cloudflare Tunnel（需域名）替代。

## 关联参考

- `references/html-video-setup.md` — 基地上 html-video 项目的安装记录与坑
- `references/tailscale-funnel.md` — Funnel 详细配置与安全注意事项
