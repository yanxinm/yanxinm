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

### DERP 中继 ping 通但 TCP 全超时（Windows 防火墙拦截 relay 流量）

**症状**：`tailscale ping` 双向通（通过 DERP relay），但 `nc -zv <ip> 22` / `nc -zv <ip> 445` 等 TCP 端口全部超时。基地 `tailscale status` 显示 `active; relay "sfo", tx XXXX rx 0`（rx=0 是关键信号）。

**根因**：Windows 防火墙只添加了 `RemoteAddress 100.64.0.0/10`（Tailscale IP 范围）的放行规则，但 DERP 中继流量实际来自 DERP 服务器的公网 IP，不匹配 Tailscale 子网规则。

**诊断步骤**：
1. 笔记本临时关防火墙确认根因：
   ```powershell
   Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
   ```
2. 基地重试 TCP 连接。
   - 通了 → 证实是防火墙误拦 relay 流量，用下方永久修复。
   - 仍然不通 → **问题不在 Windows 防火墙层面**，继续排查 DERP relay 本身或 Tailscale ACL。
3. **诊断完后立即恢复防火墙**：
   ```powershell
   Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
   ```

**永久修复（防火墙误拦场景）**：不做 IP 范围限制，直接放行 Tailscale 网卡的所有入站流量：
```powershell
New-NetFirewallRule -DisplayName "Tailscale All Inbound" -Direction Inbound -InterfaceAlias "Tailscale" -Action Allow
```

#### 防火墙全关后 TCP 仍不通（DERP relay 层面故障）

**症状**：已确认 `tailscale ping` 双向通（走 DERP），Windows 防火墙已完全关闭，SSH/HTTP/SMB 等所有 TCP 端口仍全超时。`tailscale status` 显示 `active; relay`。

**根因**：TCP 连接在 DERP relay 节点处被丢弃，而非 Windows 侧。可能原因包括：
- DERP relay 节点（如 `sfo`/`lax`）不做 TCP 中继或限制端口
- Tailscale ACL 阻止了特定端口
- 两台设备 NAT 环境叠加 DERP 导致 TCP 握手包在某个环节丢失

**诊断**：
```bash
# 基地侧：验证哪个 DERP 节点在服务
tailscale status | grep ethan
# 输出示例：active; relay "sfo", tx 468 rx 0
# rx=0 是关键信号 — 基地发出了包但回包没回来

# 双向验证 ping（Tailscale 层）
tailscale ping --c 3 ethan          # 基地→笔记本
tailscale ping --c 3 miao-thinkcentre-m710q-n080  # 笔记本→基地（需在笔记本跑）
```

**Python HTTP 快速验证法**（排除应用层协议干扰）：
```powershell
# 笔记本启动简易 HTTP 服务
cd "E:\百度云同步盘\工作台账"
python -m http.server 18888
# 基地 curl 测试
curl -m 10 http://100.86.148.56:18888/
# 返回 000 + Connection timed out → TCP 层全阻断，非端口/协议问题
```

**备选方案**：如果 DERP 层面确实不转发 TCP，尝试 Tailscale 原生文件传输绕过 TCP：
```powershell
# 笔记本→基地：tailscale file cp（Tailscale 自有协议，不走 TCP/SSH）
tailscale file cp <文件路径> miao-thinkcentre-m710q-n080:
```
⚠️ `tailscale file cp` 需要接收端同意（Desktop/CLI 会弹通知），且仅支持单文件，不适合目录同步。如果此路也不通，考虑用云中转（如 S3/r2 presigned URL）或 `tailscale funnel` 反向暴露。

### DERP 中继延迟正常但特定端口 TCP 超时（ufw 侧）

**症状**：`tailscale ping` 双向通，但浏览器访问 `http://100.86.13.11:<port>` 超时（ERR_CONNECTION_TIMED_OUT）

**优先排查 ufw**（基地防火墙默认 DROP INPUT，新服务端口需显式放行）：

**优先排查 ufw**（基地防火墙默认 DROP INPUT，新服务端口需显式放行）：

```bash
sudo ufw status                    # 看当前规则
sudo iptables -L ufw-user-input -n -v  # 检查是否有对应端口的 ACCEPT 规则
sudo ufw allow <port>/tcp          # 放行
```

⚠️ `tailscale status` 和 `tailscale ping` 通了只说明 Tailscale 层没问题。TCP 连接是 OS 层，ufw 挡了就是挡了。**这是常见坑：Tailscale 通了就以为万事大吉，忘了 ufw。**

### SMB/CIFS 端口 445 在 DERP 中继下不可靠

**症状**：Windows 笔记本 Samba 共享已配好、防火墙已放行 Tailscale 网段（100.64.0.0/10），但基地 `nc -zv <ip> 445` 仍超时。`tailscale status` 显示 `active; relay`。

