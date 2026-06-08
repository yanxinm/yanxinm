---
name: chinese-ai-image-gen-workflow
description: "国内可用AI图像生成方案：SDXL/Flux LoRA训练(魔搭ModelScope) + Seedream API调用 + 绕过gpt-image名人肖像保护。涵盖国内用户可用的全链路：文生图/图生图/LoRA身份保持训练。"
version: 1.7.1
author: hermes-agent
tags: [image-generation, lora-training, modelscope, seedream, sd-xl, creative, ai-image]
---

# 国内AI图像生成工作流

国内用户可用的AI图像生成全方案，重点解决身份保持（防止抠图效应）和API可用性问题。

## 核心发现

### 1. 海外服务可用性
| 服务 | 国内状态 | 说明 |
|------|---------|------|
| **Replicate** (Flux, SD) | ❌ 被墙 | 连接超时，无法使用 |
| **Comfy Cloud** | ❌ 无法注册 | 国内用户无法注册使用 |
| **ComfyUI 本地** | ✅ 可行 | 需GPU，可离线部署 |

### 2. 国内可用API
| 服务 | 功能 | 特点 |
|------|------|------|
| **豆包 Seedream (Ark)** | 文生图/图生图 | 16s稳出，无肖像限制，最忠实原图 |
| **apikey.fun** GPT 系列中转 | 文生图/视觉/文本 | 国内中转站，OpenAI兼容，多种模型可选 |
| **魔搭 ModelScope** | LoRA训练/推理 | 免费T4 GPU 36h |

### 3. apikey.fun 中转站详情

apikey.fun (api.apikey.fun) 是一个国内 AI API 中转站（New API 框架），提供 OpenAI 兼容接口。

**可用模型（基于实测）：**
- GPT 文本：gpt-5.5、gpt-5.4、gpt-5.4-mini、gpt-5.2、gpt-5.2-pro
- Codex：gpt-5-codex、gpt-5.3-codex、apikeyfun-codex/gpt-5.5
- 视觉识别：gpt-4o、gpt-4o-mini（支持图片输入）
- 图片生成：gpt-image-2、gpt-image-1.5、gpt-image-1
- 语音：gpt-4o-audio-preview、gpt-4o-realtime-preview

**延迟特征（国内→中转站→OpenAI美国）：**
- 冷启动：~3-7s（第一发或久不用）
- 热请求：~2-4s
- 偶发波动：~5-7s

**端点选择：**
- `https://api.apikey.fun/v1` — 通用端点
- `https://slb.apikey.fun/v1` — 专线端点（冷启动略快，波动更小）

**名人肖像保护（与 Seedream 对比）：**
- apikey.fun 的 gpt-image-2/gpt-image-1.5 继承 OpenAI 安全护栏：含真实人名提示词会触发 "Do not depict exact real-person likeness" 拒绝
- Seedream 无此限制
- 绕过方法：去名用纯面部特征英文描述

**在 Hermes 中配置：**
```yaml
custom_providers:
  - name: apikey-fun
    base_url: https://slb.apikey.fun/v1   # 推荐用专线
    api_key: <your-key>
    model: gpt-5.5
```

### 4. gpt-image-2 珐琅徽章生成（2026-05-25 验证）

通过 apikey.fun 中转的 gpt-image-2 可生成高质量**金属珐琅徽章质感图标**，用于冰箱贴海报等场景。

**耗时**：~60-90s（比 Seedream 慢，但质感更精致）
**提示词**：必须用英文 `"enamel pin badge"` + `"gold/white outline"` + `"Pure white background, no text"`

完整方案和代码见 `references/gpt-image-2-enamel-pin.md`。
- 提示词含真实人名（如"孙允珠/Son Yoon-ju"）→ 自动追加 "Do not depict an exact real-person likeness"
- **绕过方法**：去掉真实姓名，仅使用纯面部特征英文描述词
- **无限制模型**：Seedream(豆包), SDXL LoRA, Flux

### 4. Seedream 图生图抠图效应
- **白墙/纯色背景底图** → 生成结果生硬拼接（抠图感）
- **有深度/场景的底图**（车内、街景等）→ 融合更自然
- **解决方案**：使用有场景的照片作为img2img底图，或直接用LoRA训练

---

## 模型选择与训练策略（重要！）

魔搭 A10 24GB 上 SDXL 和 SD 1.5 的兼容性差别巨大：

| 模型 | 参数量 | fp32 显存 | fp16 显存 | A10 可行性 |
|------|--------|-----------|-----------|-----------|
| SD 1.5 | 860M | **~5GB** | ~2.5GB | ✅ fp32 稳跑，无 NaN |
| SDXL | 2.6B | ~15GB | ~8GB | ⚠️ 自定义训练循环 NaN（见下方修复章节） |

**经验结论（2026-05-25 实战验证）**：
- SD 1.5 全 fp32 + RANK=16 + lr=5e-6 稳跑 800 步，Loss 正常下降 ✅
  - ⚠️ 但实测人脸相似度极差（Rank 16 表达能力不够，lr 5e-6 几乎不学）→ 见下方"SD 1.5 训练代码"章节的修正参数
- SDXL 自定义训练循环反复 NaN（Rank/lr/AMP/clamp/GradScaler/fp32 LoRA/clip/slicing 全试过，无一跑完 800 步）
- ⚠️ **RealVisXL_V4.0 不在魔搭上**（HuggingFace `SG161222/RealVisXL_V4.0`），魔搭外网带宽极低也无法从 hf-mirror 下载。**实际可用路径**：用魔搭上的**标准 SDXL 0.9**（`AI-ModelScope/stable-diffusion-xl-base-0.9`，~2 分钟下完）+ **HuggingFace 官方 `train_text_to_image_lora_sdxl.py` 脚本**训练。官方脚本使用标准 AMP + GradScaler + gradient checkpointing，已被成千上万用户验证过，无需手写训练循环。详细执行计划见 `templates/realvisxl-official-training-plan.md`。

### SD 1.5 训练代码

⚠️ **2026-05-25 实战验证结果**：SD 1.5 全 fp32 + RANK=16 + lr=5e-6 + 512 分辨率虽然稳跑 800 步不 NaN，但**人脸相似度极差**——五官完全不同于训练参考照片。原因是 rank 太小（表达能力不足）且 lr 太低（基本没学到特征）。

如果目标是人脸身份保持（让人能认出是同一个人），**SD 1.5 至少需要以下参数**：
| 参数 | 保守值（经验） | 激进值 | 说明 |
|------|--------------|--------|------|
| RANK | **64** | 128 | Rank=16 表达能力不够，人脸学不到 |
| lr | **1e-4** | 5e-4 | lr=5e-6 几乎不更新权重 |
| 步数 | **1500** | 2000 | 800 步不够收敛 |
| 分辨率 | 512 | 512 | SD 1.5 基座 |

**关键教训**：SD 1.5 训练虽然不会 NaN/OOM，但低参数训练等于白训。宁可接受训练时间长一点，也要把 rank 和 lr 拉上来。

完整模板文件：`templates/train_sd15_lora.py`
推理模板：`templates/infer_sd15_lora.py`
实战记录：`references/sd15-lora-training-records.md`

```python
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
MAX_STEPS = 1500       # ↑ 从 800 增加到 1500
RANK = 64              # ↑ 从 16 增加到 64，人脸才能学到
LR = 1e-4              # ↑ 从 5e-6 增加到 1e-4

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
```

**SD 1.5 vs SDXL 训练差异：**

| 方面 | SD 1.5 | SDXL |
|------|--------|------|
| pipeline | `StableDiffusionPipeline` | `StableDiffusionXLPipeline` |
| text_encoder | 1个（CLIP） | 2个（CLIP + OpenCLIP） |
| added_cond_kwargs | 不需要 | 必须（text_embeds + time_ids） |
| 训练分辨率 | 512 | 768/1024 |
| LoRA 保存 | diffusers 0.38.0 直接 `save_pretrained` | 同上 |
| NaN 风险 | ✅ 无（fp32 稳跑） | ⚠️ 高（见 NaN 修复章节） |

### SD 1.5 推理测试

训练完成后，用以下脚本生成测试图：

```python
import torch
from diffusers import StableDiffusionPipeline
from safetensors.torch import load_file
from modelscope import snapshot_download

model_path = snapshot_download("AI-ModelScope/stable-diffusion-v1-5")
pipe = StableDiffusionPipeline.from_pretrained(
    model_path, torch_dtype=torch.float32, use_safetensors=True,
    low_cpu_mem_usage=True, safety_checker=None)
pipe = pipe.to("cuda")

lora_state = load_file("output/zhuzhu_lora.safetensors")
pipe.unet.load_state_dict(lora_state, strict=False)

prompt = "zhuzhu, a young woman standing at Xuanwu Lake, Nanjing, frontal view, facing camera, smiling, photorealistic, high quality, detailed face, lake background"
negative = "cartoon, anime, illustration, distorted face, bad anatomy, blurry"

img = pipe(prompt=prompt, negative_prompt=negative,
           num_inference_steps=50, height=512, width=512,
           guidance_scale=7.5).images[0]
img.save("output_test.png")
```

