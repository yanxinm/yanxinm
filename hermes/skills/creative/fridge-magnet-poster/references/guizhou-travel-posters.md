# gpt-image-2 图片生成经验（贵州自驾海报项目）

## 2026-06-20 关键发现

### 1. API Key 401 问题
直接调用 `https://slb.apikey.fun/v1/images/generations` 时出现 `HTTP 401 Unauthorized`。
**解决方案**：通过 Hermes Web UI 端点中转：
```bash
TOKEN=$(cat ~/.hermes-web-ui/.token)
curl -sS -X POST "http://127.0.0.1:8648/api/hermes/media/apikey-image-generate" \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode":"text","prompt":"...","size":"1024x1440","output_path":"/tmp/out.jpg"}'
```
⚠️ **注意**：Python 中拼接字符串时避免 `***` 导致语法错误（shell 或 Python 可能误解析）。用 `python3 -c "..."` 单行命令最安全。

### 2. gpt-image-2 中文文字不可靠
| 期望 | AI 生成 |
|------|--------|
| 浠岸酒店 | 西安酒店 |
| 夺夺粉 | 多多粉 |
| 裹卷 | 锅卷 |
| 7.18 周六 | 7.18 Saturday |

**根因**：gpt-image-2 对复杂汉字的字形渲染不稳定，尤其是非常用字（浠、裹）。
**对策**：行程信息图的海报**必须用 PIL 代码排版**，文生图仅用于生成装饰性插图（底部风景线描等）。

### 3. 尺寸异常
gpt-image-2 有时返回非标准尺寸（如 941×1672 而非请求的 1024×1440）。需检查后 resize。

### 4. 提示词技巧
- 中文地名/美食名在提示词中用**拼音+英文辅助**可提高准确率（但无法根治）
- 描述布局时用"3 rows 2 columns"比详细坐标更有效
- 明确写"NO WATERMARKS"减少水印

## 2026-06-20 迭代日志（Day 1 安顺海报）

### v1 — 初始尝试
- 失败：直接调用 apikey.fun 端点 401
- 改用 Web UI 端点成功

### v2 — 冰箱贴模板（被用户否决）
- 用户反馈：冰箱贴模板不适合行程信息图，文字放上去不好看
- 教训：区分"冰箱贴打卡"和"行程信息图"两种海报类型

### v3 — 方案2 PIL代码排版
- 效果：用户评价"太丑"
- 教训：用户偏好文生图的视觉设计感，但中文文字必须准确

### v4 — 文生图修正
- 酒店名"浠岸"→"Xi岸"（拼音识别错误）
- 美食"夺夺粉裹卷"→"多多粉锅卷"（字形相似错误）
- 问候语变成通用模板"旅途愉快..."而非"出发啦！贵阳见～"

### v5 — 拼音辅助
- 酒店名改为"西安酒店"（浠→西，字形混淆）
- 美食改为"多多粉锅卷"（夺→多，裹→锅）
- 教训：拼音辅助只能缓解不能根治

### v6 — 加入拼音标注
- 问候语变成拼音 "Chu Fa La Gui Yang Jian"
- 教训：gpt-image-2 对非标准中文词汇（问候语）容易输出拼音而非汉字

### v7 — 修正航班信息
- 加入真实航班数据：10:35 南京禄口T2 → 13:15 贵阳龙洞堡T3
- 租车信息：13:30 店员送车上门
- 问候语正确显示中文
- 日期 7.18 字号最大，Day 1 字号较小（符合用户要求）
- 酒店名正确：浠岸酒店
- 美食名正确：夺夺粉裹卷
- **关键发现**：在提示词末尾追加 "ALL CHINESE TEXT MUST BE ACCURATE" 和具体拼音标注能提高准确率

### v8 — 最终版
- 所有信息准确
- 时间线按实际行程顺序排列
- 天气穿搭放最后
- 无黄果树（Day 1 是安顺不是黄果树）
- 输出：`/home/miao/出图/Day1_安顺_终稿.jpg`

