---
name: fridge-magnet-poster
description: 小红书风格旅行打卡海报 — 上半金属珐琅徽章图标+纯色背景，下半原图照片，高级ins旅行卡片风
tags: [aigc, poster, travel, seedream, enamel-pin, xiaohongshu, gpt-image-2]
---

# 冰箱贴风格旅行打卡海报（v2 — 珐琅徽章版）

## 适用场景
用户说"做冰箱贴海报"、"旅行打卡海报"、"高级旅行卡片"、"修成冰箱贴风格"时，按此流程执行。

## 定稿参数（v2 — 2026-05-25已验证通过）

基于两张样图（`references/sample-grid.png`, `references/sample-single.png`）学习 + 汕头小公园实做出图验证，用户已确认满意。

| 维度 | 参数 | 说明 |
|------|------|------|
| 画布比例 | **3:4 竖版** (1080×1440) | 小红书/ins常见比例 |
| **上下分区** | **1:1** | 上半50% = 720px 图标区 + 下半50% = 720px 原图区 |
| **图标材质** | **金属珐琅徽章 (Enamel Pin)** | 光滑珐琅釉面，温润光泽，边缘金属包边 |
| 高光效果 | 柔和高光在建筑凸起面/圆顶顶部 | 模拟珐琅釉面的光滑反光 |
| 立体厚度 | 视觉约2-3mm厚度 | 通过底部阴影+边缘厚度实现浮雕感 |
| **描边** | **金色或白色细描边，1-2px** | 精致勾勒轮廓，有金属包边感 |
| 阴影 | 柔和投影 (Drop Shadow)，透明度30-50% | 形状与图标轮廓一致，边缘轻微模糊 |
| **背景色** | **从照片提取主色**（KMeans聚类或颜色频率分析） | 纯色、明亮干净，旅行明信片感。**禁止渐变** |
| **图标大小** | **40% 画布宽度** (432px / 1080px) | 小巧精致，周围大量留白 ✅ 用户已确认 |
| 图标位置 | 上半区 **iy=80px**，居中 | 不可太大，不可压边 ✅ 用户已确认 |
| 图标去底 | 白色像素阈值 >235 变透明 | 确保图标外框干净无残边 |
| **文字字体** | **Dancing Script** (38px / 画布3.5%) | 手写连笔体 |
| 文字内容 | `"{地名} | {月份全称},{年份}"` | 如 "Shantou \| May,2026"，竖线+逗号 |
| **文字位置** | **图标底部 +20px**，居中 | ✅ 文字完全在上半区内；注意竖构图照片裁切（见 `references/photo-crop-strategy.md`） |
| 文字颜色 | (40, 22, 10) 深棕 | 与背景对比清晰 |
| 图片质量 | JPEG 97 | 清晰不模糊 |
| 整体气质 | 高级旅行摄影卡片 | 真实照片+极简珐琅徽章+主色背景+手写英文 |

## 工作流程

冰箱贴海报有两种徽章模式，根据用户需求选择：

| 模式 | 适用场景 | 生成方式 | 效果 |
|------|---------|---------|------|
| **Image-to-Image（推荐）** | 人物合影/需保留真实样貌 | Hermes WebUI img2img | 保留人物特征 |
| **文生图（备选）** | 纯建筑/风景打卡 | gpt-image-2 文生图 | 珐琅徽章质感 |

### 🏆 推荐：Image-to-Image 转珐琅徽章（保留真实样貌）

当用户提供的是**人物合影照片**，希望珐琅徽章保留真实人物样貌时，优先使用此方案：

1. 确保 `config.yaml` 中有 `fun-codex` provider（复制 `apikey-fun` 配置，加上 `api_mode: codex_responses`）
2. 用 Hermes Web UI 的 image-to-image 端点：

```bash
TOKEN="$(cat ~/.hermes-web-ui/.token)"
curl -sS -X POST "http://127.0.0.1:8648/api/hermes/media/apikey-image-generate" \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
    "mode": "image",
    "prompt": "Convert this photo into a flat enamel pin badge illustration. Keep the people recognizable: [详细描述每人的服装颜色和特征]. Style: flat vector enamel pin badge, smooth glossy enamel colors, gold metal edging around all shapes, fine gold outlines, slight 3D thickness with soft drop shadow. Simplified but recognizable facial features and clothing. Pure white background, no text, clean minimalist travel souvenir magnet style.",
    "image_path": "/absolute/path/to/photo.jpg",
    "size": "1024x1024",
    "output_path": "/tmp/icon_output.png"
  }'
```

3. 验证图标质量后用 `travel-poster-compose.py` 拼合

### 📋 备选：纯文本生成珐琅徽章（建筑/风景）

适用于无人物照片或仅需建筑地标场景。