**根因**：SMB 协议对延迟和丢包容忍度极低。DERP 中继（尤其是跨国 relay 如 `lax`）引入的延迟使 SMB 握手超时。即使 `tailscale ping` 双向通，TCP 445 的 SMB 协商也无法完成。

**替代方案**：用 **SSH + rsync** 代替 SMB 进行文件传输。SSH（端口 22）对 DERP 中继容忍度远高于 SMB。

**Windows OpenSSH Server 安装坑位**：

笔记本启用 OpenSSH Server 有多个陷阱，按以下步骤避免：

1. **优先用 Windows 设置界面安装**（命令行常卡死）：
   - `Win + I` → 系统 → 可选功能 → 查看功能 → 搜索 "OpenSSH 服务器" → 安装
   - 如果必须用命令行但卡住（进度条不动），`Ctrl+C` 无效时直接关窗口重开
   - `Add-WindowsCapability` 和 `dism` 都可能无限挂起，界面安装最稳定

2. **安装后必须手动启动服务**（默认 Stopped + StartType Manual）：
   ```powershell
   Set-Service -Name sshd -StartupType Automatic
   Start-Service sshd
   ```

3. **验证 SSH 正在监听**（不是看服务状态，是看端口）：
   ```powershell
   netstat -an | findstr ":22 "
   # 期望输出：TCP  0.0.0.0:22  0.0.0.0:0  LISTENING
   ```

4. **放行防火墙**（Tailscale 网卡级放行，避免 IP 范围误判）：
   ```powershell
   New-NetFirewallRule -DisplayName "SSH for Tailscale" -Direction Inbound -Protocol TCP -LocalPort 22 -RemoteAddress 100.64.0.0/10 -Action Allow
   ```
   如果此规则仍不生效（DERP relay IP 不匹配），改用网卡级放行：
   ```powershell
   New-NetFirewallRule -DisplayName "Tailscale All Inbound" -Direction Inbound -InterfaceAlias "Tailscale" -Action Allow
   ```

rsync 命令格式（基地拉取笔记本文件）：
```bash
rsync -av yanxi@100.86.148.56:'/cygdrive/e/百度云同步盘/工作台账/' ~/工作台账/
```

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

**症状**：把应用挂到 Funnel 子路径（如 `/ha`），应用返回 400/404；或多个应用反复“抢”同一个 Funnel 根路径，浏览器打开根域名时显示旧应用（如 Home Assistant），Desktop/WebSocket 发送失败。

**根因**：
- 很多 Web 应用（如 Home Assistant）假定自己运行在根路径 `/`，不认子路径前缀。
- `tailscale serve --set-path` 和 `tailscale funnel --bg` 顺序/目标混用时，容易把 `/` 覆盖回最近设置的服务。
- 浏览器/Service Worker 可能缓存旧的 HA 前端：即使服务端 `/` 已回到 Hermes，浏览器仍显示 HA 的 “Unable to connect”。
- Hermes Desktop/Chat 发送不是普通 HTTP，而是走 Dashboard `/api/ws` WebSocket；网页能打开不等于发送通道可用。

**原则**：老缪基地上 Hermes Desktop 必须长期占 Funnel 根路径 `/`；HA 不再挂同一根域名，需另开独立入口（端口或域名），避免再抢。

**Hermes 根路径修复（只恢复 Desktop，先移除 HA）**：
```bash
# 清掉 443 上所有旧 serve/funnel 路由，避免 / 被 HA 残留占用
tailscale serve --https=443 off
sleep 1

# 只把 Hermes Dashboard 放回根路径 /
tailscale funnel --bg 9119

# 验证：/ 必须是 Hermes，/api/status 必须 200，/api/ws 必须 101
tailscale serve status
curl -sS -o /tmp/hermes_status.json -w '%{http_code}\n' \
  https://miao-thinkcentre-m710q-n080.tail589fe7.ts.net/api/status
```

**WebSocket 握手验收**（判断“网页打开但提示词发送失败”是否为基地端问题）：
```bash
python3 - <<'PY'
import re, urllib.request, socket, ssl, base64, os, urllib.parse
host='miao-thinkcentre-m710q-n080.tail589fe7.ts.net'
html=urllib.request.urlopen('https://'+host+'/', timeout=10).read().decode('utf-8','ignore')
token=re.search(r'__HERMES_SESSION_TOKEN__\\s*=\\s*["\\']([^"\\']+)', html).group(1)
key=base64.b64encode(os.urandom(16)).decode()
raw=socket.create_connection((host,443),timeout=10)
raw=ssl.create_default_context().wrap_socket(raw,server_hostname=host)
path=f'/api/ws?token={urllib.parse.quote(token)}'
req=f'GET {path} HTTP/1.1\\r\\nHost: {host}\\r\\nUpgrade: websocket\\r\\nConnection: Upgrade\\r\\nSec-WebSocket-Key: {key}\\r\\nSec-WebSocket-Version: 13\\r\\nOrigin: https://{host}\\r\\n\\r\\n'
raw.sendall(req.encode())
print(raw.recv(300).decode('latin1','ignore').splitlines()[0])
raw.close()
PY
# 期望：HTTP/1.1 101 Switching Protocols
```

