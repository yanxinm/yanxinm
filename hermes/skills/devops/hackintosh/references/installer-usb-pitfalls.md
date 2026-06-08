# macOS Installer USB — Deep-Dive Pitfalls

This reference consolidates the USB creation pitfalls from `hackintosh-installer-usb` (now archived into `hackintosh`). For the main workflow, see the `hackintosh` skill Phase 3.

## Recommended Path (verified 2026-06-03)

After extensive testing across multiple USB drives and Windows builds, the ONLY reliable end-to-end workflow is:

```
gibMacOS → Extract SharedSupport.dmg → MBR pre-create partitions → dd for Windows write → copy EFI
```

**DO NOT attempt:**
- PowerShell raw write to `\\.\PhysicalDrive<N>` (fails at 99.9% with IO exception — verified 3 times)
- PowerShell `\\.\T:` volume device write (null `$fs` when drive letter disappears)
- GPT + Etcher + diskpart shrink/create (GPT backup header blocks partition creation; needs DiskGenius GUI rescue)

**The winning combo: MBR pre-create both partitions → dd one-shot write at offset → EFI untouched → copy EFI → done.** No shrinkage, no DiskGenius, no IO boundary bugs.

## Pitfall Index

### 1. gibMacOS MakeInstall.bat crashes
Python multiprocessing spawn mode fails on some Windows setups when running from a removable drive. Workaround: run gibMacOS from a fixed drive (D:, desktop), extract SharedSupport.dmg manually.

### 2. DiskPart "No volume selected" error
Happens when cleaning an already-clean disk. Re-run the full sequence or create partitions manually.

### 3. Drive letter disappears after diskpart exits
diskpart-assigned letters (S:, T:) are not guaranteed to persist. Always verify with `Get-Disk -Number N | Get-Partition | Format-Table -AutoSize` in PowerShell before attempting DMG write.

