# Watchdog 脚本迁移：笔记本 → 基地案例

## 背景

基地（M710q Ubuntu）是固定的 Linux 主机，老缪的笔记本（Ethan, Win + WSL）是移动工作站。一些 cron 脚本是从笔记本复制到基地的，但保留了笔记本的硬编码路径。

## 故障现象

watchdog.sh 每 2 分钟 cron 执行失败（`last_status: error`），日志：

```
/home/miao/.hermes/scripts/watchdog.sh: 第 31 行： cd: /home/yanxin/Hermes-Agent: 没有那个文件或目录
[2026-06-22 08:07:45] ⚠️ Hermes Gateway 未运行，正在重启...
[2026-06-22 08:07:45] ❌ 无法进入 Hermes-Agent
```

## 旧脚本问题

```bash
# 笔记本环境 —— 直接 hermes gateway run，无 systemd
cd /home/yanxin/Hermes-Agent || { log "❌ 无法进入 Hermes-Agent"; exit 1; }
source venv/bin/activate
nohup hermes gateway run --replace >> /home/yanxin/.hermes/logs/gateway.log 2>&1 &

# 还检查笔记本专属的 TDAI Gateway
cd /home/yanxin/.memory-tencentdb || ...
```

## 基地环境差异

| 项目 | 笔记本 | 基地 |
|------|--------|------|
| 用户名 | `yanxin` | `miao` |
| Hermes 启动方式 | `hermes gateway run` (direct) | `systemctl start hermes-gateway` (systemd) |
| TDAI Gateway | 独立进程 + tsx | `hermes-tdai.service` |
| 日志路径 | `/home/yanxin/.hermes/logs/` | `/home/miao/.hermes/logs/` |

## 修复方案

### 1. 路径统一
用 `grep -n '/home/' watchdog.sh` 找出所有硬编码路径，全部改为 `$HOME` 或基地路径。

### 2. 进程管理方式改造
从直接拉进程改为 systemd 管理：

```bash
SERVICE="hermes-gateway"
if ! systemctl is-active --quiet "$SERVICE" 2>/dev/null; then
  systemctl restart "$SERVICE" 2>/dev/null || {
    # 备用：直接拉起
    export PATH="/home/miao/.local/bin:/home/miao/.hermes/venv/bin:$PATH"
    cd /home/miao && nohup hermes gateway run --replace >> /home/miao/.hermes/logs/gateway.log 2>&1 &
  }
fi
```

### 3. 移除不适用模块
笔记本上的 TDAI Gateway 是用 `node --import tsx/esm` 手动启动的，基地上有 systemd 管理，不需要 watchdog 监控。

### 4. 验证
```bash
bash -n watchdog.sh          # 语法检查通过
bash watchdog.sh             # 运行静默退出（Gateway 正常时无输出）
exit: 0
```
