# Memory Capacity Management

The built-in memory system has a **2,200 character limit** across all MEMORY.md entries. This is a hard cap enforced by the memory tool — attempts to add beyond it are rejected with "Memory at X/2,200 chars. Adding this entry would exceed the limit."

## Strategies

### 1. Replace Before You Add

When adding new info, **always replace** an existing low-value entry rather than appending. Use `memory(action='replace', old_text=...)`.

Good candidates for replacement:
- Completed-task artifacts ("fixed bug X", "submitted PR Y")
- Session outcomes or phase completions
- Outdated or superseded info (e.g., old provider names)

Bad candidates for replacement:
- User preferences (never replace corrections or formatting rules)
- Environment facts (API keys, paths, installed tools)

### 2. Use hindsight_retain for Overflow

The `hindsight_retain` tool stores facts in the hindsight database which has **no character limit**. Use it for:
- API keys and provider configs
- User preferences and workflow rules
- Environment quirks and tool installation notes
- Project conventions and code style preferences

Fact density preference: `hindsight_retain` > `memory` tool.

### 3. Prune Aggressively

Entries that should NOT be in memory:
- Task progress logs ("Phase 1 done", "PR #42 submitted")
- Timestamps of completed actions
- File counts or directory listings
- Information that can be re-discovered from session_search or hindsight_recall

Each memory entry should answer: "Will this prevent the user from having to remind me?" — if no, it doesn't belong.

### 4. Keep Entries Compact

Preferred formats:
- **Bullet lists** over full sentences: `Models: doubao, deepseek, minimax` > `The models currently configured are doubao, deepseek, and minimax`
- **Key-value pairs**: `Memory limit: 2200 chars`
- **Abbreviate where unambiguous**: `GBrain: 724 docx imported` > `GBrain knowledge base: 724 working ledger documents have been converted from docx format and imported as markdown chunks`

### 5. Know the Limits

| Store | Limit | Duration | Purpose |
|-------|-------|----------|---------|
| MEMORY.md | 2,200 chars | Permanent | Facts that prevent re-correction |
| USER.md | 1,375 chars | Permanent | User identity and preferences |
| hindsight_retain | Unlimited | Permanent | Overflow + rich metadata |
| Session search | Unlimited | 90 days | Task progress, temporary state |

## When It Fills Up

The memory tool returns this error:
```
Memory at 2,162/2,200 chars. Adding this entry would exceed the limit.
Replace or remove existing entries first.
```

Recovery steps:
1. Identify stale entries via `memory(action='list')` — look for completed tasks, old version numbers, superseded facts
2. Replace the stalest entry with new content
3. If multiple entries are stale, `memory(action='remove')` the weakest ones
4. If no old entries can be removed, fall back to `hindsight_retain` for the new information
