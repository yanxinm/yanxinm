# Diffusers 官方训练脚本 SDXL LoRA 执行计划

## 目标
使用 Diffusers 官方 `train_text_to_image_lora_sdxl.py` 脚本 + 魔搭可用 SDXL 基座训练 LoRA。

## ⚠️ 2026-05-26 实战更新
- **RealVisXL_V4.0 不在魔搭上**（HuggingFace `SG161222/RealVisXL_V4.0`），魔搭无镜像
- **hf-mirror.com 下载不可行**（魔搭外网带宽极低 ~1.7 KB/s）
- **使用标准 SDXL 0.9**（魔搭 `AI-ModelScope/stable-diffusion-xl-base-0.9`）作为基座，~2 分钟下完
- **SDXL 1.0** 魔搭下载可能卡住（~10GB 大文件超时），优先用 0.9
- **训练命令参数**：用 `--train_data_dir` 代替 `--dataset_name` 引用本地 metadata.csv

## 魔搭模型可用性速查
| 模型 | 魔搭状态 | 下载方式 |
|------|---------|---------|
| `AI-ModelScope/stable-diffusion-xl-base-0.9` | ✅ | `snapshot_download("AI-ModelScope/stable-diffusion-xl-base-0.9")` |
| `AI-ModelScope/stable-diffusion-xl-base-1.0` | ⚠️ 可能超时 | 同上，大文件下载可能无响应 |
| `AI-ModelScope/RealVisXL_V4.0` | ❌ 不存在 | HuggingFace `SG161222/RealVisXL_V4.0` |
| hf-mirror.com → 任何 HF 模型 | ❌ 带宽不足 | 魔搭外网出口极窄 |

## 预计时间
- 环境准备（DSW 重启后恢复）：3-5 分钟
- 模型下载：2-5 分钟（SDXL 0.9，魔搭内网）
- 训练：20-30 分钟（A10 24GB）
- 推理测试：1-2 分钟

## Step 1: 环境恢复（实例重启后必做！）
DSW 实例闲置关闭后重启，venv 目录在但 pip/torch 全丢：
```bash
# 重建 venv
rm -rf /mnt/workspace/lora_env && python3 -m venv /mnt/workspace/lora_env
source /mnt/workspace/lora_env/bin/activate && pip install --upgrade pip setuptools wheel

# 装 torch cu124
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124

# 装其他依赖
pip install "diffusers[training]" accelerate datasets tensorboard peft transformers -i https://mirrors.aliyun.com/pypi/simple/
pip install huggingface_hub modelscope -i https://mirrors.aliyun.com/pypi/simple/

# 验证
python3 -c "import torch; print('CUDA:', torch.cuda.is_available(), '| torch:', torch.__version__)"
```
> 2026-05-26 实测：diffusers 0.38.0 本次**没有**偷升级 torch，无需最后重装 cu124。
> 如果验证显示 `torch: 2.12.0+cu130` → 说明被偷升级了，需重装 `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124`

## Step 2: 下载官方训练脚本
```bash
cd /mnt/workspace/zhuzhu_photos
wget https://raw.githubusercontent.com/huggingface/diffusers/main/examples/text_to_image/train_text_to_image_lora_sdxl.py
```

## Step 3: 脚本版本兼容性补丁
脚本要求 `diffusers >= 0.39.0.dev0`，但 pip 装的是 0.38.0。贴这个：
```bash
sed -i 's/"0.39.0.dev0"/"0.38.0"/' train_text_to_image_lora_sdxl.py
python3 train_text_to_image_lora_sdxl.py --help 2>&1 | head -5
```
验证输出显示 `usage:` 即可。

## Step 4: 下载 SDXL 基座（魔搭内网）
```bash
source /mnt/workspace/lora_env/bin/activate && python3 -c "
from modelscope import snapshot_download
path = snapshot_download('AI-ModelScope/stable-diffusion-xl-base-0.9')
print('✅ Model path:', path)
"
```
> 魔搭路径中包含 `0___9`（双下划线替代点号）。
> 如果下载卡住按 Ctrl+C 重试，或换 1.0：`AI-ModelScope/stable-diffusion-xl-base-1.0`

## Step 5: 准备 metadata.csv
```bash
source /mnt/workspace/lora_env/bin/activate && cd /mnt/workspace/zhuzhu_photos && python3 -c "
from pathlib import Path
import random
caps = ['studio lighting','natural lighting','candid smile','elegant pose','detailed face','fashion look','street style','golden hour','casual walk']
imgs = [p for p in Path('.').glob('*') if p.suffix.lower() in ('.jpg','.jpeg','.png')]
with open('metadata.csv','w') as f:
    f.write('file_name,text\n')
    for img in imgs:
        cap = f'zhuzhu, portrait of a young woman, beautiful face, {random.choice(caps)}'
        f.write(f'{img.name},{cap}\n')
print(f'Wrote {len(imgs)} captions to metadata.csv')
"
```

