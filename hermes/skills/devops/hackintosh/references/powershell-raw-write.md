# PowerShell USB Raw Write Script

Writes `SharedSupport.dmg` to a USB partition via raw disk I/O.
Two approaches documented below. **Prefer balenaEtcher** for simplicity, but the volume-device
approach (Option B) has been verified working when Etcher + GPT shrink flow fails.

---

## Known Failure Modes (all encountered 2026-06-01, Windows 10.0.26220)

### Failure 1: Int32 overflow in [Math]::Min
```
无法将"Min"的参数"val2"(其值为"15638301899")转换为类型"System.Int32"
```
Root cause: `[Math]::Min($buffer.Length, $size - $total)` — PowerShell auto-converts
`$size - $total` to `[long]` (>2GB) but `Int32` overload is chosen, causing overflow.
Fix: Use explicit if/else casting.

### Failure 2: Null $fs after partition not found
```
不能对 Null 值表达式调用方法。$fs.Write($buffer, 0, $read)
```
Root cause: Windows auto-assigns drive letters differently than diskpart requested.
The data partition (intended as T:) may have no letter, or the EFI partition gets T:.
Fix: Find partition by size, not by drive letter; use `Add-PartitionAccessPath` manually.

### Failure 3: IO error on $fs.Write() at 99.9% (PhysicalDrive)
```
使用"3"个参数调用"Write"时发生异常:"IO 操作将无效。很可能是因为文件变得太长，
或者没有打开句柄来支持同步 IO 操作。"
```
Root cause: `FileStream` writing to `\\.\PhysicalDrive<N>` with offset hits a boundary
bug near the end of large writes (15GB+). `FileShare::Read` + 1MB buffers reduce
frequency but don't eliminate it. **Solution:** Use `\\.\T:` volume device instead (Option B).

---

## Option A: PhysicalDrive + offset (FRAGILE — may fail)

```powershell
$dmgPath = "D:\macOS_Sequoia_extracted\SharedSupport.dmg"

# Find partition by size (58GB data partition), NOT by drive letter
$disk = Get-Disk | Where-Object {$_.Size -lt 64GB -and $_.Size -gt 50GB}
$partition = $disk | Get-Partition | Where-Object {$_.Size -gt 1GB}
if (-not $partition) { Write-Error "Data partition not found"; exit 1 }

# Assign drive letter if missing, then unmount
$letter = "T"
if (-not $partition.DriveLetter) {
    $partition | Add-PartitionAccessPath -AccessPath "${letter}:\"
    $partition = Get-Partition -DriveLetter $letter
}
Remove-PartitionAccessPath -DriveLetter $letter -AccessPath "${letter}:\" -ErrorAction SilentlyContinue

$diskPath = "\\.\PhysicalDrive$($partition.DiskNumber)"
$offset = $partition.Offset

$fs = [System.IO.File]::Open($diskPath, [System.IO.FileMode]::Open, [System.IO.FileAccess]::Write, [System.IO.FileShare]::Read)
$fs.Seek($offset, [System.IO.SeekOrigin]::Begin) | Out-Null

$dmg = [System.IO.File]::OpenRead($dmgPath)
$buffer = New-Object byte[] 1048576
$total = 0; $size = $dmg.Length

while ($total -lt $size) {
    $remaining = $size - $total
    $chunkSize = if ($remaining -lt $buffer.Length) { [int]$remaining } else { $buffer.Length }
    $read = $dmg.Read($buffer, 0, $chunkSize)
    $fs.Write($buffer, 0, $read)
    $total += $read
    if ($total % 104857600 -eq 0 -or $total -eq $size) {
        Write-Host "$([int]($total * 100 / $size))% - $total / $size"
    }
}
$dmg.Close(); $fs.Close()
Write-Host "Done! Written $total bytes."
```

---

## Option B: Volume device `\\.\T:` (VERIFIED WORKING, 2026-06-01)

**Key insight:** Writing to the volume device path instead of PhysicalDrive + offset
bypasses the physical disk boundary issues. This succeeded after PhysicalDrive failed
3 times.

```powershell
$dmgPath = "D:\macOS_Sequoia_extracted\SharedSupport.dmg"

# Verify partition is mounted and get the drive letter
$partition = Get-Partition -DriveLetter T
if (-not $partition) {
    $partition = Get-Disk | Where-Object {$_.Size -lt 64GB -and $_.Size -gt 50GB} `
        | Get-Partition -PartitionNumber 2
    $partition | Add-PartitionAccessPath -AccessPath "T:\"
    $partition = Get-Partition -DriveLetter T
}

# Unmount before opening raw handle
Remove-PartitionAccessPath -DriveLetter T -AccessPath "T:\" -ErrorAction SilentlyContinue

# Write to volume device (NOT PhysicalDrive!)
$fs = New-Object System.IO.FileStream("\\.\T:", [System.IO.FileMode]::Open,
    [System.IO.FileAccess]::Write, [System.IO.FileShare]::Read)

$dmg = [System.IO.File]::OpenRead($dmgPath)
$buffer = New-Object byte[] 1048576
$total = 0
$size = $dmg.Length

while ($total -lt $size) {
    $c = [Math]::Min($size - $total, 1048576)
    $r = $dmg.Read($buffer, 0, [int]$c)
    $fs.Write($buffer, 0, $r)
    $total += $r
    if ($total % 104857600 -eq 0 -or $total -eq $size) {
        Write-Host "$([int]($total*100/$size))% - $total/$size"
    }
}
$dmg.Close()
$fs.Close()
Write-Host "Done! $total bytes."
```

**⚠️ Retry behavior:** Even `\\.\T:` may fail with IO error on the first attempt near
99.9%. This is because the previous attempt's partial data is already written and
the handle gets confused. Simply close PowerShell, reopen, and retry — the second
attempt typically succeeds because most data is already on disk.

---

## Prerequisites for both options

USB must be pre-partitioned with MBR (not GPT — GPT backup header blocks partition
creation after DMG write). See SKILL.md Phase 3 for the diskpart sequence.

After write completes, the EFI partition (S:) must have `set id=ef` run in diskpart
(MBR requirement for OpenCore to recognize the EFI System Partition).
