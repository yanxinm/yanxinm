# Date-Gated Cron Jobs (Last Working Day Pattern)

Standard cron cannot express "last working day of month" directly. This pattern gates agent execution by running on a date range and filtering with a script.

## The Pattern

```
Schedule: 0 12 28-31 * *     (runs on 28th-31st of every month)
Script:   is_last_working_day.py
  ↓ If NOT_TODAY → agent skips (checks Script Output)
  ↓ If LAST_WORKING_DAY → agent proceeds with task
```

The agent always fires on schedule (28th-31st), but the script output tells it whether to proceed. Max 4 wasted invocations per month vs running daily.

## The Gate Script

Save as `~/.hermes/scripts/is_last_working_day.py`:

```python
#!/usr/bin/env python3
"""Check if today is the last working day of month/quarter/year."""
import calendar
from datetime import date, timedelta

def last_working_day(ref_date):
    last_day = ref_date.replace(
        day=calendar.monthrange(ref_date.year, ref_date.month)[1]
    )
    while last_day.weekday() >= 5:  # Mon=0..Sun=6
        last_day -= timedelta(days=1)
    return last_day

today = date.today()
lwd = last_working_day(today)

if today != lwd:
    print("NOT_TODAY")
else:
    print(f"LAST_WORKING_DAY|{today.isoformat()}|month")
    if today.month in [3, 6, 9, 12]:
        print(f"LAST_WORKING_DAY|{today.isoformat()}|quarter")
    if today.month == 12:
        print(f"LAST_WORKING_DAY|{today.isoformat()}|year")
```

## Cron Schedule Templates

| Task | Cron Expression | Script Output Check |
|------|----------------|---------------------|
| Monthly report | `0 12 28-31 * *` | `LAST_WORKING_DAY\|month` |
| Quarterly report | `0 12 28-31 3,6,9,12 *` | `LAST_WORKING_DAY\|quarter` |
| Annual report | `0 12 28-31 12 *` | `LAST_WORKING_DAY\|year` |

## Prompt Pattern

Include in the cron job prompt:

```
【Step 1】Check Script Output
Read the "Script Output" section. If it contains "NOT_TODAY" or doesn't contain
the expected flag, respond with "Today is not the right day, skipping." and stop.

【Step 2+】Proceed with task only if the condition matched.
```

## Time Zone/Chinese Calendar

Cron uses the system timezone. Ensure it matches the user's locale (`Asia/Shanghai`). For Chinese holiday handling (holidays that fall on weekdays), use `chinese_calendar`:

```python
import chinese_calendar as cc
if cc.is_workday(today):  # True for 调休工作日, False for 法定假日
    ...
```

See also: [chinese_calendar on PyPI](https://pypi.org/project/chinese_calendar/)

## Batch Creation Pattern

When creating multiple cron jobs (e.g., weekly + monthly + quarterly + annual), use this pattern:

### Mechanical Jobs (no_agent=True)

For repetitive data-processing tasks (file scans, git backup, DB cleanup):

```
cronjob_create(
    name="每周台账扫描",
    schedule="0 12 * * 5",       # Friday noon
    script="weekly_scan.py",      # Python/bash script
    no_agent=true,                # Zero token cost
    deliver="origin"              # Push result to WeChat
)
```

The script must be in `~/.hermes/scripts/` and be self-contained (all logic inline). Output is delivered verbatim.

### Agent-Driven Jobs (date-gated)

For tasks requiring LLM reasoning (report generation, analysis, summarization):

```
cronjob_create(
    name="季度工作报告",
    schedule="0 12 28-31 3,6,9,12 *",  # Quarter-end range
    script="is_last_working_day.py",     # Gate script
    enabled_toolsets=["terminal", "file", "session_search"],
    deliver="origin"
)
```

**Prompt structure for agent-driven jobs** — include all of:
1. **Gate check**: "Read Script Output. If NOT_TODAY or missing expected flag, skip."
2. **Data gathering**: Specific commands to run, files to read, searches to perform
3. **Knowledge base queries**: GBrain recall commands with placeholder dates
4. **Style reference**: Which historical documents to consult for writing style
5. **Output format**: Explicit template with sections (headers, tables, signatures)
6. **Fallback**: What to do if data is unavailable

### Recommended enabled_toolsets for Report Jobs

| Toolset | Why needed |
|---------|-----------|
| `terminal` | Run date/disk/gbrain commands, execute scripts |
| `file` | Read reference documents from filesystem |
| `session_search` | Search past conversations for context |
| `web` | Optional—verify facts, research current events |

### Avoiding Duplicate Work

When multiple cron jobs share the same gating script (e.g., monthly + quarterly report both check `is_last_working_day.py`), they will both fire on the last working day of a quarter. This is fine — their prompts differ so they produce different outputs. Just be aware of potential overlap.

### Testing Pattern

Before scheduling, verify the cron fires correctly:
1. Run the script manually: `python3 ~/.hermes/scripts/<script>`
2. Call `cronjob(action='run', job_id='...')` to trigger an unscheduled run
3. Check delivery: the output arrives in your messaging platform immediately

## Pitfalls

### Same-day collisions — The last working day of a quarter is also the last working day of the month. Both jobs will fire on the same day. Ensure prompts don't conflict.
### Holiday handling — This script only excludes weekends (Sat/Sun). For Chinese public holidays that fall on weekdays, the script treats them as working days. If strict holiday awareness is needed, use `chinese_calendar` library.
### Resource waste — The agent fires on 28th-31st even if the last working day is earlier. For months where the 31st is the last day, at most 4 fires/month. Acceptable for agent-driven tasks.
### Token cost — agent-driven jobs consume LLM tokens on every fire. If the script gating fails (e.g., TODAY flag misinterpreted), the agent still runs. Keep prompts tight and gate checks explicit.
### Cron state persistence — Cron jobs survive gateway restarts and machine reboots. To pause: `cronjob_pause(job_id)`. To remove: `cronjob_remove(job_id)`.