### 4. UNC path warnings from WSL
Running `cmd.exe /c` from WSL triggers "UNC path not supported". Mitigation: use `cd /d C:\` first in cmd commands, or write .bat files.

### 5. GPT + DMG partition creation FAILS (CRITICAL)
After Etcher/bare-write of SharedSupport.dmg to USB, the GPT backup header occupies the tail of the disk. Neither diskpart nor PowerShell can create a new partition from freed space. **Use MBR instead of GPT**, then write DMG to the data partition.

### 6. diskpart hangs on launch with USB plugged in
If diskpart shows the banner but never responds to `list disk`, the USB drive enumeration is stalling. Close diskpart, unplug USB, restart diskpart, then plug USB and use `rescan`.

### 7. PowerShell $fs null after Remove-PartitionAccessPath
`$fs.Write()` fails with "Cannot call a method on a null-valued expression" when the target partition has no drive letter. Always verify with `Get-Partition -DriveLetter T` first.

### 8. Etcher writes no EFI partition
After Etcher flashes SharedSupport.dmg, the USB has only APFS volumes (no FAT32). Windows shows phantom drive letters for unreadable APFS volumes. Must use diskpart/DiskGenius to create a 200MB FAT32 EFI partition afterward.

### 9. Etcher "找不到分区表" warning is expected
SharedSupport.dmg contains only the APFS filesystem, not a partition table. Click "继续" (Continue). The USB becomes bootable when EFI + OpenCore are added.

### 10. Disk number changes on USB re-plug
Unplugging and re-plugging the USB can change its disk number (Disk 1 → Disk 3) and drive letter assignments. Always run `list disk` or `Get-Disk` to re-verify.

### 11. CRITICAL: `format` after failed `create partition primary` destroys DMG
If `create partition primary` fails and you proceed with `format fs=fat32`, diskpart formats partition 1 (the APFS DMG data) as FAT32, destroying the macOS installer. **Prevention:** Always run `list partition` after `shrink`. If `create partition primary` fails, STOP immediately.

### 12. USB thermal throttling slows write to <1 MB/s
After sustained writes, the USB drive heats up and write speed drops from ~47 MB/s to <1 MB/s. Fix: Cancel, unplug USB, cool 5 min, plug into REAR USB 3.0 (blue) port, re-flash.

### 13. `shrink → rescan → create partition primary` FAILS on Etcher-flashed disks
After Etcher writes SharedSupport.dmg, the GPT backup header blocks new partition creation. **Fix — DiskGenius GUI (verified working 2026-06-03):**
1. Download [DiskGenius free](https://www.diskgenius.cn/)
2. Click the `+` to expand your 58GB USB drive
3. Right-click the APFS partition → 调整分区大小 (Resize Partition)
4. Set "分区后部的空间" to 200 MB → Start
5. Right-click the gray 200MB area → 建立新分区 (Create Partition)
6. Configure: Primary → FAT32 → 200 MB → Label: EFI → OK
7. Top-left → 保存更改 (Save Changes)

### 14. PowerShell raw-write is fragile — BOTH approaches can fail

**Path A: `\\.\T:` volume device**
- ✅ Can work if T: is unmounted first (`Remove-PartitionAccessPath`)
- ❌ Fails with null reference if partition has no drive letter

**Path B: `\\.\PhysicalDriveN` + partition offset**
- ✅ More reliable when drive letters are missing
- ❌ May fail at 99.9% with IO exception on some USB controllers
- **Offset discovery:** `(Get-Disk -Number 3 | Get-Partition | Where DriveLetter -eq '').Offset`

**Procedure:** Try Path A first. If it throws "InvokeMethodOnNull", immediately switch to Path B.

### 15. MBR EFI partition needs `set id=ef`
When using MBR, the EFI partition must be marked as type `EF` for OpenCore to recognize it. Run in diskpart: `select partition 1` → `set id=ef`.

### 16. `\\.\T:` / `\\.\H:` volume write fails with "Null 值表达式"
After `Remove-PartitionAccessPath`, the volume device path frequently produces a null `$fs` reference. **Fix**: Write to `\\.\PhysicalDrive<N>` at the partition's byte offset.

### 17. diskpart `offline disk` fails on removable media
`select disk N → offline disk` returns "可移动媒体不支持此操作". Workaround: remove drive letters (`select partition 2 → remove`) or proceed without offlining.

### 18. WSL `dd` requires USB passthrough — may not work
`wsl --mount \\.\PHYSICALDRIVE3 --bare` fails with `ERROR_SHARING_VIOLATION` if Windows holds the disk. Try: remove all drive letters, close File Explorer, then `usbipd bind`+`usbipd attach --wsl`.

### 19. aigo U268 USB drive quirks
Shows as `RD3:aigoU268` in DiskGenius. After Etcher: H: (RAW, APFS). After MBR repartitioning: S: (EFI) + data partition with NO drive letter. ALWAYS verify with `Get-Disk -Number N | Get-Partition | Format-Table`.

### 20. AX210 Wi-Fi kexts — verify before deployment
EFI may lack AX210 drivers. Sequoia needs: itlwm.kext + BlueToolFixup + IntelBTPatcher + IntelBluetoothFirmware. Check EFI includes all 4 kexts and they're in config.plist.

## dd for Windows Approach (recommended)

Download `ddrelease64.exe` from http://www.chrysocome.net/downloads/ddrelease64.exe (2.4MB). Run as Administrator in CMD:

```cmd
D:\ddrelease64.exe if=D:\macOS_Sequoia_extracted\SharedSupport.dmg of=\\.\PhysicalDrive3 bs=1M seek=201 --progress
```

- `seek=201` skips the first 201MB (200MB EFI partition + 1MB alignment gap)
- Takes ~5 minutes for 15GB

## Phase 2 Extraction Script

See `scripts/extract_dmg_from_pkg.py` — standalone Python script to extract SharedSupport.dmg from InstallAssistant.pkg. Parses XAR TOC XML to find DMG offset and extracts with binary read.

## Supporting Files

- `scripts/extract_dmg_from_pkg.py` — Extract SharedSupport.dmg from InstallAssistant.pkg
- `references/dd-windows-write.md` — dd for Windows detailed workflow
- `references/powershell-raw-write.md` — PowerShell raw write approach (fragile, for reference)