**浏览器仍显示 HA 时**：先不要改路由，先清缓存：`Ctrl+Shift+R`；不行就 `F12` → 右键刷新按钮 → “清空缓存并硬性重新加载”；或无痕窗口访问。

**Desktop 发送仍失败时**：
1. 完全退出 Desktop 后重开，刷新 Dashboard 注入的 session token。
2. 后端地址只填根域名：`https://miao-thinkcentre-m710q-n080.tail589fe7.ts.net`，不要填 `8642` 或 `/ha`。
3. 若 `/api/status=200` 且 `/api/ws=101`，但单位网络下失败、手机热点可用，基本锁定为单位网络/客户端拦 WebSocket，不是基地端。

### Hermes Desktop：网页能打开但提示词发送失败

当 Desktop/Dashboard 网页能打开但提示词发送失败时，不要只看 `/api/status`。Hermes Chat 发送走 Dashboard WebSocket `/api/ws`，必须验收到 `101 Switching Protocols`；模型侧还要用 CLI 实发 `gpt-5.5` 返回 `OK`。详见 `references/hermes-desktop-funnel-websocket.md`。

### DERP 中继不转发原始 TCP（关键发现）

**DERP 中继仅支持 Tailscale 自有协议**（如 `tailscale ping`、`tailscale file cp`），**不支持原始 TCP**。
2026-06-09 全面实测：SSH(22)、SMB(445)、HTTP(18888) 全部超时，即使关闭 Windows 防火墙也如此。
`tailscale ping` 正常是因为它是 Tailscale 自己的 WireGuard 隧道内协议，不依赖 TCP。

- **症状**：`tailscale status` 显示直连/在线，端口通但服务全超时
- **根因**：走 DERP 中继而不是直连
- **唯一解法**：建立直连（两台设备在同一局域网时自动直连）
- **检测直连**：`tailscale status` 输出中看到 `direct <IP>:<port>` 即为直连；JSON 中的 `Relay` 字段始终非空不可用来判断

### 在家（同局域网）自动直连

周末/晚上笔记本和基地在同一局域网（如 192.168.1.x）时，Tailscale 自动建立直连。
此时 SSH、rsync、SFTP 全部可用，延迟 < 5ms。

### 检测连通性的正确方式

不要依赖 Tailscale JSON 的 `Relay` 字段（始终非空），直接用 socket 测试：

```python
import socket
s = socket.socket()
s.settimeout(5)
s.connect(("100.86.148.56", 22))
s.close()
# 成功 = 可达
```

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

- 笔记本切换网络（家→单位）后 Tailscale 需要时间重建连接，最多等 30 秒
- 单位网络环境下依赖 DERP 中继，仅 Tailscale 自有协议可用，SSH 等功能受限
- **在家（同局域网）自动直连**：延迟 < 5ms，SSH/SFTP 全功能可用
- **Web UI 空白页**：Hermes Web UI 的 JS bundle 约 750KB，通过 DERP 中继加载可能被截断或超时，表现为 HTML 正常但页面空白。可尝试多次刷新。

### DERP 中继的 TCP 限制（重要）

**`tailscale ping` 通 ≠ TCP 通。** `tailscale ping` 使用 Tailscale 自有协议走 WireGuard 隧道能过中继，但 TCP 连接（SSH:22、HTTP、SMB:445）通过 DERP 中继时全部超时。这是 DERP 中继的已知限制——它不转发原始 TCP SYN。

**验证方法**：不要用 `tailscale status --json` 的 `Relay` 字段判断。该字段始终非空（存的是首选中继节点名如 "tok"、"sfo"），即使实际已是直连。**正确的连通性检测**是直接尝试 socket 连接：

```python
import socket
s = socket.socket()
s.settimeout(5)
s.connect(("100.86.148.56", 22))  # 直接试连 SSH 端口
s.close()
```

**绕过方案**：
- `tailscale file cp` — 使用 Tailscale 自有协议，可穿透中继
- 同一局域网时 SSH/SFTP 直连（周末回家场景）
- **直连条件**：两台设备在同一局域网（如家中的 WiFi）时，Tailscale 自动建立直连（`tailscale status` 显示 `direct 192.168.x.x`）。在家实测可行。
- 不同网络时全程依赖 DERP 中继

