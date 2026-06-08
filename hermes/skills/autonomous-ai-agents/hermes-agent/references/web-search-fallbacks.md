# Web Search Fallbacks (Domestic Network)

When `web_search` (ddgs/Yahoo backend) fails with `ConnectError`, `Errno 101`, or consistent timeouts:

## Symptom Pattern

- `web_search` returns `error: "DuckDuckGo search failed: ConnectError"`
- `web_extract` returns `"DuckDuckGo (ddgs) is a search-only backend"`
- Multiple retries with different queries all fail identically
- This is **not** a quota/rate-limit issue — the backend itself is unreachable

## Circuit-Break: Don't Keep Retrying

After 3 consecutive failures, the backend is dead. Stop retrying `web_search` and switch strategies.

## Fallback: curl + Bing (Domestic China)

Bing is accessible from domestic networks. Search via command line:

```bash
curl -s -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  "https://cn.bing.com/search?q=$(echo '查询关键词' | python3 -c 'import sys,urllib.parse; print(urllib.parse.quote(sys.stdin.read().strip()))')" 2>/dev/null
```

To parse the HTML response for titles/URLs:
```bash
curl -s -L -A "Mozilla/5.0" "https://cn.bing.com/search?q=..." 2>/dev/null | python3 -c "
import sys, re, html
c = sys.stdin.read()
# Extract search result links (adjust selectors for Bing's DOM)
links = re.findall(r'<a[^>]*href=\"(https?://[^\"]+)\"[^>]*>(.*?)</a>', c)
for url, title in links[:10]:
    t = re.sub(r'<[^>]+>', '', title).strip()
    if t and len(t) > 5 and 'bing.com' not in url:
        print(f'{html.unescape(t)}')
        print(f'  {url}')
"
```

Note: Bing may redirect to `cn.bing.com` — use that URL directly for China.

## Fallback: Archive Sites for Known Content

For Chinese investigative journalism, specific authors, or long-form articles that may have been removed:
- `xitalk` (wwyy.org) — archives many deleted WeChat articles
- `chinamediaproject.org` — Chinese media analysis

```bash
# Fetch archived article
curl -s -L -A "Mozilla/5.0" "https://wwyy.org/..." 2>/dev/null | python3 -c "
import sys
from html.parser import HTMLParser
# Parse and extract article content
..."
```

## Fallback: Direct URL Fetch

If you know the exact URL (from a search snippet or prior knowledge):
```bash
curl -s -L -A "Mozilla/5.0" "https://example.com/article" 2>/dev/null
```

## Fallback: Model Knowledge (Last Resort)

When ALL network fetch methods fail, use the model's training knowledge with explicit honesty marking. Say "Based on available knowledge (not live search)" and label uncertain claims. This is acceptable for well-known public figures, major events, and widely-documented techniques — the training data contains verified facts about them. Never fabricate quotes, specific data points, or claims of fact.
