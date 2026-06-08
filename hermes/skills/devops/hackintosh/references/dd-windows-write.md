# dd for Windows — USB Write Workflow (verified 2026-06-03)

## Why dd Wins

PowerShell .NET `FileStream.Write()` on `\\.\PhysicalDrive<N>` consistently fails at 99.9% on USB drives (15GB write). The same IO exception occurs with 1MB, 64KB, and 64MB buffers. The root cause is a Windows sync-IO boundary issue on removable media — not buffer-size-dependent.

Unix `dd(1)` uses `write(2)` syscalls with proper block-aligned I/O, immune to .NET's abstraction-layer boundary bugs. `ddrelease64.exe` is a native Win32 port of GNU dd — no .NET, no sync-IO boundary limitation.

## Verified Workflow

### Step 1: MBR + pre-create partitions (diskpart, Administrator CMD)

```cmd
diskpart
select disk 3              # your USB drive — verify with list disk first
clean
convert mbr
create partition primary size=200
format fs=fat32 quick label=EFI
assign letter=S
create partition primary    # occupies remaining space
assign letter=H             # or any available letter
exit

diskpart
select disk 3
select partition 1
set id=ef                  # MBR EFI partition type — OpenCore requirement
exit
```

### Step 2: Write DMG with dd (Administrator CMD)

```cmd
D:\ddrelease64.exe if=D:\macOS_Sequoia_extracted\SharedSupport.dmg of=\\.\PhysicalDrive3 bs=1M seek=201 --progress
```

- `seek=201`: skips first 201MB (200MB EFI + 1MB MBR alignment). Writes DMG to partition 2 only.
- `bs=1M`: 1MB block size. Typical speed ~30-50 MB/s on USB 3.0.
- `--progress`: live transfer stats.
- Takes ~5-7 minutes for 15GB.

**Why seek=201 works:** The DMG is a raw APFS filesystem image (no partition table). Writing it at the partition's start offset means the data begins exactly where macOS expects it — the EFI partition at the front handles boot, the DMG at the back handles installation.

### Step 3: Copy EFI to S: (Administrator CMD)

```cmd
xcopy /E /H /Y "C:\Users\<user>\Desktop\EFI\*" "S:\"
```

Verify:
```cmd
dir S:\EFI\OC\Kexts
```

Should list all kext folders — bootable USB ready.

## Tested On

- **USB:** aigo U268 64GB (shows as `RD3:aigoU268` in DiskGenius)
- **Windows:** 11 Pro 10.0.26100
- **DMG:** macOS Sequoia 15.7.3 SharedSupport.dmg (15.6GB)
- **dd version:** rawwrite dd for windows 1.0beta1 WIN64 (from chrysocome.net)
- **MBR layout:** partition 1 = 200MB FAT32 (S:), partition 2 = 58.4GB raw (no drive letter)

## Things That Failed (don't retry)

| Approach | Failure mode | Attempts |
|----------|-------------|:---:|
| PowerShell `\\.\PhysicalDrive3` at offset | IO 操作将无效 at 99.9% | 3 |
| PowerShell `\\.\T:` / `\\.\H:` volume device | Null $fs (drive letter gone) | 2 |
| Etcher → diskpart shrink+create | GPT backup header blocks `create partition primary` | 1 |
| Etcher → DiskGenius resize+create | Works but requires GUI tool | Untried (skipped for dd) |
| WSL `dd` via `wsl --mount` | ERROR_SHARING_VIOLATION | 1 |
| diskpart `offline disk` on removable media | "可移动媒体不支持此操作" | 1 |
