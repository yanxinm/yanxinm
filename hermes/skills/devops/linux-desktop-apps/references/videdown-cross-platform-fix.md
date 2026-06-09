# videdown Cross-Platform Fix

## Problem

`electron/main.ts` hardcoded `yt-dlp.exe` (Windows) — crashes on Linux with `spawn yt-dlp.exe ENOENT`.

`getFfmpegPath()` already had cross-platform detection, but `getYtDlpPath()` did not.

## Fix applied

```diff
 function getYtDlpPath(): string {
+  const isWin = process.platform === 'win32'
+  const ytDlpName = isWin ? 'yt-dlp.exe' : 'yt-dlp'
+
   const possiblePaths = [
-    path.join(process.env.APP_ROOT, 'yt-dlp.exe'),
-    path.join(process.resourcesPath || '', 'yt-dlp.exe'),
-    path.join(__dirname, '..', '..', 'yt-dlp.exe'),
+    path.join(process.env.APP_ROOT, ytDlpName),
+    path.join(process.resourcesPath || '', ytDlpName),
+    path.join(__dirname, '..', '..', ytDlpName),
   ]
-  ...
-  return 'yt-dlp.exe'
+  return ytDlpName
 }
```

## Verification

- Vite dev server detected file change, auto-rebuilt `dist-electron/main-*.js`
- Electron restarted, yt-dlp correctly resolved to `/home/miao/.local/bin/yt-dlp`
- Douyin requires browser cookies (yt-dlp limitation, not a videdown bug)
