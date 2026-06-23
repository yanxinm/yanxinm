---
name: taste-image-gen
description: 视觉 taste-skill（anti-slop 出图版）—— 从 taste-skill 前端设计反模板化原则延伸至 AI 图像生成。
---

# 视觉 Taste Skill — Anti-Slop 出图版

核心原则：先读需求，再定调，最后出图。不默认、不重复、不偷懒。

---

## 0. 读需求（出图前的设计读）

### 0.A 信号识别

1. 图种 — 小红书封面 / 活动海报 / 公众号头图 / 节气海报 / Ins 旅行卡 / 品牌宣传图 / 知识信息图
2. 风格关键词 — 小红书面包风 / Ins 旅行风 / 国潮扁平 / 复古海报 / 侘寂风 / 科技感 / 极简 / 温暖治愈 / 国风 / 赛博
3. 受众 — 小红书年轻女性 / 文旅爱好者 / 商务客户 / 大众市民
4. 格式 — 竖图(3:4/9:16) / 方图(1:1) / 横图(16:9/4:3)
5. 已有元素 — 是否有品牌色/logo/标准字体需要保留

### 0.B 出设计读

出图前先输出一句：判定：此图为[图种]，面向[受众]，走[风格]路线，色系倾向[色调]，留白[多/中/少]

例：
- 小红书店招封面，面向年轻女性，走面包风治愈路线，色系倾向暖白+陶土粉，留白多
- 文旅公众号头图，面向旅行爱好者，走纪实温暖路线，色系倾向青绿+米黄，留白中

---

## 1. 三旋钮（出图版）

- 设计差异度: 1=标准居中构图, 10=大胆非对称/留白实验
- 色彩饱和度: 1=高级灰/莫兰迪色系, 10=高饱和撞色
- 视觉密度: 1=大量留白/极简, 10=满版信息/密集纹理

基线推荐 — 小红书/Ins 风：差异度5-7 / 饱和度3-5 / 密度2-4

按图种调表：
- 小红书封面(面包风): 差异度5-6 / 饱和度4-6 / 密度2-3
- 活动海报: 差异度6-8 / 饱和度5-7 / 密度4-6
- 节气海报: 差异度4-6 / 饱和度4-5 / 密度3-4
- 公众号头图: 差异度3-5 / 饱和度3-4 / 密度3-4
- Ins 旅行卡: 差异度5-7 / 饱和度5-7 / 密度2-3
- 品牌宣传图: 差异度4-6 / 饱和度3-5 / 密度3-5

---

## 2. AI 模板特征禁令

### 2.A 构图禁令
- 正中央主体+对称构图 — 必须偏移或给负空间
- 人物/物体居中正面怼脸 — 除非品牌需要
- 地平线居中 — 天空占2/3或地面占2/3

### 2.B 色彩禁令
- AI紫蓝渐变背景 — 默认科技感色。禁
- 奶油米白+黄铜+深棕 — 高端消费AI默认色盘。禁
- 纯黑#000000纯白#FFFFFF — 用off-black和off-white
- 替代色系: 冷灰+银 / 深绿+骨色+琥珀 / 钴蓝+米白 / 陶土+石板灰 / 橄榄+砖红

### 2.C 内容禁令
- 三个人在正开会/握手/微笑 — 经典AI stock photo
- bokeh虚化滥用
- 无意义的漂浮粒子/水面倒影
- 白色背景上孤立物体无阴影

---

## 3. 色盘设计规范

| 色系 | 场景 | 饱和度 | 配色 |
|------|------|--------|------|
| 暖白+陶土粉 | 小红书/美食 | 40-60% | #faf6f1 + #d4826c |
| 青绿+米黄 | 文旅/自然 | 40-55% | #e8ede9 + #d4c9b3 |
| 冷灰+苍蓝 | 科技/品牌 | 30-45% | #f0f0ee + #8a9ba8 |
| 墨黑+金 | 高端/文化 | 低/高 | #1a1a18 + #c9a96e |
| 深绿+琥珀 | 自然/复古 | 50-65% | #2d4a3e + #c4913a |
| 雾紫+灰 | 文艺/女性 | 30-50% | #e8e0ec + #b4a7b8 |

