#!/usr/bin/env python3
"""
SDXL LoRA Training Script for ModelScope (魔搭) T4 GPU
======================================================
Train a character-specific LoRA on 10-20 face photos.
Output: zhuzhu_lora.safetensors (~100MB)

Usage in ModelScope Studio Jupyter Notebook:
    1. Upload 10-20 photos to ./train_data/
    2. Run this script (30 min on T4)
    3. Output saved to ./output/zhuzhu_lora.safetensors

Prerequisites:
    pip install diffusers transformers accelerate peft safetensors torchvision

    ⚠️ 2026-05-21 实测：魔搭 DSW-GPU 预装的环境可能存在 peft/transformers
    版本冲突（ImportError: HybridCache）。如遇此错误，先在终端运行：
        pip install --upgrade transformers peft
    然后跳过本脚本的 pip install 行，直接运行训练循环。
    （详见父 skill 的 references/modelscope-lora-workflow.md 第五节）
"""

import os, torch, math
from diffusers import StableDiffusionXLPipeline, DDPMScheduler, AutoencoderKL
from diffusers.optimization import get_scheduler
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from torchvision import transforms
from pathlib import Path
from peft import LoraConfig, get_peft_model

# ======== PRE-FLIGHT CHECK ========
print("🔍 环境预检...")
try:
    import peft, transformers
    # Verify HybridCache exists (peft compat check)
    from transformers import HybridCache
    print(f"  ✅ peft {peft.__version__}, transformers {transformers.__version__}")
except ImportError as e:
    print(f"  ❌ 版本冲突: {e}")
    print("  💡 请先在终端运行: pip install --upgrade transformers peft")
    print("  📖 详见 skill references/modelscope-lora-workflow.md 第5节")
    exit(1)

# ======== CONFIG ========
IMAGE_DIR = "./train_data"       # Place 10-20 face photos here
TRIGGER_WORD = "zhuzhu"          # Trigger word for inference
RESOLUTION = 1024
BATCH_SIZE = 1
LEARNING_RATE = 1e-4
MAX_STEPS = 800                  # 20-30 min on T4
RANK = 64                        # LoRA rank
LORA_ALPHA = RANK * 2

# ======== DATASET ========
class FaceDataset(Dataset):
    def __init__(self, image_dir, res=1024):
        paths = list(Path(image_dir).glob("*"))
        self.paths = [p for p in paths if p.suffix.lower() in ('.jpg','.jpeg','.png')]
        print(f"📸 找到 {len(self.paths)} 张照片")
        self.tfm = transforms.Compose([
            transforms.Resize(res), transforms.CenterCrop(res),
            transforms.ToTensor(), transforms.Normalize([0.5],[0.5]),
        ])
        descs = ["studio lighting","natural lighting","candid smile",
                 "elegant pose","detailed face","fashion look"]
        self.caps = [f"{TRIGGER_WORD}, portrait of a young woman, beautiful face, {d}"
                     for d in descs]
    def __len__(self): return len(self.paths)
    def __getitem__(self, i):
        img = Image.open(self.paths[i]).convert("RGB")
        return {"px": self.tfm(img), "cap": self.caps[i % len(self.caps)]}

# ======== LOAD SDXL ========
print("🔄 加载 SDXL (ModelScope 镜像)...")
vae = AutoencoderKL.from_pretrained(
    "AI-ModelScope/sdxl-vae-fp16-fix", torch_dtype=torch.float16)
pipe = StableDiffusionXLPipeline.from_pretrained(
    "AI-ModelScope/stable-diffusion-xl-base-1.0", vae=vae,
    torch_dtype=torch.float16, variant="fp16", use_safetensors=True)
pipe.to("cuda")
tokenizer, text_encoder = pipe.tokenizer, pipe.text_encoder
noise_scheduler = DDPMScheduler.from_pretrained(
    "AI-ModelScope/stable-diffusion-xl-base-1.0", subfolder="scheduler")

# ======== SETUP LORA ========
pipe.unet.requires_grad_(False)
lora_cfg = LoraConfig(
    r=RANK, lora_alpha=LORA_ALPHA,
    target_modules=["to_q","to_k","to_v","to_out.0"])
pipe.unet = get_peft_model(pipe.unet, lora_cfg)
pipe.unet.train()
opt = torch.optim.AdamW(pipe.unet.parameters(), lr=LEARNING_RATE)

# ======== TRAIN ========
dataset = FaceDataset(IMAGE_DIR)
loader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)
print(f"🎯 开始训练 {MAX_STEPS} 步...")

step = 0
for epoch in range(999):
    for batch in loader:
        if step >= MAX_STEPS: break
        txt = tokenizer(batch["cap"], padding="max_length",
               max_length=77, truncation=True, return_tensors="pt")
        with torch.no_grad():
            embed = text_encoder(txt.input_ids.to("cuda"))[0]
        latents = pipe.vae.encode(
            batch["px"].to("cuda", dtype=torch.float16)).latent_dist.sample()
        latents = latents * pipe.vae.config.scaling_factor
        noise = torch.randn_like(latents)
        ts = torch.randint(0, noise_scheduler.config.num_train_timesteps,
                          (latents.shape[0],), device="cuda").long()
        noisy = noise_scheduler.add_noise(latents, noise, ts)
        pred = pipe.unet(noisy, ts, embed).sample
        loss = torch.nn.functional.mse_loss(pred.float(), noise.float())
        loss.backward(); opt.step(); opt.zero_grad(); step += 1
        if step % 100 == 0:
            print(f"  Step {step}/{MAX_STEPS} | Loss: {loss.item():.6f}")
    if step >= MAX_STEPS: break

print("✅ 训练完成！")

# ======== SAVE LORA ========
os.makedirs("./output", exist_ok=True)
pipe.unet.save_pretrained("./output")
from diffusers.utils import convert_unet_state_dict_to_lora
from safetensors.torch import save_file
sd = convert_unet_state_dict_to_lora(pipe.unet.state_dict())
save_file(sd, "./output/zhuzhu_lora.safetensors")
sz = os.path.getsize("./output/zhuzhu_lora.safetensors") / 1024 / 1024
print(f"💾 LoRA 已保存: output/zhuzhu_lora.safetensors ({sz:.1f} MB)")
