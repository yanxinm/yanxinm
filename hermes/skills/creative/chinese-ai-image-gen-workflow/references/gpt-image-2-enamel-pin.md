# gpt-image-2 珐琅徽章（Enamel Pin）生成方案

## 概述

2026-05-25 验证：通过 apikey.fun 中转的 gpt-image-2 可以直接生成高质量的**金属珐琅徽章质感图标**，用于冰箱贴海报的上半图标区。

## 已验证的参数

| 参数 | 值 | 说明 |
|------|-----|------|
| 端点 | `https://slb.apikey.fun/v1/images/generations` | 专线端点，比 `api.` 冷启动快 1s |
| 模型 | `gpt-image-2` | 最新版，效果最好 |
| 尺寸 | `1024x1024` | 够用，gpt-image-2 原生支持 |
| 输出格式 | `b64_json` | 直接返回 base64，避免二次下载 |
| 响应时间 | ~60-90s | 比 Seedream 慢（~16s），但质感更好 |

## 提示词模板（已验证可行）

```text
{地名/主体描述}标志性建筑/主体，正面视角，{结构特征}，{颜色特征}。
Design as a delicate metal enamel pin badge (Enamel Pin),
smooth glossy enamel surface, warm luster, metal edging,
fine gold/white outline (1-2px), soft highlights on raised surfaces,
slight 3D thickness and soft drop shadow.
Flat minimalist style but retains core silhouette and landmark features.
Pure white background, no text, moderately simplified details.
Like a精致 travel souvenir fridge magnet.
```

**关键约束**：
- 必须用**英文**提示词 — gpt-image-2 对 "enamel pin badge" 理解远好于中文"珐琅徽章"
- 必须包含 `"Pure white background, no text"` — 否则 AI 会加复杂背景或手写字
- 主体描述要具体（建筑层数、颜色、特征），但图标本身简化到核心轮廓
- 人物图标（如两个小孩手牵手）也能生成，保持面部特征简化

## 调用代码

```python
import json, urllib.request, base64

payload = {
    "model": "gpt-image-2",
    "prompt": "...",
    "size": "1024x1024",
    "n": 1,
    "response_format": "b64_json"
}
req = urllib.request.Request(
    'https://slb.apikey.fun/v1/images/generations',
    data=json.dumps(payload).encode(),
    headers={
        'Content-Type': 'application/json',
        'Authorization': 'Bearer <API_KEY>'
    },
    method='POST'
)
with urllib.request.urlopen(req, timeout=180) as resp:
    d = json.loads(resp.read())
    b64 = d['data'][0]['b64_json']
    with open('/tmp/icon.png', 'wb') as f:
        f.write(base64.b64decode(b64))
```

## 使用时机

- **建筑/地标照片** → gpt-image-2 生成珐琅徽章效果最佳（金色描边+光滑釉面）
- **人物合影** → 可生成简化人物徽章，但面部相似度不如 Seedream 图生图
- **优先 gpt-image-2** 当需要精致珐琅质感时；优先 **Seedream** 当需要快速出图或忠实现场时
