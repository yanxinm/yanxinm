#!/usr/bin/env python3
"""
扫描件PDF OCR工具 — 针对图片式PDF（扫描件）做文字识别
支持中文 + 英文混合识别

用法:
    python scan_pdf_ocr.py <pdf_path> [-o output.md]

依赖:
    pip install pymupdf
    apt install tesseract-ocr tesseract-ocr-chi-sim
"""

import sys
import os
import argparse
import subprocess
import tempfile

try:
    import fitz  # PyMuPDF
except ImportError:
    print("需要安装 PyMuPDF: pip install pymupdf")
    sys.exit(1)


def ocr_pdf(pdf_path: str, lang: str = "chi_sim+eng", dpi: int = 300) -> str:
    """对扫描件PDF做OCR，返回提取的文本"""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"文件不存在: {pdf_path}")

    doc = fitz.open(pdf_path)
    pages_text = []

    for i in range(len(doc)):
        page = doc[i]
        # 先尝试提取原生文字（如果是混合型PDF）
        native_text = page.get_text().strip()
        if native_text:
            pages_text.append(f"--- 第{i+1}页（原生文字）---\n{native_text}")
            continue

        # 否则渲染页面进行OCR
        pix = page.get_pixmap(dpi=dpi)
        tmp_path = f"/tmp/hermes_ocr_page_{i}.png"
        pix.save(tmp_path)

        result = subprocess.run(
            ["tesseract", tmp_path, "stdout", "-l", lang],
            capture_output=True, text=True, timeout=60
        )
        os.unlink(tmp_path)

        if result.returncode == 0:
            pages_text.append(f"--- 第{i+1}页（OCR识别）---\n{result.stdout.strip()}")
        else:
            pages_text.append(f"--- 第{i+1}页（OCR失败）---\n{result.stderr}")

    doc.close()
    return "\n\n".join(pages_text)


def main():
    parser = argparse.ArgumentParser(description="扫描件PDF OCR转文字")
    parser.add_argument("pdf_path", help="PDF文件路径")
    parser.add_argument("-o", "--output", help="输出Markdown文件路径（默认打印到终端）")
    parser.add_argument("--lang", default="chi_sim+eng", help="OCR语言（默认: chi_sim+eng）")
    parser.add_argument("--dpi", type=int, default=300, help="渲染DPI（默认: 300）")

    args = parser.parse_args()

    print(f"正在OCR识别: {args.pdf_path}")
    text = ocr_pdf(args.pdf_path, args.lang, args.dpi)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✅ 结果已保存: {args.output}")
    else:
        print(text)

    print(f"\n共 {len(text)} 字符")


if __name__ == "__main__":
    main()
