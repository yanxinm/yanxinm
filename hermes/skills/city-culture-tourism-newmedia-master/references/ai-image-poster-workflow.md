# AI 辅助旅行海报/小红书打卡图制作工作流

> 迭代经验：基于建水古城旅行海报（Jianshui, 07.2025）项目从 v1 到 v6 的完整演进路径。

## 场景

文旅新媒体从业者需要快速生成城市/景区打卡海报（小红书风格），核心结构：

- **上半部分**：纯色背景 + 建筑/地标冰箱贴风格图标 + 地名+时间
- **下半部分**：实景照片（原图）
- **比例**：竖版 3:4（推荐 1080×1440）
- **风格**：冰箱贴/贴纸感（白描边 + 投影 + 手写文字）

## 完整工作流（4步）

### 第1步：原图分析 + 提示词设计

使用 `vision_analyze` 提取建筑特征——**不能只写"城堡塔楼"**，要写精确的建筑结构：

**建水案例**（三段式艺术塔楼）：
```
三段式塔楼：底部毛石基座，中部红砖墙面带拱形窗，顶部锯齿状城垛檐口+陶罐装饰
左侧中式石拱门（带传统雕刻）
正面锥形陶罐堆叠装饰
材质：毛石(灰)、红砖(红棕)、陶罐(暖橙/棕)
```

通用模板：
```
旅行纪念冰箱贴设计，{城市名/地点}标志性建筑，正面视角。
{精确建筑结构描述，分层写}，
{附属建筑/装饰描述}。
扁平矢量插图风格，保留{主色调}。
画面简洁干净，白色背景，只有建筑主体，没有文字。
```

**⚠️ 关键教训**：第一次提示词写"中国城堡式塔楼，锯齿城垛，拱形窗"，AI 生成了**通用欧洲城堡白剪影**，和实际建水建筑完全不同。必须写精确到具体结构层次。

### 第2步：豆包 Seedream 生成建筑图标

**调用方式**：
```bash
cd ~/.hermes/scripts
bash ark-image-gen.sh "详细提示词" doubao-seedream-4-5-251128 1920x1920 1
```

- 最小尺寸：1920×1920（API 要求 ≥ 3,686,400 像素）
- 模型：doubao-seedream-4-5-251128
- 输出：方形图标图，建筑居中，白色背景

**初版常见问题**：第一次生成的可能是**反白剪影**（白色建筑轮廓在深色背景上），需要调整提示词改为"彩色扁平矢量插图风格，保留建筑材质色彩"。

**验证方法**：用 `vision_analyze` 检查生成的图标是否和照片里的建筑匹配。

### 第3步：Pillow 处理 → 冰箱贴贴纸效果

这是**最关键的步骤**。AI 生成的图标是白底彩色图，需要以下处理才能变成冰箱贴：

**顺序**：
1. **白底去背**：Pillow 中把亮度 > 230 的像素设为透明
   ```python
   gray = icon.convert("L")
   new_alpha = gray.point(lambda x: 0 if x > 230 else 255)
   new_alpha = new_alpha.filter(ImageFilter.MaxFilter(5))  # 避免白边
   icon.putalpha(new_alpha)
   ```

2. **白描边**：从透明蒙版扩张得到白色边框
   ```python
   alpha_mask = icon_scaled.getchannel("A")
   border_mask = alpha_mask.filter(ImageFilter.MaxFilter(21))  # 奇数
   border = Image.new("RGBA", (iw, ih), (255, 255, 255, 255))
   border.putalpha(border_mask)
   ```

3. **投影阴影**：从蒙版扩张+高斯模糊生成半透明投影
   ```python
   shadow_mask = alpha_mask.filter(ImageFilter.MaxFilter(25))
   shadow_mask = shadow_mask.filter(ImageFilter.GaussianBlur(15))
   shadow = Image.new("RGBA", (iw, ih), (90, 55, 30, 0))
   shadow.putalpha(shadow_mask.point(lambda x: int(x * 0.35)))
   ```

4. **叠加顺序**：阴影（偏移+4,+6）→ 白色边框 → 彩色图标

5. **文字**：使用手写体（Dancing Script）程序化叠加，不可用 AI 生成
   - Dancing Script 下载：`fonts.gstatic.com/s/dancingscript/v29/...`
   - 文字偏移投影增强可读性

### 第4步：拼合最终海报

参考模板 `templates/travel-poster-compose.py`（注意用 v6 版本，不是旧版）。

关键参数：
- 图标大小：图像宽度 × 0.55（留出文字空间）
- 图标位置：顶部下移 10px
- 文字位置：图标底部 + 25px 间距
- 文字字体：Dancing Script 44pt（地名）/ 24pt（日期）
- 分割线：3 像素淡色线

## 迭代教训总结

| 版本 | 方案 | 结果 | 教训 |
|------|------|------|------|
| v1 | OpenCV 轮廓提取 | ❌ 模糊不可识 | 算法轮廓不是冰箱贴 |
| v2 | Pillow 手绘矢量 | ⚠️ 可辨识但生硬 | 手绘精度和风格有限 |
| v3 | AI 生成 + 直接裁剪合成 | ⚠️ 图标是反白剪影不符 | 提示词要精确到结构，不要用通用描述 |
| v4 | AI 生成精确建筑 + Pillow 合成 | ✅ 图标对上了但背景去不干净 | 需要白底去背处理 |
| v5 | 添加白描边+阴影 | ⚠️ 阴影太淡+文字被图标遮挡 | 图标尺寸要缩小留文字空间 |
| v6 | 完整贴纸效果流水线 | ✅ 冰箱贴感满配 | 白描边+阴影+手写字体+合理间距 |

**关键原则**：AI 做创意（图标生成），Pillow 做精确（去背+描边+阴影+文字）。

## 配套工具

| 阶段 | 工具 | 备注 |
|------|------|------|
| 原图分析 | `vision_analyze` | 提取精确建筑结构特征 |
| 图标生成 | `ark-image-gen.sh` (Seedream) | 1920×1920，提示词要精确 |
| 贴纸效果 | Python Pillow | 去背→白描边→阴影→文字→拼合 |
| 效果审图 | `vision_analyze` | 检查: 描边? 阴影? 文字? 匹配度? |

## 手写字体安装

WSL 中无 sudo 时（pip 方式不可行），从 Google Fonts CDN 直接下载：
```bash
mkdir -p ~/.fonts
# 先获取实际下载 URL
curl -s "https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700"
# 再用 gstatic URL 下载
curl -sL "https://fonts.gstatic.com/s/dancingscript/v29/If2cXTr6YS-zF4S-kcSWSVi_sxjsohD9F50Ruu7BMSoHTQ.ttf" \
  -o ~/.fonts/DancingScript.ttf
fc-cache -f ~/.fonts/
```
然后在 Pillow 中用 `ImageFont.truetype(os.path.expanduser("~/.fonts/DancingScript.ttf"), size)` 加载。
