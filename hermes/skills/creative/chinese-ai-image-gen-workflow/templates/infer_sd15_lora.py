# SD 1.5 LoRA 推理测试模板
# 用法：复制到训练输出目录（如 /mnt/workspace/zhuzhu_photos/）p
# 运行：python3 infer_sd15.py

import torch
from diffusers import StableDiffusionPipeline
from safetensors.torch import load_file
from modelscope import snapshot_download

model_path = snapshot_download("AI-ModelScope/stable-diffusion-v1-5")
pipe = StableDiffusionPipeline.from_pretrained(
    model_path, torch_dtype=torch.float32, use_safetensors=True,
    low_cpu_mem_usage=True, safety_checker=None)
pipe = pipe.to("cuda")

# 方式A: 从 safetensors 文件加载（推荐）
lora_state = load_file("output/zhuzhu_lora.safetensors")
pipe.unet.load_state_dict(lora_state, strict=False)

# 方式B: 从目录加载（如果保存的是目录）
# from peft import PeftModel
# pipe.unet = PeftModel.from_pretrained(pipe.unet, "./output/zhuzhu_lora")

prompt = ("zhuzhu, a young woman standing at Xuanwu Lake, Nanjing, "
          "frontal view, facing camera, smiling, photorealistic, "
          "high quality, detailed face")
negative = "cartoon, anime, illustration, distorted face, bad anatomy, blurry"

print("Generating...")
with torch.no_grad():
    img = pipe(
        prompt=prompt,
        negative_prompt=negative,
        num_inference_steps=50,
        height=512, width=512,
        guidance_scale=7.5,
    ).images[0]

img.save("output_test.png")
print("Saved: output_test.png")
