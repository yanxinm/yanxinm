# Videdown Cross-Platform Fix Example

## The Bug

Videdown's `electron/main.ts` had a `getYtDlpPath()` function that hardcoded `yt-dlp.exe` on all platforms. On Linux, this caused:
```
Error: spawn yt-dlp.exe ENOENT
```

## The Fix

Changed the function to mirror the existing cross-platform `getFfmpegPath()` pattern:

```typescript
// BEFORE (Windows-only)
function getYtDlpPath(): string {
  const possiblePaths = [
    path.join(process.env.APP_ROOT, 'yt-dlp.exe'),
    path.join(process.resourcesPath || '', 'yt-dlp.exe'),
    path.join(__dirname, '..', '..', 'yt-dlp.exe'),
  ]
  for (const p of possiblePaths) {
    if (fs.existsSync(p)) return p
  }
  return 'yt-dlp.exe'
}

// AFTER (cross-platform)
function getYtDlpPath(): string {
  const isWin = process.platform === 'win32'
  const ytDlpName = isWin ? 'yt-dlp.exe' : 'yt-dlp'
  const possiblePaths = [
    path.join(process.env.APP_ROOT, ytDlpName),
    path.join(process.resourcesPath || '', ytDlpName),
    path.join(__dirname, '..', '..', ytDlpName),
  ]
  for (const p of possiblePaths) {
    if (fs.existsSync(p)) return p
  }
  return ytDlpName
}
```

## Search Pattern

To find these issues in any Electron app:
```bash
grep -rn "\.exe" electron/ src/ --include="*.ts" --include="*.js" | grep -v node_modules
```

Cross-reference with existing cross-platform functions (like `getFfmpegPath`) in the same file for the correct pattern.
