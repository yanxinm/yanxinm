#!/usr/bin/env python3
"""
基地 → 笔记本 SSH+SFTP 增量同步工作台账。
SFTP walk 扫描 + SFTP get 下载（二进制协议，中文路径无编码问题）。
"""
import os, sys, time, stat
import paramiko

SSH_HOST = "100.86.148.56"
SSH_USER = "yanxi"
SSH_KEY = "/home/miao/.ssh/id_ed25519"
SRC = "E:/百度云同步盘/工作台账"
LOCAL = "/home/miao/工作台账"
DOC_EXTS = {'.docx', '.doc', '.xlsx', '.xls', '.pdf', '.txt', '.md'}


def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def can_connect():
    try:
        import socket
        s = socket.socket()
        s.settimeout(5)
        s.connect((SSH_HOST, 22))
        s.close()
        return True
    except Exception:
        return False


def scan_remote(sftp, path):
    """SFTP 递归扫描，返回 [(local_rel, remote_full, size, mtime)]"""
    results = []
    try:
        for entry in sftp.listdir_attr(path):
            name = entry.filename
            if name.startswith('.') or name.startswith('~'):
                continue
            remote_full = f"{path}/{name}".replace('\\', '/')
            if stat.S_ISDIR(entry.st_mode):
                results.extend(scan_remote(sftp, remote_full))
            else:
                ext = os.path.splitext(name)[1].lower()
                if ext in DOC_EXTS:
                    # 构建本地相对路径
                    rel = remote_full.replace("E:/百度云同步盘/工作台账/", "").replace("\\", "/")
                    results.append((rel, remote_full, entry.st_size, entry.st_mtime))
    except IOError:
        pass
    return results


def sync_file(sftp, remote_path, local_path):
    """SFTP 下载到本地，创建父目录"""
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    sftp.get(remote_path, local_path)
    return os.path.getsize(local_path)


def main():
    log("=" * 50)
    log("台账同步开始")

    if not can_connect():
        log("SSH 不可达，跳过同步")
        return

    log("SSH 可达 ✓")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(SSH_HOST, username=SSH_USER, key_filename=SSH_KEY, timeout=15)
    except Exception as e:
        log(f"SSH 连接失败: {e}")
        return

    sftp = ssh.open_sftp()
    log("SFTP 已连接")

    # ===== 扫描 =====
    log("扫描远程目录...")
    remote_files = scan_remote(sftp, SRC)
    log(f"远程文档: {len(remote_files)} 个")
    if not remote_files:
        sftp.close()
        ssh.close()
        return

    # ===== 差量计算 =====
    to_download = []
    new_cnt = updated_cnt = skipped_cnt = 0

    for rel, remote_full, r_size, r_mtime in remote_files:
        local_path = os.path.join(LOCAL, rel)
        if not os.path.exists(local_path):
            to_download.append((rel, remote_full))
            new_cnt += 1
        elif os.path.getsize(local_path) != r_size:
            to_download.append((rel, remote_full))
            updated_cnt += 1
        else:
            skipped_cnt += 1

    log(f"需下载: 新增 {new_cnt} + 更新 {updated_cnt} = {len(to_download)} 个 (跳过 {skipped_cnt})")

    # ===== 下载 =====
    if to_download:
        log("开始下载...")
        total_bytes = 0
        errors = 0
        for i, (rel, remote_full) in enumerate(to_download):
            local_path = os.path.join(LOCAL, rel)
            try:
                sz = sync_file(sftp, remote_full, local_path)
                total_bytes += sz
                if (i + 1) % 500 == 0:
                    log(f"  进度: {i + 1}/{len(to_download)} ({total_bytes/1024/1024:.0f} MB)")
            except Exception as e:
                errors += 1
                if errors <= 3:
                    log(f"  失败: {rel} — {e}")

        if errors:
            log(f"  完成: {len(to_download) - errors}/{len(to_download)} (失败 {errors})")
        log(f"下载总计: {total_bytes/1024/1024:.0f} MB")
    else:
        log("无文件需要下载")

    sftp.close()
    ssh.close()

    # ===== 统计 =====
    total_local = total_size = 0
    for r, _, fs in os.walk(LOCAL):
        for f in fs:
            if os.path.splitext(f)[1].lower() in DOC_EXTS:
                total_local += 1
                total_size += os.path.getsize(os.path.join(r, f))

    log(f"本地总计: {total_local} 个文件, {total_size/1024/1024:.0f} MB")
    log("同步完成 ✓")
    log("=" * 50)


if __name__ == "__main__":
    main()
