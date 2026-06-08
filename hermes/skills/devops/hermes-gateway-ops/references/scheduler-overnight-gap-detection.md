# 定时调度器过夜停顿检测模式

## 问题

Hermes Cron 调度器在凌晨可能停止响应，导致凌晨定时任务（凌晨3点备份等）被遗漏。用户直到早上检查才会发现。

**典型症状**：

```
# 灾备 cron job 状态
last_run_at: 2026-05-22T03:00:18    ← 上次正常运行
next_run_at: 2026-05-25T03:00:00    ← 跳过了5/23和5/24的3:00
```

实际上调度器在凌晨 01:15 就停止了，错过 2 个备份窗口。

## 检测方法

### 方法1：对比 last_run_at 与今天

```bash
hermes cron list | grep "每日灾备\|last_run_at"
```

如果 `last_run_at` 日期不是昨天或今天，说明有跳过。

### 方法2：检查 watchdog 进程输出连续性

watchdog 每2分钟跑一次，如果输出目录中断超过5分钟：

```bash
# 检查最近10个watchdog输出文件的间隔
ls -t ~/.hermes/cron/output/4a134f589e91/ | head -10
```

若文件时间戳之间有超过5分钟的间隙，说明调度器在那段时间停止了。

### 方法3：检查调度器进程存活时间

```bash
ps -o pid,lstart,etime,cmd -p $(pgrep -f "hermes.*gateway" | head -1)
ps -o pid,lstart,etime,cmd -p $(pgrep -f "hermes.*cron\|scheduler" | head -1) 2>/dev/null
```

如果调度器进程的启动时间早于某次跳跃，说明调度器进程本身存活但未调度任务——这可能是 timer 队列问题。

## 常见停顿原因

| 原因 | 特征 | 解决方案 |
|------|------|---------|
| WSL 进程被宿主机挂起（电源管理） | 凌晨时间段整段缺失 | 关闭 Windows 的 USB/硬盘节能，检查 WSL 电源策略 |
| Gateway OOM | 调度器是 Gateway 子进程，OOM 后子进程也被杀 | `watchdog.sh` 检测 Gateway 健康；加大 swap |
| SSH 连接卡住（备份脚本内） | watchdog 正常，但 cron 调度器线程阻塞 | 给备份脚本加超时 `GIT_SSH_COMMAND="ssh -o ConnectTimeout=10"` |
| 宿主机睡眠/休眠 | 整段缺失，从凌晨到用户起床后才恢复 | 确保 Windows 不进入睡眠（电源设置 → 从不睡眠） |

## 加固建议

### 选项A：将自动灾备时间改到可靠时段

当前凌晨3点容易错过。改到每日简报（08:30）之前的 **08:00**，此时调度器大概率已重新激活：

```bash
hermes cron schedule set job_id=efb38b0f36c1 schedule="0 8 * * *"
```

### 选项B：调度器健康自检

在 `watchdog.sh` 中增加检测，如果调度器停止超过10分钟则重启 Gateway：

```bash
# 在 watchdog.sh 中补充
LAST_WD=$(ls -t ~/.hermes/cron/output/4a134f589e91/ 2>/dev/null | head -1)
if [ -n "$LAST_WD" ]; then
    LAST_TS=$(date -d "$(echo "$LAST_WD" | sed 's/\.md$//' | tr '_' ' ')" +%s 2>/dev/null)
    NOW_TS=$(date +%s)
    GAP=$((NOW_TS - LAST_TS))
    if [ "$GAP" -gt 600 ]; then  # 超过10分钟
        echo "⚠️ 调度器疑似停止（上次watchdog距今${GAP}秒），正在重启Hermes Gateway..."
        cd /home/yanxin/Hermes-Agent && source venv/bin/activate
        hermes gateway run --replace
    fi
fi
```

### 选项C：双重保障——在Windows宿主机上设置备用定时任务

WSL内的调度器不可靠时，用Windows任务计划程序触发WSL命令：

```
操作: 启动程序 "C:\Windows\System32\wsl.exe"
参数: bash -lc 'source ~/Hermes-Agent/venv/bin/activate && bash ~/.hermes/scripts/hermes_backup.sh'
触发器: 每天上午8:30
```

## 恢复已丢失的备份

如果某天自动备份未执行，手动运行一次即可（不会丢失数据，因为备份脚本是状态快照而非增量日志）：

```bash
bash ~/.hermes/scripts/hermes_backup.sh
```

验证：

```bash
cd ~/yanxinm && git log --oneline -3
```
