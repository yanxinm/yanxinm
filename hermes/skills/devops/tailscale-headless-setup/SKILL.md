---
name: tailscale-headless-setup
description: 在 headless Linux 服务器上安装和配置 Tailscale，加入已有 tailnet。
---

# Tailscale Headless Setup

在无图形界面的 Linux 服务器上配置 Tailscale 接入 tailnet。

## 触发条件
- 用户需要在 Linux 服务器上安装/配置 Tailscale
- Tailscale 离线需要重新连接
- 新机器加入已有 tailnet

## 步骤

### 1. 检查当前状态
```bash
which tailscale && tailscale status || echo "not installed"
```

### 2. 安装（如未安装）
```bash
curl -fsSL https://tailscale.com/install.sh | sh
```

### 3. 连接 tailnet（headless 正确方式）

**⚠️ 关键：headless 服务器必须用 auth key，不能用链接认证。**

链接认证方式（`tailscale up` 生成 URL 等用户在浏览器点）在 headless 服务器上不可行：
- `tailscale up` 阻塞等待认证，超时即断连
- 即便用户在浏览器完成认证，原进程已超时退出，新拉起又生成新链接
- 反复循环

**正确方式：**

用户在 Tailscale admin 面板生成 auth key：
- 地址：`https://login.tailscale.com/admin/settings/keys`
- 点 **Generate auth key**，复制 key

然后用 auth key 一步连接：
```bash
sudo tailscale up --auth-key=<key> --accept-routes
```

### 4. 验证
```bash
tailscale status
tailscale ip -4   # 查看本机 Tailscale IP
```

## 常用命令速查

| 命令 | 作用 |
|------|------|
| `tailscale status` | 查看所有设备及在线状态 |
| `tailscale ip -4` | 本机 Tailscale IPv4 |
| `tailscale ping <hostname>` | Tailscale 内置 ping（测试直连/中继） |
| `ping -c 3 <tailscale-ip>` | 标准 ICMP ping，验证跨节点 IP 层互通 |
| `sudo tailscale up --accept-routes` | 重新连接（会生成认证链接） |
| `sudo tailscale up --auth-key=<key> --accept-routes` | 用 auth key 连接（headless 推荐） |
| `sudo tailscale down` | 断开连接 |

### 验证跨节点互通

连接成功后，从本机 ping 其他节点确认 tailnet 内通信正常：

```bash
# 1. 先看目标节点的 Tailscale IP
tailscale status

# 2. 标准 ping 测试（3 包，0% 丢包 = 通）
ping -c 3 <目标节点IP>

# 3. 同时检查 Web 服务可达性（如有）
curl -s -o /dev/null -w "%{http_code}" http://<目标节点IP>:<端口>
```

## 注意事项
- auth key 是敏感信息，不存储、不记录
- 需要 sudo 权限
- `--accept-routes` 接受其他节点发布的路由