### DERP 中继的 TCP 限制（重要）

**`tailscale ping` 通 ≠ TCP 通。** `tailscale ping` 使用 Tailscale 自有协议走 WireGuard 隧道能过中继，但 TCP 连接（SSH:22、HTTP、SMB:445）通过 DERP 中继时全部超时。`tailscale status` 显示 `rx=0` 是关键信号。

**⚠️ `--json` 的 Relay 字段不可靠**：JSON 中的 `Relay` 字段始终非空（存的是首选中继节点名如 "tok"、"sfo"），即使实际已是直连。**正确检测方式**是直接 socket 连接测试，而非解析 JSON：

```python
import socket
s = socket.socket(); s.settimeout(5)
s.connect(("100.86.148.56", 22)); s.close()  # 直接试连 SSH
```

**绕过 TCP 限制的方案**：
- 同一局域网时 SSH/SFTP 直连（周末回家场景）
- `tailscale file cp` — Tailscale 自有协议，可穿透中继
- `tailscale funnel` — 公网 HTTPS，不依赖笔记本侧客户端

### SSH 隧道不可靠（重要教训）

SSH 隧道（`ssh -L 8648:127.0.0.1:8648 miao@100.86.13.11`）**不能解决 DERP 断连问题**，因为 SSH 本身就走 Tailscale DERP。DERP 断了 SSH 也断。2026-06-07/08 实测验证：笔记本在单位网络 DERP 反复断开时，SSH 同样 connection timed out。

### Windows OpenSSH 管理员密钥陷阱

Windows OpenSSH Server 对管理员账户使用**独立的** authorized_keys：

| 用户类型 | 密钥路径 |
|---------|---------|
| 普通用户 | `C:\Users\<user>\.ssh\authorized_keys` |
| **管理员** | `C:\ProgramData\ssh\administrators_authorized_keys` |

管理员账户的 `~\.ssh\authorized_keys` **会被忽略**。错误现象：`paramiko` 连接报 `No authentication methods available`。

```powershell
# 管理员正确添加方式
mkdir C:\ProgramData\ssh -Force
Add-Content C:\ProgramData\ssh\administrators_authorized_keys "ssh-ed25519 AAA..."
```

### Tailscale Funnel（真正的解法）

Tailscale 内置的 **Funnel** 功能可将基地服务暴露到公网 HTTPS，**不依赖笔记本侧 Tailscale 客户端**，笔记本任何网络都能直接打开。免费，自带 Let's Encrypt 证书。

**`tailscale serve` vs `tailscale funnel`**：
| 命令 | 范围 | 场景 |
|------|------|------|
| `tailscale serve` | tailnet 内 | 两台设备正常通信时使用 |
| `tailscale funnel` | 公网互联网 | 笔记本→基地直连断时兜底 |

⚠️ 如果笔记本 Funnel URL 也超时 → Tailscale 客户端本身有问题（DNS/路由），笔记本重启 Tailscale。

### Funnel URL 从笔记本超时但服务端正常（MagicDNS 干扰）

**症状**：基地 `curl https://xxx.ts.net` 秒回 200，笔记本浏览器同 URL 超时。笔记本 `nslookup` 解析 ts.net 域名得到基地 Tailscale IP（如 `100.86.13.11`）。

**根因**：笔记本启用了 Tailscale MagicDNS，将 `*.ts.net` 域名解析到 Tailscale 内网 IP。浏览器尝试直连 Tailscale IP 的 443 端口，但 `tailscale serve` 只监听在基地本地的 Tailscale IP 上，来自远程 Tailscale 节点的 TCP 连接可能因 iptables/路由问题超时。

**诊断**：
```powershell
# 笔记本 PowerShell
nslookup miao-thinkcentre-m710q-n080.tail589fe7.ts.net
# 如果解析到 100.86.13.11 → MagicDNS 在干扰
Test-NetConnection 100.86.13.11 -Port 443
# 如果 TCP 超时 → 确认问题
```

**修复（按优先级）**：
1. **用 Tailscale 直连替代 Funnel**：`http://100.86.13.11:8123`（走 Tailscale 内网，不经过 Funnel/TLS）
2. **关掉笔记本 MagicDNS**：Tailscale 设置 → "Use Tailscale DNS" → 关闭
3. **笔记本用公共 DNS**：`nslookup xxx.ts.net 8.8.8.8` 解析到公网 IP 后再访问

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

- `references/tailscale-ssh-sync.md` — 笔记本 SSH+SFTP 工作台账同步完整配置
- `references/html-video-setup.md` — 基地上 html-video 项目的安装记录与坑
- `references/tailscale-funnel.md` — Funnel 详细配置与安全注意事项
- `references/cross-machine-sync.md` — 基地↔笔记本文件同步方案探索记录
