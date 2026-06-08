# gpt-image-2 珐琅徽章图标生成指南

## 概述

通过 apikey.fun 中转站的 gpt-image-2 模型，可在 60-120s 内生成立体金属珐琅徽章（Enamel Pin）图标，用于旅行打卡海报的上半部分。

## 通用提示词模板（已验证）

```
{地名}标志性建筑，正面视角，{结构特征描述}，{颜色特征描述}。
Design as a delicate metal enamel pin badge (Enamel Pin),
smooth glossy enamel surface, warm luster, metal edging,
fine gold/white outline (1-2px), soft highlights on raised surfaces,
slight 3D thickness and soft drop shadow.
Flat minimalist style but retains core silhouette and landmark features.
Pure white background, no text, moderately simplified details.
Like a精致 travel souvenir fridge magnet.
```

**关键要点**：
1. 先用中文描述主体和结构，再用英文指定珐琅徽章材质
2. 必须包含 `Pure white background, no text`
3. "Enamel Pin" 比 "珐琅徽章" 理解更准确
4. 尺寸固定为 1024×1024

## 建筑类图标（已验证成功）

**汕头小公园钟楼**（2026-05-25 实测通过）：
- 提示词包含：钟楼 + 白色墙面 + 红色圆顶 + 金色描边
- 生成结果：✅ 珐琅质感到位，描边清晰，有高光和投影
- 耗时：~60s

## 人物类图标（设计中）

**双胞胎男孩合影**（2026-05-25 设计）：
对于人物为主的照片，提示词需调整：
- 描述两人的姿势、站位（正面、肩并肩、手拉手等）
- 描述穿着（同款服装、颜色）
- 不适合描述具体长相，用轮廓和姿态代替
- 考虑用双人剪影 + 标志性元素（如合影背景的简化轮廓）

**注意事项**：
- gpt-image-2 有名人肖像保护，含真实人名会拒绝生成
- 人物图标可选用双人头像轮廓、背影、简化卡通等风格
- 如人物面部特征很重要 → 建议用 LoRA 训练替代

## 风格对照

| 风格 | 提示词关键词 | 适用场景 |
|------|-------------|---------|
| 金属珐琅徽章 | enamel pin, glossy enamel, metal edging, gold outline | ✅ 已验证 |
| 树脂立体 | resin charm, 3D resin, transparent layering | 未验证 |
| 搪瓷胸针 | cloisonne pin, fine wire inlay, vitreous enamel | 未验证 |
| 白描扁平 | flat vector, minimal line art, solid color | 旧版已废弃 |

## 性能

| 指标 | 值 | 说明 |
|------|-----|------|
| 生成耗时 | 60-120s | 从提交到返回 |
| 输出尺寸 | 1024×1024 | 固定 |
| 输出文件大小 | ~900KB-1.5MB | base64 编码 |
| 端点 | `https://slb.apikey.fun/v1/images/generations` | 推荐专用线 |

## 失败模式

| 现象 | 原因 | 修复 |
|------|------|------|
| 无珐琅质感，像扁平贴纸 | 提示词缺少 "enamel pin" | 中英文结合描述材质 |
| 图标带复杂背景 | 漏写 "Pure white background" | 必须显式要求纯白背景 |
| 图标内有乱码文字 | 漏写 "no text" | 必须显式要求无文字 |
| 拒绝生成（肖像保护） | 提示词含真实人名 | 去掉人名，用特征描述 |
| 人物面部不像原图 | gpt-image-2 不支持身份保持 | 换 LoRA 或接受风格化抽象 |
