# Hermes Web UI Dashboard 访问指南

## Dashboard 地址

- 默认端口：8648
- `hermes-web-ui start` 监听 `0.0.0.0:8648`
- 在 Windows 浏览器访问 `http://<WSL-IP>:8648`
- 查 WSL IP：`ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1`

## 登录令牌

Dashboard 首次启动时自动生成一个随机令牌，存储在：

```
~/.hermes-web-ui/.token
```

查看令牌：

```bash
cat ~/.hermes-web-ui/.token
```

复制输出内容粘贴到浏览器登录页的令牌输入框即可。

## 禁用令牌认证（不推荐）

启动前设置环境变量可完全关闭登录认证：

```bash
AUTH_DISABLED=1 hermes-web-ui start
```

或在 systemd service 文件 `[Service]` 段添加：

```
Environment=AUTH_DISABLED=1
```

## 自定义令牌

通过 `AUTH_TOKEN` 环境变量设置固定令牌（替代随机生成的）：

```bash
AUTH_TOKEN=mytoken123 hermes-web-ui start
```

## 常见问题

### 页面打开但 API 返回 401
说明令牌认证正常工作。在页面上输入正确的令牌即可。令牌首次访问失败会记入登录锁文件 `~/.hermes-web-ui/.login-lock.json`。

### WSL 重启后打不开
两个原因：IP 变了，或 web-ui 进程没有自动重启。参见 `references/wsl-migration-d-drive.md` 的迁移后检查清单。

### 找不到令牌文件
如果 `cat ~/.hermes-web-ui/.token` 提示不存在，说明 web-ui 可能还没有启动过至少一次。运行 `hermes-web-ui start` 后，文件会自动生成。

### Windows 计划任务 / wsl.exe 启动后 hermes-web-ui 找不到命令
当通过 `wsl.exe -d Ubuntu -u yanxin bash -lc "hermes-web-ui start"` 启动时，即使 `.bashrc` 中设置了 `PATH="$HOME/.npm-global/bin:$PATH"`，命令仍可能报 `command not found`。原因是 `wsl.exe` 启动的 login shell 环境传播路径与交互式 shell 不一致。

**修复：在 .bat 脚本中使用绝对路径代替命令名。**
```batch
REM ❌ 不工作
wsl.exe -d Ubuntu -u yanxin bash -lc "hermes-web-ui start"

REM ✅ 工作
wsl.exe -d Ubuntu -u yanxin /home/yanxin/.npm-global/bin/hermes-web-ui start

REM ✅ 带环境变量
wsl.exe -d Ubuntu -u yanxin env AUTH_DISABLED=1 /home/yanxin/.npm-global/bin/hermes-web-ui start
```

同理，其他 npm 全局安装的工具（`n`, `bun`, `pnpm`, `opencli` 等）通过 `wsl.exe` 调用时也应使用绝对路径。
