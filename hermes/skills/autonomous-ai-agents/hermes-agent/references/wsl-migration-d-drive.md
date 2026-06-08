# WSL 迁移到 D 盘（完整流程）

## 核心教训

**不要从 WSL 内部执行 `wsl --export`。** Gateway 重启会杀死 WSL 内部的后台进程，导致导出中断（已跑 20 分钟后丢失）。必须使用 Windows .bat 脚本从外部执行。

## 迁移脚本模板

```batch
@echo off
chcp 65001 >nul
title WSL迁移工具 - C盘→D盘

echo ============================================
echo   WSL Ubuntu 迁移到 D 盘
echo ============================================

:: [1/4] 导出
if not exist "D:\wsl-backup" mkdir D:\wsl-backup
wsl --export Ubuntu "D:\wsl-backup\ubuntu.tar"
if %errorlevel% neq 0 ( pause & exit /b %errorlevel% )

:: [2/4] 注销旧 WSL
wsl --unregister Ubuntu

:: [3/4] 导入到 D 盘
if not exist "D:\wsl" mkdir D:\wsl
wsl --import Ubuntu "D:\wsl" "D:\wsl-backup\ubuntu.tar"

:: [4/4] 设置默认用户 + 启动 Gateway
wsl -d Ubuntu -u root bash -c "echo '[user]' > /etc/wsl.conf && echo 'default=yanxin' >> /etc/wsl.conf"
wsl --terminate Ubuntu
timeout /t 3 /nobreak >nul
wsl -d Ubuntu -u yanxin bash -lc "cd /home/yanxin/Hermes-Agent && source venv/bin/activate && nohup hermes gateway run --replace > /home/yanxin/.hermes/logs/gateway-restart.log 2>&1 &"

echo 迁移完成。新位置：D:\wsl\Ubuntu\ （备份 D:\wsl-backup\ubuntu.tar 可删除）
pause
```

## 关键坑点

### 1. CRLF 换行符
在 WSL 里用 `write_file` 写的 .bat 文件是 LF 换行，Windows CMD 打开会闪退。必须转换：
```bash
sed -i 's/$/\r/' /mnt/d/path/to/migrate-wsl.bat
```
或直接在 Windows 里用记事本另存为。

### 2. 导出文件大小
`wsl --export` 不压缩，一个 34GB 的 WSL 实例导出为约 39GB 的 tar 文件。确保目标盘有足够空间。

### 3. 迁移后必须检查
- **备份文件可删除**：`D:\\wsl-backup\\ubuntu.tar` 占用约 39GB，迁移完成后安全删除
- **WSL IP 可能变化**：Web UI 浏览器收藏夹里存的旧 IP 打不开，运行 `ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1`（或 `hostname -I`）查新 IP
- **Dashboard 令牌**：Web UI 登录页会要求输入令牌。令牌自动生成于 `~/.hermes-web-ui/.token`，运行 `cat ~/.hermes-web-ui/.token` 查看。如需禁用令牌认证，启动前设置 `AUTH_DISABLED=1` 环境变量
- **systemd 需要显式启用**：迁移后 `/etc/wsl.conf` 只有 `[user]` 段，需手动加 `[boot]\\nsystemd=true` 才能开机自启
- **Web UI 自启**：如果之前用 systemd 自启，迁移后需确认 systemd 可用

### 4. Gateway 恢复
迁移脚本最后一步自动启动 Gateway，等待约 30 秒后在微信发送消息测试。
