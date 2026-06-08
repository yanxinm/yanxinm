# Linux systemd 自启配置模板

适用于常年挂机的 Linux 主机，开机自动拉起全部 Hermes 服务。4 个 systemd unit 文件，相互独立但按依赖顺序启动。

## 前提

- Linux 主机，systemd 为 PID 1（`cat /proc/1/comm` → `systemd`）
- 用户有 sudo 权限
- 所有服务已安装：hermes-agent、hermes-web-ui (npm)、TDAI Memory Gateway

## 路径变量

以下模板中 `<USER>` 替换为实际用户名，`<HERMES_HOME>` 替换为 hermes-agent 安装路径（常见：`/home/<USER>/.hermes/hermes-agent` 或 `/home/<USER>/Hermes-Agent`）。用 `hermes --version` 输出的 `Project:` 行确认。

npm global prefix 用 `npm config get prefix` 确认。

## 1. hermes-tdai.service

TDAI Memory Gateway — 端口 8420。最先启动，Gateway 依赖它。

```ini
[Unit]
Description=Hermes TDAI Memory Gateway
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=<USER>
WorkingDirectory=/home/<USER>/.memory-tencentdb
ExecStart=/home/<USER>/.local/bin/node --import tsx/esm node_modules/@tencentdb-agent-memory/memory-tencentdb/src/gateway/server.ts
Restart=always
RestartSec=10
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
```

## 2. hermes-web-ui.service

Web UI 管理面板 — 端口 8648。Type=forking（start 命令会 daemonize）。

```ini
[Unit]
Description=Hermes Web UI
After=network-online.target
Wants=network-online.target

[Service]
Type=forking
User=<USER>
Environment=PATH=/home/<USER>/.local/bin:/usr/local/bin:/usr/bin:/bin
PIDFile=/home/<USER>/.hermes-web-ui/server.pid
ExecStart=<NPM_PREFIX>/bin/hermes-web-ui start
ExecStop=<NPM_PREFIX>/bin/hermes-web-ui stop
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

> `<NPM_PREFIX>` 用 `npm config get prefix` 获取，常见值为 `/home/<USER>/.hermes/node` 或 `/home/<USER>/.npm-global`。

## 3. hermes-dashboard.service

Dashboard 仪表盘 — 端口 9119。**必须加 `--skip-build`**，否则启动时 tsc 类型检查失败导致 HTTP 超时。

```ini
[Unit]
Description=Hermes Dashboard
After=network-online.target hermes-web-ui.service
Wants=network-online.target

[Service]
Type=simple
User=<USER>
ExecStart=<HERMES_HOME>/venv/bin/hermes dashboard --port 9119 --host 127.0.0.1 --no-open --skip-build
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

## 4. hermes-gateway.service

Hermes Gateway — 端口 8642。**最后启动**，依赖前三个服务就绪。

```ini
[Unit]
Description=Hermes Gateway
After=network-online.target hermes-tdai.service hermes-web-ui.service hermes-dashboard.service
Wants=network-online.target hermes-tdai.service hermes-web-ui.service hermes-dashboard.service

[Service]
Type=simple
User=<USER>
ExecStart=<HERMES_HOME>/venv/bin/hermes gateway run --replace
Restart=always
RestartSec=15

[Install]
WantedBy=multi-user.target
```

## 部署步骤

```bash
# 1. 将 4 个 .service 文件写入 /etc/systemd/system/
sudo cp hermes-tdai.service hermes-web-ui.service hermes-dashboard.service hermes-gateway.service /etc/systemd/system/

# 2. 重载 systemd
sudo systemctl daemon-reload

# 3. 启用开机自启
sudo systemctl enable hermes-tdai hermes-web-ui hermes-dashboard hermes-gateway

# 4. 立即启动
sudo systemctl start hermes-tdai hermes-web-ui hermes-dashboard hermes-gateway

# 5. 验证
sudo systemctl status hermes-tdai hermes-web-ui hermes-dashboard hermes-gateway --no-pager
ss -tlnp | grep -E '8420|8642|8648|9119'
```

## 日常管理

```bash
sudo systemctl status hermes-gateway        # 查看单个状态
sudo systemctl restart hermes-gateway       # 重启单个
sudo systemctl stop hermes-gateway          # 停止单个
sudo journalctl -u hermes-gateway -f        # 实时日志
sudo journalctl -u hermes-gateway -n 50     # 最近 50 行
sudo systemctl list-units 'hermes-*'        # 列出所有 hermes 服务
```

## 故障排查

| 症状 | 原因 | 解决 |
|------|------|------|
| `EADDRINUSE` (TDAI) | 旧 TDAI 进程还占着 8420 | `kill` 旧 PID 后 systemd 的 Restart=always 会自动重试 |
| Web UI `already running` | 旧进程未清理，PID 文件残留 | `kill` 旧进程 + `rm ~/.hermes-web-ui/server.pid` + `systemctl restart` |
| Gateway 启动后立刻退出 | 端口冲突或平台连接失败 | `journalctl -u hermes-gateway -n 30` 查看原因 |
| Dashboard HTTP 000 | 没加 `--skip-build`，卡在 tsc | 加 `--skip-build` 重启 |
| Gateway 只有 2/3 平台在线（缺 api_server） | API_SERVER_KEY 未在 `.env` 设置（v0.16+ 强制要求） | `echo 'API_SERVER_KEY=xxx' >> ~/.hermes/.env` + `systemctl restart hermes-gateway` |
| Web UI 聊天报 500 | Gateway 的 API Server 返回 401（API Key 缺失/错误） | 检查 `.env` 中 `API_SERVER_KEY`，确认 Gateway 有 3/3 平台在线 |
