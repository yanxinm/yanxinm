# 2026-05-30 阿里云 PAI 个人实例迁移实录

## 背景
魔搭免费 DSW 实例 GPU 免费额度耗尽（剩余 0 小时 14 分钟），需切换到阿里云 PAI 个人云账号授权实例继续 rank=128 + text_encoder 训练。

## 关键决策点

### 1. 实例选择
- 魔搭免费实例 Tab：「免费额度已耗尽 立即升级」
- 个人云账号已绑定（`njhfd`），PAI 已授权
- 数据迁移：免费实例数据在 `/mnt/workspace/zhuzhu_photos/` 和 `lora_env`，需在新实例重建

### 2. 资源规格
- 选型：`ecs.gn7i-c8g1.2xlarge`（NVIDIA A10 × 1, 8 vCPU, 30 GiB）
- 费用：¥10.49/h
- 镜像：`modelscope:1.37.1-pytorch2.10.0-gpu-py312-cu128-ubuntu22.04`
- 驱动：NVIDIA 550 (CUDA 12.4)，系统 PyTorch 2.10+cu128 直接匹配

### 3. 关键环境差异

| 项目 | 魔搭免费 DSW | 阿里云 PAI 个人实例 |
|------|-------------|-------------------|
| torch 版本 | 2.9.1+cu128（❌需重装 cu124） | 2.10.0+cu128（✅驱动匹配） |
| venv 策略 | 独立 venv + 下载 torch wheel | `--system-site-packages` 复用系统 torch |
| SDXL 缓存路径 | `.../cache/modelscope/models/...` | `.../cache/modelscope/hub/models/...` |
| transformers 兼容 | 旧版 OK | 系统 5.8.1 拒绝本地路径 |

## 踩坑记录

### 坑 1：pip 下载 torch 超时
`pip install diffusers ...` 时 resolve 到 torch-2.12.0（532MB），阿里云镜像下载超时。
**解决**：删 venv 重建，用 `--system-site-packages` 复用系统 torch。

### 坑 2：transformers 版本双陷阱
**陷阱 A（太新）**：PAI 系统预装 transformers 5.8.1，其 `AutoTokenizer.from_pretrained()` 对本地路径做了严格的 repo_id 校验，报错 `HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name'`。`HF_HUB_OFFLINE=1` 也拦不住新版。

**陷阱 B（太旧 — 2026-05-31 新发现）**：`transformers==4.46.0` 缺少 `Dinov2WithRegistersConfig`，导致 diffusers 0.38.0 导入 `autoencoder_rae` 时报 `ImportError: cannot import name 'Dinov2WithRegistersConfig'`。

**解决**：pin `"transformers>=4.48,<5.0"` 覆盖系统版——既能处理本地文件系统路径，又满足 diffusers 0.38 的导入需求。
```bash
pip install "transformers>=4.48,<5.0" -i https://mirrors.aliyun.com/pypi/simple/
```

### 坑 3：模型缓存路径不同
第一次训练命令用了旧路径 `/mnt/workspace/.cache/modelscope/models/...`（无 `hub/`），找不到模型。
PAI 实例的 `snapshot_download` 把模型放在 `/mnt/workspace/.cache/modelscope/hub/models/...`。
**解决**：用 `find` 定位实际路径后修正命令参数。

## 训练配置（2026-05-31 实际运行）
- 基座：SDXL 0.9
- 训练照片：29 张
- Rank：128
- Text Encoder：训练
- 分辨率：1024×1024
- 训练步数：2000
- 有效 batch：4（bs=1 × grad_accum=4）
- 输出目录：`output-sdxl-rank128`
- Checkpoint：每 500 步
- Loss 初值：0.323，速度 ~4.3s/it

> ⚠️ 2026-05-30 当天只建了空目录，训练命令未实际执行。5/31 重新连接实例后才启动训练。

## 环境重建步骤总结
```bash
# 1. venv 创建（复用系统 torch）
python3 -m venv --system-site-packages /mnt/workspace/lora_env
source /mnt/workspace/lora_env/bin/activate

# 2. 装依赖（⚠️ transformers 必须 >=4.48 且 <5.0）
pip install diffusers accelerate peft "transformers>=4.48,<5.0" datasets safetensors -i https://mirrors.aliyun.com/pypi/simple/

# 3. 下载模型
python3 -c "from modelscope import snapshot_download; snapshot_download('AI-ModelScope/stable-diffusion-xl-base-0.9')"

# 4. 上传训练照片到 /mnt/workspace/zhuzhu_photos/

# 5. 生成 metadata.csv + 下载训练脚本并打 sed 补丁

# 6. 开训
```
