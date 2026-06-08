# 魔搭 LoRA 训练 Session 记录 — 2026-05-25

## 硬件环境
- 平台：ModelScope DSW-GPU
- GPU：NVIDIA A10 (23.68 GB VRAM)
- 镜像：ubuntu22.04-cuda12.8.1-py311-torch2.9.1
- 剩余免费额度：~5 小时（训练结束时）
- 存续时间：约 2 小时（20:07 开始调试，20:30 第一批错误，~21:00 训练成功）

## 可选方案总结

| 方案 | 结果 | 原因 |
|------|------|------|
| SDXL fp16 + RANK_all_variants | ❌ 全部 NaN @ Step 100 | 未知根本原因 |
| SDXL fp16 + AMP + GradScaler | ❌ NaN @ Step 100 | 同上 |
| SDXL fp16 + fp32 LoRA weights | ❌ NaN @ Step 100 | 同上 |
| SDXL fp16 + clamp(-10,10) | ❌ NaN @ Step 100 | 同上 |
| SDXL fp32 + gradient accumulation | ❌ OOM | A10 24GB 不够 |
| **SD 1.5 fp32 + RANK=16 lr=5e-6** | ✅ 800 步跑完但人脸不相似 | 参数太低学不到特征 |
| **RealVisXL + 官方训练脚本** | ⏳ 计划明天（5/26） | 预期最好效果 |

## 关键发现

### 1. SDXL 自定义训练循环的 NaN 问题（未解决）
A10 24GB 上无论怎么调参，SDXL 自定义训练循环都 NaN。已试 7 种方案全部失败。

### 2. Nvidia 驱动版本陷阱
- 预装 `torch 2.9.1+cu128`，但 A10 驱动支持 CUDA 12.4
- `pip install torch --index-url https://download.pytorch.org/whl/cu124` 后再装 `diffusers` 会被偷升到 cu130
- **必须**装完所有包后**最后一步重装** `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124`

### 3. 环境变量防 OOM（必须）
```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

### 4. venv 激活至关重要
- 系统 Python 的 transformers 版本旧（无 `HybridCache`）
- 提示符必须显示 `(lora_env)` 前缀
- 路径必须指向 `/mnt/workspace/lora_env/lib/...` 而非 `/usr/local/lib/...`

### 5. Code Editor 缩进问题
反复 IndentationError，最终通过 Python `f.write()` 或 heredoc 解决。

### 6. diffusers 0.38.0 API 变化
- `convert_unet_state_dict_to_lora` 已不存在 → 用 `pipe.unet.save_pretrained("./output/zhuzhu_lora")`
- `pipe.enable_vae_slicing()` 已弃用 → 用 `pipe.vae.enable_slicing()`
- `torch.cuda.amp.autocast()` 已弃用 → 用 `torch.amp.autocast('cuda')`

### 7. SD 1.5 RANK=16 lr=5e-6 的局限性
训练完成后推理出的图**五官完全不像**训练照片里的形象。原因是：
- RANK=16 表达能力太弱（lora_B 只有 16 维，无法编码足够的面部特征细节）
- lr=5e-6 几乎不更新权重（初始随机权重几乎没有被优化）
- SD 1.5 本身的人脸细节上限不如 SDXL

## 最终决定
**明天（5/26）尝试 RealVisXL V4.0 + Diffusers 官方 `train_dreambooth_lora_sdxl.py` 脚本**。官方脚本使用标准 AMP + GradScaler + gradient checkpointing，已经在各种 GPU 上被验证过，应该能解决自定义循环的 NaN 问题。
