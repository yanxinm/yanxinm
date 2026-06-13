---
name: hermes-base-operations
description: Hermes 基地运维操作——远程 Desktop 连接、Tailscale Funnel 配置、安全加固、服务管理、Windows 客户端安装。
tags: [hermes, tailscale, desktop, security, devops]
---

# Hermes 基地运维

## 适用场景
基地（Linux headless 主机）上的 Hermes 运维任务：远程 Desktop 连接、网络穿透、安全加固、服务启停、Windows 客户端安装踩坑。

---

## 一、Hermes Desktop 远程连接（完整工作流）

### 背景
Hermes Desktop 支持 **Remote 模式**——笔记本 Desktop 客户端通过 HTTPS 连接基地上的后端，完全不依赖 Tailscale 客户端，任何网络环境都能用。

### 前提
- 基地已安装 Tailscale 且启用 Funnel
- 基地运行 `hermes gateway` 和 `hermes dashboard`

### 步骤

**1. 基地侧：Dashboard 绑定 0.0.0.0 + 关闭 auth gate**

```bash
# 停掉旧 Dashboard
hermes dashboard --stop

# 用 --insecure + --host 0.0.0.0 重启（关闭 OAuth gate，允许非 loopback 访问）
hermes dashboard --port 9119 --host 0.0.0.0 --insecure --no-open --skip-build
```

⚠️ 不加 `--insecure` 会导致 Host header 校验拒绝（"Invalid Host header"），因为 Funnel 进来的请求 Host 是 TS.net 域名。

**2. 固化 Session Token**

Dashboard 每次重启生成随机 token，Desktop 需要固定 token：

```bash
# 生成固定 token 写入 .env
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
# 例如：pMbaoVMiN5HU8q7xHvGzu7dRWlz_gDWYz1LvP4UbT5s

echo "HERMES_DASHBOARD_SESSION_TOKEN=<你的token>" >> ~/.hermes/.env

# 重启 Dashboard 载入
hermes dashboard --stop
hermes dashboard --port 9119 --host 0.0.0.0 --insecure --no-open --skip-build
```

验证 token 生效：
```bash
curl -s http://127.0.0.1:9119/ | grep HERMES_SESSION_TOKEN
# 应输出固定 token
```

**3. Funnel 指向 Dashboard**

```bash
# Funnel 必须指向 9119（Python Dashboard），不能指向 8648（Node SPA）
sudo tailscale funnel --bg 9119
```

⚠️ 端口选择陷阱：
| 端口 | 服务 | Desktop 远程模式 |
|------|------|:--:|
| 8648 | Node SPA / Hermes Studio | ❌ 不转发 auth header |
| 8642 | Gateway API | ❌ 缺少 `/api/model/options` 等端点 |
| **9119** | **Python Dashboard** | **✅ 正确** |

**4. Desktop 侧配置**

Settings → 网关 → 选择「远程网关」：
- 远程 URL：`https://miao-thinkcentre-m710q-n080.tail589fe7.ts.net`
- 认证方式：Token
- Token：固定 token

### 验证
```bash
curl -s https://<ts-net域名>/api/status \
  -H "X-Hermes-Session-Token: <token>"
# 应返回 200 + version/gateway_state/gateway_platforms
```

### 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| "Invalid Host header" | Dashboard 绑在 127.0.0.1，Host 不匹配 | 改绑 0.0.0.0 |
| 401 Unauthorized | Token 未注入或过期 | 固化 token 到 .env |
| "Timed out...8000ms" | Funnel 指向了 8648（Node SPA） | 改指 9119 |
| "Timed out...15000ms"（模型页） | WebSocket 端点 404 | 正常——切到对话页即可 |
| Dashboard 重启后被 Gateway 覆盖 | Gateway 自动重启 Dashboard 用原参数 | 先 gateway stop → 手动 dashboard start → gateway start |

---

## 二、基地安全加固

### 标准清单

