# Hotel Search on Chinese OTAs — Limitations

## Session Log: Guizhou Trip Hotel Search (2026-06-03)

### What We Tried

Searching for hotels in small Chinese cities (Maotai/茅台镇, Kaili/凯里, Zunyi/遵义, Huangguoshu/黄果树) with specific criteria:
- New hotels (opened ≤3 years)
- Parking available
- Twin beds ≥1.35m width
- 4 rooms total (1 king + 3 twin)

### What FAILED

1. **web_search with general queries** — Returns mostly alcohol ads, travel agency packages, and spam. Search engines over-index on "茅台" (liquor) over "茅台镇" (town). Very little structured hotel data.

2. **Browser → Ctrip (携程)** — Search URL redirected to a generic results page. Ctrip's hotel search page requires login for most interactions. Typing "茅台镇" in search box triggered a login wall.

3. **site-specific searches** (site:trip.com, site:ctrip.com) — Still returned mostly irrelevant results. Chinese OTAs don't expose hotel data well to external search engines.

### What PARTIALLY WORKED

- TripAdvisor (cn.tripadvisor.com) listed some hotels but information was outdated
- Finding individual hotel names (Atour X, Hilton Garden Inn) then searching for those specific names returned their pages

### Recommended Alternative

For hotel research in Chinese cities, especially small ones with specific criteria, web_search and browser tools are inefficient. The user is better off using:
- **Ctrip / Meituan / Qunar mobile app** — native filtering by opening date, parking, bed size
- **Xiaohongshu (小红书)** — real user reviews with hotel photos, but also behind login wall

### When to Use This Reference

If the agent finds itself doing 5+ web_search calls for hotels with zero useful results, STOP and tell the user directly: "hotel search on Chinese platforms via web tools is ineffective — use your phone app with these filter criteria instead." Output the filter criteria as a checklist.
