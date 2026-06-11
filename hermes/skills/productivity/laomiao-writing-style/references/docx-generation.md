# .docx 公文生成指南（python-docx）

> 在 WSL/Linux 环境中用 python-docx 生成符合老缪排版规范的 Word 公文。
> 字体通过文档元数据设置——.docx 在 Windows Office 中打开时自动生效。

---

## 1. 完整生成函数

```python
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

def make_doc():
    doc = Document()
    
    for section in doc.sections:
        section.top_margin = Cm(2.54)
        section.bottom_margin = Cm(2.54)
        section.left_margin = Cm(3.17)
        section.right_margin = Cm(3.17)
    
    # 各元素类型
    paragraphs = [
        ("title", "紫金山事业部5月意识形态（网络意识形态）领域情况分析研判报告"),
        ("body", "现将5月意识形态领域情况及问题……做如下汇报。"),
        ("h1", "一、5月开展的意识形态工作"),
        ("body", "部门在工作部署时，将意识形态工作纳入日常工作布局……"),
        ("h1", "二、发现的问题及整改措施"),
        ("body", "无"),
        ("h1", "三、当前及下一阶段存在的风险隐患及应对措施"),
        ("h2", "1. 重点项目集中推进期的意识形态把关压力"),
        ("body", "6月将迎来……"),
        ("sign", "报送单位：紫金山事业部"),
        ("sign", "报送时间：2026年5月25日"),
        ("sign", "部门负责人签字并盖章："),
    ]
    
    for kind, text in paragraphs:
        if kind == "title":
            add_title(doc, text)
        elif kind == "h1":
            add_heading(doc, text, bold=True)
        elif kind == "h2":
            add_heading(doc, text, bold=True)
        elif kind == "body":
            add_body(doc, text)
        elif kind == "sign":
            add_signature(doc, text)
    
    doc.save("output.docx")
```

## 2. 元素生成函数

### 主标题（方正小标宋_GBK 22pt 居中）

```python
def add_title(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = Pt(28)
    run = p.add_run(text)
    run.font.size = Pt(22)
    run.font.name = '方正小标宋_GBK'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '方正小标宋_GBK')
```

### 一级/二级标题（黑体 16pt 加粗 首行缩进2字符）

```python
def add_heading(doc, text, bold=True):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Pt(32)
    p.paragraph_format.line_spacing = Pt(28)
    run = p.add_run(text)
    run.font.size = Pt(16)
    run.bold = bold
    run.font.name = '黑体'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
```

### 正文（仿宋_GB2312 16pt 首行缩进2字符）

```python
def add_body(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Pt(32)
    p.paragraph_format.line_spacing = Pt(28)
    run = p.add_run(text)
    run.font.size = Pt(16)
    run.font.name = '仿宋_GB2312'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '仿宋_GB2312')
```

### 落款（仿宋_GB2312 16pt 右对齐 无缩进）

```python
def add_signature(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p.paragraph_format.line_spacing = Pt(28)
    run = p.add_run(text)
    run.font.size = Pt(16)
    run.font.name = '仿宋_GB2312'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '仿宋_GB2312')
```

## 3. 从 Markdown 内容批量生成

推荐工作流：
1. 先用 markitdown 读取历史 docx 获取结构和风格参考
2. 按三段式结构写出 markdown 内容
3. 用 python-docx 逐段解析 markdown 并调用对应函数
4. 写入同步盘目录

```python
# 模式匹配参考
import re
line = line.strip()
if re.match(r'^[一二三四五六七八九十]+、', line):    # 一级标题
    add_heading(doc, line)  # 黑体
elif re.match(r'^\d+[\.\、]', line):                 # 二级标题/序号条
    add_heading(doc, line)  # 黑体
elif line.startswith(('报送单位', '报送时间', '部门负责人')):
    add_signature(doc, line)                         # 右对齐落款
else:
    add_body(doc, line)                              # 仿宋正文
```

## 4. 基地字体环境

基地已安装公文核心中文字体（Fandol + Noto CJK + cwTeX），并通过 fontconfig 设置了别名映射。

### 字体别名映射表

| docx 中使用的字体名 | 基地上实际渲染 | 用途 |
|---|---|---|
| 方正小标宋_GBK / 方正公文小标宋 | FandolSong Bold | 主标题 22pt |
| 仿宋_GB2312 / 仿宋 | FandolFang Regular | 正文 16pt |
| 黑体 / SimHei | FandolHei Bold | 一级标题 16pt |
| 楷体_GB2312 / 楷体 | FandolKai Regular | 落款/标注 |
| 宋体 / SimSun | FandolSong Regular | 表格/注释 |
| 微软雅黑 / Microsoft YaHei | Noto Sans CJK SC | PPT/新媒体 |
| Times New Roman | Liberation Serif | 英文数字 |
| Arial | Liberation Sans | PPT 英文 |

### 验证字体映射

```bash
fc-match "仿宋_GB2312"       # → FandolFang-Regular.otf
fc-match "方正小标宋_GBK"    # → FandolSong-Bold.otf
fc-match "黑体"              # → FandolHei-Bold.otf
```

### 字体文件位置

| 来源 | 路径 |
|---|---|
| Fandol（仿宋/宋/黑/楷） | `/usr/local/share/fonts/Fandol*.otf` |
| cwTeX（仿宋/黑/楷/明） | `/usr/share/fonts/truetype/cwtex/` |
| Noto CJK 全家桶 | `/usr/share/fonts/opentype/noto/` |
| 文泉驿 | `/usr/share/fonts/truetype/wqy/` |
| fontconfig 别名配置 | `~/.config/fontconfig/fonts.conf` |

> **注意**：Hermes 修改了 `$HOME`（到 `~/.hermes/profiles/jike/home/`），因此 fontconfig 配置文件需放在该路径下的 `.config/fontconfig/fonts.conf` 才能被加载。

## 5. 关键陷阱

| 陷阱 | 说明 |
|------|------|
| `first_line_indent` 属性名 | 是 `first_line_indent` 不是 `first_line_indent` |
| 字体可在基地预览 | 2026年6月已安装中文字体，`fc-match` 可验证。生成后可在基地直接验证结构 |
| 方正小标宋在 Windows 上 | Ethan 笔记本不一定自带此字体，.docx 在 Office 中会 fallback 到默认宋体。如需精确还原，需在 Ethan 上安装方正小标宋 |
| `set(qn('w:eastAsia'), ...)` 必须 | 只在 `run.font.name` 设中文名不生效，需加 XML 属性 |
| 行距最小 pt | `Pt(28)` 对应 28 磅固定行距。设置 `space_before/after` 为 0 避免额外间距 |
| 页边距单位 | `Cm()` 是厘米，不用 Cm 时默认单位是 EMU |

## 6. 验证方法

```python
from markitdown import MarkItDown
result = MarkItDown().convert("output.docx")
print(result.text_content[:500])  # 预览前500字
```