| 步骤 | 命令 |
|------|------|
| 关 CUPS | `sudo systemctl disable --now cups` |
| 装 Fail2ban | `sudo apt install fail2ban -y`<br>`sudo systemctl enable --now fail2ban` |
| 开 UFW | `sudo ufw default deny incoming`<br>`sudo ufw allow ssh`<br>`sudo ufw allow from 100.64.0.0/10`<br>`sudo ufw enable` |
| SSH 加固 | `sudo tee /etc/ssh/sshd_config.d/99-hardening.conf << 'EOF'`<br>`PasswordAuthentication no`<br>`PermitRootLogin no`<br>`MaxAuthTries 3`<br>`EOF`<br>`sudo systemctl restart sshd` |

⚠️ 以上全部需要 **sudo 密码**。Agent terminal 无密码时命令会失败。有两种解法：
1. **推荐**：配置 NOPASSWD 白名单（见本技能 §二-A）
2. **备选**：将密码写入 `~/.hermes/.env`（`SUDO_PASSWORD=<pw>`），Hermes terminal 工具自动读取。详见 `hermes-gateway-ops` 技能 §四-B「Headless sudo」。

### Tailscale 网段
`100.64.0.0/10` 是 Tailscale 的 CGNAT 地址空间，放行此段保证 Tailnet 内设备互通。

### 无人值守更新
```bash
systemctl is-enabled unattended-upgrades  # 确认已启用
```

---

## 二-A、远程 sudo 免密方案

### 背景

H 远程执行 `sudo` 命令时必须回家输入密码。以下方案让常用 sudo 命令免密，**一次配置永久解决**。

### 推荐：NOPASSWD 白名单

```bash
# 在基地终端执行一次（替换 miao 为你的系统用户名）
sudo visudo -f /etc/sudoers.d/hermes-agent
```

写入：

```
Cmnd_Alias HERMES_CMDS = /usr/bin/systemctl, /usr/bin/apt, /usr/bin/apt-get, /usr/bin/docker, /usr/bin/pkill, /usr/bin/kill, /usr/bin/ufw, /usr/bin/journalctl, /usr/sbin/reboot
miao ALL=(ALL) NOPASSWD: HERMES_CMDS
```

配置后 H 可直接执行：

| 命令 | 用途 |
|------|------|
| `sudo systemctl restart/stop/start/status` | 服务管理 |
| `sudo apt install/update/remove` | 软件包管理 |
| `sudo docker ...` | Docker 操作 |
| `sudo ufw allow/deny` | 防火墙 |
| `sudo journalctl -u xxx` | 查系统日志 |
| `sudo reboot` | 重启 |

**安全**：白名单只放行特定命令，不是 `ALL` 免密，`sudo bash`、`sudo rm -rf` 等高风险命令仍然需要密码。

### 备选：密码写入 .env

```bash
echo 'SUDO_PASSWORD=*** >> ~/.hermes/.env
```

H 自动读取 `SUDO_PASSWORD` 环境变量。但不安全（明文存储），仅在无法配置 NOPASSWD 时使用。

## 三、Windows 客户端安装（国内环境）

### 必须预先配置的镜像

Hermes Desktop 安装程序从境外下载多个大型依赖，直接装必卡死。**开装前先配：**

```cmd
# npm 镜像
npm config set registry https://registry.npmmirror.com

# 环境变量（需新开 cmd 窗口生效）
setx ELECTRON_MIRROR "https://npmmirror.com/mirrors/electron/"
setx PLAYWRIGHT_DOWNLOAD_HOST "https://npmmirror.com/mirrors/playwright/"

# Git 代理
git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"

# PowerShell 执行策略（如遇 npm.ps1 禁止运行）
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 常见错误

| 错误 | 原因 | 解决 |
|------|------|------|
| `git fetch failed (exit 128)` | GitHub 被墙 | 配 git insteadOf 代理 |
| npm 卡 30 分钟不动 | npm 下载被墙 | 配 npmmirror 镜像 |
| `npm EBUSY -4082` | Windows Defender 锁 node_modules | 关杀软实时防护 / 重启后删 `node_modules` 重装 |
| `build failed (exit 1)` | Electron 二进制下载失败 | 配 `ELECTRON_MIRROR` |
| `npm.ps1 禁止运行` | PowerShell 执行策略 | `Set-ExecutionPolicy RemoteSigned` |

### 如果实在装不上
直接用浏览器打开 Funnel URL 使用 Hermes Web UI——功能和 Desktop 完全一致。

---

## 四、git clone GitHub 加速

基地和笔记本通用：

```bash
git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"
```

测试可用镜像：
```bash
for url in https://ghproxy.net https://ghproxy.com https://mirror.ghproxy.com; do
  echo -n "$url → "; curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 "$url"
  echo
