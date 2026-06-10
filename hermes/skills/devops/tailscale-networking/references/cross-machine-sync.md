# 跨机器文件同步方案（基地 ↔ 笔记本）

## 背景

Hermes Agent 从笔记本（Ethan, Windows）迁移到基地（M710q, Ubuntu）后，
工作台账文件夹（`E:\百度云同步盘\工作台账`）仍在笔记本上。
需要在基地建立本地副本，每周从笔记本增量同步。

## 网络环境

- 两台设备通过 Tailscale 连接，走 DERP 中继（无法直连）
- DERP 延迟 400ms–1.5s（SFO relay）
- TCP 连接在 DERP 中继下不稳定

## 已探索方案

| 方案 | 状态 | 原因 |
|------|------|------|
| Samba 挂载 (port 445) | ❌ 放弃 | SMB 对 DERP 延迟零容忍 |
| SSH + rsync (port 22) | ❌ 不通 | TCP 在 DERP 层面全阻断（防火墙关也不行） |
| tailscale file cp | ⏳ 待测试 | Tailscale 自有协议，可能绕过 TCP 问题 |
| Python HTTP (port 18888) | ❌ 不通 | TCP 层面已阻断 |
| 基地本机百度云客户端 | ❌ 放弃 | Linux 客户端残废 |

## 笔记本 OpenSSH Server 安装记录

2026-06-09 在笔记本（Ethan, Windows 11）安装 OpenSSH Server：

1. `Add-WindowsCapability` 命令行卡死 → 改用设置界面安装
2. 路径：Win+I → 系统 → 可选功能 → 查看功能 → "OpenSSH 服务器"
3. 安装后需重启（内核驱动），重启后手动启动服务：
   ```powershell
   Set-Service -Name sshd -StartupType Automatic
   Start-Service sshd
   ```
4. 验证监听：`netstat -an | findstr ":22 "` 应输出 `TCP 0.0.0.0:22 LISTENING`

## 笔记本当前防火墙规则

```powershell
# 已添加
New-NetFirewallRule -DisplayName "SMB for Tailscale" -Direction Inbound -Protocol TCP -LocalPort 445 -RemoteAddress 100.64.0.0/10 -Action Allow
New-NetFirewallRule -DisplayName "SSH for Tailscale" -Direction Inbound -Protocol TCP -LocalPort 22 -RemoteAddress 100.64.0.0/10 -Action Allow

# ⚠️ 未尝试但建议的规则（网卡级放行，可能绕过 DERP IP 匹配问题）：
New-NetFirewallRule -DisplayName "Tailscale All Inbound" -Direction Inbound -InterfaceAlias "Tailscale" -Action Allow
```

## 基地端已准备

- cifs-utils 已安装
- 挂载点 `/mnt/ethan_taizhang` 已创建
- 本地副本 `/home/miao/工作台账/` 已创建
- 同步脚本 `/home/miao/.hermes/scripts/sync_taizhang.sh` 已写（依赖 Samba/SSH）
- 扫描脚本 `/home/miao/.hermes/scripts/weekly_scan.py` 已重写为本地路径版
- 定时任务 `dfdd687d1890` prompt 已更新为 `/home/miao/工作台账/`

## 待决

- DERP 层面 TCP 阻断的根本原因和解决方案
- `tailscale file cp` 是否可作为替代传输方式
- 笔记本侧 `-InterfaceAlias "Tailscale"` 防火墙规则是否有效（尚未测试）
