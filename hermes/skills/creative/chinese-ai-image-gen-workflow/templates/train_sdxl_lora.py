"""
SDXL LoRA Training on ModelScope DSW-GPU (A10 24GB)
Last updated: 2026-05-25

STATUS: NaN at Step 100 — still an open problem with custom training loop.
This template represents the latest approach being tested:
fp16 model + fp32 LoRA + GradScaler + clamp + gradient_checkpointing.

Run:
  export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
  source /mnt/workspace/lora_env/bin/activate
  cd /mnt/workspace/zhuzhu_photos && python3 train.py
"""

import os
import torch
from diffusers import StableDiffusionXLPipeline, DDPMScheduler
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from torchvision import transforms
from pathlib import Path
from peft import LoraConfig, get_peft_model
from modelscope import snapshot_download

IMAGE_DIR = "."
TRIGGER_WORD = "zhuzhu"
MAX_STEPS = 800
RANK = 16


class ZhuzhuDataset(Dataset):
    """Dataset for SDXL LoRA training with person photos and captions."""

    def __init__(self, image_dir, res=768):
        paths = list(Path(image_dir).glob("*"))
        self.paths = [
            p for p in paths if p.suffix.lower() in (".jpg", ".jpeg", ".png")
        ]
        print(f"Photos: {len(self.paths)}")
        self.tfm = transforms.Compose([
            transforms.Resize(res),
            transforms.CenterCrop(res),
            transforms.ToTensor(),
            transforms.Normalize([0.5], [0.5]),
        ])
        caps = [
            "studio lighting", "natural lighting", "candid smile",
            "elegant pose", "detailed face", "fashion look",
        ]
        self.caps = [
            f"{TRIGGER_WORD}, portrait of a young woman, beautiful face, {d}"
            for d in caps
        ]

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, i):
        img = Image.open(self.paths[i]).convert("RGB")
        return {"px": self.tfm(img), "cap": self.caps[i % len(self.caps)]}


# === MODEL LOADING ===
print("Loading SDXL...")
model_path = snapshot_download("AI-ModelScope/stable-diffusion-xl-base-1.0")
pipe = StableDiffusionXLPipeline.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    variant="fp16",
    use_safetensors=True,
    low_cpu_mem_usage=True,
)
pipe = pipe.to("cuda")
pipe.vae.enable_slicing()
pipe.unet.gradient_checkpointing_enable()

tokenizer = pipe.tokenizer
text_encoder = pipe.text_encoder
noise_scheduler = DDPMScheduler.from_pretrained(model_path, subfolder="scheduler")

# === LORA SETUP ===
pipe.unet.requires_grad_(False)
lora_cfg = LoraConfig(
    r=RANK,
    lora_alpha=RANK,
    target_modules=["to_q", "to_k", "to_v", "to_out.0"],
)
pipe.unet = get_peft_model(pipe.unet, lora_cfg)
pipe.unet.train()

opt = torch.optim.AdamW(
    [p for p in pipe.unet.parameters() if p.requires_grad],
    lr=5e-6,
)
scaler = torch.cuda.amp.GradScaler()

# === DATASET ===
dataset = ZhuzhuDataset(IMAGE_DIR)
loader = DataLoader(dataset, batch_size=1, shuffle=True)
print("Training started...")

# === TRAINING LOOP ===
step = 0
for epoch in range(999):
    for batch in loader:
        if step >= MAX_STEPS:
            break

        # SDXL dual tokenizer
        txt = tokenizer(
            batch["cap"], padding="max_length", max_length=77,
            truncation=True, return_tensors="pt",
        )
        txt.input_ids = txt.input_ids.to(pipe.unet.device)
        txt_2 = pipe.tokenizer_2(
            batch["cap"], padding="max_length", max_length=77,
            truncation=True, return_tensors="pt",
        )
        txt_2.input_ids = txt_2.input_ids.to(pipe.unet.device)

        # Text encoder forward (frozen)
        with torch.no_grad():
            embed_1 = text_encoder(txt.input_ids)[0]
            outputs_2 = pipe.text_encoder_2(
                txt_2.input_ids, output_hidden_states=False,
            )
            embed_2 = outputs_2.last_hidden_state
            pooled = outputs_2.text_embeds
            embed = torch.cat([embed_1, embed_2], dim=-1)
            added_cond_kwargs = {
                "text_embeds": pooled,
                "time_ids": torch.tensor(
                    [[768, 768, 0, 0, 768, 768]], device=pipe.unet.device
                ),
            }

        # VAE encode
        latents = pipe.vae.encode(
            batch["px"].to(device=pipe.unet.device, dtype=torch.float16)
        ).latent_dist.sample()
        latents = latents * pipe.vae.config.scaling_factor

        # Forward diffusion
        noise = torch.randn_like(latents)
        ts = torch.randint(
            0, noise_scheduler.config.num_train_timesteps,
            (latents.shape[0],), device=pipe.unet.device,
        ).long()
        noisy = noise_scheduler.add_noise(latents, noise, ts)
        noisy = torch.clamp(noisy, -10.0, 10.0)

        # UNet pred + loss (under autocast)
        with torch.amp.autocast("cuda"):
            pred = pipe.unet(
                noisy, ts,
                encoder_hidden_states=embed,
                added_cond_kwargs=added_cond_kwargs,
            ).sample
            loss = torch.nn.functional.mse_loss(pred.float(), noise.float())

        # Backward + step (under GradScaler)
        scaler.scale(loss).backward()
        scaler.unscale_(opt)
        torch.nn.utils.clip_grad_norm_(pipe.unet.parameters(), max_norm=1.0)
        scaler.step(opt)
        scaler.update()
        opt.zero_grad()
        step += 1

        if step % 100 == 0:
            print(f"  Step {step}/{MAX_STEPS} | Loss: {loss.item():.6f}")

    if step >= MAX_STEPS:
        break

print("Training complete!")
os.makedirs("./output", exist_ok=True)
pipe.unet.save_pretrained("./output")
from diffusers.utils import convert_unet_state_dict_to_lora
from safetensors.torch import save_file

sd = convert_unet_state_dict_to_lora(pipe.unet.state_dict())
save_file(sd, "./output/zhuzhu_lora.safetensors")
print("Saved: output/zhuzhu_lora.safetensors")
