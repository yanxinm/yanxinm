---
name: markitdown
description: 将各种文件格式（Office 文档、PDF、图片（OCR）、HTML、CSV 等）转换为 Markdown，便于 AI 处理、知识库导入或文案复用。
category: productivity
tags: [文档转换, markdown, pdf转markdown, 文件处理, ocr]
---

# MarkItDown — 文件转 Markdown 技能

## 简介

基于 Microsoft 开源的 [MarkItDown](https://github.com/microsoft/markitdown) 库（v0.1.5），将多种格式的文件统一转换为 Markdown，方便后续 AI 分析、知识库导入或二次编辑。

## 支持的格式

| 格式 | 说明 |
|------|------|
| `.txt` | 纯文本 |
| `.csv` | CSV 表格数据 |
| `.json` | JSON 数据 |
| `.xml` | XML 数据 |
| `.html` / `.htm` | HTML 网页 |
| `.docx` | Word 文档 |
| `.pptx` | PowerPoint 演示文稿 |
| `.xls` / `.xlsx` | Excel 表格（旧版+新版） |
| `.pdf` | PDF 文档 |
| `.jpg` / `.png` / `.gif` / `.webp` 等 | 图片（OCR 提取文字） |
| `.mp3` / `.wav` / `.m4a` 等 | 音频（语音转文字） |
| `.epub` | 电子书 |
| `.ipynb` | Jupyter Notebook |
| `.msg` | Outlook 邮件 |
| `.zip` | 压缩包（解压后逐个处理内部文件） |

## 用法

### 导入与初始化

```python
from markitdown import MarkItDown
md = MarkItDown()
```

### 转换本地文件

```python
result = md.convert("/path/to/文件.docx")
print(result.text_content)  # 获取 Markdown 文本
```

或使用更明确的 `convert_local`：

```python
result = md.convert_local("/path/to/文件.pdf")
markdown_text = result.text_content
```

### 转换网页 URL

```python
result = md.convert_url("https://example.com/article.html")
print(result.text_content)
```

### 批量转换目录下所有文件

```python
from pathlib import Path
from markitdown import MarkItDown

md = MarkItDown()
input_dir = Path("/mnt/e/百度云同步盘/工作台账/待处理")
output_dir = Path("/mnt/e/百度云同步盘/工作台账/Markdown输出")
output_dir.mkdir(exist_ok=True)

for f in input_dir.glob("*"):
    if f.suffix.lower() in ['.docx', '.pptx', '.xlsx', '.pdf', '.txt', '.csv']:
        result = md.convert(str(f))
        out_path = output_dir / f"{f.stem}.md"
        out_path.write_text(result.text_content, encoding='utf-8')
        print(f"✅ {f.name} → {out_path.name}")
```

## 实用场景（针对老缪的业务）

### 1. 方案/合同转 Markdown 后导入 GBrain 知识库

```python
from markitdown import MarkItDown
md = MarkItDown()

# 把 Word 方案转成 Markdown
result = md.convert("/mnt/e/百度云同步盘/工作台账/活动方案.docx")
markdown_content = result.text_content

# 然后可以保存为 .md 文件，或直接喂给其他 AI 工具分析
```

### 2. 报表/Excel 数据转成结构化 Markdown 表格

```python
result = md.convert("/mnt/e/百度云同步盘/工作台账/抖音数据报表.xlsx")
print(result.text_content)  # 自动转为 Markdown 表格
```

### 3. 合同 PDF 扫描件提取文字

```python
result = md.convert("/mnt/e/百度云同步盘/工作台账/合同扫描件.pdf")
print(result.text_content)  # OCR 提取的文字内容
```

## 🔄 批量处理健壮性

批量处理大量文件（如5000+工作台账扫描）时需注意：

```python
from markitdown import MarkItDown
from docx import Document  # 备用：python-docx
from pathlib import Path

md = MarkItDown()
input_dir = Path("/mnt/e/百度云同步盘/工作台账/")
success, fail = 0, 0

for f in sorted(input_dir.rglob("*")):
    # 跳过临时文件和非文档
    if f.name.startswith("~$") or f.suffix.lower() not in ['.docx','.xlsx','.pdf','.doc','.xls','.pptx','.txt']:
        continue
    try:
        if f.suffix.lower() in ('.doc', '.xls'):
            # 旧格式：python-docx/openpyxl 可能无法直接读取，尝试用markitdown
            result = md.convert(str(f))
        else:
            result = md.convert(str(f))
        text = result.text_content
        if text.strip():
            success += 1
        else:
            # 空内容 → 可能是扫描件或格式不支持，记录
            fail += 1
    except Exception as e:
        # 单个文件失败不中断批量处理
        fail += 1
        
print(f"✅ 成功: {success} | ❌ 失败: {fail}")
```

### 常见失败原因
- **`.doc`旧格式**：markitdown不支持，需先用LibreOffice转`.docx`
- **扫描件PDF**：使用`scripts/scan_pdf_ocr.py`逐页OCR
- **文件路径含特殊字符**：中文引号、空格等需用`glob`模式匹配
- **损坏的`.docx`**：提示"Package not found"或"File is not a zip"，用python-docx的`Document()`尝试读取

## ⚠️ 已知限制：扫描件PDF

MarkItDown 内置的 PDF 转换器**只支持文字型 PDF**，对于**扫描件/图片式 PDF** 会返回空内容。已提供一个专用脚本解决：

```bash
python ~/.hermes/skills/productivity/markitdown/scripts/scan_pdf_ocr.py \
  "/mnt/e/百度云同步盘/工作台账/2026/新业务/项目论证会会议纪要.pdf" \
  -o /tmp/会议纪要_OCR.md
```

该脚本自动判断：有原生文字 → 直接提取；纯图片扫描件 → 用 Tesseract OCR 逐页识别。

## 注意事项

- **Tesseract OCR 已安装完成** ✅（含中英文语言包）
- **中文识别**：印刷体效果较好，手写体精度有限
- **音频转文字**：依赖系统音频处理和 Whisper 类模型，长音频可能较慢
- 已安装版本：**v0.1.5**（2026-02-20 发布，当前最新）
- MarkItDown 转换后的 Markdown 内容可以直接保存为 `.md` 文件

## 验证转换结果

```python
from markitdown import MarkItDown
md = MarkItDown()
result = md.convert("/mnt/e/百度云同步盘/工作台账/某个文件.docx")
text = result.text_content
print(f"转换成功！共 {len(text)} 字符")
# 检查内容是否完整
print(text[:500])  # 预览前500字
```
