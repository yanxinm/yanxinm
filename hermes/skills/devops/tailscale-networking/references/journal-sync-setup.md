# 工作台账同步架构

笔记本（Ethan）→ 基地（M710q）的文档同步方案，用于定时任务自动拉取工作台账。

## 架构

```
笔记本 E:/百度云同步盘/工作台账/
    │  SSH + SFTP (Python paramiko)
    │  仅周末局域网直连时生效
    ▼
基地 ~/工作台账/ (本地副本)
    │  周一 LLM 扫描
    ▼
timeline 推送简报
```

## 核心组件

| 组件 | 路径 | 说明 |
|------|------|------|
| 同步脚本 | `~/.hermes/scripts/sync_taizhang.py` | Python SFTP 增量同步 |
| Shell 包装 | `~/.hermes/scripts/sync_taizhang.sh` | 调用 Python 脚本 |
| 定时任务 | cron `5323ccd7cf51` | 周六+周日 12:00 |
| 扫描任务 | cron `dfdd687d1890` | 周一 9:00，加载 laomiao-writing-style + markitdown |

## 同步逻辑

1. socket 直连检测（`connect(100.86.148.56, 22)`，5 秒超时）
2. SSH 连接 → SFTP 会话
3. 递归列出远程文档（`.docx/.doc/.xlsx/.xls/.pdf/.txt/.md`）
4. 对比本地大小/mtime，增量下载
5. 统计输出

## 笔记本端依赖

- Windows OpenSSH Server（已安装，通过"可选功能"添加）
- 密钥配置：`C:\ProgramData\ssh\administrators_authorized_keys`
- Tailscale 客户端（已安装，同 tailnet）

## 文件规模

- 远程：3726 个文档，2.49 GB（排除 PPT 后）
- 首次全量同步：局域网千兆 ≈ 3-4 分钟
- 后续增量：通常 < 50 MB

## 踩过的坑

1. **Samba 方案不可行**：Tailscale DERP 中继不转发 TCP 445
2. **rsync 依赖 Windows**：笔记本 OpenSSH 不带 rsync，改用 paramiko SFTP
3. **`tailscale status --json` Relay 字段误导**：直连时也非空，改用 socket 检测
4. **Windows 管理员密钥路径**：不在 `~/.ssh/authorized_keys`，在 `C:\ProgramData\ssh\administrators_authorized_keys`
