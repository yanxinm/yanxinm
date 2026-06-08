# 2026-05-31 rank=128 + text_encoder 训练记录

## 训练配置

| 参数 | 值 |
|------|-----|
| 平台 | 阿里云 PAI DSW 个人实例 (njhfd) |
| 实例 | ecs.gn7i-c8g1.2xlarge (A10 24GB) |
| 镜像 | modelscope:1.37.1-pytorch2.10.0-gpu-py312-cu128-ubuntu22.04 |
| 基座 | SDXL 0.9 (`AI-ModelScope/stable-diffusion-xl-base-0.9`) |
| 脚本 | `train_text_to_image_lora_sdxl.py` (Diffusers 官方，sed 补丁已打) |
| 照片 | 29 张 |
| Rank | 128 |
| Text Encoder | 训练 |
| 分辨率 | 1024×1024 |
| 训练步数 | 2000 |
| 学习率 | 1e-4 |
| 混合精度 | fp16 |
| 批次 | bs=1 × grad_accum=4 (有效 batch=4) |
| Checkpoint | 每 500 步 |
| 输出 | `output-sdxl-rank128/` |

## 环境搭建

```bash
# PAI 实例：--system-site-packages 复用系统 torch (2.10+cu128)
python3 -m venv --system-site-packages /mnt/workspace/lora_env
source /mnt/workspace/lora_env/bin/activate

# ⚠️ transformers 必须 >=4.48 (有 Dinov2WithRegistersConfig) 且 <5.0 (本地路径兼容)
pip install diffusers accelerate peft "transformers>=4.48,<5.0" datasets safetensors -i https://mirrors.aliyun.com/pypi/simple/

# 下载模型
python3 -c "from modelscope import snapshot_download; snapshot_download('AI-ModelScope/stable-diffusion-xl-base-0.9')"
```

## 训练结果

| 指标 | 数值 |
|------|------|
| 状态 | ✅ 成功完成 |
| 耗时 | 2h 22min 57s |
| 速度 | ~4.3s/it |
| 最终 Loss | 0.0392 |
| Checkpoints | 500/1000/1500/2000 |
| 权重大小 | 905 MB (`pytorch_lora_weights.safetensors`) |
| NaN | 无 |

## 推理参数网格搜索 (9 张: 3场景 × 3参数)

| 场景 | CFG 5.5/0.7 | CFG 4.5/0.8 | CFG 3.5/0.9 | 旧A4(rank=64) |
|------|:--:|:--:|:--:|:--:|
| 玄武湖 | 6/10 | **7/10** | **7/10** | 8/10 |
| 书店 | — | — | — | — |
| 街巷 | — | — | 7/10* | — |

> *街巷 cfg3.5_lora0.9 生成了两个人物（前景黑发女非训练对象，背景棕发女才是），prompt 偏宽泛。

## 结论

rank=128 + text_encoder 训练稳定（Loss 0.0392 正常收敛，无 NaN）。

但与旧 A4 (rank=64) 对比：面质提升不明显。旧 A4 玄武湖 8/10 vs 新 rank128 最佳 7/10。可能原因：
- 训练照片集相同（29张），更多 LoRA 容量无法发挥
- 需要补充不同光照/角度/全身照
- 推理参数 CFG/lora_scale 可能有更好组合（已被搜索到的格点有限）

建议：
1. 补充半身+全身训练照片
2. 尝试更广的推理参数范围（CFG 2-7, lora_scale 0.5-1.2）
3. 考虑用 checkpoint-1500 而非最终 2000 步的权重（防过拟合）
