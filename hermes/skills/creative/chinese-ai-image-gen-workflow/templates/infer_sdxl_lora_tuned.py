# SDXL LoRA 调优推理模板（DPM++ Karras + 多场景/多分辨率/多种子）
# 用途：在魔搭 DSW A10 上对训练好的 SDXL LoRA 做批量质量评估
# 调用前：source /mnt/workspace/lora_env/bin/activate && cd /mnt/workspace/zhuzhu_photos
#
# ⚠️ 新旧 LoRA 对比时：复制一份脚本，改 LORA_PATH 和 OUT_DIR 即可
#     如 LORA_PATH='./output-sdxl' vs './output-sdxl-1024'
#     OUT_DIR='infer_old'           vs 'infer_a4'

import torch, os
from diffusers import StableDiffusionXLPipeline, DPMSolverMultistepScheduler

MODEL_PATH = '/mnt/workspace/.cache/modelscope/models/AI-ModelScope/stable-diffusion-xl-base-0___9'
LORA_PATH = './output-sdxl-1024'   # ★ 改这里切换 LoRA 版本
OUT_DIR = 'infer_a4'               # ★ 输出目录，区分不同 LoRA 版本的结果

os.makedirs(OUT_DIR, exist_ok=True)

# ── 加载模型 ──
# ⚠️ 魔搭 SDXL 是 .bin 格式，不能传 variant='fp16' 或 use_safetensors=True
pipe = StableDiffusionXLPipeline.from_pretrained(
    MODEL_PATH, torch_dtype=torch.float16, low_cpu_mem_usage=True)
pipe.load_lora_weights(LORA_PATH)
pipe = pipe.to('cuda')

# DPM++ 2M Karras — 30 步 ≈ 原 DDIM 40-50 步质量
pipe.scheduler = DPMSolverMultistepScheduler.from_config(
    pipe.scheduler.config, use_karras_sigmas=True)

# ── 参数矩阵 ──
scenes = [
    ('玄武湖', 'standing at Xuanwu Lake, Nanjing, cherry blossoms, spring morning, soft golden light, lake reflections, depth of field, photorealistic, 8k, detailed face, natural skin pores, film grain, Fujifilm Pro 400H'),
    ('街巷', 'on an old Nanjing street, historic buildings, afternoon sun, candid walking shot, natural expression, shallow depth of field, photorealistic, 8k, detailed face, natural skin, Leica Summilux 50mm f/1.4, cinematic'),
    ('书店', 'inside Librairie Avant-Garde bookstore, Nanjing, surrounded by books, warm ambient tungsten light, reading pose, photorealistic, 8k, detailed face, soft shadows, Zeiss Otus 55mm, portrait lighting'),
]

resolutions = [
    ('sq', 1024, 1024),
    ('pt', 768, 1024),
    ('pt2', 896, 1152),   # 竖图更大脸
]

LORA_SCALE = 0.7        # 0.5-0.8 之间微调，低了脸不像高了过拟合
SEEDS = [42, 888, 7777]
STEPS = 30
CFG = 5.5

NEG = (
    'cartoon, anime, 3d render, illustration, painting, drawing, sketch, '
    'distorted face, bad anatomy, extra fingers, fused fingers, ugly, deformed, '
    'blurry, low quality, watermark, text, signature, oversaturated, plastic skin, '
    'doll-like, unnatural skin, airbrushed, generic face, cloned face'
)

# ── 批量生成 ──
total = len(scenes) * len(resolutions) * len(SEEDS)
count = 0
for name, prompt in scenes:
    for rname, h, w in resolutions:
        for seed in SEEDS:
            gen = torch.Generator('cuda').manual_seed(seed)
            label = f'{name}-{rname}-s{seed}'
            count += 1
            print(f'[{count}/{total}] {label}...')
            img = pipe(
                prompt=f'zhuzhu, a young woman, {prompt}',
                negative_prompt=NEG,
                num_inference_steps=STEPS,
                height=h, width=w,
                guidance_scale=CFG,
                cross_attention_kwargs={'scale': LORA_SCALE},
                generator=gen
            ).images[0]
            fname = os.path.join(OUT_DIR, f'infer_{label}.png')
            img.save(fname)
            print(f'  OK {fname}')

print(f'---ALL {total} DONE @ {OUT_DIR}---')
