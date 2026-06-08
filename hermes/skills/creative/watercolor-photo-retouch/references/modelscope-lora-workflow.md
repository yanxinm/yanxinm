# ModelScope (魔搭) LoRA 训练全流程

> 2026-05-21 实测。当 img2img 的"抠图效应"不可接受时，LoRA 训练是**唯一能实现自然渲染**的解决方案。

## 一、为什么需要 LoRA

| 方式 | 面部还原 | 场景融合 | 适用 |
|------|---------|---------|------|
| Seedream img2img | ★★★★ | ★★ 抠图感 | 快速出图 |
| **SDXL LoRA** | **★★★★★** | **★★★★★ 自然渲染** | 长期、反复使用 |

**抠图效应根本原因**: Seedream 的 img2img 是"局部更换"而非"重新渲染"——它试图保留原图内容，改背景时只在边缘做过渡。LoRA 则是"学会了脸再生成"，从零渲染整个场景。

## 二、平台注册

1. 打开 [modelscope.cn](https://modelscope.cn)
2. 点右上角 **login/register**
3. 用支付宝/微信/阿里云账号登录（1 分钟）
4. 登录后进入 **Studios → New Studio**
   - Name: 任意英文名（如 `zhuzhu-lora`）
   - Template: **Jupyter Notebook**
   - GPU: **T4**（免费额度 36 小时/月）

## 三、准备工作

### 照片要求

| 条件 | 要求 |
|------|------|
| 数量 | **10-20 张**（太少学不到特征，太多训练慢） |
| 角度 | 正面/半侧面/侧面/全身/自拍 **尽可能多样** |
| 尺寸 | 清晰，面部 ≥ 512px |
| 背景 | **无限制**（LoRA 学会的是面部，不受背景影响） |
| 格式 | jpg / png / webp |

### 照片命名

无需特定命名规则。脚本会读取 `./train_data/` 下所有支持的图片文件。

## 四、训练流程

### Step 0: 环境诊断（必须先做）

**不要直接进 Notebook 跑代码。先在终端做环境检查，避免踩版本冲突的坑。**

在 Code Editor 底部点 **终端** 标签，运行：

```bash
# 检查核心环境
python3 -c "import torch; print(f'PyTorch: {torch.__version__}, CUDA: {torch.cuda.is_available()}')"
python3 -c "import peft; print('peft:', peft.__version__); import transformers; print('transformers:', transformers.__version__); import diffusers; print('diffusers:', diffusers.__version__)"
```

**经典版本冲突及其修复**（2026-05-21 实测）：

| 症状 | 报错 | 根因 | 修复 |
|------|------|------|------|
| `from transformers import ... HybridCache` → `ImportError` | `cannot import name 'HybridCache' from 'transformers'` | peft 新版本依赖 transformers 5.x，但预装的是旧版 | `pip install --upgrade transformers peft` |
| `ms-swift` 或 `vllm` 兼容性警告 | `ERROR: pip's dependency resolver... but you have peft X.X.X which is incompatible` | 魔搭预装了 ms-swift/vllm，升级 peft/transformers 后与这些包版本冲突 | **不影响 LoRA 训练**，可安全忽略红色警告 |
| 运行 `pip` 时提示 root 用户 | `WARNING: Running pip as the 'root' user...` | 魔搭环境默认 root 权限 | 安全忽略，推荐用虚拟环境但不强制 |

**终端诊断流程**：

```bash
# 1. 如果 peft/transformers 版本不兼容 → 升级
pip install --upgrade transformers peft

# 2. 验证修复
python3 -c "import peft; print('peft:', peft.__version__); import transformers; print('transformers:', transformers.__version__)"

# 3. 确认 CUDA 可用
python3 -c "import torch; print(f'CUDA: {torch.cuda.is_available()}, Device count: {torch.cuda.device_count()}')"
```

确认无误后，再切回 Notebook 运行训练代码。

### Step 1: 上传照片到训练目录

在 ModelScope Web UI:
1. **My Notebook** → 选择 **GPU 环境**（方式二，显存24G）
2. 点击 **启动**（约 1-2 分钟）
3. 启动后点 **查看 Notebook**

**⚠️ 注意：启动后可能进入 Code Editor（VS Code风格界面）而非 JupyterLab**
- Code Editor 界面：左侧文件管理器 + 底部终端/输出/问题面板
- 如果进入 Code Editor，需要手动创建 Notebook：
  - 方案 A：终端中运行 `jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser`
  - 方案 B：在 Code Editor 顶部菜单 **文件 → 新建文件** → 输入文件名 `train.ipynb`，或用命令面板 `Ctrl+Shift+P` → 输入 `Notebook: Create New Notebook`
- Code Editor 没有标准的 "Kernel" 菜单项，中断运行需点工具栏 **■ 停止** 按钮

### Step 2: 进入 JupyterLab

如果进入的是 Code Editor（VS Code 界面）：
1. 先确认左上角的 **终端** 标签可用
2. 在终端中：
   ```bash
   mkdir -p train_data
   ```
3. 在左侧文件管理器上传照片到 `train_data/` 目录
4. 创建新的 Jupyter Notebook（File → New → Notebook）

### Step 3: 运行训练脚本

在 Notebook 第一个单元格粘贴：

```python
%pip install diffusers transformers accelerate peft safetensors torchvision -q
```

运行（Shift+Enter）。完成后，从 skill 中加载 `train_sdxl_lora.py` 的完整代码到第二个单元格，运行。

**训练输出**:
```
📸 找到 15 张照片
🔄 加载 SDXL (ModelScope 镜像)...
🎯 开始训练 800 步...
  Step 100/800 | Loss: 0.123456
  Step 200/800 | Loss: 0.098765
  ...
✅ 训练完成！
💾 LoRA 已保存: output/zhuzhu_lora.safetensors (96.5 MB)
```

### Step 4: 推理测试

创建新单元格，跑推理：

```python
from diffusers import StableDiffusionXLPipeline
from peft import PeftModel

pipe = StableDiffusionXLPipeline.from_pretrained(
    "AI-ModelScope/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16, variant="fp16", use_safetensors=True)
pipe.unet = PeftModel.from_pretrained(pipe.unet, "./output")
pipe.to("cuda")

prompt = "zhuzhu, young woman on Nanjing street, historic buildings, plane trees, photorealistic portrait"
img = pipe(prompt=prompt, negative_prompt="cartoon, anime, illustration",
           num_inference_steps=30).images[0]
img.save("test_nanjing.png")
display(img)
```

## 五、常见问题

### 5.1 GPU 环境启动后没反应
- 点 **查看 Notebook** 按钮进入
- 如果进入 Code Editor 而非 JupyterLab，手动创建 Notebook（File → New → Notebook）

### 5.2 训练代码一直转圈没输出
- **原因排查**：
  - `%pip install -q` 是静默安装模式 → 改为 `!pip install` 去掉 `-q` 看到进度条
  - **peft/transformers 版本冲突** → 切到终端先做环境诊断（见 Step 0）
  - 模型首次加载需下载约 7GB，国内连魔搭约 3-5 分钟
- **正确操作**：先终端检查环境，确认依赖没问题后，在 Notebook 中**直接跑训练代码**（跳过 `%pip install` 行）
- 如果超过 10 分钟无反应：点 **■ 停止** 按钮重新运行

### 5.3 在 Code Editor 中找不到 "Kernel" 菜单
- Code Editor（VS Code 风格界面）内置了 Jupyter 支持，但没有独立的 Kernel 菜单
- **中断运行**：点工具栏 **■ 停止** 按钮（方块图标），或直接**关闭终端标签**再重新打开
- **不用**尝试找 Kernel → Interrupt 路径

### 5.4 第一次点运行错了（点了 Debug 而非 Run）
- 不要点 🐞 调试按钮
- 正确操作：点 ▶️ 播放按钮，或按 **Shift+Enter**
- 如果点了 Debug 导致弹窗 `Can't start debugging`，关闭弹窗即可，不影响

### 5.5 终端诊断优于 Notebook 调试
- 当 Notebook 执行无输出时，**优先切到终端标签页做诊断**，而不是在 Notebook 里反复重启
- 终端能直接看到 Python 报错堆栈，而 Notebook 可能隐藏错误信息

### 5.4 导出 LoRA 权重
- 训练完成后，文件在 `./output/zhuzhu_lora.safetensors`
- 可通过 Notebook 的文件管理器下载到本地

## 六、推理词模板

LoRA 训练完后，用触发词 `zhuzhu` 配合场景描述：

```
zhuzhu, [场景描述], photorealistic, DSLR quality portrait, high detail
```

示例：
```
zhuzhu, young woman at Nanjing Confucius Temple, beautiful face
zhuzhu, woman drinking coffee in Nanjing cafe, photorealistic
zhuzhu, woman walking on Nanjing street autumn leaves, golden light
```

## 七、备选方案

| 平台 | 套餐 | 费用 | 特点 |
|------|------|------|------|
| **魔搭 ModelScope** | 免费 T4 (36h/月) | ¥0 | ✅ 推荐首选 |
| AutoDL | RTX 3090/4090 | ~¥2-5/h | 可搭 ComfyUI + InstantID |
| 恒源云 | RTX 4090 | ~¥3-6/h | 同上 |
