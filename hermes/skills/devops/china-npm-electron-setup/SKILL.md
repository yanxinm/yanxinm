---
name: china-npm-electron-setup
description: Install Node.js/Electron apps from source when npm/electron registries are blocked or slow (China GFW). Covers registry mirrors, pnpm build-script approval, manual Electron binary rescue, and common pitfalls.
---

# China NPM/Electron 源安装

在墙内从源码安装 Node.js / Electron 应用的标准化流程。

## 触发条件

- `pnpm install` 极慢、超时、或包下载失败
- `electron` postinstall 失败
- 新 `pnpm` 版本拦截 build scripts
- Electron 启动报 `ENOENT` 或 `path.txt` 缺失

---

## 1. 镜像配置（一次性）

### npm registry
```bash
npm config set registry https://registry.npmmirror.com
```

### Electron 二进制镜像
```bash
export ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/
```

pnpm 不读取 `.npmrc` 中的 `ELECTRON_MIRROR`，必须用环境变量传入或在命令前设置。

---

## 2. pnpm install

```bash
ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/ pnpm install
```

如果 pnpm 版本较新（≥10）且提示 `Ignored build scripts`：

```bash
pnpm approve-builds electron esbuild bufferutil utf-8-validate
```

这会触发被拦截包的 postinstall 脚本。如果 electron 仍下载失败，进入第 3 步。

---

## 3. 手动救援 Electron 二进制

当 `electron` 的 postinstall 下载失败时，手动操作：

### 3.1 下载
```bash
ELECTRON_VER="30.0.1"  # 从 package.json devDependencies 获取
ELECTRON_DIR="node_modules/.pnpm/electron@${ELECTRON_VER}/node_modules/electron/dist"
mkdir -p "$ELECTRON_DIR"

curl -L -o /tmp/electron.zip \
  "https://npmmirror.com/mirrors/electron/v${ELECTRON_VER}/electron-v${ELECTRON_VER}-linux-x64.zip"

unzip -o /tmp/electron.zip -d "$ELECTRON_DIR"
```

### 3.2 创建 path.txt（关键）
```bash
# 错误：echo "electron" 会带尾随换行 → 路径变成 "electron\n" → ENOENT
# 正确：
printf 'electron' > node_modules/.pnpm/electron@<VER>/node_modules/electron/path.txt
```

### 3.3 可执行权限
```bash
chmod +x node_modules/.pnpm/electron@<VER>/node_modules/electron/dist/electron
```

---

## 4. 启动验证

```bash
DISPLAY=:0 pnpm dev
# Electron main + GPU + renderer 进程应出现在 ps 中
ps aux | grep '[e]lectron'
```

## 5. 常见坑

| 症状 | 原因 | 解决 |
|------|------|------|
| `pnpm install` 超时 | npm 直连慢 | 切 npmmirror |
| `Ignored build scripts` | pnpm ≥10 默认拦截 | `pnpm approve-builds` |
| `Electron failed to install` + `path.txt` 不存在 | postinstall 被拦截/失败 | 手动创建 path.txt（用 printf） |
| `ENOENT ... electron\n` | path.txt 有尾随换行 | 用 `printf` 不用 `echo` |
| Electron 启动报错但无明确信息 | 二进制没执行权限 | `chmod +x` |
| `No protocol specified` 或无法连接 display | DISPLAY 未设 | `export DISPLAY=:0` |
