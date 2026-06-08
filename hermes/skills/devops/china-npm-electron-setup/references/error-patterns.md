# 常见错误输出速查

## 1. pnpm 拦截 build scripts
```
Ignored build scripts: bufferutil@4.1.0, electron@30.0.1, esbuild@0.19.3, utf-8-validate@6.0.6
Run "pnpm approve-builds" to pick which dependencies should be allowed to run scripts.
```
→ `pnpm approve-builds electron esbuild bufferutil utf-8-validate`

## 2. electron postinstall 下载超时
```
.../node_modules/electron postinstall: Failed
[Command timed out after 60s]
```
→ 手动下载 electron 二进制（见 SKILL.md §3）

## 3. path.txt 缺失
```
Error: Electron failed to install correctly, please delete node_modules/electron and try installing again
    at getElectronPath (.../electron/index.js:17:11)
```
原因：`electron/index.js` 读取 `path.txt`，文件不存在。
解决：`printf 'electron' > .../electron/path.txt`

## 4. path.txt 尾随换行 → ENOENT
```
Error: spawn .../electron/dist/electron\n ENOENT
    errno: -2,
    code: 'ENOENT',
    path: '.../electron/dist/electron\n',
```
关键：路径中有 `\n` 字面量。
原因：用了 `echo "electron"` 而不是 `printf 'electron'`。
解决：`printf 'electron' > path.txt`

## 5. electron 二进制无执行权限
无明确错误信息，进程直接退出 exit code 1。
解决：`chmod +x .../electron/dist/electron`
验证：`file .../electron/dist/electron` 应显示 `ELF 64-bit LSB pie executable`

## 6. npm registry 直连慢
```
[WARN] Tarball download average speed 6 KiB/s (size 7 KiB) is below 50 KiB/s
[WARN] Request took 30514ms: https://registry.npmjs.org/...
```
→ `npm config set registry https://registry.npmmirror.com`
