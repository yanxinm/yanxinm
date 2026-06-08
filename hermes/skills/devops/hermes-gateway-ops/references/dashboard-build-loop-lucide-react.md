# Dashboard 构建死循环：lucide-react TypeScript 类型检查失败

**发现日期**: 2026-06-01
**触发条件**: lucide-react 升级到 0.577.0 + tsconfig `verbatimModuleSyntax: true`
**影响组件**: Hermes Dashboard（启动时的 Web UI 构建阶段）

## 故障现象

Dashboard 启动命令执行后，进程存活但端口 9119 始终无监听（`ss -tlnp | grep 9119` 无输出）。
进程状态 `S (sleeping)`，无任何 stdout/stderr 输出。

前台运行时可以看到：
```
→ Building web UI...
    > web@0.0.0 build
    > tsc -b && vite build
    src/App.tsx(36,3): error TS2305: Module '"lucide-react"' has no exported member 'PanelLeftClose'.
    src/App.tsx(37,3): error TS2305: Module '"lucide-react"' has no exported member 'PanelLeftOpen'.
    (重复无限循环...)
```

## 根因分析

1. `web/package.json` 中 build 脚本为 `"tsc -b && vite build"` —— `&&` 意味着 `tsc -b` 失败时 `vite build` 永远不执行
2. `tsc -b`（build mode）使用项目引用，与 `tsc --noEmit` 在某些情况下行为不同
3. lucide-react 0.577.0 的类型声明文件（`.d.ts`）中 `PanelLeftClose`/`PanelLeftOpen` 通过 `index_PanelLeftClose as PanelLeftClose` 重新导出，在 `verbatimModuleSyntax: true` 下 TypeScript 不识别
4. Dashboard 的启动逻辑在构建失败时无限重试（每轮失败后重新调用 `npm run build`）

## 验证

```bash
# 确认图标运行时存在（Node.js 可以导入）
cd ~/Hermes-Agent/web
node -e "const {PanelLeftClose, PanelLeftOpen} = require('lucide-react'); console.log('OK')"
# 输出: OK

# 确认 TypeScript 类型声明文件中已声明
grep 'declare const PanelLeftClose' node_modules/lucide-react/dist/lucide-react.d.ts
# 输出: declare const PanelLeftClose: react.ForwardRefExoticComponent<...>
# 且有 export 行: index_PanelLeftClose as PanelLeftClose

# tsc -b 失败
npx tsc -b
# 输出: error TS2305

# tsc --noEmit 却通过
npx tsc --noEmit
# 无输出（成功）

# vite build 单独执行成功
npx vite build
# ✓ built in 4.02s
```

## 修复方案

### 紧急修复（跳过类型检查）
```bash
# 如果 node_modules 不存在（新环境/首次部署），先安装依赖
cd ~/Hermes-Agent/web && npm install

# 跳过 tsc，直接 vite build
npx vite build
# dist 输出到 ../hermes_cli/web_dist/

# 启动时 MUST 加 --skip-build，否则 Dashboard 会再次尝试 tsc -b && vite build
# 导致端口监听但 HTTP 超时（HTTP 000）
hermes dashboard --port 9119 --host 127.0.0.1 --no-open --skip-build
```

### 长期修复选项
1. 升级 lucide-react 到修复了类型导出的版本
2. 将 `package.json` 的 `"build"` 改为 `"vite build"`（去掉 `tsc -b`）
3. 在 tsconfig 中关闭 `verbatimModuleSyntax`（不推荐，会影响其他导入）
4. 使用 `// @ts-expect-error` 注释绕过这两行

## 相关：Dashboard 绑定 0.0.0.0 限制

Dashboard 启动时若指定 `--host 0.0.0.0`（非 loopback），会触发 OAuth 认证门控：
```
Refusing to bind dashboard to 0.0.0.0 — the OAuth auth gate engages on non-loopback binds,
but no auth providers are registered...
```

**解决**: 加 `--insecure` 标志：
```bash
hermes dashboard --port 9119 --host 0.0.0.0 --insecure --no-open
```

## 相关：WSL2 localhost 转发回退

WSL2 localhost 转发偶发失效时，使用 WSL 直连 IP：
```bash
WSL_IP=$(ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1)
curl -s http://$WSL_IP:8648/  # Web UI
```
