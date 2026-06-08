# diffusers 0.38.0 API 变动记录

## 1. `convert_unet_state_dict_to_lora` 已移除

**现象**：`from diffusers.utils import convert_unet_state_dict_to_lora` 报 `ImportError`

**原因**：diffusers 0.38.0 移除了此函数。LoRA 保存方式改为直接调用 `save_pretrained`。

**修复**：
```python
# ❌ 旧方式（diffusers < 0.38.0）
from diffusers.utils import convert_unet_state_dict_to_lora
from safetensors.torch import save_file
sd = convert_unet_state_dict_to_lora(pipe.unet.state_dict())
save_file(sd, "./output/zhuzhu_lora.safetensors")

# ✅ 新方式（diffusers >= 0.38.0）
pipe.unet.save_pretrained("./output/zhuzhu_lora")
# 或保存为 safetensors 文件：
pipe.unet.save_pretrained("./output", safe_serialization=True)
```

## 2. LoRA 权重加载方式

加载 safetensors 文件到 pipe 的两种方式：

```python
# 方式A: 使用 load_file + load_state_dict（推荐，兼容性好）
from safetensors.torch import load_file
lora_state = load_file("output/zhuzhu_lora.safetensors")
pipe.unet.load_state_dict(lora_state, strict=False)

# 方式B: 使用 PeftModel（如果保存的是目录结构）
from peft import PeftModel
pipe.unet = PeftModel.from_pretrained(pipe.unet, "./output/zhuzhu_lora")
```

## 3. `enable_vae_slicing()` 弃用

```python
# ❌ 旧方式（diffusers < 0.38.0，FutureWarning 提示将在 0.40.0 移除）
pipe.enable_vae_slicing()

# ✅ 新方式（diffusers >= 0.38.0）
pipe.vae.enable_slicing()
```

## 4. `torch.cuda.amp.autocast()` 弃用

```python
# ❌ 旧方式
with torch.cuda.amp.autocast():

# ✅ 新方式
with torch.amp.autocast('cuda'):
```