done
```

⚠️ ghproxy.com 经常挂，ghproxy.net 是目前最稳定的。

---

## 六、Home Assistant 集成

Hermes Agent 原生支持 Home Assistant，通过 `HASS_TOKEN` 激活。

### 配置

```bash
# 1. 在 HA Web UI 创建长期访问令牌
#    个人资料 → 长期访问令牌 → 创建（名称：Hermes Agent）

# 2. 写入 ~/.hermes/.env
echo "HASS_TOKEN=<令牌>" >> ~/.hermes/.env
echo "HASS_URL=http://127.0.0.1:8123" >> ~/.hermes/.env  # 可选，基地本地

# 3. 重启 Gateway 生效
hermes gateway restart
```

### 可用工具（配置后自动启用）

| 工具 | 功能 | 示例 |
|------|------|------|
| `ha_get_state` | 获取实体状态和属性 | 查温度、开关状态 |
| `ha_call_service` | 控制设备 | 开灯、调温、启动扫地机 |
| `ha_list_entities` | 列出实体（可按 domain/area 过滤） | 列出所有灯、客厅设备 |
| `ha_list_services` | 列出可用服务 | 查看空调支持的操作 |

另有 WebSocket 实时订阅状态变更。

### 部署要点

- HA 用 Docker `network_mode: host` → HASS_URL 用 `http://127.0.0.1:8123`
- ufw 需放行 8123（Tailscale 远程访问）
- HACS 手动安装到 `/home/miao/docker/ha/config/custom_components/hacs/`
- **HA 在 Funnel 后面需要反向代理信任配置**（`http: use_x_forwarded_for: true, trusted_proxies: - 127.0.0.1`），否则返回 400
- **Funnel 子路径陷阱**：HA 不认子路径（如 `/ha`），需让 HA 占 Funnel 根路径 `/`，Hermes Dashboard 挪到 `/dash`。用 `tailscale funnel --bg --https=443 --set-path=/ <target>` 配置

WebSocket JSON-RPC 端到端验证脚本：`references/ws-rpc-verify.py` — 模拟 Desktop 发送 `prompt.submit` 并验证模型返回。  
详见 [`base-machine-ops`](../devops/base-machine-ops/SKILL.md) §七。

---

## 七、Dashboard 稳定性排障

### 核心问题：随机 Token 导致 Desktop 断连

**根因链路**：`hermes-dashboard.service`（systemd enabled）→ 每次重启生成随机 `_SESSION_TOKEN` → Desktop 缓存的旧 token 无效 → WebSocket 连接后 `model.options` / `ready` 帧发送失败 → "提示词发送失败" / "网关断"

**关键诊断命令**：
```bash
# 检查 token 是否固定
python3 -c "
import re,urllib.request
f=open('/home/miao/.hermes/dashboard_session_token').read().strip()
html=urllib.request.urlopen('http://127.0.0.1:9119/').read().decode()
t=re.search(r\"__HERMES_SESSION_TOKEN__\s*=\s*['\\\"]([^'\\\"]+)\",html).group(1)
print('matches_file:', t==f, '  html_len:', len(t), '  file_len:', len(f))
"

# 检查是否有 systemd 服务在抢端口
systemctl is-active hermes-dashboard.service

# 检查 Dashboard 进程的环境变量
PID=$(ss -tlnp | awk -F'pid=' '/:9119/{split($2,a,\",\"); print a[1]; exit}')
tr '\0' '\n' < /proc/$PID/environ 2>/dev/null | grep HERMES_DASHBOARD
```

### 修复步骤

