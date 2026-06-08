# Hermes Web UI 完全卸载指南

## 适用范围

卸载 npm 包 `hermes-web-ui`（Node.js 管理仪表盘，默认端口 8648）。

> **不要混淆**：`hermes dashboard`（Hermes Agent 内置 Python CLI 仪表盘，端口 9119）是 Hermes 核心功能，与本 npm 包无关。卸载 hermes-web-ui 不会影响 `hermes dashboard`。

## 卸载清单

hermes-web-ui 涉及 6 个组件，全部都需要清理：

```
[组件]                    [位置]
Node 服务进程              ~/.local/bin/node ... hermes-web-ui/dist/server/index.js
systemd 自启服务           ~/.config/systemd/user/hermes-web-ui.service
自启链接                   ~/.config/systemd/user/default.target.wants/hermes-web-ui.service
npm 全局包                 ~/.npm-global/lib/node_modules/hermes-web-ui/
npm bin 软链接             ~/.npm-global/bin/hermes-web-ui
数据目录                   ~/.hermes-web-ui/（含 SQLite 数据库、日志、token、上传文件）
端口                       8648
Windows 独立启动脚本       C:\Tools\hermes-web-ui-start.bat（或类似位置）
Windows .bak 备份文件      C:\Tools\hermes-gateway-start.bat.bak（自启脚本还原源）
```

> **重要坑点**：hermes-web-ui 卸载后可能自动复活。导致复活的常见机制：
> 1. Windows 系统重启后，有**独立的** `hermes-web-ui-start.bat` 脚本单独启动 web-ui
> 2. `.bat.bak` 备份文件被系统还原，恢复了含 web-ui 的旧版批处理脚本
> 3. `hermes-gateway-start.bat` 未锁定为只读，被 Windows 覆盖还原
> 4. npm 包被删除后，Windows 自启脚本调用 `hermes-web-ui start` 会**自动重新安装** npm 包

```
[组件]                    [位置]
Node 服务进程              ~/.local/bin/node ... hermes-web-ui/dist/server/index.js
systemd 自启服务           ~/.config/systemd/user/hermes-web-ui.service
自启链接                   ~/.config/systemd/user/default.target.wants/hermes-web-ui.service
npm 全局包                 ~/.npm-global/lib/node_modules/hermes-web-ui/
npm bin 软链接             ~/.npm-global/bin/hermes-web-ui
数据目录                   ~/.hermes-web-ui/（含 SQLite 数据库、日志、token、上传文件）
端口                       8648
```

## 卸载步骤

### 1. 停止进程

```bash
# 终止 hermes-web-ui Node 服务进程
pkill -f 'hermes-web-ui/dist/server/index.js' 2>/dev/null || true

# 确认无残留
ps aux | grep 'hermes-web-ui' | grep -v grep
```

### 2. 禁用并删除 systemd 服务

```bash
systemctl --user disable hermes-web-ui.service
rm -v ~/.config/systemd/user/hermes-web-ui.service
# disable 命令会同时删除 default.target.wants 下的软链接
```

### 3. 卸载 npm 全局包

**常见坑：npm uninstall 报 `ENOTEMPTY` 错误**（目录重命名冲突，约 20% 情况下发生）。

先尝试正常卸载：

```bash
npm uninstall -g hermes-web-ui
```

如果报 `ENOTEMPTY`，手动清理：

```bash
rm -rf ~/.npm-global/lib/node_modules/hermes-web-ui
rm -f ~/.npm-global/bin/hermes-web-ui
# 清理 npm 残留的临时目录
rm -rf ~/.npm-global/lib/node_modules/.hermes-web-ui-*
```

验证：

```bash
npm list -g hermes-web-ui 2>&1 | head -3
# 输出 "(empty)" 或报错 "not found" 表示已卸载
```

### 4. 删除数据目录

```bash
rm -rf ~/.hermes-web-ui/
```

该目录包含：

