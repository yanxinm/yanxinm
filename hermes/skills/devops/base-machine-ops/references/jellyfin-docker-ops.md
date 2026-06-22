# Jellyfin Docker 运维

> 2026-06-21 整理，基地 Jellyfin 容器的日常操作。

## 部署信息

| 项目 | 值 |
|------|-----|
| 镜像 | `jellyfin/jellyfin:latest` |
| 配置路径 | `/home/miao/1tb-data/nas/media/jellyfin-config` |
| 缓存路径 | `/home/miao/1tb-data/nas/media/jellyfin-cache` |
| 媒体目录 | `/home/miao/1tb-data/nas/media/movies/`（电影） |
| 端口 | 8096 |
| docker-compose | `/home/miao/1tb-data/nas/docker-compose.yml` |

## 卷挂载映射

容器内路径 → 宿主机路径：

| 容器路径 | 宿主机路径 | 用途 |
|----------|------------|------|
| `/config` | `~/1tb-data/nas/media/jellyfin-config` | 配置 + 数据库 |
| `/cache` | `~/1tb-data/nas/media/jellyfin-cache` | 转码缓存 |
| `/media/movies` | `~/1tb-data/nas/media/movies` | 电影库 |
| `/media/tvshows` | `~/1tb-data/nas/media/tvshows` | 剧集库 |
| `/media/music` | `~/1tb-data/nas/media/music` | 音乐库 |
| `/media/photos` | `~/1tb-data/nas/media/photos` | 照片库 |

⚠️ **关键**：媒体文件必须放入上述宿主机路径，Jellyfin 才能扫描到。下载目录（如 `~/Downloads/torrents/`）不在挂载范围内。

## 添加媒体文件

### 从下载目录移动到媒体库

```bash
# 查看 docker-compose 中的卷挂载
grep -A20 "jellyfin:" /home/miao/1tb-data/nas/docker-compose.yml | grep volumes -A10

# 移动文件（跨文件系统用 rsync，不用 mv/cp）
rsync -ah --progress "/home/miao/Downloads/torrents/Movie.Name/" "/home/miao/1tb-data/nas/media/movies/Movie.Name/"

# 修复权限（如果需要）
sudo chown -R miao:miao "/home/miao/1tb-data/nas/media/movies/Movie.Name/"
```

### 为什么用 rsync 而不是 mv/cp

- `mv` 跨文件系统会报错：`无法进行跨设备的移动`
- `cp` 大文件时无进度显示，难以判断是否卡住
- `rsync -ah --progress` 显示进度、支持断点续传、保留权限

### 刷新媒体库

添加文件后，在 Jellyfin Web UI：
1. 控制台 → 媒体库 → 选择对应库 → 点击「...」→ 扫描媒体库

或通过 API：
```bash
curl -X POST "http://localhost:8096/Library/Refresh?api_key=<API_KEY>"
```

## 常见问题

### 文件在目录里但 Jellyfin 不显示

1. **检查路径是否在挂载范围内** - 下载目录默认不挂载
2. **检查权限** - `ls -la` 确认文件可读
3. **手动扫描** - 控制台触发媒体库刷新

### 权限问题

Docker 卷目录可能由其他用户创建（如 `debian-transmission`），导致无法写入：

```bash
# 查看目录属主
ls -la /home/miao/1tb-data/nas/media/movies/

# 修改权限
sudo chmod 777 /home/miao/1tb-data/nas/media/movies/
# 或修改属主
sudo chown -R miao:miao /home/miao/1tb-data/nas/media/movies/
```

### 容器管理

```bash
# 查看状态
docker ps | grep jellyfin

# 重启
docker restart jellyfin

# 查看日志
docker logs jellyfin --tail 50
```

## 已安装影片清单

| 影片 | 分辨率 | 大小 | 路径 |
|------|--------|------|------|
| 南海十三郎 (1997) | 1080p | 7.2 GB | `movies/南海十三郎.../` |
| 黑夜传说 (2003) | 2160p HDR | 23.5 GB | `movies/黑夜传说.../` |
| 黑夜传说加长版 | 2160p HDR | 25.5 GB | `movies/黑夜传说.../` |
| 蝴蝶效应 (2004) | 2160p | 33 GB | `movies/The.Butterfly.Effect.2004/` |