### Step 0: 确认信息
收到用户照片后：
1. `vision_analyze` 分析建筑主体、结构细节、颜色
2. **必须问**：地名、日期（精确到月份）
3. 提取照片主色（RGB）
4. **确认后**再生成，不要自己猜

### Step 1: 用 gpt-image-2 生成珐琅徽章图标（推荐）

通过 apikey.fun 中转的 gpt-image-2 生成珐琅徽章质感图标。约 60-90s，效果优于 Seedream。

```python
import json, urllib.request, base64
payload = {
    'model': 'gpt-image-2',
    'prompt': '...详细提示词...',
    'size': '1024x1024',
    'n': 1,
    'response_format': 'b64_json'
}
req = urllib.request.Request('https://slb.apikey.fun/v1/images/generations',
    data=json.dumps(payload).encode(),
    headers={'Content-Type':'application/json',
             'Authorization':'Bearer sk-87739841b0d96ef1d705bce4de5f900e0e97248843a6aebc1b581f8510d5b8b8'})
with urllib.request.urlopen(req, timeout=180) as resp:
    d = json.loads(resp.read())
    with open('/tmp/icon.png','wb') as f:
        f.write(base64.b64decode(d['data'][0]['b64_json']))
```

**提示词公式**（详见 `references/enamel-pin-prompt-guide.md`）：
```
{地名}标志性建筑，正面视角，{结构特征}，{颜色特征}。
Design as a delicate metal enamel pin badge (Enamel Pin),
smooth glossy enamel surface, warm luster, metal edging,
fine gold/white outline (1-2px), soft highlights on raised surfaces,
slight 3D thickness and soft drop shadow.
Flat minimalist style but retains core silhouette and landmark features.
Pure white background, no text, moderately simplified details.
Like a精致 travel souvenir fridge magnet.
```

**⚠️ 关键约束**：
- 用英文提示词 — gpt-image-2 对 "enamel pin badge" 理解最准
- 必须写 "Pure white background, no text"
- 尺寸 1024×1024，输出格式用 b64_json

### 备选：用豆包 Seedream 生成图标

仅当 gpt-image-2 不可用时（如网络问题）退回到 Seedream。Seedream 提示词见下方，尺寸 2048×2048。

### Step 1b: 真实人物珐琅徽章（Image-to-Image）⭐ NEW

当用户要求徽章保留照片中**真实人物样貌**（如"用照片中这三个人物"），不能用文生图——gpt-image-2 无法还原具体人脸。必须用 Hermes Web UI 的 image-to-image 模式。

**前置条件**：
- Hermes Web UI 运行中（默认 `http://127.0.0.1:8648`）
- `config.yaml` 的 `custom_providers` 中有 `fun-codex` 条目（如没有，从 `apikey-fun` 复制：`name: fun-codex`, `api_mode: codex_responses`，其余不变）
- Token 在 `~/.hermes-web-ui/.token`

**流程**：

1. **vision_analyze 照片**：提取每个人的服装颜色、配饰、姿态、站位，以及背景地标特征

2. **构建 image-to-image prompt**：精确描述人物特征，确保模型在风格化过程中保持识别度

3. **调用 WebUI 端点**：
   ```bash
   TOKEN=$(cat ~/.hermes-web-ui/.token)
   curl -sS -X POST "http://127.0.0.1:8648/api/hermes/media/apikey-image-generate" \
     -H "Authorization: Bearer $TOKEN" -H 'Content-Type: application/json' \
     -d '{
       "mode": "image",
       "prompt": "Convert this photo into flat enamel pin badge. Keep people recognizable: [服装/姿态描述]. Flat vector, gold edging, glossy enamel, 3D shadow, pure white bg, no text.",
       "image_path": "/path/to/photo.jpg",
       "size": "1024x1024",
       "output_path": "/tmp/icon_people.png"
     }'
   ```

4. **验证**：`vision_analyze` 检查人物服装/姿态是否保留、去底是否干净

5. **拼合海报**：同 Step 4 compose 脚本

**⚠️ 踩坑**：
- gpt-image-2 文生图**无法还原具体人脸**，即使 prompt 写得再详细 → 必须用 image-to-image
- `missing_fun_codex_provider` 错误 → 见上方前置条件，用 python yaml 脚本添加 provider
- 生成结果会保留服装品牌文字（如 ADIDAS），属正常——风格化不抹除图案内容

### Step 2: 提取照片主色
```python
from PIL import Image
import numpy as np
from collections import Counter
img = Image.open(photo_path).resize((100,100))
pixels = np.array(img).reshape(-1, 3)
top_color = Counter([tuple(p) for p in pixels]).most_common(1)[0][0]
print(f"主色: RGB{top_color} #{top_color[0]:02x}{top_color[1]:02x}{top_color[2]:02x}")
```

### Step 3: 确认照片裁切位置（关键）

照片裁切是最容易出错的步骤，**必须先 vision_analyze 定位主体位置再裁切**：