| 文件 | 说明 |
|------|------|
| `server.pid` | 服务 PID 文件 |
| `.token` | API 认证 token |
| `.login-lock.json` | 登录防双送锁 |
| `hermes-web-ui.db` | SQLite 数据库（会话/配置） |
| `hermes-web-ui.db-shm` | SQLite 共享内存 |
| `hermes-web-ui.db-wal` | SQLite WAL 日志 |
| `logs/` | 服务运行日志 |
| `upload/` | 上传文件缓存 |

## 5. 更新 Windows 自启脚本（如适用）

如果 hermes-web-ui 是通过 Windows 任务计划程序 + 批处理文件（`C:\\Tools\\hermes-gateway-start.bat` 等）随系统启动的，卸载后需要从批处理文件中移除 web-ui 启动行，否则下次重启会尝试启动已卸载的程序。

典型场景：某个 bat 文件同时启动了 web-ui 和 gateway：

```bat
@echo off
echo Starting Hermes Web UI...          ← 删除本行
wsl.exe -d Ubuntu -u yanxin ... start   ← 删除本行
echo Starting Hermes Gateway...
wsl.exe -d Ubuntu -u yanxin ... gateway run --replace
```

改为仅启动 gateway：

```bat
@echo off
echo Starting Hermes Gateway...
wsl.exe -d Ubuntu -u yanxin bash -lc "cd /home/yanxin/Hermes-Agent && source venv/bin/activate && hermes gateway run --replace"
```

### 5.1 检查并清理所有相关脚本

```bash
# 列出 C:\Tools\ 下所有与 Hermes 相关的脚本
ls -la /mnt/c/Tools/*.bat /mnt/c/Tools/*.ps1 2>/dev/null

# 查找独立 web-ui 启动脚本（常见文件名）
ls /mnt/c/Tools/hermes-web-ui-start.bat 2>/dev/null && rm -f /mnt/c/Tools/hermes-web-ui-start.bat

# 查找并删除 .bak 备份（可能被系统用于还原）
ls /mnt/c/Tools/hermes-gateway-start.bat.bak 2>/dev/null && rm -f /mnt/c/Tools/hermes-gateway-start.bat.bak

# 检查 Windows 启动文件夹
powershell.exe -Command "Get-ChildItem '$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup' -Filter '*hermes*'" 2>/dev/null
```

### 5.2 锁定批处理文件为只读（防 WSL/Windows 还原覆盖）

```bash
# 从 WSL 内锁定（chmod 对跨文件系统有效但可能被 Windows 覆盖）
chmod -w /mnt/c/Tools/hermes-gateway-start.bat

# 或从 Windows 侧锁定（更可靠）
powershell.exe -Command "attrib +R C:\Tools\hermes-gateway-start.bat" 2>&1
```

> 锁定只读是防止自启脚本在 Windows 系统更新/重启后被旧版本覆盖的关键步骤。

## 验证彻底清除

```bash
echo "=== 进程 ==="
ps aux | grep 'hermes-web-ui' | grep -v grep || echo "✓ 无"
echo "=== systemd ==="
ls ~/.config/systemd/user/hermes-web-ui.service 2>/dev/null || echo "✓ 已删"
echo "=== npm ==="
npm list -g hermes-web-ui 2>&1 | grep -v "empty" || echo "✓ 已卸"
echo "=== 数据 ==="
ls ~/.hermes-web-ui 2>/dev/null || echo "✓ 已删"
echo "=== 端口 ==="
ss -tlnp 2>/dev/null | grep 8648 || echo "✓ 无监听"
```

## 注意事项

- **Port 9119 的 `hermes dashboard` 不动**：它是 Hermes Agent 内置功能，与 npm 的 hermes-web-ui 无关。
- **npm uninstall 的 ENOTEMPTY 错误**：npm 已跟踪到该 bug（https://github.com/npm/cli/issues/XXXX），但未完全修复。手动 `rm -rf` 是可靠的变通方案。
- **`hermes-web-ui` 不会影响 Hermes 核心功能**：卸载后 Hermes 的 CLI、gateway、cron、skills 等一切正常。
