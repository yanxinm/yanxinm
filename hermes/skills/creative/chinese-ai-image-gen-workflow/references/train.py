import os, torch
from diffusers import StableDiffusionXLPipeline, DDPMScheduler, AutoencoderKL
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from torchvision import transforms
from pathlib import Path
from peft import LoraConfig, get_peft_model
from modelscope import snapshot_download

IMAGE_DIR = "."
TRIGGER_WORD = "zhuzhu"
MAX_STEPS = 800
RANK = 64

class ZhuzhuDataset(Dataset):
    def __init__(self, image_dir, res=1024):
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

print("Loading SDXL...")
model_path = snapshot_download("AI-ModelScope/stable-diffusion-xl-base-1.0")
pipe = StableDiffusionXLPipeline.from_pretrained(
    model_path,
    torch_dtype=torch.float16, variant="fp16", use_safetensors=True,
    low_cpu_mem_usage=True,
)
pipe = pipe.to("cuda")
pipe.enable_vae_slicing()
pipe.enable_attention_slicing()
tokenizer, text_encoder = pipe.tokenizer, pipe.text_encoder
noise_scheduler = DDPMScheduler.from_pretrained(
    model_path, subfolder="scheduler")

pipe.unet.requires_grad_(False)
lora_cfg = LoraConfig(r=RANK, lora_alpha=RANK*2,
    target_modules=["to_q","to_k","to_v","to_out.0"])
pipe.unet = get_peft_model(pipe.unet, lora_cfg)
pipe.unet.train()
opt = torch.optim.AdamW(pipe.unet.parameters(), lr=1e-4)

dataset = ZhuzhuDataset(IMAGE_DIR)
loader = DataLoader(dataset, batch_size=1, shuffle=True)
print("Training started...")

step = 0
for epoch in range(999):
    for batch in loader:
        if step >= MAX_STEPS: break

        # Tokenize with both SDXL text encoders
        txt = tokenizer(batch["cap"], padding="max_length", max_length=77,
               truncation=True, return_tensors="pt")
        txt.input_ids = txt.input_ids.to(pipe.unet.device)

        txt_2 = pipe.tokenizer_2(batch["cap"], padding="max_length", max_length=77,
                truncation=True, return_tensors="pt")
        txt_2.input_ids = txt_2.input_ids.to(pipe.unet.device)

        with torch.no_grad():
            embed_1 = text_encoder(txt.input_ids)[0]
            outputs_2 = pipe.text_encoder_2(txt_2.input_ids, output_hidden_states=False)
            embed_2 = outputs_2.last_hidden_state
            pooled = outputs_2.pooler_output

            # Concatenate both text encoder outputs (SDXL-specific)
            embed = torch.cat([embed_1, embed_2], dim=-1)

            added_cond_kwargs = {
                "text_embeds": pooled,
                "time_ids": torch.tensor([[1024, 1024, 0, 0, 1024, 1024]],
                                          device=pipe.unet.device)
            }

        latents = pipe.vae.encode(batch["px"].to(device=pipe.unet.device,
                                   dtype=torch.float16)).latent_dist.sample()
        latents = latents * pipe.vae.config.scaling_factor
        noise = torch.randn_like(latents)
        ts = torch.randint(0, noise_scheduler.config.num_train_timesteps,
                          (latents.shape[0],), device=pipe.unet.device).long()
        noisy = noise_scheduler.add_noise(latents, noise, ts)
        pred = pipe.unet(noisy, ts, encoder_hidden_states=embed,
                         added_cond_kwargs=added_cond_kwargs).sample
        loss = torch.nn.functional.mse_loss(pred.float(), noise.float())
        loss.backward(); opt.step(); opt.zero_grad(); step += 1
        if step % 100 == 0:
            print(f"  Step {step}/{MAX_STEPS} | Loss: {loss.item():.6f}")
    if step >= MAX_STEPS: break

print("Training complete!")
os.makedirs("./output", exist_ok=True)
pipe.unet.save_pretrained("./output")
from diffusers.utils import convert_unet_state_dict_to_lora
from safetensors.torch import save_file
sd = convert_unet_state_dict_to_lora(pipe.unet.state_dict())
save_file(sd, "./output/zhuzhu_lora.safetensors")
print(f"Saved: output/zhuzhu_lora.safetensors")
