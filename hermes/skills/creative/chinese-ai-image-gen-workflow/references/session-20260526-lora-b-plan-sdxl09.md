# 2026-05-26 B 方案执行记录 — SDXL 0.9 + Diffusers 官方训练脚本

## 执行概述

**目标**：RealVisXL V4.0 + Diffusers 官方训练脚本 → 因模型不可得，改用 SDXL 0.9

## 时间线

| 时间 | 步骤 | 结果 |
|------|------|------|
| 07:33 | DSW 实例重启 | 新 IP: dsw-1926774-56464d5877-2882b |
| 07:35 | 检查 venv | ❌ torch 丢失，pip 损坏 |
| 07:38 | 重建 venv | ✅ |
| 07:40 | 安装 torch 2.6.0+cu124 | ✅ CUDA: True |
| 07:42 | 安装 diffusers[training] + 依赖 | ✅ 无偷升级 |
| 09:17 | 下载训练脚本 + 生成 metadata.csv | ✅ 24 张图 |
| 09:25 | 尝试下载 RealVisXL_V4.0 | ❌ 模型不在魔搭（404） |
| 09:29 | 尝试 hf-mirror 下载 | ❌ 外网带宽不足 |
| 09:37 | 下载 SDXL 0.9（魔搭内网） | ✅ ~2 分钟 |
| 09:38 | 卡住尝试下载 SDXL 1.0 | ❌ 无法完成 |
| 10:38 | sed 补丁版本检查 | ✅ |
| 10:58 | 首次运行（--dataset_name） | ❌ DataFilesNotFoundError |
| 11:00 | 修复 metadata.csv（csv.writer + CRLF） | ✅ |
| 11:02 | 重新运行（--train_data_dir） | ✅ 训练开始 |
| 11:25 | Step 96 | ✅ Loss 0.006, 无 NaN |
| 13:36 | Step 612 | ✅ Loss 0.05-0.27, 无 NaN |
| 15:22 | 训练仍在运行 | 实例时间可能耗尽 |

## 最终训练参数

```bash
python3 train_text_to_image_lora_sdxl.py \
  --pretrained_model_name_or_path="/mnt/workspace/.cache/modelscope/models/AI-ModelScope/stable-diffusion-xl-base-0___9" \
  --train_data_dir="/mnt/workspace/zhuzhu_photos" \
  --caption_column="text" \
  --resolution=768 \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --max_train_steps=1000 \
  --learning_rate=1e-4 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --output_dir="/mnt/workspace/zhuzhu_photos/output-sdxl" \
  --mixed_precision="fp16" \
  --rank=64 \
  --checkpointing_steps=500 \
  --validation_prompt="zhuzhu, a young woman at Xuanwu Lake, Nanjing, photorealistic, high quality, detailed face" \
  --report_to="tensorboard" \
  --seed=42
```

## 新发现与教训

1. **RealVisXL_V4.0 不在魔搭上**：HuggingFace 模型 `SG161222/RealVisXL_V4.0`，魔搭无镜像（404），hf-mirror 也下不动
2. **SDXL 0.9 作为备用基座**：魔搭 `AI-ModelScope/stable-diffusion-xl-base-0.9`（~2分钟下载），本地路径含三个下划线 `0___9`
3. **官方脚本参数**：本地图片用 `--train_data_dir`（不是 `--dataset_name`），metadata.csv 需 csv.writer 注引号+清理 CRLF
4. **版本检查 sed 补丁**：`sed -i 's/"0.39.0.dev0"/"0.38.0"/'`
5. **训练稳定**：官方脚本在 fp16 mixed precision + rank=64 + lr=1e-4 下无 NaN、无 OOM，Loss 正常下降
6. **DSW 实例重启后 venv 重建**：pip/torch 全部丢失，需完全重建（参考 pitfall 9c/18）
