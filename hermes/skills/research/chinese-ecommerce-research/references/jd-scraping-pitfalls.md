# JD.com Scraping Pitfalls & Workarounds

## Actual Session Log: Intel AX210 Price Research (2025-06-03)

### Attempts That FAILED

1. **`browser_navigate` → jd.com homepage → type search → Enter**
   Result: "内容太火爆了，请稍后再试" + login prompt

2. **`browser_navigate` → `search.jd.com/Search?keyword=...` (direct URL)**
   Result: "抱歉由于访问频繁导致无法搜索，请稍后再试！"

3. **`browser_navigate` → `item.jd.com/100027785129.html` (product detail)**
   Result: Page loads but price area shows "登录查看更多优惠~"
   Price number is hidden behind JS dynamic rendering + auth wall.
   `browser_console` to extract price returns nothing.
   `browser_vision` confirms: "login is required to see price"

4. **`curl p.3.cn/prices/mgets?skuIds=J_...` (price API)**
   Result: Timeout after 15s — API rate-limited for unauthenticated requests

5. **`browser_navigate` → `m.jd.com/search?keyword=...` (mobile site)**
   Result: Redirects to app download page, no search results

6. **`browser_navigate` → `smzdm.com/p/...` (deal site via browser)**
   Result: CAPTCHA wall — "安全验证" dialog

### What WORKED

1. **`web_search` with site-specific queries** against deal aggregation sites:
   ```
   site:manmanbuy.com AX210 京东 价格
   site:smzdm.com AX210 网卡 京东
   site:best.pconline.com.cn AX210 京东
   ```

2. **General web_search** for product + platform + price keywords:
   ```
   "AX210" "京东" "价格" "元"
   Fenvi 奋威 AX210 京东 价格
   SSU AX210 京东 79元
   ```

3. **Cross-referencing** prices from 2+ independent deal sites to validate

### Key Data Sources That Returned Useful Results

| Source | URL Pattern | What It Provides |
|--------|------------|-----------------|
| 慢慢买 | `cu.manmanbuy.com/discuxiao_<id>.aspx` | Current JD price, price history |
| 什么值得买 | `post.smzdm.com/p/<id>/` | User deal posts with prices |
| 聚超值 | `best.pconline.com.cn/youhui/<id>.html` | Aggregated deals, "京东现价XX元" |

### Price Accuracy Caveat

Deal site prices may be hours-to-weeks old. Always:
- Note the data source in the response
- Use "≈" for approximate prices
- Mention that exact current prices require JD login
- Cross-validate across 2+ sources when possible