```bash
# 1. 停用 systemd 服务（否则每次手动启动被抢占）
sudo systemctl stop hermes-dashboard.service
sudo systemctl disable hermes-dashboard.service

# 2. 生成固定 token
umask 077
python3 -c "import secrets; print(secrets.token_urlsafe(32))" > ~/.hermes/dashboard_session_token
chmod 600 ~/.hermes/dashboard_session_token

# 3. 用固定 token 启动 Dashboard（需清空 9119 端口）
PID=$(ss -tlnp | awk -F'pid=' '/:9119/{split($2,a,\",\"); print a[1]; exit}')
[ -n "$PID" ] && kill -9 "$PID" 2>/dev/null
sleep 2
env HERMES_DASHBOARD_SESSION_TOKEN=*** ~/.hermes/dashboard_session_token)" \
  ~/.hermes/hermes-agent/venv/bin/hermes dashboard --port 9119 --host 0.0.0.0 \
  --insecure --no-open --skip-build &
```

### Watchdog 自恢复

每分钟检查 Dashboard HTTP + WebSocket 健康，不通自动重启：
- 脚本：`/home/miao/.hermes/scripts/dashboard_watchdog.sh`
- crontab：`* * * * * /home/miao/.hermes/scripts/dashboard_watchdog.sh >/dev/null 2>&1`

### WebSocket JSON-RPC 端到端验证

不用打开 Desktop，在基地直接验证完整发送链路：

```bash
python3 ~/.hermes/skills/devops/hermes-base-operations/scripts/ws_rpc_probe.py
```

该脚本模拟 Desktop 的完整协议：`session.create` → `prompt.submit` → 接收 `gateway.ready` / `message.start` / `message.delta` / `message.complete` 事件流。成功返回模型回复即证明发送链路正常。

**什么时候用**：Desktop 显示"提示词发送失败"但 Dashboard 200、WebSocket 101 都正常时。
- 如果探针返回 `OK` → 问题在 Desktop 客户端本地缓存/版本/后端地址，不在基地
- 如果探针失败 → 基地发送链路有问题，按本节其他步骤修复

### 排障原则：重复失败 → 升级到根因

**不要**在同一个修复模式（重启 Dashboard、检查端口、测 WebSocket 握手）上反复循环。
当第三个修复尝试仍失败时，必须**升级分析层级**：
1. 首次失败 → 重启服务
2. 再次失败 → 查端口/进程/日志
3. 第三次失败 → 查**为什么每次重启都治标不治本**（systemd 自动拉起？token 不一致？网关覆盖？）

### 常见误判

| 表面现象 | 可能根因 |
|----------|----------|
| Desktop "提示词发送失败" | 页面 token ≠ 进程 token |
| Dashboard 显示 `200` 但 Desktop 发不出 | 随机 token 未被 Desktop 刷新 |
| "网关断"但 Gateway 日志正常 | Desktop 侧 WS 通道用旧 token 连不上 |
| watchdog 显示 unhealthy 但手动检查正常 | 多个 Dashboard 进程抢占 9119 |
| 重启后恢复，几分钟后又断 | systemd 自动拉起新实例（随机 token 覆盖固定 token） |

### 常见陷阱：Desktop 切换远程地址后报 "Hermes couldn't start"

**症状**：在 Desktop 设置里把后端地址改成 Funnel 公网 URL，保存后重启，弹出 "Hermes couldn't start — Timed out connecting to Hermes backend after 15000ms"。

**根因**：Desktop 安装时默认配置为"本地模式"，首次改远程地址后，Desktop 依然先在笔记本本地尝试启动 Hermes 后端。15 秒连不上后超时报错——**不一定是基地端有问题**。

**处理顺序**：
1. 先验证基地端 Dashboard 是否可达（浏览器打开 Funnel URL，看能否显示页面）
2. 如果基地可达，点 "Use local gateway" 让 Desktop 本地跑通
3. 跑通后进设置再次确认后端地址是否正确保存
4. 完全退出 Desktop 重开

**不要在 Desktop 报 "Hermes couldn't start" 时反复重启基地 Dashboard**——这是两个独立的故障域。

### Funnel 切换：Dashboard ↔ Web UI

Funnel 根路径目前指向 Dashboard（端口 9119）。如需改为 Web UI（端口 8648）：

```bash
# 查看当前 Funnel
tailscale serve status

# 切换根路径指向 Web UI
sudo tailscale funnel --bg --https=443 http://127.0.0.1:8648

# 如需同时保留 Dashboard，加子路径
sudo tailscale serve --bg --https=443 /dash http://127.0.0.1:9119
```