### 提示词模板（v7 验证有效）
```
Vertical travel itinerary poster 9:16, clean modern Xiaohongshu style.
TOP: greeting "出发啦贵阳见" small light gray with leaf icon.
Then date 7.18 Saturday in LARGE bold font.
Then Day 1 in smaller muted green font below date.
Divider line.
MIDDLE TIMELINE: N events vertically with time labels, connected by subtle vertical line.
[每个事件：时间 + 图标 + 中文描述]
BOTTOM: weather + outfit info.
Subtle line art decoration. Warm cream background.
Sharp readable Chinese text. No watermarks.
```

**关键参数**：
- 问候语用小字浅色放最顶部
- 日期 7.18 用最大字号
- Day 1 用较小字号
- 时间线事件按实际发生顺序排列
- 天气穿搭永远放最后
- 底部装饰用"subtle line art"不要太显眼
- 明确说"No watermarks"

## 2026-06-22 新发现：全中文 prompt + taste-skill 四风格验证

### 背景
用户要求用 taste-image-gen 的四个风格模板（小红书面包风/Ins旅行风/复古海报风/国潮扁平风）各出一版同款 Day 1 行程海报。之前 v3-v6 认为"gpt-image-2 中文文字不可靠，必须 PIL 代码排版"，本次验证推翻了这个结论。

### 方法
**全中文 prompt** — 整段提示词用纯中文写，详细描述每个行程节点的排版位置、颜色、图标。末尾加英文约束 `ALL CHINESE TEXT MUST BE ACCURATE`。

示例 prompt 结构：
```
9:16竖版旅行行程海报 [风格描述]
顶部: [问候语](字体颜色) [日期](小字颜色)
中间时间线: [描述串联方式]
[时间] [地点]([色块颜色])
...
底部: 天气[数据] 穿搭[建议]
[装饰风格] 无英文无拼音
NO watermark NO English text ALL CHINESE TEXT MUST BE ACCURATE
```

### 结果
| 风格 | 文件 | 大小 | 中文准确率 |
|------|------|------|-----------|
| 小红书面包风 | Day1_01_xiaohongshu_bakery.jpg | 1.5MB | ✅ 全部正确 |
| Ins旅行风 | Day1_02_ins_travel.jpg | 2.3MB | ✅ 全部正确 |
| 复古海报风 | Day1_03_vintage_poster.jpg | 3.0MB | ✅ 全部正确 |
| 国潮扁平风 | Day1_04_guochao_flat.jpg | 2.6MB | ✅ 全部正确 |

所有中文字（含"浠岸酒店""夺夺粉""裹卷""顾府街""儒林路""虹山湖"等非常用字）均准确渲染。

### 对之前规律的修正
1. **全中文 prompt 优于英文 prompt** — 英文 prompt 里写中文词会被翻译/误读（浠岸→Xi An），全中文 prompt 反而准确
2. **"ALL CHINESE TEXT MUST BE ACCURATE" 在末尾有效** — 作为安全网强制约束
3. **无需 PIL 代码排版作为唯一方案** — 文生图在正确 prompt 策略下可以胜任，但需要 vision_analyze 验证
4. **size 约束**：1024×1440 可以，但注意最低 655K 像素

### 建议工作流
1. 全中文写 prompt（不用英文/拼音替代中文词）
2. 末尾加 `ALL CHINESE TEXT MUST BE ACCURATE NO English text`
3. 生成后用 vision_analyze 逐字验证（酒店名/美食名/生僻字）
4. 发现错字：修正 prompt 重试，不要退回到 PIL

## 相关文件
- 拼合脚本：`templates/travel-poster-compose.py`
- 信息图脚本：`templates/travel-poster-info.py`
- taste-image-gen skill 四风格：`~/.hermes/skills/taste-image-gen/SKILL.md`
- 主技能：`SKILL.md`
