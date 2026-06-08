# DiskPart from WSL — Patterns & Pitfalls

## UNC Path Problem

When running `cmd.exe` from WSL, the current directory is a UNC path (`\\wsl.localhost\Ubuntu\...`). CMD refuses to operate from UNC paths. DiskPart inherits this issue.

**Fix**: Always `cd /d C:\` before invoking diskpart:

```bash
cmd.exe /c "cd /d C:\ && echo list disk | diskpart"
```

## Pipe vs Tempfile

**Piping to diskpart from bash is unreliable** — multiple commands separated by `&` inside the pipe often fail silently (especially with Chinese-localized diskpart output).

**Use a temp file** instead:

```bash
cat > /tmp/diskpart_cmds.txt << 'EOF'
select disk 1
select partition 1
remove letter=F
select partition 2
assign letter=F
exit
EOF
cmd.exe /c "cd /d C:\ && diskpart /s \\\\wsl.localhost\\Ubuntu\\tmp\\diskpart_cmds.txt"
```

Note: the temp file path passed to `diskpart /s` must use Windows UNC format (`\\wsl.localhost\...`), and the `\\\\` escaping is necessary because bash → cmd double-interpolation.

## Drive Letter Juggling

When a USB disk has multiple partitions and you need to reassign a letter from one partition to another:

```
select disk 1
select partition 1          # the old EFI partition holding F:
remove letter=F             # release F:
select partition 2          # the new data partition
assign letter=F             # assign F: to the data partition
exit
```

Without `remove letter=F` first, `assign letter=F` will fail with "指定的驱动器号对于分配不可用" (drive letter not available).

## Verifying Changes

```bash
cmd.exe /c "cd /d C:\ && echo list volume | diskpart"
```

Look for the target volume with correct FS type (exFAT/NTFS) and size.
