# Tailscale Funnel

## 什么是 Funnel

Tailscale 内置的公网暴露工具。将 tailnet 内部服务映射到 `https://<hostname>.<tailnet>.ts.net`，
公网可访问，自带 Let's Encrypt HTTPS 证书。

**关键优势**：访问方不需要安装 Tailscale 客户端，不经过 DERP 中继，
彻底规避企业网络 DERP 阻断问题。

## 启用步骤

### 1. 管理员启用 Funnel（一次性）

管理员（tailnet owner）访问 Tailscale Admin → Settings → Funnel 启用。
或者走 CLI 提示的链接：
```bash
sudo tailscale funnel --bg 8648
# 输出：Funnel is not enabled. To enable, visit:
# https://login.tailscale.com/f/funnel?node=<node-id>
```

管理员在浏览器打开该链接，按指引启用。

### 2. 基地启动 Funnel

```bash
# 暴露 Hermes Web UI
sudo tailscale funnel --bg 8648

# 查看状态
tailscale funnel status
```

公网地址：`https://miao-thinkcentre-m710q-n080.<tailnet>.ts.net`
（具体域名取决于 tailnet 名称）

### 3. 停止 Funnel

```bash
tailscale funnel reset
```

## 安全注意事项

- **Funnel 是公网可访问的**，任何知道 URL 的人都能访问
- 建议配合 Tailscale ACL 限制访问来源
- 敏感服务（如 API Server 8642）不要通过 Funnel 暴露，只暴露 Web UI
- 生产环境更推荐 Cloudflare Tunnel（支持 OAuth/SSO 登录验证）

## 替代方案对比

| 方案 | 成本 | 稳定性 | 安全性 | 依赖 |
|------|------|--------|--------|------|
| Tailscale DERP 直连 | 免费 | ⭐⭐ (企业网常断) | ⭐⭐⭐ | TS 客户端 |
| SSH 隧道 | 免费 | ⭐⭐ (走 DERP) | ⭐⭐⭐ | TS+SSH |
| Tailscale Funnel | 免费 | ⭐⭐⭐ | ⭐⭐ (公网) | 无 |
| Cloudflare Tunnel | 免费 | ⭐⭐⭐ | ⭐⭐⭐ (SSO) | 域名 |
| frp + VPS | ¥20-30/月 | ⭐⭐⭐ | ⭐⭐ | VPS |
