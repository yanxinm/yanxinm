# apikey.fun Image Generation Test Results — 2026-05-20

> 📝 **后续更新 (2026-05-25)**: 端点从 `api.apikey.fun` 切换为 `slb.apikey.fun`（专线），冷启动时间缩短~1s。所有模型和参数不变，但 `gpt-image-2` 的超时从 120s 调整为 180s（有时需更长时间）。详见 `fridge-magnet-poster` 技能的 `gpt-image-2` 调用方式。

## Test Photos
1. **BBQ Camping** (man grilling at campsite)
2. **Family of 3** (man/white shirt/sunglasses, woman/red shirt/white cardigan, girl/red shirt/adidas jacket) on bench, Yandang Mountain
3. **Xuankong Temple** (Hanging Temple, Shanxi)

## Summary Table

| Test | Model | Mode | Prompt Length | Status | Time | User Verdict |
|------|-------|------|-------------|--------|------|-------------|
| BBQ→Manga | gpt-image-1.5 | text-to-image | ~60 chars | ✅ 200 | 120s | ⭐ "这个更好" |
| BBQ→Manga | Seedream | img2img | long | ✅ 200 | **16s** | OK, but gpt preferred |
| Family→Manga v1 | gpt-image-2 | img2img | ~40 chars | ✅ 200 | 77s | ❌ 4 people, Fuji bg |
| Family→Manga v2 | gpt-image-2 | img2img | ~90 chars (constrained) | ❌ 524 | 127s | — |
| Family→Manga v3 | gpt-image-2 | img2img | ~60 chars | ❌ 524 | 127s | — |
| Family→Manga v4 | gpt-image-2 | img2img | ~50 chars | ✅ 200 | 108s | 3 people ✅, green bg ✅, no Fuji ✅, but no sunglasses/adidas |
| Family→Manga | gpt-image-1.5 | text-to-image | ~100 chars | ✅ 200 | 120s | Fuji bg, 4 people ❌ |
| Family→Manga | gpt-image-1.5 | img2img | ~40 chars | ❌ 524 | 128s | — |
| Family→Manga | Seedream | img2img | long (w/ gpt-4o) | ✅ 200 | **16s** | faithful ✅ |
| Xuankong→Fridge | gpt-image-1.5 | text-to-image | ~60 chars | ✅ 200 | 72s | white border, shadow, text ✅ |
| Xuankong→Vintage | gpt-image-1.5 | text-to-image | ~80 chars (short) | ✅ 200 | 72s | ochre top, ink line art, DAT info ✅ |
| Xuankong→Vintage | gpt-image-1.5 | text-to-image | ~400 chars (long) | ❌ 524 | 126s | — |
| Xuankong→Watercolor | gpt-image-1.5 | text-to-image | ~80 chars | ❌ 524 | 127s | — |
| Xuankong→Watercolor | gpt-image-1.5 | text-to-image | ~45 chars | ✅ 200 | 70s | pastel watercolor, warm ✅ |

## Key Findings

### gpt-image-2 (model: "gpt-image-2")
- **Only img2img mode works** (text-to-image always times out)
- **Only works with very short prompts** (< ~60 chars)
- **Creative reinterpretation behavior**: tends to add people (family of 3 → 4 with extra children), change backgrounds (green mountains → Fuji with lake), modify clothing colors/details (remove sunglasses, change brand logos)
- **⚠️ Celebrity likeness protection**: when prompt contains a real person name (e.g., "Son Yoon-ju"), the model's revised_prompt adds "Do not depict an exact real-person likeness; use the described features only." This prevents accurate facial feature reproduction. **Fix**: use pure feature descriptions (oval face, almond eyes, high nose, M-lip, pale skin) instead of the celebrity name.
- **To maximize fidelity**: keep prompt extremely short, only specify the absolute minimum constraints, avoid real person names
- **Response format**: base64 data in the `b64_json` field
- **Success rate**: ~50% (2/4 attempts succeeded)

### gpt-image-1.5 (model: "gpt-image-1.5")
- **Only text-to-image mode works** (img2img with image parameter always 524)
- **Prompt length sensitivity**: 
  - < 80 chars: ✅ usually works (70-120s)
  - > 80 chars: ❌ times out (524)
- **Response format**: base64 data in the `b64_json` field (not `url`)
- **Also creatively interprets**: will change backgrounds to iconic scenes (Fuji) and may add/change people
- **Success rate**: ~60% for text-to-image, 0% for img2img

### Seedream (doubao-seedream-4-5-251128)
- **Always reliable**: 5/5 attempts succeeded
- **Fastest**: 16s average
- **Most faithful**: preserves original composition, people count, clothing colors
- **No prompt length issues**
- **Minimum size**: 1920×1920 (3,686,400 pixels)
- **Recommended size**: 2048×2048

### Preferred Pipeline (per user priority)
1. gpt-image-2 img2img (short prompt) — for pure GPT effect
2. gpt-image-1.5 text-to-image (short prompt) — fallback
3. gpt-4o analyze → Seedream img2img — for speed + fidelity
4. gpt-4o analyze → gpt-image-1.5 text-to-image — for GPT style with analysis

### ⚠️ Always check response format
```python
# Both gpt-image-2 and gpt-image-1.5 return base64 in b64_json
import base64
b64 = response["data"][0]["b64_json"]
# b64_json may be a raw base64 string or a data: URI
if b64.startswith("data:"):
    _, encoded = b64.split(",", 1)
    img_data = base64.b64decode(encoded)
else:
    img_data = base64.b64decode(b64)
```
