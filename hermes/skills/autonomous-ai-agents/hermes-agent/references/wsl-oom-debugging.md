# WSL OOM 排查与预防

Gateway 进程被 OOM killer 杀死的诊断方法和预防措施。

## 诊断：进程是否被 OOM 杀死

### 关键证据链

| 日志特征 | 含义 |
|----------|------|
| 日志戛然而止，最后一行是常规 INFO（非错误） | 进程被外部强制终止，来不及写日志 |
| `gateway-exit-diag.log` 中 `gateway.exit_nonzero` 但 `sys_exc: (None, None, None)` | 进程退出时没有 Python 异常（SIGKILL） |
| 日志中没有 ERROR/CRITICAL 级别的 traceback | 不是 Python 内部错误 |

### 排查命令

```bash
# 1. 看 gateway 日志结尾
tail -20 ~/.hermes/logs/gateway.log

# 2. 看退出诊断日志的尾部（最近的条目）
tail -50 ~/.hermes/logs/gateway-exit-diag.log

# 3. 看 errors 日志
tail -50 ~/.hermes/logs/errors.log

# 4. 检查当时系统内存压力
# 日志中可以看到各进程的 RSS 占用：
# ps aux 输出的 %MEM 列 + RSS 列
```

## 主要内存大户

| 进程 | 典型 RSS | 说明 |
|------|----------|------|
| `hindsight-api --daemon` | **1.0-1.5 GB** | 嵌入模型 + 数据库，最大耗内存 |
| `hermes gateway run` | ~500 MB | 网关主进程 |
| `hermes chat` | ~300-500 MB | 交互会话 |
| `hermes-web-ui` (Node.js) | ~180-200 MB | Web管理界面 |
| PostgreSQL (hindsight) | ~120 MB (含连接) | 记忆数据库 |

## 预防措施

### 1. hindsight-api 内存调优

修改 `~/.hermes/hindsight/config.json`：

```json
{
  "idle_timeout": 60,           // 闲置60秒后退出（默认300）
  "retain_every_n_turns": 3,    // 每3轮存一次记忆（默认1）
  "auto_recall": true,          // 保持启用
  "auto_retain": true           // 保持启用
}
```

参数说明：
- `idle_timeout`：daemon 空闲多少秒后自动退出。设为 60（1分钟）比默认 300（5分钟）更激进，daemon 在 session 结束后很快释放内存。下次使用时自动重启（有短暂冷启动延迟）。
- `retain_every_n_turns`：每 N 轮对话保存一次记忆。设为 3 减少 daemon 被唤醒的频率。

**如何应用**：修改 config.json 后，杀掉当前 hindsight daemon，下次自动启动时按新配置运行：
```bash
kill $(pgrep -f hindsight-api)  2>/dev/null
```

### 2. WSL swap（最有效）

创建 `C:\Users\<用户名>\.wslconfig`：

```ini
[wsl2]
swap=4GB
```

然后执行 `wsl --shutdown` 再重新打开 WSL 终端。swap 作为安全垫，在内存峰值时允许系统换出闲置页面，避免 OOM killer 乱杀进程。

> 不设 `memory=` 硬限制（保持 WSL 默认 50% 主机内存），以免正常使用时不够用。

### 3. 减少并发进程

- 避免同时运行多个 `hermes chat` 会话
- 如果本机不常使用 hermes-web-ui，可以考虑不启动它
- Gateway 意外退出后不要反复 `run --replace`，先用 `stop` 清理旧进程

## 进程被 OOM kill 后的恢复

```bash
# 1. 释放内存
kill $(pgrep -f hindsight-api) 2>/dev/null

# 2. 重启 gateway
hermes gateway run
# 或用后台模式：
# terminal(background=true, command="hermes gateway run")

# 3. 验证
hermes gateway status
tail -5 ~/.hermes/logs/gateway.log | grep "✓"
```
