# 笔记本 SSH+SFTP 同步工作台账

## 架构

```
笔记本 (Ethan, Windows, 100.86.148.56)
  E:/百度云同步盘/工作台账/
    ↓ SSH + SFTP (Python paramiko)
基地 (M710q, Ubuntu, 100.86.13.11)
  ~/工作台账/  (本地副本)
```

## 笔记本端配置

### 1. 安装 OpenSSH Server
Windows 设置 → 可选功能 → 添加功能 → "OpenSSH 服务器"

### 2. 添加基地公钥（管理员账户）
```powershell
mkdir C:\ProgramData\ssh -Force
Add-Content C:\ProgramData\ssh\administrators_authorized_keys "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBoGROVU5D4FY04HiAHRtTM7tHCO/l7Yfj5fjyJ2BMhU hermes-base-m710q"
```

> ⚠️ Windows 管理员账户的 authorized_keys 在 `C:\ProgramData\ssh\administrators_authorized_keys`，不是 `~/.ssh/authorized_keys`。

### 3. 防火墙规则
```powershell
New-NetFirewallRule -DisplayName "SSH for Tailscale" -Direction Inbound -Protocol TCP -LocalPort 22 -RemoteAddress 100.64.0.0/10 -Action Allow
```

## 基地端配置

### SSH 密钥
`~/.ssh/id_ed25519` — 自动被 paramiko 使用，无需显式指定。

### 同步脚本
`/home/miao/.hermes/scripts/sync_taizhang.py`

特性：
- SFTP 扫描远程文档目录，过滤 `.docx/.doc/.xlsx/.xls/.pdf/.txt/.md`
- 按文件大小比较增量（比 mtime 更可靠，避免跨平台时间戳差异）
- 仅直连时有效（中继时 socket 测试失败自动跳过）
- 首次全量 ~3700 文件 / 2.5GB，局域网千兆 ~4-5 分钟

### 定时任务
- `5323ccd7cf51` "周末台账同步" — 周六+周日 12:00，no_agent，脚本 sync_taizhang.py
- `dfdd687d1890` "工作台账扫描" — 周一 9:00，wenan profile，加载 laomiao-writing-style + markitdown，扫描 ~/工作台账/

## Windows SSH 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| `No authentication methods available` | 密钥在错误位置 | 管理员账户用 `C:\ProgramData\ssh\administrators_authorized_keys` |
| `Connection timed out` | 走 DERP 中继 | 确保两台设备在同一局域网，建立 Tailscale 直连 |
| `tailscale status` 显示 relay 但已是直连 | JSON `Relay` 字段始终非空 | 用 socket 测试代替 JSON 解析 |
