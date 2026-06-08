#!/bin/bash
# 豆包 Seedream 图片生成脚本
# 用法: ./ark-image-gen.sh "提示词" [模型] [尺寸] [数量]
# 模型可选: doubao-seedream-4-0-250828, doubao-seedream-4-5-251128, doubao-seedream-5-0-260128
# 尺寸可选: 1024x1024, 2048x2048, 等
# 默认模型: doubao-seedream-4-5-251128 (最新版)

PROMPT="${1:?错误：请提供提示词}"
MODEL="${2:-doubao-seedream-4-5-251128}"
SIZE="${3:-2048x2048}"
N="${4:-1}"

# 从 .env 读取密钥
ARK_KEY=$(grep '^ARK_IMAGE_API_KEY=' ~/.hermes/.env | head -1 | cut -d'=' -f2- | xargs)

if [ -z "$ARK_KEY" ]; then
  echo "错误：未找到 ARK_IMAGE_API_KEY，请检查 ~/.hermes/.env"
  exit 1
fi

echo "🎨 正在生成图片..."
echo "模型: $MODEL"
echo "提示: $PROMPT"
echo "尺寸: $SIZE"
echo ""

RESPONSE=$(curl -s -X POST "https://ark.cn-beijing.volces.com/api/v3/images/generations" \
  -H "Authorization: Bearer $ARK_KEY" \
  -H "Content-Type: application/json" \
  -d "$(jq -n \
    --arg model "$MODEL" \
    --arg prompt "$PROMPT" \
    --arg size "$SIZE" \
    --argjson n "$N" \
    '{model: $model, prompt: $prompt, size: $size, n: $n, response_format: "url", watermark: false}'
  )" 2>/dev/null)

HTTP_CODE=$?
if [ $HTTP_CODE -ne 0 ]; then
  echo "❌ 请求失败 (curl exit code: $HTTP_CODE)"
  echo "$RESPONSE"
  exit 1
fi

# 检查是否有错误
ERROR_MSG=$(echo "$RESPONSE" | jq -r '.error.message // empty')
if [ -n "$ERROR_MSG" ]; then
  echo "❌ API错误: $ERROR_MSG"
  echo "$RESPONSE" | jq '.'
  exit 1
fi

echo "✅ 生成成功！"
echo "$RESPONSE" | jq -r '.data[] | .url' | while read -r URL; do
  echo "📷 $URL"
done

# 显示使用信息
echo ""
echo "📊 用量: $(echo "$RESPONSE" | jq -r '.usage | "\(.generated_images)张图片, \(.output_tokens) tokens"')"

# 保存图片到本地缓存目录
CACHE_DIR="$HOME/.hermes/cache/images"
mkdir -p "$CACHE_DIR"

echo "$RESPONSE" | jq -r '.data[] | .url' | while read -r URL; do
  TS=$(date +%Y%m%d_%H%M%S)
  LOCAL_PATH="$CACHE_DIR/seedream_${TS}_$(echo "$URL" | md5sum | cut -c1-8).jpeg"
  curl -s -o "$LOCAL_PATH" "$URL" 2>/dev/null
  echo "💾 已保存: $LOCAL_PATH"
done
