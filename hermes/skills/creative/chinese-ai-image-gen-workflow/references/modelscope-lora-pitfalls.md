# 魔搭 ModelScope LoRA 训练踩坑实录

本文件记录了在魔搭 ModelScope 免费 GPU 实例上进行 SDXL LoRA 训练时遇到的所有故障及解决方案。
最后更新：2026-05-25（含第3轮NaN调试）

## 环境概览

| 项目 | 值 |
|------|-----|
| 实例规格 | DSW-GPU (8核 32GB 显存24G) |
| GPU型号 | NVIDIA A10 (23GB VRAM) |
| 免费额度 | 36小时 |
| 自动关闭 | 闲置超1小时自动关闭 |
| 预装镜像 | ubuntu22.04-cuda12.8.1-py311-torch2.9.1 |
| WebIDE | ModelScope Code Editor (beta) - 类VS Code界面 |

---

## 故障1: CUDA版本不匹配 → 所有操作报OOM

### 现象
- `nvidia-smi` 显示 A10 正常（显存空闲23GB）
- `torch.cuda.is_available()` 返回 True
- 但在 GPU 上创建任意张量（即使 4MB）都报 CUDA OOM
- `python3 train.py` 启动后立即被 `已杀死`（OOM killer）

### 根因
魔搭预装的 PyTorch 2.9.1 编译为 CUDA 12.8（`cu128`），但 A10 实例驱动仅支持 CUDA 12.4。

### 修复
```bash
pip uninstall torch torchvision -y
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

---

## 故障2: 进程被杀（OOM — 内存不足）

### 现象
SDXL 模型（~7GB）加载时被杀死。

### 修复
```python
pipe = StableDiffusionXLPipeline.from_pretrained(
    ..., low_cpu_mem_usage=True,
)
pipe = pipe.to("cuda")  # 训练用！不要用 enable_model_cpu_offload()
pipe.vae.enable_slicing()
pipe.enable_attention_slicing()
```

---

## 故障3: 文件创建后重启丢失

### 正确做法
使用 Code Editor 左侧文件浏览器 → 右键 New File → 粘贴 → Ctrl+S 保存到 `/mnt/workspace/` 下。

---

## 故障4: Jupyter Notebook 无输出/卡死

优先使用底部终端运行 `.py` 文件。

---

## 故障5: CUDA 上下文污染

OOM 后开**全新终端标签页**（点 `+` 号），不要用旧终端。

---

## 故障6: 依赖版本冲突

### 现象
```python
ImportError: cannot import name 'HybridCache' from 'transformers'
```

### 修复
```bash
pip install --upgrade transformers peft
```

---

## 故障7: 实例重启后的完整恢复步骤

```bash
nvidia-smi
python3 -c "import torch; print(torch.__version__, torch.cuda.is_available())"
# 如不是 cu124 → 重装torch
pip uninstall torch torchvision -y
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
# 激活venv
source /mnt/workspace/lora_env/bin/activate
cd /mnt/workspace/zhuzhu_photos && python3 train.py
```

---

## 故障8: pip 装包后内核崩溃

### 现象
ms-swift 依赖链冲突 → Jupyter 内核反复崩溃。

### 终极修复：创建虚拟环境
```bash
python3 -m venv /mnt/workspace/lora_env
source /mnt/workspace/lora_env/bin/activate
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
pip install diffusers transformers accelerate peft safetensors
# ★ 关键：最后重装 torch cu124（防被偷升级）
pip uninstall torch torchvision -y
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

---

## 故障9: torch 被下游依赖偷升级

**现象**：装了 diffusers/peft 等包后，torch 从 cu124 升到 cu130，CUDA 不可用。

**修复**：安装完所有 ML 包后，**最后一步重装 torch cu124**。

---

## 故障10: enable_model_cpu_offload() 导致训练设备不匹配

**修复**：训练用 `pipe.to("cuda")` 替代。enable_model_cpu_offload() 只适合推理。

---

## 故障11: 魔搭实例连不上 HuggingFace Hub

**修复**：用 modelscope SDK 内网下载。
```python
from modelscope import snapshot_download
model_path = snapshot_download("AI-ModelScope/stable-diffusion-xl-base-1.0")
# scheduler 也必须用本地路径！
noise_scheduler = DDPMScheduler.from_pretrained(model_path, subfolder="scheduler")
```

---

## 故障12: SDXL 训练 — 双 text encoder + added_cond_kwargs

SDXL 的 UNet forward 需要：
- 双 tokenizer + 双 text_encoder → concat 输出
- `added_cond_kwargs` 含 `text_embeds`（不是 pooler_output！）和 `time_ids`
- `time_ids` 必须与训练分辨率匹配（res=768 → time_ids=[[768,768,0,0,768,768]]）

完整代码见 skill 中的模板 `templates/train_sdxl_lora.py`。

---

## 故障13: SDXL 训练持续 NaN — 多次修复合集（2026-05-25）

### 现象
经 RANK=64→32→16, lr=1e-4→5e-6, lora_alpha=RANK, grad_clip=1.0, 
LoRA fp32 升精度、AMP、clamp、GradScaler 等多轮调试，均在 Step 100 输出 NaN。

### 已测试的所有方案（均 NaN @ Step 100）

| 编号 | 方案 | 精度策略 | 额外措施 | 结果 |
|------|------|---------|---------|------|
| A | RANK+lr+alpha 调参 | 纯fp16 | - | NaN |
| B | LoRA fp32 | fp16模型+fp32 LoRA | - | NaN |
| C | 输入.float() | fp16模型+fp32 LoRA | noisy/embed/pred → float | NaN |
| D | AMP + .float() | autocast | noisy.float() before UNet | NaN |
| E | clamp | fp16 | torch.clamp(noisy, -10, 10) | NaN |
| F | GradScaler | fp16 | scaler.scale/unscale/step/update | NaN |
| G | gradient_checkpointing | fp16 | 替代attention_slicing | ⏳待测试 |
| H | 全fp32模型 | fp32 | - | OOM (24GB不够) |

### 诊断
1. VAE fp16 encode 本身没问题
2. add_noise 后某些时间步的 latent 值超过 fp16 范围（~65504）→ UNet attention score 指数运算溢出
3. LoRA 权重升 fp32、AMP、clamp 均对溢出有帮助但不够彻底
4. 自定义训练循环本身可能与 diffusers 0.38 + peft 0.19 的 attention 层有兼容问题

### 最有希望的未验证方案
- fp16 模型 + GradScaler + clamp + gradient_checkpointing（去掉 attention_slicing）
- 参见模板 `templates/train_sdxl_lora.py`

### 备用方案
1. Diffusers 官方训练脚本 `train_text_to_image_lora_sdxl.py`（经过广泛验证）
2. 降到 SD 1.5 基座（不需要双 text_encoder，训练更稳定）
3. Seedream 图生图 + gpt-4o 面部分析组合（零训练）