每张图不超过3色，饱和度不超过80%。

---

## 4. GPT出图提示词工程

### 4.A 核心结构

[风格宣言] + [主体描述] + [构图/视角] + [色彩/光影] + [质感/细节] + no text overlay

### 4.B 风格宣言模板

- 小红书面包风: cozy Korean cafe flat lay, warm lighting, soft pastel tones, aesthetic
- Ins旅行风: editorial travel photography, cinematic, Kodak Portra film color grading
- 国潮扁平: Chinese modern flat vector art, bold geometric, ink wash inspired
- 复古海报: vintage poster style, 1960s retro, screen print texture
- 侘寂极简: wabi-sabi, minimalist, natural materials, soft diffused light
- 科技感: futuristic clean tech, high contrast, cool blue+silver, volumetric light
- 温暖治愈: warm inviting hygge, golden hour, cozy atmosphere
- 国风: traditional Chinese ink painting, misty mountains, restrained palette
- 赛博霓虹: cyberpunk neon, purple+teal, rain slicked streets

### 4.C 构图多样化（每次必须换）

1. 偏移构图: 主体放左/右1/3，另一侧留大空
2. 对角线构图: 主体沿对角线展开
3. 框架构图: 前景围框，主体在框内
4. 俯视平铺: 90度俯拍，适合食物/产品
5. 极低角度: 从下往上

### 4.D 关于文字

gpt-image-2中文渲染不准，所以：
1. **默认策略**：提示词带 `no text overlay, no words on the image` 禁止 GPT 加字，文字用 Pillow 后期叠加
2. **例外策略（行程海报/信息图）**：当文字量大且布局复杂（如时间线+7个行程节点+底部天气穿搭）时，可用**全中文 prompt** 让 gpt-image-2 直接渲染全部文字
   - 提示词用纯中文写，末尾加 `ALL CHINESE TEXT MUST BE ACCURATE NO English text`
   - 生成后用 vision_analyze 逐字验证（重点检查酒店名、美食名、生僻字）
   - 已验证：浠岸酒店、夺夺粉、裹卷、儒林路、虹山湖等非常用字均准确
   - 参考：fridge-magnet-poster references/guizhou-travel-posters.md §2026-06-22
3. 出图始终留够空白区

---

## 5. GPT出图全模板

### 小红书面包风封面
Cozy Korean cafe style flat lay, [主体] arranged on warm wood table, window light creating soft shadows, pastel cream and rose palette, shallow DOF, slight film grain, minimalist with negative space on right for text, no text overlay, no watermark, shot from above 45deg

### Ins旅行风
Editorial travel photography style, [主体/场景], cinematic composition, Kodak Portra 400 film color grading, warm golden hour, desaturated earth tones, rule of thirds, soft haze, high detail, no text overlay, vertical 3:4

### 海报/节气海报底图
Vintage minimalist poster background, [主体], muted palette of [色系], large empty space in [上/下/左/右] for text, no text overlay, clean composition, subtle paper texture, matte finish, ambient soft lighting

### 国潮扁平插画
Modern Chinese flat illustration style, [主体], bold geometric shapes, ink wash inspired palette of [色系], clean vector lines, traditional decorative elements, flat lighting, no gradients, no text, 2D illustration

---

## 6. 出图前自检清单

- 设计读已输出（图种/受众/风格/色系/留白）
- 三旋钮已设定
- 无AI紫蓝渐变 / 奶油米白套装 / 纯黑白
- 构图非居中对称
- 不超过3色
- 留白充足
- 提示词含 no text overlay
- 风格宣言已选
- 构图模式跟上次不同
- 色彩饱和度<80%
- 含质感关键词
