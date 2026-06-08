# 水彩插画修图 — 2026-05-20 测试记录

## 测试结果总览

| 项目 | 结果 |
|------|------|
| 测试时间 | 2026-05-20 17:50~18:00 |
| API | 火山引擎 Ark Seedream 4-5 |
| API Key | ARK_IMAGE_API_KEY（读自 ~/.hermes/.env） |
| 端点 | https://ark.cn-beijing.volces.com/api/v3/images/generations |
| 图生图能力 | ✅ 通过（image 参数 dataURI 格式） |
| 测试图片 | 7人团队聚餐合影（4096×3072） |
| 输出尺寸 | 2048×2048 |
| 耗时 | ~40秒 |
| Token 消耗 | 16,384 tokens |

## 验证通过的提示词

### 团队/会议合影（已验证）
```
Convert this team/colleague gathering photo into a warm watercolor illustration with hand-drawn black sketch outlines.
Style: hand-drawn speed-sketch black outline (varying thickness, organic lines) + soft watercolor wash fills,
warm pastel color palette (beige, soft blue, light gray, warm earth tones),
7 people standing and seated together, some in suits and some in casual wear, friendly atmosphere.
decorative handwritten text like 'Great Team' and 'Together' in casual script font,
small decorative hearts, stars and simple flower doodles scattered around the edges,
abstract background with soft watercolor color blots/splashes in beige/soft blue/warm gray tones.
Overall warm, commemorative, collegial illustration style, like a team keepsake.
No realistic photo texture, full hand-drawn illustration feel.
```

### 结果评价
- ✅ 7人全部可辨（服装、发型、姿态清晰区分）
- ✅ "Great Team Together" 手写文字出现
- ✅ 装饰元素（粉色爱心、金色/白色星星、小花）完整
- ✅ 水彩晕染质感到位，背景米黄+柔和蓝
- ✅ 用户确认：**"可以"**

## 注意事项

1. **尺寸要求**：Seedream 最小像素 3,686,400（1920×1920），推荐 2048×2048
2. **base64 编码**：不要用 jq 传 base64（参数超长），用 Python requests 直接发
3. **输出尺寸**：用 `response_format: url` 让 API 返回图片 URL，然后 curl 下载
4. **水印关闭**：必须设 `watermark: false`
5. **API Key**：`ARK_IMAGE_API_KEY` 是图片专用 Key（与聊天用的 DeepSeek Key 不同）