1. **用 vision_analyze 查主体纵向位置**：问"人物的头顶在画面百分之几的位置？脚底呢？"
2. **先缩放到宽度=1080px**，保持原比例
3. **从主体头顶位置向下取720px**：
   ```python
   # crop_start = int(缩放后高度 * 头顶百分比)
   crop_start = int(new_h * head_percent)  # 如 42% → 0.42
   if crop_start + 720 > new_h:
       crop_start = new_h - 720  # 防超出底部
   photo = photo.crop((0, crop_start, 1080, crop_start + 720))
   ```
4. **验证**：拼合后用 vision_analyze 确认主体完整可见

**⚠️ 经验教训（西双版纳双胞胎照片）**：
- 人物从头到脚占了画面58%高度，下半区720px装不下全身
- 必须从**头顶位置**开始裁，优先保证脸部和上半身可见
- 错误策略：从底部裁切 → 只剩腰以下，被用户批评"小朋友只剩半身"
- 正确策略：用 vision_analyze 先定位头部百分比 → 从该位置向下裁

### Step 4: 拼合海报
```bash
python3 templates/travel-poster-compose.py \
  --icon /tmp/icon.png \
  --photo <照片路径> \
  --place "Shantou" \
  --date "May,2026" \
  --bg-rgb 111 144 185
```

或手动执行 Pillow 脚本（参考 `templates/travel-poster-compose.py` 的逻辑）。

### Step 5: 展示并迭代
常见调整方向：
- 图标太大 → 缩到 35% 或 30%
- 背景色不对 → 换一个主色候选
- 文字缺失 → 检查文字是否超出上半区
- 人物/主体只剩半身 → ⚠️ 最常见错误。必须先 vision_analyze 定位头部%位置再从头顶裁
- **用户要求换图标主题** → 如"用地标改成用人物"，无需重跑全流程，只需重新生成图标并 `--icon` 替换后重拼合

## 人物主题珐琅徽章提示词公式

当用户要求徽章以人物（而非纯建筑/地标）为主题时，使用以下提示词公式。**关键：人物背面/侧影比正面效果好**——AI 画正面脸容易崩，背面剪影+地标背景的组合既安全又有旅行打卡感。

```
{人数} people standing together at {地点/场景}, seen from behind or slight side profile,
casual travel clothing, {标志性地标/山峰} rising in the background against {天空颜色} sky.
Design as a delicate metal enamel pin badge, smooth glossy enamel surface,
warm earthy colors for people silhouettes, {地标颜色} for the landmark,
soft {背景色} for the sky area, gold metal edging outline on all shapes,
fine thin gold outline, soft highlights on raised surfaces,
slight 3D thickness and soft drop shadow.
Flat minimalist vector style, simplified recognizable silhouettes,
compact composition, the {最高元素} is the tallest element.
Pure white background, no text, no faces, no photo-real details.
Like an elegant travel souvenir fridge magnet capturing a {旅行类型} trip.
```

**已验证案例（神仙居，2026-05-27）**：
- 三人背影 + 尖峰山 + 观景台栏杆
- 颜色：暖土色人物 + 深绿山脉 + 浅蓝天
- 提示词追加 `no faces` 和 `simplified recognizable silhouettes` 防止崩脸

## 颜色提取参考
> 详见 `references/color-extraction-and-api-key.md` — 包含 numpy uint8 溢出修复、API Key 获取方法。
## 参考文件
- `references/sample-grid.png` — 4组样图参考
- `references/sample-single.png` — 单张海报参考
- `templates/travel-poster-compose.py` — 可复用的 Pillow 拼合脚本（v2 已验证）

## 关键 Pitfalls
| 问题 | 解决 |
|------|------|
| **gpt-image-2 img2img prompt 过长超时** | prompt **< 100 字符**，超过 150 字符触发 `stream_read_error` |
| **缺少 fun-codex provider** | config.yaml 需复制 apikey-fun 配置 + `api_mode: codex_responses` |
| 文字超出下半区被照片遮挡 | 文字底部必须 < 720px |
| 图标自带白底 | 阈值 >235 去除，再腐蚀边缘 |
| 图标太大显得拥挤 | 限制 40% 画布宽度 |
| 背景色不协调 | 从照片饱和度最高区域提取 |
| ⚠️ **API Key 获取** — `~/.hermes/.env` 和 `config.yaml` 中 Key 为脱敏/截断值 | 用 `hermes config get custom_providers` 获取完整 Key，或直接让用户提供 |
| ⚠️ **颜色提取 numpy uint8 溢出** — `r + g + b` 可能溢出 numpy 范围 | 显式 `int(r) + int(g) + int(b)` 或用 `np.int32` 转换 |
| ⚠️ **人物主题珐琅徽章** — 用户可能要求"用人物来做"而非建筑地标 | 见下方「人物主题珐琅徽章提示词」章节 |
