#!/usr/bin/env python3
"""
水彩插画修图 — Seedream 图生图 (img2img)
将照片转为水彩插画风格，支持家庭合照/聚会庆祝/自定义场景。

用法:
  python3 watercolor-img2img.py --input <照片路径> --type family|party
  python3 watercolor-img2img.py --input <照片路径> --prompt "自定义提示词"
  python3 watercolor-img2img.py --input <照片路径> --type family --size 2048x2048

API Key 从 ~/.hermes/.env 的 ARK_IMAGE_API_KEY 读取。
"""

import argparse
import base64
import json
import os
import re
import sys
import time
from pathlib import Path

import cv2
import numpy as np
import requests
from PIL import Image

# ─── 常量 ──────────────────────────────────────────────────────────────

API_URL = "https://ark.cn-beijing.volces.com/api/v3/images/generations"
MODEL = "doubao-seedream-4-5-251128"  # 最新稳定版
MIN_PIXELS = 3_686_400  # 1920×1920
DEFAULT_SIZE = "2048x2048"
CACHE_DIR = os.path.expanduser("~/.hermes/cache/images")
ENV_FILE = os.path.expanduser("~/.hermes/.env")
ENV_KEY = "ARK_IMAGE_API_KEY"

# ─── 提示词模板 ───────────────────────────────────────────────────────

PROMPTS = {
    "family": (
        "Convert this family photo into a warm watercolor illustration "
        "with hand-drawn black sketch outlines. "
        "Style: hand-drawn speed-sketch black outline (varying thickness, organic lines) "
        "+ soft watercolor wash fills, warm pastel color palette "
        "(beige, light purple, light blue, pink, low saturation). "
        "Decorative handwritten text like 'love' and 'Happy together' "
        "in casual script font. "
        "Small decorative hearts, stars and flower doodles scattered around the edges. "
        "Abstract background with soft watercolor color blots/splashes "
        "in beige/pink/purple. "
        "Overall warm, cozy, commemorative illustration style, "
        "like a personalized family keepsake. "
        "No realistic photo texture, full hand-drawn illustration feel."
    ),
    "party": (
        "Convert this group party photo into a warm watercolor illustration "
        "with hand-drawn black sketch outlines. "
        "Style: hand-drawn speed-sketch black outline (varying thickness) "
        "+ soft watercolor wash fills, warm pastel color palette. "
        "Many people celebrating together. "
        "Decorative handwritten text like 'Good Friends, Great Memories!' "
        "and 'BEST DAY EVER' and 'CHEERS!' in casual script. "
        "Small decorative hearts, star doodles, party balloons, "
        "bunting/garlands, crown scattered around. "
        "Abstract background with soft watercolor color blots/splashes. "
        "Overall warm, festive, commemorative illustration style. "
        "No realistic photo texture, full hand-drawn illustration feel."
    ),
}

# ─── 工具函数 ──────────────────────────────────────────────────────────


def load_api_key() -> str:
    """从 .env 文件读取 ARK_IMAGE_API_KEY"""
    if not os.path.exists(ENV_FILE):
        print(f"❌ 错误：未找到 {ENV_FILE}")
        sys.exit(1)

    with open(ENV_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(ENV_KEY + "="):
                # 支持带或不带引号的值
                val = line.split("=", 1)[1].strip().strip('"').strip("'")
                if val:
                    return val

    print(f"❌ 错误：未在 {ENV_FILE} 中找到 {ENV_KEY}")
    sys.exit(1)


def image_to_data_uri(img: np.ndarray, fmt: str = "jpeg") -> str:
    """将 OpenCV BGR 图像转为 base64 data URI"""
    success, buf = cv2.imencode(f".{fmt}", img)
    if not success:
        print("❌ 错误：图像编码失败")
        sys.exit(1)
    b64 = base64.b64encode(buf).decode("utf-8")
    return f"data:image/{fmt};base64,{b64}"


def ensure_min_size(img: np.ndarray) -> np.ndarray:
    """检查并调整图像到最小像素要求"""
    h, w = img.shape[:2]
    pixels = w * h

    if pixels >= MIN_PIXELS:
        return img

    # 需要放大
    scale = np.sqrt(MIN_PIXELS / pixels) * 1.02  # 稍大一点确保满足
    new_w = int(w * scale)
    new_h = int(h * scale)
    # 确保至少 1920 一边
    if new_w < 1920 and new_h < 1920:
        if w >= h:
            new_w = 1920
            new_h = int(h * 1920 / w)
        else:
            new_h = 1920
            new_w = int(w * 1920 / h)
    # 确保偶数
    new_w = new_w + (new_w % 2)
    new_h = new_h + (new_h % 2)

    print(f"📐 原图 {w}x{h} 像素不足 ({pixels:,} < {MIN_PIXELS:,})")
    print(f"📐 自动放大至 {new_w}x{new_h}")
    return cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)