结果：
- `https://<node>.ts.net/` → Web UI（8648）
- `https://<node>.ts.net/dash` → Dashboard（9119）

**Web UI 限制**：不能在 Desktop 远程模式中作为后端使用（不转发 auth header），仅适合浏览器直接操作。

---

## 七之补充：Cron 定时任务投递排障

### 问题模式：任务执行成功但微信收不到

**症状**：用户反馈「没收到全链路自检/灾备报告/待办事项等定时任务的完成信息」，但任务本身实际已执行。

### 诊断流程（按顺序）

| 步骤 | 命令/操作 | 看什么 |
|------|-----------|--------|
| 1. 查任务状态 | `cronjob(action='list')` | 看 `last_run_at`（执行时间）和 `last_delivery_error`（投递错误） |
| 2. 确认投递失败 | 查 `last_delivery_error` 字段 | `delivery error: Weixin send failed: iLink sendmessage rate limited; cooldown active for 30.0s` |
| 3. 查日志确认执行 | `grep <job_id> ~/.hermes/logs/gateway.log ~/.hermes/logs/agent.log` | 区分「任务没跑」和「跑了但投递失败」 |
| 4. 跑健康检查 | `bash ~/.hermes/scripts/hermes-health-check.sh` | 确认系统实际状态正常 |
| 5. 确认入站正常 | 给用户发消息看能否回复 | 入站正常 = iLink 连接没断，只是出站被限 |

### iLink 单向速率限制特征

| 特征 | 说明 |
|------|------|
| **入站** | ✅ 用户发消息正常，能收到并回复 |
| **出站（实时对话）** | ✅ 对话中的回复正常投递 |
| **出站（Cron 定时任务）** | ❌ 返回 `iLink sendmessage rate limited; cooldown active for 30.0s` |
| **持续时间** | 可能持续数小时不自动恢复 |

这表明 iLink（微信桥接软件）对**自动化出站消息**有独立的速率限制，与实时对话的投递通道不同。

### 错误日志特征

```
ERROR gateway.platforms.weixin: [Weixin] send failed to=o9cq801d: iLink sendmessage rate limited; cooldown active for 30.0s
WARNING cron.scheduler: Job '<job_id>': live adapter send to weixin:... failed (...), falling back to standalone
ERROR cron.scheduler: Job '<job_id>': delivery error: Weixin send failed: iLink sendmessage rate limited; cooldown active for 30.0s
```

注意：错误日志中会先尝试 `live adapter`（实时通道），失败后回退到 `standalone`（独立投递），两者都失败。

### 修复方案

| 方案 | 操作 | 适合场景 |
|------|------|----------|
| **减频** | 调低 cron 推送频率（如把每6小时自检改为每天一次汇总） | 推送太多触发了 iLink 限制 |
| **换通道** | 把关键告警改为飞书（`deliver: feishu`）投递 | 飞书无此限制 |
| **重启 iLink** | 重启 Gateway（`hermes gateway restart`）有时可重置限流状态 | 试探性恢复 |
| **等恢复** | 什么都不做，等待 iLink 限流窗口过期 | 如果限流是临时的 |

### 主动投递纪律

当用户询问「为啥没收到报告」时：

1. **不要只解释原因**——补上缺失的报告内容（手动跑健康检查/备份检查/待办扫描）
2. **用表格呈现**哪些任务执行成功但投递失败，让用户一目了然
3. **给出修复选项**让用户决策，不要坐等指示

---

## 八、服务管理速查

```bash
# Dashboard
hermes dashboard --status           # 查看状态
hermes dashboard --stop             # 停止
hermes dashboard --port 9119 --host 0.0.0.0 --insecure --no-open --skip-build  # 手动启动

# Gateway
hermes gateway status               # 查看状态
hermes gateway restart              # 重启

# Tailscale Funnel
tailscale serve status              # 查看
sudo tailscale funnel --bg <port>   # 切换到新端口

# 全链路自启验证
sudo reboot
# 等 2 分钟，微信发消息 → 有回复即成功
```
