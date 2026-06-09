# 每日灾备配置详情

## Cron 任务

```bash
# 创建 cron（已存在则跳过）
hermes cron create "0 10 8 * * *" \
  --name "每日灾备" \
  --script "hermes_backup.sh" \
  --no-agent \
  --deliver weixin
```

- **时间**：每天 08:10（避开凌晨网络低谷）
- **模式**：`no_agent` — 直接跑脚本，不经过 LLM
- **投递**：结果推送到微信

## 备份仓库结构

```
~/hermes-backup/
├── .git/                  # Git 仓库（remote → yanxinm/yanxinm）
├── .gitignore             # 排除嵌入仓库（guizang-ppt-skill）
├── hermes/                # 备份文件
│   ├── config/
│   ├── skills/
│   ├── scripts/
│   ├── cron/
│   ├── memories/
│   └── hindsight/
└── hermes-backup-*.tar.gz # 本地 tar 兜底
```

## Git 代理配置

基地上已配置全局 `insteadOf`：

```bash
git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"
```

所有 `git clone/fetch/push https://github.com/...` 自动走 ghproxy 镜像。

## SSH 密钥

基地专属密钥（用于 git push）：

```
~/.ssh/id_ed25519        # 私钥
~/.ssh/id_ed25519.pub    # 公钥 → 添加到 GitHub Settings
```

SSH 配置文件 `~/.ssh/config`：

```
Host github.com
    Hostname ssh.github.com
    Port 443
    User git
```

> ⚠️ 当前网络环境（2026-06-08）SSH over 443 仍被 DPI 阻断。HTTPS + ghproxy 代理对 git push 也不可靠。因此脚本以本地 tar 为主，git push 为可选增强。

## 恢复步骤

```bash
# 从本地 tar 恢复
tar -xzf ~/hermes-backup/hermes-backup-202606082233.tar.gz -C /tmp/restore/

# 从 GitHub 恢复（网络可用时）
git clone git@github.com:yanxinm/yanxinm.git ~/hermes-backup-restore/
```