def save_result(image_url: str, out_name: str = None) -> str:
    """下载结果图片到缓存目录"""
    os.makedirs(CACHE_DIR, exist_ok=True)

    ts = time.strftime("%Y%m%d_%H%M%S")
    if out_name:
        filename = f"watercolor_{out_name}_{ts}.jpeg"
    else:
        filename = f"watercolor_{ts}.jpeg"

    out_path = os.path.join(CACHE_DIR, filename)

    resp = requests.get(image_url, timeout=60)
    if resp.status_code != 200:
        print(f"❌ 下载结果图片失败: HTTP {resp.status_code}")
        sys.exit(1)

    with open(out_path, "wb") as f:
        f.write(resp.content)

    return out_path


# ─── 主流程 ────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="水彩插画修图 — Seedream 图生图"
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="输入照片路径",
    )
    parser.add_argument(
        "--type", "-t",
        choices=["family", "party", "custom"],
        default="family",
        help="场景类型（默认: family）",
    )
    parser.add_argument(
        "--prompt", "-p",
        default=None,
        help="自定义提示词（覆盖场景模板）",
    )
    parser.add_argument(
        "--size", "-s",
        default=DEFAULT_SIZE,
        help=f"输出尺寸（默认: {DEFAULT_SIZE}）",
    )
    parser.add_argument(
        "--model", "-m",
        default=MODEL,
        help=f"模型（默认: {MODEL}）",
    )

    args = parser.parse_args()
    input_path = os.path.expanduser(args.input)

    # ── 1. 读取输入图片 ──
    if not os.path.exists(input_path):
        print(f"❌ 错误：文件不存在 — {input_path}")
        sys.exit(1)

    img = cv2.imread(input_path)
    if img is None:
        print(f"❌ 错误：无法读取图片 — {input_path}")
        sys.exit(1)

    h, w = img.shape[:2]
    print(f"🖼️  输入: {w}x{h}")

    # ── 2. 检查/调整尺寸 ──
    img = ensure_min_size(img)
    h, w = img.shape[:2]
    print(f"🎨 处理后尺寸: {w}x{h} ({w*h:,} px)")

    # ── 3. 转为 base64 data URI ──
    data_uri = image_to_data_uri(img)
    print(f"🔑 Base64: {len(data_uri):,} chars")

    # ── 4. 拼装提示词 ──
    if args.prompt:
        prompt = args.prompt
        print(f"📝 使用自定义提示词")
    elif args.type in PROMPTS:
        prompt = PROMPTS[args.type]
        print(f"📝 使用 {args.type} 场景模板")
    else:
        print(f"❌ 错误：未知场景类型 '{args.type}'")
        sys.exit(1)

    print(f"📝 提示词: {prompt[:80]}...")

    # ── 5. 加载 API Key ──
    api_key = load_api_key()

    # ── 6. 调用 API ──
    print(f"🚀 调用 Seedream ({args.model}) 图生图...")
    print(f"   输出尺寸: {args.size}")

    payload = {
        "model": args.model,
        "prompt": prompt,
        "image": data_uri,
        "size": args.size,
        "n": 1,
        "response_format": "url",
        "watermark": False,
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    try:
        resp = requests.post(API_URL, headers=headers, json=payload, timeout=120)
    except requests.exceptions.Timeout:
        print("❌ 错误：API 请求超时（120s）")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"❌ 错误：API 请求失败 — {e}")
        sys.exit(1)

    if resp.status_code != 200:
        print(f"❌ API 错误 (HTTP {resp.status_code}):")
        try:
            err = resp.json()
            print(json.dumps(err, indent=2, ensure_ascii=False))
        except Exception:
            print(resp.text[:500])
        sys.exit(1)

    result = resp.json()

    # ── 7. 处理响应 ──
    data = result.get("data", [])
    if not data:
        print("❌ 错误：API 返回空 data")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        sys.exit(1)

    image_url = data[0].get("url", "")
    if not image_url:
        print("❌ 错误：返回数据中没有 URL")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        sys.exit(1)

    # 显示用量
    usage = result.get("usage", {})
    if usage:
        gen_count = usage.get("generated_images", 1)
        tokens = usage.get("output_tokens", "?")
        print(f"📊 用量: {gen_count} 张, {tokens} tokens")

    # ── 8. 下载保存 ──
    out_path = save_result(image_url, out_name=args.type)
    file_size = os.path.getsize(out_path)
    print(f"\n✅ 水彩插画完成！")
    print(f"   保存: {out_path}")
    print(f"   大小: {file_size / 1024:.0f} KB")
    print(f"   模型: {args.model}")
    print(f"\n📷 MEDIA:{out_path}")


if __name__ == "__main__":
    main()
