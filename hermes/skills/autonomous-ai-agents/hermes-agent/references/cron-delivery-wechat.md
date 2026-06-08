# Cron Delivery via WeChat (iLink) — Rate Limiting & Best Practices

## The Problem

Cron job outputs delivered to WeChat via the iLink bridge are subject to aggressive rate limiting. When a job's output is too long or multiple jobs fire close together, iLink returns `rate limited` errors and the delivery is silently dropped.

The cron job itself reports `last_status: ok` but `last_delivery_error` contains:

```
delivery error: Weixin send failed: iLink sendmessage rate limited: ret=-2 errcode=None errmsg=rate limited
```

The job's output is saved to `~/.hermes/cron/output/<job_id>/` but never reaches the user.

## Symptoms

- Cron job shows `last_status: ok` with `last_delivery_error: rate limited`
- Gateway log shows repeating pattern:
  ```
  [Weixin] rate limited for USERID; backing off 3.0s before retry
  ... (4 retries, then)
  [Weixin] send failed to=USERID: iLink sendmessage rate limited
  ```
- Output file exists locally but user never saw the message

## Rate Limit Characteristics

- **Sliding window (20-30 min)**: Once triggered, subsequent sends may also fail even tens of minutes later
- **Message length**: Longer outputs are more likely to trigger the limit
- **Frequency**: Multiple cron deliveries within a 30-minute window compound the problem

## Mitigation Strategies

### 1. Merge adjacent cron jobs

Instead of separate cron jobs that each push to WeChat independently, combine them:

- ❌ Two jobs: "每日自检" @ 8:30 + "每日待办提醒" @ 9:00 = 2 delivery attempts, each may hit limits
- ✅ One job: "每日简报" @ 8:30 = 1 concise delivery

### 2. Keep output extremely short (3-6 lines max)

**Bad** (triggered rate limiting):
```
Detailed markdown report with tables, code blocks, multiple sections, version details, skills list...
```

**Good** (passes every time):
```
✅ 每日简报 5/15(周五)
• Hermes v0.13.0，全部最新
• 🔴 今日：9:15约丁剑、培训
• 🟡 近期待办：5/20/22/27培训 · 5/28湖州调研
• 📌 跟进：抖音客户池、动物园合同
```

### 3. Cron prompt directive

In the cron job's prompt, add explicit length constraints:

```
最终输出格式（仅限3-5行，务必精简）：
注意：
- 务必简短！总量不要超过6行
- 全部正常时不要问用户要不要更新，直接推送结果
- 版本和技能如无更新，只写「全部最新」四个字
- 不要用表格——用行内格式
```

### 4. Use `no_agent` scripts for silent operations

For backup-style jobs that don't need LLM analysis:

```yaml
deliver: local       # Save to file only, no WeChat push
no_agent: true       # Run shell script, not LLM
```

If you want notification:
```yaml
deliver: origin      # Push result to the user's home channel
no_agent: true       # Script output becomes the message
```

### 5. Space non-mergeable jobs apart

If jobs can't merge, space them at least 60 minutes apart (not 30).

## Delivery Mode Reference

| `deliver` | Behavior |
|-----------|----------|
| `origin` | Sends output back to the originating chat (WeChat). User sees the result. |
| `local` | Output saved to `~/.hermes/cron/output/<job_id>/<timestamp>.md` only. **User gets no notification.** |

⚠️ **Pitfall**: Jobs with `deliver: local` that use `|| true` to mask script errors will never alert the user.

## Testing Delivery

`cronjob(action='run')` schedules a run on the scheduler's next tick. **This method has a known issue**: delivery can silently fail — output saved locally but never sent to WeChat. The status shows `last_delivery_error: null` misleadingly.

**Reliable test**: Use `send_message` directly:

```
send_message(target="weixin", message="✅ 测试：Cron消息格式测试")
```

This bypasses the scheduler and tests the real iLink delivery path.

## Checking Delivery History

```bash
# Check cron delivery errors
grep "delivery error\|rate limited" ~/.hermes/logs/agent.log

# Check gateway outbound
grep "weixin.*send" ~/.hermes/logs/gateway.log

# Check cron output files (even if delivery failed)
ls -la ~/.hermes/cron/output/<job_id>/
cat ~/.hermes/cron/output/<job_id>/*.md
```

## Recovery

If a cron job's delivery failed but the output is correct (verified from local file), manually forward via `send_message`.

## Real-World Example

A user had two cron jobs at 8:30 (self-check) and 9:00 (todo reminder). Both produced detailed output (~500-2000 chars). Both were rate limited.

**Fix:**
1. Merged into one "每日简报" at 8:30
2. Output shortened to 4-5 lines max
3. Test delivery confirmed successful with `last_delivery_error: null`

## See Also

- `references/github-backup-china-ssh.md` — China network workarounds for GitHub
- `references/cron-date-gating.md` — date-gated cron patterns
