# OCR 当前状态

## 系统环境（2026-05-14）

- **Tesseract 已安装** ✅ — 含中文语言包 `chi_sim+eng`，可以处理中文扫描件
- **安装方式**：`sudo apt install tesseract-ocr tesseract-ocr-chi-sim`
- **扫描件 PDF 识别质量**：印刷体效果较好，手写体精度有限

## 处理扫描件 PDF 的工作原理

1. 用 PyMuPDF 先尝试提取原生文字
2. 如果有原生文字 → 直接返回（速度快，零误差）
3. 如果没有 → 逐页渲染为图片，用 Tesseract OCR 识别

## 检测方法

```python
import shutil
# 返回路径表示 tesseract 已安装
tesseract_path = shutil.which("tesseract")
```

判断 PDF 是否为扫描件：

```python
import fitz
doc = fitz.open("文件.pdf")
for i, page in enumerate(doc):
    text = page.get_text()
    if not text.strip():
        print(f"第{i+1}页: 扫描件/图片式PDF，需要OCR")
doc.close()
```

## 专用脚本

```bash
python ~/.hermes/skills/productivity/markitdown/scripts/scan_pdf_ocr.py \
  "扫描件.pdf" -o 输出.md
```

## 局限性

- **手写体识别**：中文手写体（特别是潦草字迹）识别准确率较低
- **排版复杂**：表格嵌套、多栏排版可能识别错乱
- **图像质量**：低分辨率/模糊扫描件会影响识别效果
- **音频转文字**：需额外依赖（Whisper 类模型）
