# Linux systemd 自启配置指南

## 适用场景

- 无显示器 Linux 主机（headless server）
- 需要开机自动拉起所有 Hermes 服务
- 代替手动 `nohup &` 或 screen/tmux 守护

## 前置条件

- `cat /proc/1/comm` → `systemd`
- 用户有 sudo 权限

## 4 个服务及依赖关系

| 服务 | 端口 | 启动命令 | 依赖 |
|------|------|----------|------|
| hermes-tdai | 8420 | `node --import tsx/esm ...` | 无 |
| hermes-web-ui | 8648 | `hermes-web-ui start` | 无 |
| hermes-dashboard | 9119 | `hermes dashboard --port 9119 --host 127.0.0.1 --no-open --skip-build` | 无 |
| hermes-gateway | 8642 | `hermes gateway run --replace` | TDAI, Web UI, Dashboard |

**启动顺序**：TDAI → Web UI → Dashboard → Gateway（Gateway 最后，`After=` 声明依赖）

## ⚠️ 关键陷阱

### 陷阱一：systemd PATH 不含用户本地 bin

`hermes-web-ui` 的 shebang 是 `#!/usr/bin/env node`，systemd 默认 PATH 不含 `/home/<user>/.local/bin`，导致找到系统旧版 Node（如 v18）而非用户安装的 v22。

**症状**：v0.6.11 升级后启动失败，日志显示 `Node.js v18.20.8` 和 `ERR_UNKNOWN_BUILTIN_MODULE: node:sqlite`

**修复**：在 `[Service]` 段添加：
```
Environment=PATH=/home/<user>/.local/bin:/usr/local/bin:/usr/bin:/bin
```

### 陷阱二：API_SERVER_KEY 强制要求（即使 loopback 绑定）

新版 Hermes（v0.16.0+）强制要求 `API_SERVER_KEY`，即使 `host: 127.0.0.1` 也不能跳过。

**症状**：Gateway 日志 `Refusing to start: API_SERVER_KEY is required for the API server, including loopback-only binds on 127.0.0.1.`，api_server 平台连接失败，Gateway 只有 2/3 平台在线。

**修复**：`.env` 中必须有 `API_SERVER_KEY=<任意值>`，Web UI 会自动从 `.env` 读取。

### 陷阱三：Dashboard 构建死循环

`hermes dashboard` 默认先执行 `tsc -b && vite build`。lucide-react 类型导出不兼容导致 tsc 失败时，vite build 永远不会执行。

**症状**：Dashboard 进程运行中但端口 9119 长时间无 HTTP 响应，curl 超时。

**修复**：先手动 `cd web && npm install && npx vite build`，然后 Dashboard 加 `--skip-build`。

### 陷阱四：Web UI Type=forking 和 PIDFile

`hermes-web-ui start` 会 daemonize 自己。systemd 必须用 `Type=forking` + `PIDFile`，不能用 `Type=simple`（否则 systemd 认为进程立即退出进入重启循环）。

### 陷阱五：旧的存活进程占端口

用 systemd 接管前，必须杀掉所有手动启动的旧进程。systemd 启动时如果端口被占会报 `EADDRINUSE`。

## 完整部署步骤

### 1. 创建服务文件

全部 4 个模板见 `templates/` 目录。

### 2. 安装并启用

```bash
sudo cp hermes-*.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable hermes-tdai.service hermes-web-ui.service hermes-dashboard.service hermes-gateway.service
```

### 3. 停掉旧进程后启动

```bash
# 先确认旧进程 PID
ss -tlnp | grep -E '8420|8642|8648|9119'
# 逐一 kill，然后
sudo systemctl start hermes-tdai.service hermes-web-ui.service hermes-dashboard.service hermes-gateway.service
```

### 4. 验证

```bash
sudo systemctl status hermes-tdai hermes-web-ui hermes-dashboard hermes-gateway --no-pager
ss -tlnp | grep -E '8420|8642|8648|9119'

# 验证 Gateway 3 平台全连
grep 'running with' ~/.hermes/logs/gateway.log | tail -1
# 预期: Gateway running with 3 platform(s)
```

## 日常管理

```bash
sudo systemctl status hermes-gateway          # 查看状态
sudo systemctl restart hermes-gateway         # 重启单个
sudo journalctl -u hermes-gateway -f          # 实时日志
```
