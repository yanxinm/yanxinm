# SD 1.5 LoRA 训练模板
# 用法：复制到魔搭 DSW 的 /mnt/workspace/zhuzhu_photos/ 目录下
# 前置条件：source /mnt/workspace/lora_env/bin/activate
# 环境变量：export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
# 运行：python3 train_sd15.py

import os, torch
from diffusers import StableDiffusionPipeline, DDPMScheduler
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
    def __init__(self, image_dir, res=512):
        paths = list(Path(image_dir).glob("*"))
        self.paths = [p for p in paths if p.suffix.lower() in ('.jpg','.jpeg','.png')]
        print(f"Photos: {len(self.paths)}")
        self.tfm = transforms.Compose([
            transforms.Resize(res), transforms.CenterCrop(res),
            transforms.ToTensor(), transforms.Normalize([0.5],[0.5])])
        caps = ["studio lighting","natural lighting","candid smile",
                "elegant pose","detailed face","fashion look"]
        self.caps = [f"{TRIGGER_WORD}, portrait of a young woman, beautiful face, {d}" for d in caps]
    def __len__(self): return len(self.paths)
    def __getitem__(self, i):
        img = Image.open(self.paths[i]).convert("RGB")
        return {"px": self.tfm(img), "cap": self.caps[i % len(self.caps)]}

print("Loading SD 1.5...")
model_path = snapshot_download("AI-ModelScope/stable-diffusion-v1-5")
pipe = StableDiffusionPipeline.from_pretrained(
    model_path, torch_dtype=torch.float32, use_safetensors=True,
    low_cpu_mem_usage=True, safety_checker=None)
pipe = pipe.to("cuda")
pipe.enable_attention_slicing()
tokenizer = pipe.tokenizer
noise_scheduler = DDPMScheduler.from_pretrained(model_path, subfolder="scheduler")

pipe.unet.requires_grad_(False)
lora_cfg = LoraConfig(r=RANK, lora_alpha=RANK,
    target_modules=["to_q","to_k","to_v","to_out.0"])
pipe.unet = get_peft_model(pipe.unet, lora_cfg)
pipe.unet.train()
opt = torch.optim.AdamW(
    [p for p in pipe.unet.parameters() if p.requires_grad], lr=5e-6)

dataset = ZhuzhuDataset(IMAGE_DIR)
loader = DataLoader(dataset, batch_size=1, shuffle=True)
print("Training started...")

step = 0
for epoch in range(999):
    for batch in loader:
        if step >= MAX_STEPS: break
        txt = tokenizer(batch["cap"], padding="max_length", max_length=77,
                        truncation=True, return_tensors="pt")
        txt.input_ids = txt.input_ids.to(pipe.unet.device)
        encoder_hidden_states = pipe.text_encoder(txt.input_ids)[0]
        latents = pipe.vae.encode(batch["px"].to(device=pipe.unet.device,
                                   dtype=torch.float32)).latent_dist.sample()
        latents = latents * pipe.vae.config.scaling_factor
        noise = torch.randn_like(latents)
        ts = torch.randint(0, noise_scheduler.config.num_train_timesteps,
                          (latents.shape[0],), device=pipe.unet.device).long()
        noisy = noise_scheduler.add_noise(latents, noise, ts)
        pred = pipe.unet(noisy, ts,
                         encoder_hidden_states=encoder_hidden_states).sample
        loss = torch.nn.functional.mse_loss(pred, noise)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(pipe.unet.parameters(), max_norm=1.0)
        opt.step()
        opt.zero_grad()
        step += 1
        if step % 100 == 0:
            print(f"  Step {step}/{MAX_STEPS} | Loss: {loss.item():.6f}")
    if step >= MAX_STEPS: break

print("Training complete!")
os.makedirs("./output", exist_ok=True)
pipe.unet.save_pretrained("./output/zhuzhu_lora")
print("Saved: output/zhuzhu_lora/")
