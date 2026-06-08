#!/usr/bin/env python3
"""
LoRA Inference — Generate character in any scene
=================================================
After training, use this script to generate the character in any scene.

Usage:
    python3 inference_lora.py

Prerequisites:
    pip install diffusers peft safetensors

The script assumes the LoRA is at ./output/ and uses trigger word "zhuzhu".
Modify the test_prompts list below for different scenes.
"""

import torch
from diffusers import StableDiffusionXLPipeline
from peft import PeftModel

LORA_PATH = "./output"
MODEL_ID = "AI-ModelScope/stable-diffusion-xl-base-1.0"
TRIGGER = "zhuzhu"

print(f"🔄 加载基础模型 + LoRA ({LORA_PATH})...")

pipe = StableDiffusionXLPipeline.from_pretrained(
    MODEL_ID, torch_dtype=torch.float16,
    variant="fp16", use_safetensors=True)
pipe.unet = PeftModel.from_pretrained(pipe.unet, LORA_PATH)
pipe.to("cuda")

test_prompts = [
    # 南京街头
    f"{TRIGGER}, young woman on Nanjing street, historic buildings, plane trees, "
    f"photorealistic portrait, natural daylight, DSLR quality",

    # 南京夫子庙
    f"{TRIGGER}, young woman at Confucius Temple in Nanjing, traditional architecture, "
    f"beautiful face, stylish outfit, photorealistic portrait",

    # 南京玄武湖
    f"{TRIGGER}, young woman by Xuanwu Lake Nanjing, willow trees, lake, "
    f"golden hour lighting, photorealistic portrait, high detail",
]

neg = "cartoon, anime, illustration, distorted face, bad anatomy"

for i, prompt in enumerate(test_prompts):
    print(f"\n🎨 生成 {i+1}/{len(test_prompts)}: {prompt[:60]}...")
    img = pipe(
        prompt=prompt, negative_prompt=neg,
        num_inference_steps=30, guidance_scale=7.5,
        height=1024, width=1024,
    ).images[0]
    path = f"./output/test_{i+1}.png"
    img.save(path)
    print(f"  ✅ {path}")

print("\n🎉 全部完成！")
