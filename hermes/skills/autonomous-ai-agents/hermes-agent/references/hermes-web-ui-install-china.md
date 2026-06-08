# Hermes Web UI 中国网络安装指南（含 WSL 自启）

## 适用范围

安装 npm 包 `hermes-web-ui`（Node.js 管理仪表盘，默认端口 8648），适用于：

- 国内网络环境（npmjs.org 超时/极慢）
- WSL 环境（可能无 systemd 用户总线）
- 重新安装（uninstall → install 完整流程）

> **不要混淆**：`hermes dashboard`（Hermes Agent 内置 Python CLI 仪表盘，端口 9119）是 Hermes 核心功能，与本 npm 包无关。hermes-web-ui 安装/卸载不会影响 `hermes dashboard`。

---

## 安装步骤

### 1. npm 全局安装（国内镜像）

```bash
npm install -g hermes-web-ui --registry=https://registry.npmmirror.com
```

- 实测约 **6 秒/54 包**完成（vs 官方源超时 120s+）
- 安装后版本通常为 **v0.5.28+**（最新版自动拉取）

### 2. 验证 symlink

`npm install -g` 有时不会自动创建 bin symlink（约 20% 概率）。验证：

```bash
which hermes-web-ui
# 预期输出: /home/yanxin/.npm-global/bin/hermes-web-ui
hermes-web-ui --version
# 预期输出: hermes-web-ui v0.5.28
```

如果 `which` 找不到，手动创建：

```bash
ln -sf /home/yanxin/.npm-global/lib/node_modules/hermes-web-ui/bin/hermes-web-ui.mjs \
       /home/yanxin/.npm-global/bin/hermes-web-ui
```

### 3. 创建 systemd 自启服务

```bash
cat > ~/.config/systemd/user/hermes-web-ui.service << 'EOF'
[Unit]
Description=Hermes Web UI - Management Dashboard
After=network-online.target
Wants=network-online.target
StartLimitIntervalSec=0

[Service]
Type=forking
PIDFile=%h/.hermes-web-ui/server.pid
ExecStart=%h/.npm-global/bin/hermes-web-ui start
ExecStop=%h/.npm-global/bin/hermes-web-ui stop
WorkingDirectory=%h
Restart=always
RestartSec=10

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable hermes-web-ui.service
systemctl --user start hermes-web-ui.service
```

**注意**：如果报 `Failed to connect to bus: No such file or directory`，说明 WSL 未启用 systemd。跳到第 4 步。

### 4. 直接启动（无 systemd 环境）

```bash
hermes-web-ui start
```

输出示例：
```
  ⏳ Starting hermes-web-ui (PID: 10049, port: 8648)...
  ✓ hermes-web-ui started
    http://localhost:8648/#/?token=79c8bb819e55f8d7669c8dd9ce1b7c1f386851e9fbae219cda0796ae3af204e2
    Log: /home/yanxin/.hermes-web-ui/server.log
```

进程结构（两个进程）：
- **Node 服务进程**：`node .../hermes-web-ui/dist/server/index.js`
- **Agent Bridge 进程**：`python3 .../hermes_bridge.py`（Hermes Agent 桥接）

### 5. 验证运行

```bash
# 进程检查
ps aux | grep 'hermes-web-ui/dist/server' | grep -v grep

# 端口检查
ss -tlnp | grep 8648
# 预期: LISTEN 0 511 0.0.0.0:8648 ...

# PID 文件
cat ~/.hermes-web-ui/server.pid

# Token 文件
cat ~/.hermes-web-ui/.token

# 服务日志
tail -5 ~/.hermes-web-ui/server.log
```

---

## WSL 自启方案

### 方案 A：启用 WSL systemd（推荐）

```bash
# 在 /etc/wsl.conf 添加
sudo sh -c 'printf "\n[boot]\nsystemd=true\n" >> /etc/wsl.conf'
```

