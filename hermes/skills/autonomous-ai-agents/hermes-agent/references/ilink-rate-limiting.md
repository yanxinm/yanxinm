# iLink 微信桥接限流说明

## 症状

Cron job 运行成功（`last_status: ok`），但微信推送失败，gateway 日志出现大量：

```
[Weixin] rate limited for o9cq801d; backing off 3.0s before retry
...
[Weixin] send failed to=o9cq801d: iLink sendmessage rate limited: ret=-2 errcode=None errmsg=rate limited
```

Cron job 状态显示：
```
last_delivery_error: delivery error: Weixin send failed: iLink sendmessage rate limited
```

## 触发条件

iLink 的速率限制在以下情况下易触发：

1. **消息过长** — 超过 iLink 单条消息长度限制
2. **多条消息短时间内密集推送** — cron job 输出包含多个段落/换行符，被切分成多条消息
3. **与其他消息发送同时发生** — 其他会话也在推送到同一用户

典型场景：cron job 产出了详细 Markdown 报告（5-20行），iLink 将其拆分为多条消息发送，超过每秒消息数限制。

## 日志特征

从 gateway.log 观察：

```
08:32:33 → rate limited, backoff 3s
08:32:36 → rate limited, backoff 3s  (首次重试)
08:32:39 → rate limited, backoff 3s
08:32:42 → rate limited, backoff 3s
08:32:46 → send failed (第一轮 4 次重试耗尽)
08:32:56 → rate limited, backoff 3s  (系统自动第二轮重试)
08:32:59 → rate limited, backoff 3s
08:33:02 → rate limited, backoff 3s
08:33:05 → rate limited, backoff 3s
08:33:08 → send failed (第二轮耗尽，彻底放弃)
```

限流窗口约为 30-60秒，期间所有发往同一用户的消息均被拒绝。

## 解决方案

### 1. 缩短 cron job 输出
修改 cron job 的 prompt/script，限定输出长度：
- 全部正常时：一句话 `✅ 每日自检：一切正常`
- 有更新时：简要列出更新项，不超过 3-5 行
- 避免详细 Markdown 表格和大段描述

### 2. 使用 no_agent 脚本
对简单的自检任务，改用 `no_agent: true` + `script` 模式，仅在有更新时推送：
```yaml
script: check_updates.sh
no_agent: true
script_gate: |
  if [ -z "$HAS_UPDATES" ]; then
    echo "NO_OUTPUT"
    exit 0
  fi
```

### 3. 紧急恢复
如果推送失败但 cron job 执行成功，手动运行一次即可恢复投递：
```bash
hermes cron run <job_id>
```
手动调用通常不受限流影响（单次消息），可以正常推送。
