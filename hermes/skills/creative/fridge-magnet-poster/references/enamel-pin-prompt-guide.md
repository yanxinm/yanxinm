# gpt-image-2 珐琅徽章图标生成指南

> 2026-05-25 通过 apikey.fun 中转的 gpt-image-2 实战验证

## 路线选择

| 生成方式 | 耗时 | 质感 | 推荐场景 |
|---------|------|------|---------|
| **gpt-image-2** (via apikey.fun) | ~60s | 珐琅徽章顶尖质感 | **主力推荐** |
| Seedream 文生图 | ~16s | 扁平矢量 | 急用/初版 |

## 提示词模板（已验证可行）

```text
{地名}标志性建筑/人物，正面视角，{结构/姿态特征}，{颜色特征}。
Design as a delicate metal enamel pin badge (Enamel Pin),
smooth glossy enamel surface, warm luster, metal edging,
fine gold/white outline (1-2px), soft highlights on raised surfaces,
slight 3D thickness and soft drop shadow.
Flat minimalist style but retains core silhouette and landmark features.
Pure white background, no text, moderately simplified details.
Like a精致 travel souvenir fridge magnet.
```

**关键约束：**
- 必须用英文 — gpt-image-2 对 "enamel pin badge" 理解最准
- 必须写 "Pure white background, no text"
- 尺寸 1024×1024
- 输出格式：`b64_json`（体验更稳定）

## 调用代码

```python
import json, urllib.request, base64

payload = {
    "model": "gpt-image-2",
    "prompt": "..."  # 上面的提示词
    "size": "1024x1024",
    "n": 1,
    "response_format": "b64_json"
}
req = urllib.request.Request(
    'https://slb.apikey.fun/v1/images/generations',  # 推荐专线
    data=json.dumps(payload).encode(),
    headers={
        'Content-Type': 'application/json',
        'Authorization': 'Bearer sk-877...b8b8'
    },
    method='POST'
)
with urllib.request.urlopen(req, timeout=180) as resp:
    d = json.loads(resp.read())
    b64 = d['data'][0]['b64_json']
    with open('/tmp/icon.png', 'wb') as f:
        f.write(base64.b64decode(b64))
```

## 实践案例

| 案例 | 主体 | 提示词重点 | 耗时 | 效果 |
|------|------|-----------|------|------|
| 汕头小公园钟楼 | 欧式钟楼 | gold/white outline + red dome + clock face | 60s | ✅ 金色描边、珐琅釉面、投影立体感 |
| 西双版纳双胞胎男孩 | 两个男孩手牵手 | matching striped shirts + holding hands | 92s | ✅ 金边描边、珐琅填色、阴影凸起 |

## 已知问题

1. 生成的人物是**卡通/通用形象**，不是原图人物的还原（gpt-image-2 不走 img2img）
2. 建筑类 icon 效果最好（轮廓清晰、结构明确）
3. 人物类 icon 生成较慢（~90s vs ~60s）
