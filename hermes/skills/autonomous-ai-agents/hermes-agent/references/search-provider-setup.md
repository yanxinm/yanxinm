# Search Provider Setup (China Network)

## DuckDuckGo via `ddgs` (Recommended for China)

The `web` / `search` toolsets in Hermes use the configured search provider. For environments where DuckDuckGo.com is blocked (e.g., mainland China network), the **old `duckduckgo_search` v8.1.1 package does NOT work** — it internally redirects to Bing and returns `None`/timeout.

### Working solution: `ddgs` package

```bash
# ddgs v9.11.3+ already installed — use this, NOT duckduckgo_search
from ddgs import DDGS

with DDGS() as ddgs:
    results = list(ddgs.text("query", max_results=5))
```

Key differences:
| Package | Version | Works in China? | Import |
|---------|---------|----------------|--------|
| `duckduckgo_search` | 8.1.1 | ❌ Redirects to Bing, timeout | `from duckduckgo_search import DDGS` |
| `ddgs` | 9.11.3+ | ✅ | `from ddgs import DDGS` |

### Calling via Python (sandbox or terminal)

When you need web search for the 6 task types below, prefer calling `ddgs` directly via `execute_code` or terminal rather than relying on the configured `web_search` tool, which may use a different backend:

1. **Installation tutorials** — install commands, dependency versions, compatibility
2. **GitHub project recommendations** — which repo to use, stars, activity
3. **Recent updates** — changelogs, release notes, deprecation notices
4. **Tool version changes** — breaking changes, new features between versions
5. **API or CLI parameters** — exact flags, env vars, config keys
6. **Skill still works** — check if a Hermes skill or third-party tool is maintained

### Troubleshooting

- `DuckDuckGoSearchException: return None` → The old `duckduckgo_search` package is being used. Switch to `ddgs`.
- Timeout on first request → DDGS may need a warm-up call (first query can be slow, subsequent calls are fast).
- Rate limiting → Add `sleep(1)` between queries. Free tier has no API key but rate limits.
- If `ddgs` also fails → Try with `proxies` parameter: `DDGS(proxies="socks5://127.0.0.1:1080")` if you have a proxy.