然后 **重启 WSL**（`wsl.exe --shutdown` + 重新打开终端）。重启后：
1. 验证 PID 1 是 systemd：`cat /proc/1/comm` → `systemd`
2. `systemctl --user daemon-reload`
3. `systemctl --user enable hermes-web-ui.service`
4. `systemctl --user start hermes-web-ui.service`

### 方案 B：Windows 任务计划程序（无 systemd 时）

> **⚠️ 关键陷阱：`bash -lc` 不加载 `~/.npm-global/bin/` 到 PATH**  
> 即使 `.bashrc` / `.profile` 里写了 `export PATH="$HOME/.npm-global/bin:$PATH"`，`wsl.exe bash -lc` 模式下该路径也不会被加载（WSL 环境变量注入机制问题）。直接用 `hermes-web-ui` 命令会报 `command not found`。  
> **修正方案：** 使用绝对路径 `/home/yanxin/.npm-global/bin/hermes-web-ui` 替代裸命令名。

追加到现有 Gateway 启动批处理文件 `C:\Tools\hermes-gateway-start.bat`（先启动 Web UI，再启动 Gateway，因为 gateway 会阻塞前台）：

```batch
@echo off
echo Starting Hermes Web UI...
wsl.exe -d Ubuntu -u yanxin /home/yanxin/.npm-global/bin/hermes-web-ui start
echo Starting Hermes Gateway...
wsl.exe -d Ubuntu -u yanxin bash -lc "cd /home/yanxin/Hermes-Agent && source venv/bin/activate && hermes gateway run --replace"
```

如果在任务计划程序中建独立任务:

1. 创建 `C:\Tools\hermes-web-ui-start.bat`：
   ```batch
   @echo off
   wsl.exe -d Ubuntu -u yanxin /home/yanxin/.npm-global/bin/hermes-web-ui start
   ```
2. 任务计划程序 → 创建任务 → 触发器："用户登录时" → 操作：启动该 bat 文件

---

## 令牌访问

### 查看令牌

```bash
cat ~/.hermes-web-ui/.token
```

复制输出内容粘贴到浏览器登录页即可。

### 禁用令牌认证

环境变量 `AUTH_DISABLED=1` 可在启动时关闭令牌验证，访问 `http://localhost:8648` 直接进入无需 token。

```bash
AUTH_DISABLED=1 hermes-web-ui start
```

启动日志中不会出现 "Auth enabled — token: ..." 行，URL 也不带 `?token=...` 参数。

**在 WSL `bash -lc` 模式下** 将 env var 注入到命令前：

```bash
wsl.exe -d Ubuntu -u yanxin bash -lc "AUTH_DISABLED=1 /home/yanxin/.npm-global/bin/hermes-web-ui start"
```

**验证免令牌已生效：** 访问任意 API 路径应返回 404 而非 401：

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8648/api/sessions
# 预期: 404 (表示请求通过了 auth 拦截)
# 如果返回 401: auth 仍开启
```

### 自定义令牌

```bash
AUTH_TOKEN=mytoken123 hermes-web-ui start
```

---

## 访问地址

| 环境 | 地址 |
|------|------|
| WSL 内部 | http://localhost:8648 |
| Windows 浏览器 | http://<WSL-IP>:8648 |

查 WSL IP：
```bash
ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1
```

---

## 常见问题

| 症状 | 原因 | 解决 |
|------|------|------|
| npm install 超时 | 国内网络访问 npmjs.org 慢 | 用 `--registry=https://registry.npmmirror.com` |
| `which hermes-web-ui` 找不到 | npm 未创建 bin symlink | 手动 `ln -sf` |
| `systemctl --user` 报错 "Failed to connect to bus" | WSL 未启用 systemd | 用直接启动或任务计划程序 |
| 重启 WSL 后 Web UI 无法访问 | systemd 不可用或未配置自启 | 见上方 WSL 自启方案 |
| 浏览器能打开页面但 API 返回 401 | 需输入令牌 | `cat ~/.hermes-web-ui/.token` 粘贴 |
| Web UI 有新版本而未更新 | 重新安装后自动拉最新版 | `npm uninstall -g hermes-web-ui && npm install -g hermes-web-ui --registry=...` |
