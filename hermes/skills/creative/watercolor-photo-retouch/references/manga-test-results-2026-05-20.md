# 日漫风格修图 — 2026-05-20 测试记录

## 测试场景

| 项目 | 值 |
|------|-----|
| 测试时间 | 2026-05-20 18:00~18:08 |
| 输入照片 | 户外BBQ露营照（1人，烤架+帐篷+草地） |
| 方案 | apikey.fun gpt-4o 视觉分析 + Seedream 4-5 图生图 |
| 输出尺寸 | 2048×2048 |

## 测试结果

- ✅ 粗黑描边（外轮廓加粗、内部细节线纤细）
- ✅ 平涂动画色（无写实渐变，纯色块上色）
- ✅ 人物可辨（深蓝外套、黑色内搭、手表、笑容）
- ✅ 背景简化虚化（帐篷、草地保留但动漫化）
- ✅ 整体日漫日常插画感（类似《孤独的美食家》《摇曳露营》画风）

## 验证通过的完整脚本

```python
import base64, json, requests, os

API_KEY = "sk-87739841b0d96ef1d705bce4de5f900e0e97248843a6aebc1b581f8510d5b8b8"
ARK_KEY = "ark-91..."  # from ~/.hermes/.env

# Encode image
with open("photo.jpg", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()
data_uri = f"data:image/jpeg;base64,{b64}"

# Step 1: gpt-4o analyzes the photo
r1 = requests.post(
    "https://api.apikey.fun/v1/chat/completions",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": "Describe this photo in detail for creating a manga/anime comic illustration version."},
            {"type": "image_url", "image_url": {"url": data_uri}}
        ]}]
    }
)
scene = r1.json()["choices"][0]["message"]["content"]

# Step 2: Feed to Seedream img2img
prompt = f"""Transform this photo into a Japanese manga style illustration.
Scene: {scene}
Style: Manga/anime cel-shaded illustration, bold black ink outlines, flat vibrant colors,
anime character proportions, clean expressive lines.
Comic book art style with screentone textures, bold shading, dynamic composition.
Keep all characters recognizable with same poses, clothing colors and expressions. 
Overall Japanese manga page illustration look."""

r2 = requests.post(
    "https://ark.cn-beijing.volces.com/api/v3/images/generations",
    headers={"Authorization": f"Bearer {ARK_KEY}"},
    json={
        "model": "doubao-seedream-4-5-251128",
        "prompt": prompt,
        "image": data_uri,
        "size": "2048x2048",
        "n": 1,
        "response_format": "url",
        "watermark": False
    },
    timeout=120
)
result_url = r2.json()["data"][0]["url"]
```

## 对比：水彩 vs 动漫提示词差异

| 维度 | 水彩插画 | 日漫风格 |
|------|---------|---------|
| 线条 | speed-sketch black outline（速写线） | bold black ink outlines（粗黑描边） |
| 上色 | watercolor wash（水彩晕染） | cel-shaded, flat colors（赛璐珞平涂） |
| 背景 | abstract watercolor blots（抽象晕染） | stylized manga elements（动漫化场景） |
| 文字 | handwritten script（手写英文） | 不需要（或漫画对话框） |
| 装饰 | hearts, stars, flowers（温馨装饰） | screentone textures（漫画网点） |
| 氛围 | warm, cozy, commemorative | dynamic, manga page feel |
