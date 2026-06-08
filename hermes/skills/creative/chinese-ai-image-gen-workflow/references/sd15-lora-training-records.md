# SD 1.5 LoRA 训练 — 魔搭 ModelScope 实战记录

## 结论概要（2026-05-25）

SD 1.5 在魔搭 A10 24GB 上全 fp32 稳跑 800 步成功，零报错，零 NaN。这是经过 SDXL 反复 7 轮 NaN/OOM 后使用的兜底方案。

## SD 1.5 相比于 SDXL 的优势

| 维度 | SDXL | SD 1.5 | 
|------|------|--------|
| 模型大小（fp32） | ~15GB | **~5GB** |
| A10 兼容性 | ⚠️ unstable | **✅ 稳跑** |
| 训练代码 | 需要双 text_encoder + added_cond_kwargs | **单 encoder，极简** |
| 训练分辨率 | 768-1024 | 512 |
| fp32 显存占用 | OOM（梯度累积也 OOM） | **~14GB，有空余** |
| NaN 风险 | 高（测试 7 种方案均 NaN） | **无（全 fp32 不会溢出）** |
| 训练时间（800步） | 慢 | **快 3 倍** |

## 成功训练环境

| 配置 | 值 |
|------|-----|
| 实例 | DSW-GPU A10 24GB |
| 环境 | `/mnt/workspace/lora_env` venv |
| torch | 2.6.0+cu124 |
| diffusers | 0.38.0 |
| peft | 0.19.1 |
| 模型 | `AI-ModelScope/stable-diffusion-v1-5` |
| 精度 | 全 fp32 |
| 分辨率 | 512 |
| 步数 | 800 |
| RANK | 16 |
| lr | 5e-6 |
| 梯度裁剪 | max_norm=1.0 |

## 依赖安装

```bash
python3 -m venv /mnt/workspace/lora_env
source /mnt/workspace/lora_env/bin/activate

# 1. 先装 torch cu124
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124

# 2. 装其余依赖
pip install diffusers transformers accelerate peft safetensors modelscope

# 3. ★ 重装 torch cu124（diffusers 会偷升级到 cu130）
pip uninstall torch torchvision -y && pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124

# 验证
python3 -c "from peft import get_peft_model; from diffusers import StableDiffusionPipeline; import torch; print('CUDA:', torch.cuda.is_available(), '| torch:', torch.__version__)"
# → CUDA: True | torch: 2.6.0+cu124
```

## 已知问题

### 1. `convert_unet_state_dict_to_lora` 报 ImportError

diffusers 0.38.0 移除了此函数。改直接用 `pipe.unet.save_pretrained("./output/zhuzhu_lora")`。

### 2. 下载模型走外网失败

魔搭实例连不上 HuggingFace Hub。用 `snapshot_download("AI-ModelScope/stable-diffusion-v1-5")` 走阿里云内网。
