# Blacklist Test Fixture

> Used by `tools/self_test.py` to verify `quality_check.check_blacklist_violations()`
> + `source_verifier classify` correctly catch banned sources without polluting
> any production prototype's manifest.
>
> **Do NOT** copy into a production skill — these URLs are intentionally
> blacklisted; their presence in a skill manifest is itself the test
> signal.

## Source Manifest

| source_id | url | bucket | last_checked | author/host | note |
|-----------|-----|--------|--------------|-------------|------|
| T99-S001 | https://baike.baidu.com/item/test | blacklisted | 2026-05-04 | 百度百科 | zh-CN blacklist |
| T99-S002 | https://zhuanlan.zhihu.com/p/12345 | blacklisted | 2026-05-04 | 知乎专栏 | zh-CN blacklist |
| T99-S003 | https://mp.weixin.qq.com/s/foo | blacklisted | 2026-05-04 | 公众号 | zh-CN article path blacklist |
| T99-S004 | https://www.csdn.net/article/123 | blacklisted | 2026-05-04 | CSDN | zh-CN blacklist |
| T99-S005 | https://www.cnblogs.com/foo/p/123 | blacklisted | 2026-05-04 | 博客园 | zh-CN blacklist |
| T99-S006 | https://www.g2.com/products/foo | blacklisted | 2026-05-04 | G2 | en blacklist |
| T99-S007 | https://www.capterra.com/foo | blacklisted | 2026-05-04 | Capterra | en blacklist |
| T99-S008 | https://www.businesswire.com/news/foo | blacklisted | 2026-05-04 | Businesswire | en PR-wire blacklist |
| T99-S009 | https://javascript.plainenglish.io/foo | blacklisted | 2026-05-04 | Medium farm | en farm subdomain |
| T99-S010 | https://arxiv.org/abs/2305.12345 | verified_primary | 2026-05-04 | arXiv | positive control — should pass |

## Expected verdicts

- `quality_check check_blacklist_violations` on this fixture must **fail** with at least 9 violations (T99-S001 ... T99-S009).
- `source_verifier classify` on each T99-S001..S009 must return `blacklisted`.
- `source_verifier classify` on T99-S010 must return `verified_primary`.