## Step 6: 运行训练
```bash
source /mnt/workspace/lora_env/bin/activate && cd /mnt/workspace/zhuzhu_photos && \
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True && \
CUDA_VISIBLE_DEVICES=0 python3 train_text_to_image_lora_sdxl.py \
  --pretrained_model_name_or_path="/mnt/workspace/.cache/modelscope/models/AI-ModelScope/stable-diffusion-xl-base-0___9" \
  --train_data_dir="/mnt/workspace/zhuzhu_photos" \
  --caption_column="text" \
  --resolution=768 \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --max_train_steps=1000 \
  --learning_rate=1e-4 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --output_dir="/mnt/workspace/zhuzhu_photos/output-sdxl" \
  --mixed_precision="fp16" \
  --rank=64 \
  --checkpointing_steps=500 \
  --validation_prompt="zhuzhu, a young woman at Xuanwu Lake, Nanjing, photorealistic, high quality, detailed face" \
  --report_to="tensorboard" \
  --seed=42
```

> **参数说明**：
> - `--train_data_dir`：指定本地图片目录（自动读取 metadata.csv）
> - `--caption_column="text"`：metadata.csv 中的描述列名
> - `--rank=64`：LoRA 矩阵秩，64 对人脸足够
> - `--resolution=768`：SDXL 0.9 原生分辨率
> - `--gradient_accumulation_steps=4`：等效 batch size=4，A10 24GB 可承受
> - 注意：没有 `--dataset_name`，用 `--train_data_dir` 替代

## Step 7: 推理测试
> ⚠️ **魔搭 SDXL 是 `.bin` 格式**（非 `.safetensors`），`from_pretrained()` 可用但必须去掉 `variant='fp16'` 和 `use_safetensors=True`。
> 模型目录结构是标准 Diffusers 格式（有 `unet/`、`vae/`、`text_encoder/` 子目录），无需 `from_single_file()`。

```bash
source /mnt/workspace/lora_env/bin/activate && python3 -c "
import torch
from diffusers import StableDiffusionXLPipeline

model_path = '/mnt/workspace/.cache/modelscope/models/AI-ModelScope/stable-diffusion-xl-base-0___9'
pipe = StableDiffusionXLPipeline.from_pretrained(
    model_path, torch_dtype=torch.float16, low_cpu_mem_usage=True)
pipe.load_lora_weights('/mnt/workspace/zhuzhu_photos/output-sdxl')
pipe = pipe.to('cuda')

img = pipe(
    prompt='zhuzhu, a young woman standing at Xuanwu Lake, Nanjing, frontal view, facing camera, smiling, photorealistic, high quality, detailed face, lake background',
    negative_prompt='cartoon, anime, illustration, distorted face',
    num_inference_steps=50, height=768, width=768,
    guidance_scale=7.5).images[0]
img.save('/mnt/workspace/zhuzhu_photos/zhuzhu_xuanwu_sdxl.png')
print('✅ Saved!')
"
```

## 潜在风险与排查
1. **OOM** — A10 24GB 预计显存 ~12GB。如 OOM 把 gradient_accumulation_steps 从 4 降到 2
2. **NaN** — 官方脚本已用 AMP + GradScaler，概率低。如 NaN 把 `--mixed_precision` 改为 `"no"`
3. **xformers 未安装** — 去掉 `--enable_xformers_memory_efficient_attention`（当前命令没用）
4. **训练卡住** — 首次运行有模型加载/缓存预热，前 2-3 分钟无输出正常；5 分钟无输出按 Ctrl+C 重试
5. **图片数量为 0** — `metadata.csv` 中 `file_name` 列必须匹配实际文件名
6. **推理报错 `variant=fp16` 不存在** — 魔搭 SDXL 模型是 `.bin` 格式，**不要传 `variant='fp16'`**。
7. **推理报错 `model.safetensors not found`** — 同上，魔搭模型是 `.bin` 格式，**不要传 `use_safetensors=True`**。

## 实战记录
详见 `references/session-20260526-lora-b-plan-sdxl09.md`

## 退路方案
| 方案 | 说明 |
|------|------|
| 自定义 SDXL 训练循环 | NaN 风险高，不推荐 |
| SD 1.5 + RANK=64 + lr=1e-4 | 训练稳，人脸上限不如 SDXL |
| Seedream 图生图 | 每张上传等几秒，有抠图效应 |
| ComfyUI 本地 | 需本地 GPU（计划中） |
