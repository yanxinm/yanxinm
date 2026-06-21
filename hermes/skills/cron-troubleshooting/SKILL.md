---
name: cron-troubleshooting
description: Cron 任务故障排查与修复 — 灾备脚本、自检脚本、watchdog 等定时任务的常见故障模式和修复方法
tags: [cron, troubleshooting, backup, watchdog, automation]
---

# Cron 任务故障排查

## 核心原则

**灾备/备份类 cron 任务一旦报错，必须主动查修，不等用户提醒。** 发现问题直接修，修完验证通过再汇报。

## 常见故障模式

### 1. 脚本超时（最常见）

**症状**：cron 输出显示 "timed out" 或 exit code 非 0

**根因**：
- `set -euo pipefail` 太严格，单个命令失败就中断
- `rm -rf` 重建目录 + `rsync --delete` 同步大文件耗时过长
- tar 压缩大文件超时

**修复方案**：
1. 去掉 `set -e`（不再因单个命令失败而中断）
2. 去掉 `rm -rf` 重建，改为增量同步（rsync 不带 --delete）
3. 所有可能失败的步骤加 `|| true`
4. 适当增加 cron 超时时间

**验证**：手动运行脚本确认能在超时前完成

### 2. 网络连接失败

**症状**：git push 被拒、API 调用 401/502

**根因**：
- GitHub 全墙（SSH/HTTPS git 不可用，仅 HTTP）
- API key 过期
- Tailscale DERP 中继不稳定

**修复方案**：
- 灾备走本地 tar 而非 GitHub
- API key 检查 `~/.hermes/.env`
- 网络问题用 curl 测试连通性

### 3. 服务进程僵死

**症状**：端口监听但无响应

**修复方案**：kill 掉重启，加 watchdog 脚本自动检测

### 4. `no_agent` 脚本缺 Python 依赖

**症状**：cron 输出显示 `ModuleNotFoundError: No module named 'xxx'`，exit code 1

**根因**：`no_agent` 模式用系统 python3 运行脚本，但依赖包未安装在对应的 venv 中。脚本 shebang 可能是 `#!/usr/bin/env python3`，解析到的 python 不一定带所有第三方包。

**排查**：
1. 读错误日志确认缺失的模块名
2. 确认 cron job 的 `script` 字段指向哪个文件
3. 用 venv 的 python 安装：`python3 -m pip install <package>`（确保用的是 Hermes venv 的 python）
4. 验证：`python3 -c 'import <module>; print("OK")'`

**防丢**：在脚本同级目录创建 `requirements-<name>.txt` 记录依赖，方便环境重建时一键安装。

## 排查流程

1. `cronjob action=list` 找到 job_id
2. 读取最近输出日志 `~/.hermes/cron/output/<job_id>/`
3. 定位错误类型（超时/连接/权限/缺依赖）
4. 修复脚本或配置
5. 手动验证修复后脚本能正常运行
6. 汇报修复结果