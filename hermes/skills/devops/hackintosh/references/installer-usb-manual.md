# Manual macOS Installer USB Creation — Session Transcript

Session: 2026-05-31 | Hermes Agent v0.15.2 | WSL + Windows (Ethan)

## Context

User downloaded macOS Sequoia 15.7.3 via gibMacOS to USB drive (F:), then MakeInstall.bat failed with multiprocessing crash. Re-downloaded to stable drive (D:), proceeded with manual USB creation.

## Step 1: Download macOS (gibMacOS)

```
D:\gibMacOS-master\gibMacOS.bat
→ Selected #16: macOS Sequoia 15.7.3 (24G419) — 15.66 GB
→ Download: 5 of 5 files succeeded
→ Saved to: D:\gibMacOS-master\macOS Downloads\publicrelease\089-70987 - 15.7.3 macOS Sequoia (24G419)
```

## Step 2: MakeInstall.bat Failure

```
C:\Python314\python.exe — MakeInstall.py
→ Checking Required Tools...
→ Couldn't locate ddrelease64.exe - downloading...
→ OSError: [Errno 22] Invalid argument: 'F:\\gibMacOS-master\\MakeInstall.py'
→ multiprocessing spawn_main crash
```

**Root cause**: Python multiprocessing spawn mode incompatible with USB drive path on this Windows install.

**DiskPart side effect**: After clean+GPT convert, only created 200MB EFI partition — no data partition for the ~16GB macOS image.

## Step 3: Fix USB Partitioning (from WSL)

```bash
# Check state
cmd.exe /c "cd /d C:\ && echo list volume | diskpart"
# Result: Volume 7 = F: 200MB RAW, no data partition

# Create primary data partition
cmd.exe /c "cd /d C:\ && (echo select disk 1 & echo create partition primary & echo format fs=exfat quick & echo assign letter=F) | diskpart"
# Partition created and formatted — but letter assignment failed (F: already taken by the 200MB EFI partition)

# Juggle drive letter from partition 1 → partition 2
cat > /tmp/diskpart_cmds.txt << 'EOF'
select disk 1
select partition 1
remove letter=F
select partition 2
assign letter=F
exit
EOF
cmd.exe /c "cd /d C:\ && diskpart /s \\\\wsl.localhost\\Ubuntu\\tmp\\diskpart_cmds.txt"
# Result: F: now 58GB exFAT on partition 2 ✅
```

## Step 4: Extract InstallAssistant.pkg

```bat
# Install 7-Zip first from https://7-zip.org/
# Then:
"C:\Program Files\7-Zip\7z.exe" x "D:\gibMacOS-master\macOS Downloads\publicrelease\089-70987 - 15.7.3 macOS Sequoia (24G419)\InstallAssistant.pkg" -o"D:\macOS_Sequoia_extracted" -y
```

Output: `SharedSupport.dmg` in `D:\macOS_Sequoia_extracted\`

## Step 5: Write SharedSupport.dmg to USB

Options:
- **balenaEtcher** (recommended): GUI tool, flash SharedSupport.dmg → USB drive
- **ddrelease64.exe**: If available in gibMacOS Scripts directory
- **Rufus**: May work with DMG in DD mode

## Step 6: Replace EFI

After flashing, mount the USB EFI partition (Windows: `mountvol F: /s` or use DiskPart), delete Apple's default EFI folder, copy in the OpenCore EFI.

## Key Takeaways

1. **gibMacOS MakeInstall.bat is unreliable** — use manual extraction + external flashing tool
2. **DiskPart from WSL**: temp files (not pipes), `cd /d C:\` first, UNC path for temp files
3. **Drive letter juggling**: remove letter from old partition before assigning to new one
4. **7-Zip install required**: Windows doesn't ship with .pkg extraction capability
5. **Re-download to stable drive**: Don't download macOS installer to the same USB you're going to format