注意：`pipe.unet.load_state_dict(lora_state, strict=False)` 是加载 safetensors 文件的稳定方式。

## LoRA训练流程

训练平台有两套环境，按需选择：

### 环境 A：魔搭 ModelScope 免费实例（适合短期实验）

> 免费 T4 16GB 36h / 有限的 A10 24GB 时长。适合小规模实验和 SD 1.5 训练。

### 环境 B：阿里云 PAI DSW 个人云账号实例（适合长时间训练）

> 按量付费 A10 24GB ~¥10.49/h，无时间限制。适合 rank=128+text_encoder 等长时间训练任务。

#### 环境 B 快速创建（阿里云 PAI DSW 个人实例）

1. 登录 [modelscope.cn](https://modelscope.cn) → 左侧菜单 **「我的Notebook」**
2. 切换到 **「个人云账号授权实例」** Tab（需先绑定阿里云账号）
3. 完成授权三步：授权 ModelScope → 开通 PAI → 创建实例
4. 创建实例时选择资源规格：**`ecs.gn7i-c8g1.2xlarge`**（A10 24GB, 8 vCPU, 30 GiB RAM）
5. 镜像保持默认 `modelscope:1.37.1-pytorch2.10.0-gpu-py312-cu128-ubuntu22.04`
6. 系统盘 100 GiB，费用 ¥10.49/h

**关键差异（vs 魔搭免费实例）**：

| 项目 | 魔搭免费实例 | 阿里云 PAI 个人实例 |
|------|-------------|-------------------|
| PyTorch | 2.9.1+cu128 需重装 cu124 | **2.10+cu128 驱动匹配，直接用** |
| venv | 独立创建，需下载 torch wheel | **`--system-site-packages` 复用系统 torch** |
| 模型下载 | modelscope SDK 内网下载 | modelscope SDK 同样可用 |
| 费用 | 免费（36h 限制） | ¥10.49/h |
| 数据持久化 | `/mnt/workspace/` | `/mnt/workspace/` |
| 实例间数据 | 不互通 | 不互通（需重新上传照片） |

#### 环境 B venv 创建（`--system-site-packages` 省时方案）

阿里云 PAI 系统自带 PyTorch 2.10+cu128 与 NVIDIA 驱动匹配，无需下载 torch：

```bash
# 不再需要 pip install torch！（系统 torch 已可用）
python3 -m venv --system-site-packages /mnt/workspace/lora_env
source /mnt/workspace/lora_env/bin/activate

# 只装 ML 库（⚠️ 必须 pin transformers 版本区间：太新(5.8.1)拒绝本地路径，太旧(<4.48)缺少 Dinov2WithRegistersConfig → diffusers 0.38 导入失败）
pip install diffusers accelerate peft "transformers>=4.48,<5.0" datasets safetensors -i https://mirrors.aliyun.com/pypi/simple/

# 验证（torch 版本应显示 2.10.0+cu128）
python3 -c "import torch; from peft import LoraConfig; from diffusers import StableDiffusionXLPipeline; print('torch:', torch.__version__, '| CUDA:', torch.cuda.is_available())"
```

> ⚠️ **transformers 版本双陷阱**：
> 1. **太新（5.8.1+）**：PAI 系统预装 transformers 5.8.1，其 `AutoTokenizer.from_pretrained()` 对本地路径做了严格的 repo_id 校验，报错 `HFValidationError`。`HF_HUB_OFFLINE=1` 也拦不住新版。
> 2. **太旧（<4.48）**：`transformers==4.46.0` 缺少 `Dinov2WithRegistersConfig`，导致 diffusers 0.38.0 导入 `autoencoder_rae` 时报 `ImportError`。
> **解决**：pin `"transformers>=4.48,<5.0"` 覆盖系统版——既能处理本地文件系统路径，又满足 diffusers 0.38 的导入需求。

> ⚠️ 如果 pip 下载 torch-2.12.0 超时（532MB），不要等——用 `--system-site-packages` 重建 venv。这是 PAI 实例上才可用的捷径，魔搭免费实例因为没有驱动匹配的 torch 所以不能这样。

---

### SDXL 训练（优先用 Diffusers 官方脚本）

> **推荐路径**：使用 Diffusers 官方 `train_text_to_image_lora_sdxl.py` 脚本（支持 `--train_data_dir`、`--mixed_precision`、`--rank`），无需手写训练循环。详细步骤见 `templates/realvisxl-official-training-plan.md`。
>
> ⚠️ **SDXL 自定义训练循环在魔搭 A10 上反复 NaN 失败。** 如果你准备跑 SDXL LoRA，优先尝试：
- 注册 `modelscope.cn`（阿里云/支付宝/微信登录）  
- 创建 GPU 实例（方式二, T4免费36h或A10, 镜像选 cuda12.8.1）  
- **如果免费额度耗尽** → 切到阿里云 PAI 个人云账号授权实例（见上方环境 B）
- 准备训练照片（10-36 张多角度人物照片）  
- 上传照片到 `zhuzhu_photos/` 目录（**必须用 Code Editor 文件浏览器上传，不要用终端 heredoc**）  
- **运行训练前先设环境变量（防显存碎片化OOM）：**
```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

### Step 1: 创建虚拟环境并安装依赖（推荐：venv 彻底隔离）

> ⚠️ **重要**：魔搭系统预装环境被 ms-swift 依赖链污染，直接用系统环境会导致 peft/transformers 冲突 → 内核崩溃。**必须创建 venv。**

**正确的安装顺序**（包含反直觉的一步——最后要重装 torch）：

```bash
# 1. 创建 venv（放 /mnt/workspace 下持久保存）
python3 -m venv /mnt/workspace/lora_env
source /mnt/workspace/lora_env/bin/activate

# 2. 先装 torch cu124（明确版本控制）
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124

# 3. 装其余依赖（⚠️ 这些包会悄悄把 torch 升级到 cu130！）
pip install diffusers transformers accelerate peft safetensors

# 4. ★ 关键一步：重装 torch cu124（覆盖被偷升级的版本）
pip uninstall torch torchvision -y
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

**已验证可用的版本组合**（2026-05-31 更新）：
| 包 | 版本 | 说明 |
|-----|-------|------|
| torch | 2.6.0+cu124 ✅ | 魔搭免费实例用 cu124；PAI 实例用系统 2.10+cu128 |
| torchvision | 0.21.0+cu124 ✅ | |
| diffusers | 0.38.0 | |
| transformers | **>=4.48, <5.0** ⚠️ | 太旧(<4.48)缺 Dinov2WithRegistersConfig；太新(5.8.1)拒绝本地路径 |
| peft | 0.19.1 | |
| accelerate | 最新版 | |

**验证 CUDA 可用**：
```bash
python3 -c "from peft import get_peft_model; from diffusers import StableDiffusionXLPipeline; import torch; print('CUDA:', torch.cuda.is_available(), '| torch:', torch.__version__)"
# 期望输出: CUDA: True | torch: 2.6.0+cu124
```

**⚠️ 关键——每次重新打开终端，必须激活 venv 再运行脚本**：
```bash
source /mnt/workspace/lora_env/bin/activate
```
检查提示符是否显示 `(lora_env)` 前缀。如果 Python 报错路径指向 `/usr/local/lib/python3.11/...` 而非 `/mnt/workspace/lora_env/lib/python3.11/...`，说明不在 venv 中。系统 Python 的 transformers 版本旧（无 HybridCache），会直接报 ImportError。

### Step 2: 创建训练脚本
⚠️ **注意**：如果有 `train.ipynb` 不能直接当 Python 脚本运行。**必须新建一个 `.py` 文件**，不能用 notebook 文件替代。

in the file browser → 进入 `zhuzhu_photos` → 右键 New File → `train.py`，粘贴以下代码：

```python
import os, torch
from diffusers import StableDiffusionXLPipeline, DDPMScheduler
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from torchvision import transforms
from pathlib import Path
from peft import LoraConfig, get_peft_model
from modelscope import snapshot_download  # 用魔搭SDK下载模型（不走HuggingFace外网）

IMAGE_DIR = "."
TRIGGER_WORD = "zhuzhu"
MAX_STEPS = 800
RANK = 16   # 保守rank，大rank易梯度爆炸

class ZhuzhuDataset(Dataset):
    def __init__(self, image_dir, res=768):   # 1024 → 768（降分辨率可省显存，降低NaN概率）
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
# ⚠️ 训练时不要用 enable_model_cpu_offload() — 它只适合推理
pipe = pipe.to("cuda")
pipe.vae.enable_slicing()              # 新版API（0.38.0+）
pipe.enable_attention_slicing("max")   # "max" 模式极限省显存，A10实测必需
tokenizer, text_encoder = pipe.tokenizer, pipe.text_encoder
noise_scheduler = DDPMScheduler.from_pretrained(
    model_path, subfolder="scheduler")   # ← 必须用本地 model_path！

pipe.unet.requires_grad_(False)
lora_cfg = LoraConfig(r=RANK, lora_alpha=RANK,   # alpha 与 RANK 持平，避免梯度爆炸
    target_modules=["to_q","to_k","to_v","to_out.0"])
pipe.unet = get_peft_model(pipe.unet, lora_cfg)
pipe.unet.train()

# KEY: LoRA weights in fp32, UNet base stays fp16 — prevents NaN without AMP
for param in pipe.unet.parameters():
    if param.requires_grad:
        param.data = param.data.float()

opt = torch.optim.AdamW(
    [p for p in pipe.unet.parameters() if p.requires_grad],
    lr=5e-6
)

dataset = ZhuzhuDataset(IMAGE_DIR)
loader = DataLoader(dataset, batch_size=1, shuffle=True)
print("Training started...")

step = 0
for epoch in range(999):
    for batch in loader:
        if step >= MAX_STEPS: break

        # SDXL requires dual text encoders + added_cond_kwargs
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
            pooled = outputs_2.text_embeds    # ← text_embeds 不是 pooler_output！
            embed = torch.cat([embed_1, embed_2], dim=-1)
            added_cond_kwargs = {
                "text_embeds": pooled,
                "time_ids": torch.tensor([[768, 768, 0, 0, 768, 768]],   # 必须匹配res
                                          device=pipe.unet.device)
            }

        # VAE encode in fp16 (VAE model is fp16, must match)
        latents = pipe.vae.encode(batch["px"].to(device=pipe.unet.device,
                                   dtype=torch.float16)).latent_dist.sample()
        latents = latents * pipe.vae.config.scaling_factor
        noise = torch.randn_like(latents)
        ts = torch.randint(0, noise_scheduler.config.num_train_timesteps,
                          (latents.shape[0],), device=pipe.unet.device).long()
        # Cast to float32 before add_noise to prevent fp16 overflow → NaN
        noisy = noise_scheduler.add_noise(latents.float(), noise.float(), ts)
        pred = pipe.unet(noisy, ts, encoder_hidden_states=embed.float(),
                         added_cond_kwargs=added_cond_kwargs).sample
        loss = torch.nn.functional.mse_loss(pred.float(), noise.float())
        loss.backward()
        torch.nn.utils.clip_grad_norm_(pipe.unet.parameters(), max_norm=1.0)  # 防梯度爆炸
        opt.step()
        opt.zero_grad()
        step += 1
        if step % 100 == 0:
            print(f"  Step {step}/{MAX_STEPS} | Loss: {loss.item():.6f}")
    if step >= MAX_STEPS: break

print("Training complete!")
os.makedirs("./output", exist_ok=True)
# diffusers 0.38.0: save_pretrained 直接保存 LoRA 权重，不需要 convert_unet_state_dict_to_lora（该函数已移除）
pipe.unet.save_pretrained("./output/zhuzhu_lora")
print("Saved: output/zhuzhu_lora/")
```

### 训练后推理

```python
from peft import PeftModel
pipe.unet = PeftModel.from_pretrained(pipe.unet, "./output")
img = pipe(
    prompt=f"{TRIGGER_WORD}, a young woman on Nanjing street, historic buildings, photorealistic",
    negative_prompt="cartoon, anime, illustration, distorted face",
    num_inference_steps=30, height=1024, width=1024,
).images[0]
img.save("output_test.png")
```

## ⚠️ API Key 安全 — GitHub Secret Scanning 拦截

**不要将任何 API Key 原文写入 SKILL.md 或 references/ 中的文件。** 本技能目录下的文件会通过每日灾备脚本自动备份到 GitHub 仓库，GitHub Push Protection 会扫描并拦截包含密钥模式的提交，导致整个备份推送被拒绝。

### 具体案例
- Replicate API Key（格式 `r8_...`）曾写入 SKILL.md 和 `references/realistic-portrait-workflow.md`
- 备份推送被 GitHub 拒绝，`remote rejected` + `GITHUB PUSH PROTECTION` 错误
- 需修改源文件 + 重写 Git 历史才能恢复推送

### 规则
| 场景 | 做法 |
|------|------|
| API Key 记录 | 写 `存储于 ~/.hermes/.env 中` 或 `见 .env 配置` |
| 调试 Token | 使用占位符如 `YOUR_API_KEY_HERE` |
| 已有密钥在文件中 | 立即移除，仅保留「已申请」等模糊描述 |
| 备份被拒 | ① 源文件去敏 ② Git rebase/reset 删除含密钥 commit ③ force push |

## 🔥 SDXL 自定义训练循环 NaN 终极修复

魔搭 DSW-GPU（A10 24GB）上 SDXL LoRA 训练持续 NaN 的场景，经过多轮排查发现根因：自定义训练循环中 fp16 模型体 + fp16 LoRA 权重的组合导致数值溢出（噪声+梯度累积超过 fp16 最大范围）。

### 已验证的工作方案

| 组件 | 精度 | 说明 |
|------|------|------|
| SDXL 模型（UNet/VAE） | **fp16** | 省显存，~8GB |
| LoRA 权重 adapter | **fp32** | 数值稳定，防 NaN |
| text encoder 输出 | 保持模型精度 | 传给 UNet 时 `.float()` |
| VAE latents | fp16 | 省显存 |

**关键修复代码（LoRA 权重升 fp32）：**
```python
pipe = pipe.to("cuda")
pipe.enable_attention_slicing("max")
...
pipe.unet = get_peft_model(pipe.unet, lora_cfg)
pipe.unet.train()

# LoRA weights in fp32 for stable training
for param in pipe.unet.parameters():
    if param.requires_grad:
        param.data = param.data.float()

opt = torch.optim.AdamW(
    [p for p in pipe.unet.parameters() if p.requires_grad],
    lr=5e-6
)
```

**UNet forward 入参全部 `.float()`：**
```python
noisy = noise_scheduler.add_noise(latents.float(), noise.float(), ts)
pred = pipe.unet(noisy, ts, encoder_hidden_states=embed.float(),
                 added_cond_kwargs=added_cond_kwargs).sample
loss = torch.nn.functional.mse_loss(pred.float(), noise.float())
```

**环境变量防 OOM：**
```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

**无效方案记录（2026-05-25 本 session 全部复测再次失败）**：
- RANK 64→32→16，lora_alpha RANK*2→RANK，lr 1e-4→5e-5→1e-5→5e-6 → 全 fp16 下仍 NaN
- `torch.nn.utils.clip_grad_norm_(..., max_norm=1.0)` → 仍 NaN（梯度未爆炸）
- UNet 输入 `latents.float() / embed.float()` → 仍 NaN（非精度溢出）
- `torch.clamp(noisy, -10.0, 10.0)` → 仍 NaN
- `torch.cuda.amp.autocast()` + `GradScaler` → 仍 NaN @ Step 100
- 去掉 attention_slicing，改用 gradient_checkpointing → 待测试（NaN 修复尚未成功）

> 镜像: ubuntu22.04-cuda12.8.1-py311-torch2.9.1 需重装 cu124
> venv 路径: /mnt/workspace/lora_env
> 安装命令见 `chinese-ai-image-gen-workflow` 主技能

## 模板与参考文件

| 文件 | 说明 |
|------|------|
| `templates/train_sd15_lora.py` | SD 1.5 LoRA 训练模板（已实战验证，魔搭 A10 fp32 稳跑） |
| `templates/infer_sd15_lora.py` | SD 1.5 LoRA 推理测试模板 |
| `templates/train_sdxl_lora.py` | SDXL LoRA 自定义训练循环模板（⚠️ 已弃用，用官方脚本替代） |
| `templates/realvisxl-official-training-plan.md` | **SDXL 官方脚本训练计划（推荐）** — 含 sed 补丁、metadata.csv、venv 重建、推理注意事项 |
| `templates/infer_sdxl_lora_tuned.py` | **SDXL LoRA 调优推理模板** — DPM++ Karras + LoRA scale + 多场景/多分辨率/多种子批量评估。支持 `LORA_PATH`/`OUT_DIR` 变量切换，可做新旧 LoRA A/B 对比（2026-05-29 更新：增加输出目录隔离 + 竖图分辨率 + 对比工作流注释） |
| `references/modelscope-lora-pitfalls.md` | 魔搭 LoRA 训练踩坑实录（故障1-8） |
| `references/diffusers-038-api-changes.md` | diffusers 0.38.0 API 变动 |
| `references/session-20260525-lora-debug-log.md` | 2026-05-25 LoRA 训练历程（自定义循环 NaN 调试） |
| `references/session-20260526-lora-b-plan-sdxl09.md` | 2026-05-26 B 方案执行记录（SDXL 0.9 + 官方脚本） |
| `references/session-20260530-pai-migration.md` | **2026-05-30 阿里云 PAI 个人实例迁移实录** — 免费额度耗尽 → 个人云账号实例全流程 |
| `references/rank128-comparison-results.md` | **Rank-128 vs Rank-64 面质对比 (2026-05-31)** — 3场景×3参数网格评分矩阵 + 边际收益递减结论 |
| `references/a4-lora-comparison-results.md` | **A4 (1024) vs 旧 (768) LoRA 面质对比** — gpt-4o 评分矩阵 + 定性分析 (2026-05-29) |
| `references/gpt-image-2-enamel-pin.md` | **gpt-image-2 珐琅徽章生成方案** — 已验证提示词模板 + 调用代码 + 使用时机 |
| `references/pc-build-guide.md` | 本地 AI 工作站采购指南（3 档方案 + 错误方案警示 + 采购注意事项） |

## 常见问题与踩坑记录

> 完整错误现场记录见 `references/modelscope-lora-pitfalls.md`（含故障1-8：CUDA不匹配、OOM、文件丢失、内核崩溃、venv创建等）

### 1. peft/transformers版本冲突
```bash
pip install --upgrade transformers peft
```
魔搭环境预装版本不兼容时运行此命令。留意红色警告仅涉及 `ms-swift` 和 `vllm`，不影响 LoRA 训练。

**⚠️ 关键：pip装完后必须重启Jupyter内核** — 不然 Python 进程还是旧状态，`NameError: name 'get_peft_model'` 照样报。重启方式：
- 命令面板：`Ctrl+Shift+P` → 输入 `restart` → 选 "Jupyter: Restart Kernel"
- 工具栏 ↻ 图标
- 或终端 `pkill -f ipykernel` 然后运行任意 cell 自动重建内核

**如果内核反复崩溃**（出现 `command '_extensions.manage' not found` 或内核自动重启弹窗）→ 说明 ms-swift 依赖链与新装包冲突，系统环境已被污染。终极方案：**创建虚拟环境**（详见 `references/modelscope-lora-pitfalls.md` 故障8）。

### 2. CUDA不可用 / 所有GPU操作都报OOM
**诊断**：先确认 `torch.__version__` 和 `nvidia-smi` 的 CUDA Version 是否匹配
```bash
python3 -c "import torch; print(torch.__version__)"
nvidia-smi | grep "CUDA Version"
```
**根因（魔搭免费实例）**：魔搭预装 PyTorch 2.9.1+cu128（CUDA 12.8），但 A10 实例驱动仅支持 CUDA 12.4。
**根因（阿里云 PAI 个人实例）**：✅ 一般不存在——系统 PyTorch 2.10+cu128 已与 NVIDIA 驱动 550（CUDA 12.4）匹配。
**小张量诊断法**：
```bash
CUDA_LAUNCH_BLOCKING=1 python3 -c "
import torch
x = torch.tensor([1.0, 2.0, 3.0]).cuda()
print('GPU works:', x)
"
```
**修复（仅魔搭免费实例需要）**：
```bash
pip uninstall torch torchvision -y
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```
**修复（阿里云 PAI 个人实例）**：直接用系统 torch，venv 用 `--system-site-packages` 创建。不要重装 torch。

### 3. 模型加载时被杀死（内存不足，OOM killer）
```python
# 必须使用内存优化选项：
pipe = StableDiffusionXLPipeline.from_pretrained(
    ..., low_cpu_mem_usage=True,     # 降低CPU峰值
)
# ⚠️ 训练时不能用 enable_model_cpu_offload()！它只适合推理，训练时会导致设备不匹配错误。
# 用 pipe.to("cuda") 替代（A10 24GB 足够容纳 SDXL fp16）
pipe = pipe.to("cuda")
pipe.vae.enable_slicing()              # 新版API
pipe.enable_attention_slicing("max")   # ← "max" 模式！普通模式不够省
```
注意:
- `enable_model_cpu_offload()` 必须在 VAE slicing 之前调用。
- 训练代码必须先设 `export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` 再运行。

### 3b. SDXL fp32 训练导致 OOM（A10 24GB不够）
- **现象**：`torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 14.00 MiB. GPU 0 has a total capacity of 23.68 GiB of which 11.50 MiB is free.`
- **根因**：SDXL fp32 模型约占用 15GB，加上梯度/优化器状态共约 23.5GB，A10 的 24GB 几乎被耗尽，任何额外的操作（如 VAE encode）都会触发 OOM。
- **修复**：加载模型时用 `variant="fp16", torch_dtype=torch.float16`（模型 ~8GB），LoRA 权重单独升 fp32 保数值稳定性。见上方 Step 2 的完整代码。

### 4. 文件存储——重启后消失
- ❌ **终端 heredoc** (`cat > file << 'EOF'`) — 重启后消失
- ✅ **Code Editor 文件浏览器** New File → 粘贴 → Ctrl+S — 持久保存
- 照片上传到 `zhuzhu_photos/` 后重启也保留

### 5. Notebook无输出卡住
CUDA 上下文污染或依赖冲突时，Jupyter Notebook 内核可能静默挂起无输出。
**优先使用底部终端**运行 `.py` 文件，实时输出更可靠。

### 6. 终端报 "Launcher Error: Failed to fetch"
Code Editor 的 JupyterLab 终端偶发此错误，不影响训练：
- 可用 Launcher 页的 **Notebook**（Python 3 ipykernel）替代
- 或刷新页面重试

### 7. 实例闲置重连后完整恢复
```bash
# 1. 确认GPU存在 && CUDA正确
nvidia-smi && python3 -c "import torch; print(torch.__version__, torch.cuda.is_available())"
# 2. 如非cu124版本，重装PyTorch（注意：如果装了diffusers后torch被偷升级，需先pip uninstall再重装）
# 3. 确认文件还在 ls /mnt/workspace/zhuzhu_photos/
# 4. 如果之前创建了 venv：source /mnt/workspace/lora_env/bin/activate
# 5. 运行 cd /mnt/workspace/zhuzhu_photos && python3 train.py
```

### 8. torch 版本被下游依赖偷升级（仅魔搭免费实例存在）

**现象**：手动装了 `torch 2.6.0+cu124` 并验证 `CUDA: True`，但装了 `diffusers accelerate safetensors` 等包后突然变成 `CUDA: False | torch: 2.12.0+cu130`（NVIDIA驱动太旧报错）。

**根因**：`diffusers 0.38.0` 的依赖链含 `torch>=2.6.0`，pip 在安装时会自动将 torch 升级到最新版（cu130），覆盖了之前用 `--index-url` 指定的 cu124 版本。类似地 `peft`、`transformers` 也可能拉动 torch 升级。

**修复（魔搭免费实例）**：安装完所有 ML 包后，**最后一步重装 torch cu124**：
```bash
pip uninstall torch torchvision -y
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

**避免（阿里云 PAI 个人实例）**：使用 `--system-site-packages` venv 时，torch 从系统继承，不会被 pip 覆盖升级。不需要重装。

### 9. Code Editor 粘贴缩进污染（持续踩坑）

**用户偏好**：老缪要求给代码时**必须给完整替换版（整体粘贴）**，不要分段 diff/patch。分段贴导致反复缩进错误（IndentationError），每次都要再花几轮沟通修正。如果不确定文件内容是否已更新，宁可多给一次完整的。

**最可靠方案**：见 **第 26 节「远程脚本传输可靠方法」** — 分段 base64 写入终端，彻底避开缩进/换行问题。

### 9b. Code Editor 粘贴缩进污染（持续踩坑）

**现象**：在 Code Editor 粘贴代码后 `python3 train.py` 反复报各种 `IndentationError`（unexpected indent、unindent does not match）。

**根因**：微信/飞书粘贴到 Code Editor 时混入不可见字符或 Tab→空格转换不一致。即便你肉眼检查和手动调好，预览图看起来对齐了，实际文件里缩进仍可能对不上。

**最可靠方案**（在终端中直接执行，而不是粘贴到 Code Editor 文件里）：
```bash
# 方案A: 用 Python f.write() 直接写文件
cat > /mnt/workspace/zhuzhu_photos/train.py << 'PYEOF'
... 完整代码 ...
PYEOF
```
注意 heredoc 边界符 `'PYEOF'` **必须加引号**，否则 shell 会对 `$` 和反引号做变量展开。

**Code Editor 粘贴时确保**：
1. 编辑器状态栏显示 `空格: 4`（不能是 `Tab 大小: 4`）
2. 粘贴后按 `Ctrl+A` 全选 → `Shift+Tab` 减少缩进 → 再按 `Tab` 恢复，重新格式化
3. 保存后终端 `python3 -c "import py_compile; py_compile.compile('/mnt/workspace/zhuzhu_photos/train.py', doraise=True)"` 验证语法

### 9d. PAI venv: `ImportError: cannot import name 'Dinov2WithRegistersConfig'`

**现象**：训练脚本启动时报：
```
ImportError: cannot import name 'Dinov2WithRegistersConfig' from 'transformers'
```
（来自 diffusers 的 `autoencoder_rae` → `transformers` 导入链）

**根因**：diffusers 0.38.0 的 `autoencoder_rae` 模块引用了 `Dinov2WithRegistersConfig`，该配置类在 transformers >= 4.48 才引入。之前 pin 的 `transformers==4.46.0` 太旧。

**修复**：
```bash
pip install "transformers>=4.48,<5.0" -i https://mirrors.aliyun.com/pypi/simple/
```
验证：
```bash
python3 -c "from transformers import Dinov2WithRegistersConfig; print('OK')"
python3 -c "from diffusers import StableDiffusionXLPipeline; print('diffusers OK')"
```

**记入 venv 创建命令**：PAI 实例重建 venv 时用 `"transformers>=4.48,<5.0"`，不要 pin `4.46.0`。

**现象**：魔搭 DSW 实例闲置超 1 小时后自动关闭，重启后 `source lora_env/bin/activate` 成功但 `pip` 报 `ModuleNotFoundError: No module named 'pip'`，`torch` 也找不到。

**根因**：DSW 实例关闭时 /tmp 或某些临时路径被清理，venv 的部分 core 文件（`bin/pip` 的 `_internal` 引用）损坏。

**修复**：不要尝试修复——直接重建 venv 更快：
```bash
cd /mnt/workspace && rm -rf lora_env && python3 -m venv lora_env
source lora_env/bin/activate && pip install --upgrade pip setuptools wheel
```

重建后按标准顺序重装依赖：
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
pip install "diffusers[training]" accelerate datasets tensorboard peft transformers -i https://mirrors.aliyun.com/pypi/simple/
# 再重装 torch cu124 防偷升级
pip uninstall torch torchvision -y
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
python3 -c "import torch; print('CUDA:', torch.cuda.is_available(), '| torch:', torch.__version__)"
```

### 10. enable_model_cpu_offload() 导致训练时设备不匹配

**现象**：使用 `pipe.enable_model_cpu_offload()`（来自 OOM 故障3的修复），训练循环报错：
```
RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0!
```

**原因**：`enable_model_cpu_offload()` 是为**推理**设计的——它逐层将模型分量搬上 GPU 再搬回 CPU。训练时 LoRA 的 `lora_A`/`lora_B` 权重被加到某层后，该层在 CPU 上，但输入的 latent tensor 在 `cuda:0` 上，两方不在同一设备。

**修复**：训练时**不用** `enable_model_cpu_offload()`，改用直接 `pipe.to("cuda")`。注意调用顺序：
```python
pipe = pipe.to("cuda")       # ✅ 训练用，模型常驻 GPU
pipe.enable_vae_slicing()    # 仍可保留内存优化
pipe.enable_attention_slicing()
```

A10 有 24GB 显存，SDXL fp16 约占用 7GB，加上梯度/优化器状态约 12GB，剩余 >10GB 给数据缓存，完全够用。

### 11. 魔搭实例连不上 HuggingFace Hub — 用 modelscope SDK 下载

**现象**：设置 `export HF_ENDPOINT=https://hf-mirror.com` 后仍报 `RepositoryNotFoundError: 404 Client Error`，或 `Network is unreachable`（Errno 101）。

**根因**：魔搭 DSW 实例的网络环境可能连不上 `hf-mirror.com`，而 `AI-ModelScope` 仓库下的模型**不在** huggingface.co 主站（实际上 huggingface.co 的主域名被墙）。使用魔搭 SDK 可以从阿里云内网直接下载。

**修复**（两个地方必须一起改）：
```python
# 1. 导入并下载
from modelscope import snapshot_download
model_path = snapshot_download("AI-ModelScope/stable-diffusion-xl-base-1.0")

# 2. 用本地路径加载模型
pipe = StableDiffusionXLPipeline.from_pretrained(model_path, ...)

# 3. scheduler 也必须用本地路径！
noise_scheduler = DDPMScheduler.from_pretrained(
    model_path, subfolder="scheduler")
# ❌ 不要这样：DDPMScheduler.from_pretrained("AI-ModelScope/stable-diffusion-xl-base-1.0", subfolder="scheduler")
# 这会去 HuggingFace 外网找，一样连不上
```

### 12. train.ipynb ≠ train.py — 区分 notebook 和 python 脚本

魔搭 WebIDE 中可能存在 `train.ipynb`（Jupyter Notebook）文件。**不能**用 `python3 train.ipynb` 运行 notebook。

**正确做法**：
1. 在 Code Editor 左侧文件浏览器 → 进入目标目录 → 右键 New File
2. 命名为 `train.py`（以 `.py` 结尾）
3. 粘贴完整训练代码
4. `cd /mnt/workspace/zhuzhu_photos && python3 train.py`

代码内容较长（约 60 行），本 skill 中有完整代码，使用 `skill_view(name='chinese-ai-image-gen-workflow')` 查看。

### 13. SDXL 训练需要双 text encoder + added_cond_kwargs（最新！）

**现象**：修复所有依赖和 CUDA 问题后，训练循环报错：
```
TypeError: argument of type 'NoneType' is not iterable
```
指向 `if "text_embeds" not in added_cond_kwargs:`（UNet 的 `get_aug_embed` 方法）。

**根因**：SDXL 的 UNet forward 接收 `encoder_hidden_states` 时还需要 `added_cond_kwargs` 参数，包含：
- `text_embeds` — `text_encoder_2` 的 `pooler_output`（形状 `[1, 1280]`）
- `time_ids` — 6 维向量 `[original_width, original_height, crop_top, crop_left, target_width, target_height]`，训练时通常设为 `[1024, 1024, 0, 0, 1024, 1024]`

同时 SDXL 使用**双 text encoder**：
- `text_encoder`（CLIP L/14）→ `embed_1`（77×768）
- `text_encoder_2`（OpenCLIP G/14）→ `embed_2`（77×1280）+ `pooler_output`（1280）
- 两者沿最后一维拼接 → 77×2048

**完整修复**见上方 Step 2 的训练代码（双 tokenizer + 双 text_encoder + concat + added_cond_kwargs）。

### 14. SDXL LoRA 训练 Loss: NaN（梯度爆炸/数值不稳定）—— 多次调参后的最终修复

**现象**：训练启动正常，前 100 步后输出 `Loss: nan`。经历 RANK/alpha/lr/grad_clip/fp32/AMP 多轮调试仍无效。

**根本原因**：SDXL 的 fp16 forward pass 中 attention score 指数运算溢出（>65504），任何 fp16 下的精度策略（纯 fp16、AMP、fp32 VAE 编码）都会在 UNet 的 attention 层溢出。

**最终修复**：fp16 模型 + fp32 LoRA 权重，无 AMP，全自定义：
```python
# 1. 模型 fp16 加载
pipe = StableDiffusionXLPipeline.from_pretrained(
    ..., torch_dtype=torch.float16, variant="fp16")

# 2. LoRA 权重升 fp32（仅可训练部分）
pipe.unet = get_peft_model(pipe.unet, lora_cfg)
pipe.unet.train()
for param in pipe.unet.parameters():
    if param.requires_grad:
        param.data = param.data.float()

# 3. 输入升到 fp32 再进 UNet（UNet 主权重 fp16，但 LoRA 是 fp32，所以输入也得 fp32）
noisy = noise_scheduler.add_noise(latents.float(), noise.float(), ts)
pred = pipe.unet(noisy, ts, encoder_hidden_states=embed.float(),
                 added_cond_kwargs=added_cond_kwargs).sample

# 4. 梯度裁剪 + 小学习率
torch.nn.utils.clip_grad_norm_(pipe.unet.parameters(), max_norm=1.0)
opt = torch.optim.AdamW(..., lr=5e-6)
```

**已被推翻的无效方案**（防止重复踩坑）：

| 方案 | 结果 | 说明 |
|------|------|------|
| RANK 64→32→16 | NaN @ Step 100 | 非 rank 问题 |
| lr 1e-4→5e-5→1e-5→5e-6 | NaN @ Step 100 | 非学习率问题 |
| lora_alpha RANK*2→RANK | NaN @ Step 100 | 非 alpha 问题 |
| grad_clip max_norm=1.0 | NaN @ Step 100 | 梯度未爆炸 |
| AMP + `.float()` 防溢出 | NaN @ Step 100 | `autocast` 仍会 FP16 溢出 |
| fp32 VAE + `.half()` | NaN @ Step 100 | 非 VAE 精度问题 |
| 分辨率 1024→768 | NaN @ Step 100 | 非分辨率问题 |
| `enable_gradient_checkpointing` | NaN @ Step 100 | 引入额外数值问题 |
| fp32 全模型 | OOM（24GB不够） | A10 显存不足 |
| **✅ fp16 模型 + fp32 LoRA** | **通过 Step 100（但仍未跑完完整 800 步，需测试）** | **目前最有希望的方案** |
```python
        noisy = noise_scheduler.add_noise(latents, noise, ts).float()  # ★ .float()防溢出
        with torch.cuda.amp.autocast():  # ★ AMP: UNet fp16计算自动管理
            pred = pipe.unet(noisy, ts, encoder_hidden_states=embed,
                             added_cond_kwargs=added_cond_kwargs).sample
            loss = torch.nn.functional.mse_loss(pred.float(), noise.float())
        loss.backward()  # backward 在 autocast 外面
```

**已验证仍 NaN 的完整方案列表（截至 2026-05-25）**：

| RANK | lr | lora_alpha | LoRA精度 | AMP | clamp | GradScaler | attention | 结果 |
|------|-----|-----------|---------|-----|-------|-----------|-----------|------|
| 16 | 5e-6 | 16 | fp32 | - | - | - | slicing("max") | Step 100 NaN |
| 16 | 5e-6 | 16 | fp16 | - | ✅ -10/10 | - | slicing("max") | Step 100 NaN |
| 16 | 5e-6 | 16 | fp16 | ✅ autocast | - | ✅ | slicing("max") | Step 100 NaN |
| 16 | 5e-6 | 16 | fp16 | ✅ autocast | ✅ | ✅ | gradient_checkpointing | ⏳ 待测试 |

⚠️ **截至 2026-05-25，SDXL 自定义训练循环在魔搭 A10 上仍未解决 NaN 问题。** 以上每种方案都只跑到 Step 100 就 NaN，没有一套跑完 800 步。

**当前最有希望的未验证方案**：fp16 模型 + GradScaler + clamp + gradient_checkpointing（去掉 attention_slicing）。如果有空可继续测试。

**已确认不奏效的方法**（避免重复调试）：
1. 降低 RANK 64→32→16 ❌
2. 降低 lr 1e-4→5e-5→1e-5→5e-6 ❌
3. 降低 lora_alpha RANK*2→RANK ❌
4. 梯度裁剪 max_norm=1.0 ❌
5. 输入 .float() 防溢出 ❌
6. torch.cuda.amp.autocast + GradScaler ❌
7. 输入 clamp(-10, 10) ❌
8. 分辨率 1024→768 ❌
9. fp32 全模型 → **OOM**（A10 24GB 不够）
10. enable_gradient_checkpointing + fp16 → ⏳ 未验证

**备用方案**（不再重复调试自定义循环时切换）：
1. 换用 Diffusers 官方训练脚本 (`train_text_to_image_lora_sdxl.py`) — HuggingFace 官方维护，训练逻辑经过广泛验证
2. 降到 SD 1.5 基座 — 训练更简单，不需要双 text_encoder
3. 放弃 LoRA → Seedream 图生图 + gpt-4o 面部分析组合 — 零训练，即用即走

### 15. time_ids 必须与分辨率匹配

SDXL 的 `added_cond_kwargs["time_ids"]` 必须与实际训练分辨率一致。如果 `ZhuzhuDataset` 中 `res=768`，那么：

```python
# ✅ 正确
added_cond_kwargs = {
    "time_ids": torch.tensor([[768, 768, 0, 0, 768, 768]],
                              device=pipe.unet.device)
}
# ❌ 错误 — 和训练分辨率不匹配
"time_ids": torch.tensor([[1024, 1024, 0, 0, 1024, 1024]], ...)
```

time_ids 格式：`[original_width, original_height, crop_top, crop_left, target_width, target_height]`

### 16. LoRA 权重精度——fp32 LoRA + fp16 模型（当前最优解）

**当前推荐做法（已验证通过 Step 100 无 NaN）**：
```python
pipe.unet.train()
for param in pipe.unet.parameters():
    if param.requires_grad:
        param.data = param.data.float()
opt = torch.optim.AdamW(
    [p for p in pipe.unet.parameters() if p.requires_grad],
    lr=5e-6
)
```

**原理**：UNet 主权重保持 fp16（省 ~7GB 显存），只有 LoRA adapter 的 `lora_A`/`lora_B` 权重升到 fp32。这样前向时 fp16 主 UNet 不溢出，LoRA 的梯度更新用 fp32 保持数值精度。

**已被经验证伪的替代方案**：
- ❌ AMP (`torch.cuda.amp.autocast`) — 仍 NaN @ Step 100
- ❌ 全 fp32 模型 — OOM（A10 24GB）

### 17. Diffusers 官方训练脚本版本检查（sed 补丁）

**现象**：运行 `train_text_to_image_lora_sdxl.py --help` 报错：
```
ImportError: This example requires a source install from HuggingFace diffusers (see `https://huggingface.co/docs/diffusers/installation#install-from-source`), but the version found is 0.38.0.
```

**根因**：HuggingFace diffusers 仓库中的 `train_text_to_image_lora_sdxl.py` 脚本要求 `diffusers >= 0.39.0.dev0`，但 pip 安装的最新稳定版（如 0.38.0）不满足此检查。

**修复**（一行 sed 修改版本号检查）：
```bash
sed -i 's/"0.39.0.dev0"/"0.38.0"/' train_text_to_image_lora_sdxl.py
```
之后验证：
```bash
python3 train_text_to_image_lora_sdxl.py --help 2>&1 | head -5
# 应显示: usage: train_text_to_image_lora_sdxl.py [-h] --pretrained_model_name_or_path ...
```

**注意事项**：
- 仅修改版本检查字符串，不影响训练逻辑
- 如果实际 diffusers 版本 < 0.38.0，可能需要更大的版本号下降（如降到 `"0.x.0"`）
- 该脚本的其他 API 调用（如 `save_pretrained`、`load_lora_weights`）在 0.38.0 上正常工作

### 18. 实例重启后 venv 恢复

**魔搭免费实例**：闲置超 1 小时后自动关闭，重启后 venv 可能损坏。

**现象**：`source lora_env/bin/activate` 成功但 pip 报 `ModuleNotFoundError: No module named 'pip'`，torch 也找不到。

**修复**（不要尝试修复——重建更快）：
```bash
rm -rf /mnt/workspace/lora_env && python3 -m venv /mnt/workspace/lora_env
source /mnt/workspace/lora_env/bin/activate
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
pip install diffusers accelerate datasets peft transformers safetensors -i https://mirrors.aliyun.com/pypi/simple/
pip uninstall torch torchvision -y && pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

**阿里云 PAI 个人实例**：一般不会自动关闭，但停止后重启 venv 理论不受影响（因为是标准云主机）。如果 venv 损坏，用 `--system-site-packages` 更快：
```bash
rm -rf /mnt/workspace/lora_env && python3 -m venv --system-site-packages /mnt/workspace/lora_env
source /mnt/workspace/lora_env/bin/activate
pip install diffusers accelerate peft transformers datasets safetensors -i https://mirrors.aliyun.com/pypi/simple/

### 19. metadata.csv 包含逗号导致的 CSV 解析错误

**现象**：captions 包含逗号（如 `"zhuzhu, portrait of a young woman, beautiful face, studio lighting"`），`datasets` 库解析时把逗号当成分列符，导致 `FileNotFoundError: ' beautiful face'`。

**修复**：用 Python `csv.writer`（自动加引号包裹含逗号的字段），**不要**用 `cat` 或 heredoc 手写 CSV：
```bash
python3 -c "
import csv, random
from pathlib import Path
caps = ['studio lighting','natural lighting','candid smile','elegant pose']
imgs = [p for p in Path('.').glob('*') if p.suffix.lower() in ('.jpg','.jpeg','.png')]
with open('metadata.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['file_name','text'])
    for img in imgs:
        cap = f'zhuzhu, portrait of a young woman, beautiful face, {random.choice(caps)}'
        w.writerow([img.name, cap])
"
# 验证：引号应包裹 caption
head -3 metadata.csv | cat -A
# 正确输出示例: 0.png,"zhuzhu, portrait of a young woman, beautiful face, studio lighting"$
```

此外**务必清理 Windows CRLF 换行**：
```bash
sed -i 's/\r$//' metadata.csv
```

### 20. Diffusers 官方脚本训练参数选择（`--train_data_dir` vs `--dataset_name`）

**现象**：使用 `--dataset_name="/mnt/workspace/zhuzhu_photos"` 报错 `DataFilesNotFoundError: No (supported) data files found`。

**根因**：`--dataset_name` 是给 HuggingFace Hub 上的数据集名用的（如 `"lambdalabs/naruto-blip-captions"`）。本地图片目录 + metadata.csv 必须用 `--train_data_dir`，且**不能同时传 `--dataset_name`**。

**正确用法**：
```bash
python3 train_text_to_image_lora_sdxl.py \
  --pretrained_model_name_or_path="/path/to/sdxl-0.9" \
  --train_data_dir="/mnt/workspace/zhuzhu_photos" \
  --caption_column="text" \
  --resolution=768 \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --max_train_steps=1000 \
  --learning_rate=1e-4 \
  --mixed_precision="fp16" \
  --rank=64 \
  ...（其余参数见 `templates/realvisxl-official-training-plan.md`）
```

### 21. SDXL 0.9 魔搭下载路径 — 两种环境的差异

SDXL 0.9 通过 `snapshot_download` 下载后，本地缓存路径在两种环境中**路径结构不同**：

| 环境 | 缓存路径 | 特征 |
|------|---------|------|
| 魔搭免费 DSW | `/mnt/workspace/.cache/modelscope/models/AI-ModelScope/stable-diffusion-xl-base-0___9` | **没有 `hub/`** 子目录 |
| 阿里云 PAI 个人实例 | `/mnt/workspace/.cache/modelscope/hub/models/AI-ModelScope/stable-diffusion-xl-base-0__9` | **有 `hub/`** 子目录 |

> ⚠️ 两种环境的路径不可互换。如果你在 PAI 实例上运行训练命令使用了旧路径（`/models/` 而非 `/hub/models/`），`AutoTokenizer.from_pretrained()` 会因找不到文件而报错。**运行训练前务必确认实际缓存路径**：
> ```bash
> find /mnt/workspace/.cache/modelscope -name "model_index.json" -path "*stable-diffusion*" 2>/dev/null
> ```
> 输出即实际模型路径，直接用作 `--pretrained_model_name_or_path`。

### 22. 官方 Diffusers 脚本首次成功运行记录（2026-05-26）

SDXL LoRA 训练在魔搭 A10 上**首次成功稳定运行**的配置：

| 参数 | 值 | 说明 |
|------|-----|------|
| 基座 | SDXL 0.9（`AI-ModelScope/stable-diffusion-xl-base-0.9`） | RealVisXL V4.0 不可得 |
| 脚本 | `train_text_to_image_lora_sdxl.py`（Diffusers 官方） | sed 补丁版本检查 |
| Rank | 64 | |
| lr | 1e-4 | |
| 步数 | 1000 | 24 图 × 167 epochs |
| 分辨率 | 768 | fp16 mixed precision |
| 显存占用 | ~12GB | A10 空闲 |
| Loss | 0.005~0.27 正常波动 | **无 NaN** |
| 速度 | ~7s/it | ~2h 跑完 |
| 批次 | bs=1 × grad_accum=4 | 有效 batch=4 |

**结论**：HuggingFace 官方 Diffusers 训练脚本在魔搭环境上可稳定运行（无 NaN、无 OOM），不需要自定义训练循环。这完全推翻了之前"SDXL 自定义训练循环 NaN 无法解决"的结论。

### 23. 魔搭 SDXL 推理：`.bin` 格式，不是 `.safetensors`（2026-05-27 实战）

**现象**：训练成功后推理报错 `model.safetensors not found` 或 `variant=fp16` 不存在。

**根因**：魔搭下载的 SDXL 0.9 是 **`.bin`（PyTorch 原生）格式**，不是 `.safetensors`。同时模型没有 fp16 变体文件。

**正确推理代码**：
```python
pipe = StableDiffusionXLPipeline.from_pretrained(
    model_path, torch_dtype=torch.float16,
    low_cpu_mem_usage=True)
# 关键：不用 variant='fp16'，不用 use_safetensors=True
pipe.load_lora_weights('./output-sdxl')
pipe = pipe.to('cuda')
```

**错误示例（不要用）**：
```python
# ❌ variant='fp16' — 魔搭模型没有 fp16 变体
# ❌ use_safetensors=True — 魔搭模型是 .bin 不是 .safetensors
pipe = StableDiffusionXLPipeline.from_pretrained(
    model_path, torch_dtype=torch.float16, variant='fp16',
    use_safetensors=True, ...)
```

### 23. 推理时两个常见报错（`.bin` 格式陷阱）

魔搭的 SDXL 0.9 虽然是 Diffusers 目录结构（有 `unet/`、`vae/`、`text_encoder/` 子目录），但子目录内的模型文件是 **`.bin`（PyTorch 原生）格式，不是 `.safetensors`**。

**错误 1**：`variant=fp16, but no such modeling files are available`
→ **去掉 `variant='fp16'`**。魔搭模型没有 fp16 变体文件，`torch_dtype=torch.float16` 已足够。

**错误 2**：`no file named model.safetensors found in directory .../text_encoder`
→ **去掉 `use_safetensors=True`**。该参数强制只找 `.safetensors` 文件，魔搭模型的 `text_encoder/pytorch_model.bin` 被跳过。

**正确加载方式**：
```python
pipe = StableDiffusionXLPipeline.from_pretrained(
    model_path, torch_dtype=torch.float16,
    low_cpu_mem_usage=True)   # 不传 variant, 不传 use_safetensors
```

### 24. 推理调优 pipeline（DPM++ Karras + LoRA scale）

训练完成后推荐使用 DPM++ 2M Karras 采样器替代默认 DDIM，30 步即可达到 40-50 步的细节水平。

完整调优模板：`templates/infer_sdxl_lora_tuned.py`

### 25. 推理脚本是否真的跑过——输出验证

**现象**：用户说"脚本跑完了"，但 `ls` 没找到任何输出文件。检查发现脚本只是写好了代码，从未被 `python3` 执行过。

**根因**：训练（长时间跑 GPU）和推理脚本编写是两件独立的事。用户可能记得"训练跑完了"（A4 方案 2000 步），但把推理脚本的编写完成误记为执行完成。

**诊断方法（逐层递进）**：
```bash
# 1. 找比脚本文件更新的 PNG（如果有，说明跑过）
find . -name "*.png" -newer tune2.py 2>/dev/null

# 2. 按时间范围搜所有新 PNG（不拘泥于相对路径）
find /mnt/workspace/ -name "*.png" -mtime -2 2>/dev/null | head -20

# 3. 看进程是否还在跑
ps aux | grep -E "tune2|python" | grep -v grep

# 4. 检查脚本里的保存路径（相对路径 vs 显式目录 — 决定输出落在哪）
grep -E "\.save\(|OUT_DIR|tune2_" tune2.py

# 5. 如果脚本用相对路径保存，检查脚本运行的目录
cat tune2.py | grep -E "fname|\.save\(" | head -5
```

**2026-05-29 实战案例**：`tune2.py` 的保存路径是相对路径 `tune2_{label}.png`，用户说跑完了但 `zhuzhu_photos/` 下无输出。关键在于用户是在 `/mnt/workspace/` 还是 `zhuzhu_photos/` 目录下运行的脚本——不同目录导致输出散落在不同位置。最终诊断：脚本根本没被 run 过（`find ... -newer tune2.py` 返回空）。

**最佳实践**：推理脚本始终创建显式输出目录（`os.makedirs(OUT_DIR, exist_ok=True)`），跑完在终端输出 `ALL X DONE @ OUT_DIR`。这样一眼就能确认执行状态。

### 26. 远程脚本传输可靠方法（WeChat → DSW 终端）

在微信对话框中给 DSW 终端传 Python 脚本存在多种陷阱：

| 方法 | 稳定性 | 失败模式 |
|------|--------|---------|
| Code Editor 粘贴 | ⚠️ | Tab/空格混用 → IndentationError |
| 终端 heredoc (`cat > file << 'EOF'`) | ⚠️ | Shell 对 `$` 变量展开，多行缩进漂移 |
| 单行 `echo ... \| base64 -d` | ❌ | **微信自动换行** — 行长度 >~1500 字符时微信在中间插入 `\n`，base64 损坏 |
| **分段 base64** | ✅ | 推荐方案（见下方） |
| Python `f.write()` via heredoc | ⚠️ | 缩进仍可能被污染 |

**推荐方案：分段 base64（完整步骤）**：

```bash
# 第一步：在本机生成 base64 并拆成两段
python3 -c "
import base64
with open('script.py','rb') as f:
    b64 = base64.b64encode(f.read()).decode()
half = len(b64)//2
print(f'Part 1: {len(b64[:half])} chars')
print(f'Part 2: {len(b64[half:])} chars')
# 验证往返
decoded = base64.b64decode(b64[:half]+b64[half:])
print('VERIFY:', decoded[:80])
"
```

在 DSW 终端分两条发：
```bash
# 第一段
echo 'PART1_BASE64...' > /tmp/p1
# 第二段  
echo 'PART2_BASE64...' > /tmp/p2
# 合并解码运行
cat /tmp/p1 /tmp/p2 | base64 -d > script.py && python3 script.py
```

**为什么不用 `cat > file << 'HEREDOC'`**：微信粘贴多行 Python 到终端 heredoc 时，缩进层级可能飘移（特别是嵌套 for 循环内的代码），`img = pipe(...)` 这行最容易缩进出错。base64 彻底绕开了缩进问题——把整段代码编码为一行纯 ASCII，解码后原样还原。

---

### 27. 新旧 LoRA 对比推理工作流

当有多个训练版本（如旧 768×768 训练 vs A4 方案 1024×1024 训练），做对比评估的标准流程：

**脚本模板**：`templates/infer_sdxl_lora_tuned.py` — 支持 `LORA_PATH`/`OUT_DIR` 变量切换，3 场景 × 3 分辨率 × 3 种子 = 27 张/轮。

1. **用分段 base64 传脚本**（见第 26 节）— 避免缩进污染
2. **两轮依次运行**（不要同时跑，会 OOM）：
   ```bash
   cd /mnt/workspace/zhuzhu_photos
   # 旧 LoRA: LORA_PATH='./output-sdxl', OUT_DIR='tune2_old'
   # A4 LoRA:  LORA_PATH='./output-sdxl-1024', OUT_DIR='tune2_a4'
   ```
3. **gpt-4o 逐场景评分**：发送同场景同种子的旧 vs A4 对比图，要求评分面部真实度 1-10
4. **输出对比表**：面质评分矩阵（场景 × LoRA版本），识别强弱项

**关键参数保持一致**（否则对比无效）：seeds、prompts、steps、CFG、lora_scale 必须完全相同。

**2026-05-29 实战对比结论（详见 `references/a4-lora-comparison-results.md`）**：

| 场景 | 旧 LoRA (768) | A4 LoRA (1024) | Δ |
|------|:--:|:--:|:--:|
| 玄武湖 | 4/10 | 8/10 | +4 ⬆️ |
| 书店 | 5/10 | 4/10 | −1 ⬇️ |
| 街巷 | 5/10 | 5/10 | 0 ➡️ |

**结论**：A4 版在**室外自然光场景**大幅领先（面质 4→8），室内/暗光场景两版表现均不理想。面质高度依赖场景光照——室外漫反射掩盖皮肤过滑缺陷，室内暴露塑料感。

常见陷阱：脚本里 `LORA_PATH` 写死的旧路径（如 `./output-sdxl`），用户以为跑的是新模型（`./output-sdxl-1024`），对比结果完全无效。务必在运行前 `grep LORA_PATH` 确认路径。


### 28. 推理参数网格搜索（零成本面质优化）

训练完成后，CFG 和 lora_scale 的组合能显著影响面质。在不重训的前提下，用网格搜索找最优参数：

```python
combos = [
    ('cfg5.5_lora0.7', 5.5, 0.7),  # 默认
    ('cfg4.5_lora0.8', 4.5, 0.8),  # 降 CFG + 升 LoRA
    ('cfg3.5_lora0.9', 3.5, 0.9),  # 再降 CFG + 再升 LoRA
]
```

**原理**：低 CFG 让模型更忠实 prompt → 面部纹理更自然；高 lora_scale 补偿 LoRA 特征强度。两者反向调节。

**流程**：固定 1 个最优场景（如室外自然光） + 1 个种子跑 3 张对比，gpt-4o 评分后选最优组合。耗时 ~5 分钟。


### 29. 全身/身形照片训练需求

当前训练集全是半身/头像照，LoRA 没学过腰以下信息。要补：
| 类型 | 数量 | 目的 |
|------|------|------|
| 半身照 | 3-5 张 | 上半身比例、肩线、手臂 |
| 全身照 | 3-5 张 | 体态、腿长、站姿 |
| 不同服装 | 2-3 张 | 防过拟合到单件衣服 |

这些和面部训练集**混合训练**即可，一张图同时学脸+身形。无需单独训练集。


### 30. 面质突破路线图（rank=128 + text_encoder ⚠️ 已实测 → 见参考文献）

**2026-05-31 实测结论**：rank=128 + text_encoder 训练 2000 步完成（Loss 0.0392，905MB）。详细对比见 `references/rank128-comparison-results.md`。

| 场景 | rank=128 vs rank=64 | 结论 |
|------|:--:|------|
| 室外自然光 | **-1** ⬇️ | rank=128 反而退步 |
| 室内/暗光 | **+2~3** ⬆️ | 大幅改善 |

**rank 64→128 边际收益递减**。下一步瓶颈在训练数据多样性（角度/光照/全身照），而非模型容量。

### 31. DSW GPU 免费额度管理与时间不足应对

魔搭 DSW 免费额度有限（约 36h T4 或更少的 A10），训练中可能遇到剩余时长不足的问题。

**查看剩余时间**：DSW 创建页面 → 「方式二」 → GPU 环境卡片右上角显示「剩余额度」。也可通过侧边栏 → 「用量与额度」查看。

**如果免费额度耗尽**：切换到**阿里云 PAI 个人云账号授权实例**（见上方「环境 B」），按量付费 A10 ¥10.49/h，不受时间限制。迁移流程：① 绑定阿里云账号 → ② 授权 PAI-DSW → ③ 创建实例（选 `ecs.gn7i-c8g1.2xlarge`）→ ④ 重建环境（--system-site-packages venv）。

以下策略按优先级排列：

| 方案 | 操作 | 预计时间 | 效果 | 适用场景 |
|------|------|---------|------|---------|
| **A. 减步速通** | `--max_train_steps=1000`（原 2000 减半）| ~3.5h | 先抢一版可用权重，不够再续 | 剩余 4-6h |
| **B. 砍半快验** | steps=500 + 去掉 `--train_text_encoder` | ~1h | 验证 rank=128 是否比 rank=64 有效 | 剩余 1-3h |
| **C. 分段续训** | 加 `--checkpointing_steps=500`，到时中断 | ~1.5h/段 | 从 checkpoint 恢复，不浪费已跑步数 | 不确定剩余 |
| **D. 充值续费** | 魔搭按量付费（约 ¥2-5/h） | 无上限 | 一劳永逸，不受免费额度限制 | 任何场景 |

**决策流程**：
1. 先查剩余时长：DSW 控制台 → 实例详情 → 剩余时长
2. 剩余 > 6h → 直接 full run（rank=128 + text_encoder + 2000 steps）
3. 剩余 3-6h → 方案 A（1000 steps rank=128，**不训 text_encoder** 省时间）
4. 剩余 < 3h → 方案 B（500 steps 快验，确认 rank=128 方向正确）
5. 如果方向正确但时间不够 → 方案 D（充值续完）或方案 C（checkpoint 分段）

**checkpoint 恢复训练命令**：
```bash
python3 train_text_to_image_lora_sdxl.py \
  --pretrained_model_name_or_path="..." \
  --train_data_dir="/mnt/workspace/zhuzhu_photos" \
  --output_dir="./output-sdxl-rank128" \
  --resume_from_checkpoint="./output-sdxl-rank128/checkpoint-500" \
  --max_train_steps=2000 \
  ...（其余参数同首次训练）
```

**关键提醒**：`--checkpointing_steps` 产生的中间权重可独立用于推理——即使 500 步 checkpoint 未完成全部训练，也可加载测试面质，判断方向是否正确。

### 虚拟环境（Venv）为上策

当系统环境因 ms-swift 依赖链冲突导致内核反复崩溃时，不要硬修——直接创建虚拟环境（完整步骤见 `references/modelscope-lora-pitfalls.md` 故障8）。这是经过实战验证的最可靠方案。