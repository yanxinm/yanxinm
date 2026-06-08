---
name: chinese-ecommerce-research
description: Research product prices, specs, and availability on Chinese e-commerce platforms (JD.com, Taobao/Tmall, Pinduoduo). Covers anti-bot countermeasures, alternative data sources, and cross-platform price comparison workflows.
triggers:
  - User asks to search/find products on JD/京东, Taobao/淘宝, Tmall/天猫, Pinduoduo/拼多多
  - User asks for prices, rankings, or product comparisons on Chinese platforms
  - User mentions 比价, 最低价, 排行榜, 多少钱, or specific product SKUs
  - User mentions any Chinese e-commerce platform name + a product to search
  - ⚠️ CRITICAL: If you find yourself about to call browser_navigate to jd.com / taobao.com — STOP. Load this skill FIRST. JD browser scraping is a known dead-end (see references/jd-scraping-pitfalls.md).
---
# ⛔ FIRST: Why You MUST Load This Skill BEFORE Touching JD.com

**Lesson from 2025-06-03 session**: Agent spent 15+ tool calls trying to scrape JD.com with browser tools (browser_navigate, browser_click, browser_console, browser_vision, curl, web_search). Every single browser-based approach was blocked by JD's anti-bot wall. Final result was obtained from third-party deal sites via web_search — which is what this skill tells you to do in step 1.

**The full waste path**: browser → search blocked → direct URL blocked → product page shows login wall → price API times out → mobile redirects to app → smzdm CAPTCHA → finally settled on web_search against deal sites. All of this is AVOIDABLE by loading this skill first.

# Chinese E-Commerce Price Research

## Platform Behavior Summary

| Platform | Anti-Bot Level | Search Access | Price Visibility | Key Workaround |
|----------|:---:|:---:|:---:|---|
| **JD.com (京东)** | 🔴 Aggressive | Blocked without login | Hidden behind login wall | Third-party deal sites |
| **Taobao/Tmall (淘宝/天猫)** | 🟡 Moderate | Partially accessible | Often visible | Direct search or deal sites |
| **Pinduoduo (拼多多)** | 🟡 Moderate | App-dependent | Mostly visible | Mobile API harder to hit |

## JD.com Specific Anti-Bot Challenges

JD.com has multiple layers of defense:
1. **Search blocking** — returns "内容太火爆了" or "访问频繁导致无法搜索" for automated requests
2. **Price hiding** — requires login to display actual price numbers (JavaScript dynamic rendering)
3. **Login wall** — even on product detail pages, price area shows "登录后查看" without authentication
4. **Mobile API gating** — `p.3.cn/prices/mgets` API may timeout or return empty for unauthenticated requests
5. **Mobile site redirect** — `m.jd.com` search redirects to app download prompt

**DO NOT try to brute-force through these defenses.** Escalating attempts wastes time and may trigger rate limits for the session's IP.

## Recommended Workflow: Third-Party Deal Aggregation Sites

When blocked from direct JD scraping, use these proxy data sources that track JD prices:

### Primary Sources (in priority order)

1. **慢慢买 (manmanbuy.com)** — `site:manmanbuy.com <product>` or `site:cu.manmanbuy.com <product>`
   - Best for: price history, current JD price, price trend alerts
   - URL pattern: `https://cu.manmanbuy.com/discuxiao_<id>.aspx`

2. **什么值得买 (smzdm.com)** — `site:smzdm.com <product>`
   - Best for: user-submitted deals, community price discussion, value analysis
   - Note: may also present CAPTCHA when accessed via browser; prefer web_search

3. **聚超值 (best.pconline.com.cn)** — `site:best.pconline.com.cn <product>`
   - Best for: aggregated deals from multiple platforms (JD + Taobao)
   - Often includes "京东现价XX元" in descriptions

### Search Pattern

Use `web_search` (not browser) with these query templates:
```
"<product_name>" "京东" "价格" "元"
"<product_name>" 京东 site:manmanbuy.com OR site:smzdm.com
site:best.pconline.com.cn "<product_name>" 京东
```

### Cross-Validation

Prices from deal sites may be stale (hours to days old). Always:
- Note the source URL and approximate freshness
- Cross-check across at least 2 sources
- Clearly label prices as approximate ("≈") when exact current price is unattainable
- Mention the limitation in the response (see `references/jd-scraping-pitfalls.md`)

## Browser Approach (Limited)

If browser navigation to JD is attempted:
- Product detail pages may load but price will be hidden
- Use `browser_vision` to confirm the login wall is present
- The mobile site (`m.jd.com`) often redirects to app download - not useful
- If a login cookie/session is available (configured separately), prices become visible

## Hotel Search on Chinese OTAs

Hotel research in small Chinese cities (e.g., Maotai Town, Kaili, Huangguoshu) via web_search or browser tools is similarly ineffective — search engines return noise, Ctrip requires login. See `references/hotel-search-limitations.md` for the full session log and recommended alternative workflow.
