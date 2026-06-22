---
name: home-media-server
description: 自建家庭媒体服务器——NAS方案选型、媒体服务器部署(Jellyfin/Navidrome)、远程访问配置、海报墙配置的完整工作流
tags:
  - nas
  - jellyfin
  - navidrome
  - plex
  - emby
  - 媒体服务器
  - 海报墙
  - home-media
---

# Home Media Server

自建家庭媒体服务器——NAS方案选型、媒体服务器部署、远程访问配置的完整工作流。

触发词：「NAS」「媒体服务器」「Jellyfin」「Plex」「Emby」「Navidrome」「海报墙」「影音库」「家庭影院」「远程播放」「电影库」「音乐库」

---

## 决策框架

### 1. 是否换NAS系统？

| 现有情况 | 建议 |
|----------|------|
| 已有Linux + Docker运行中 | **不换**，直接部署容器 |
| 全新机器/空系统 | 可选TrueNAS Scale/OMV/fnOS |
| 追求中文界面+内置穿透 | 飞牛fnOS |
| 追求数据安全(ZFS) | TrueNAS Scale |

**换系统代价**：系统重装 + Docker重建 + 配置迁移 + 穿透重配 ≈ 半天

---

## NAS系统对比

| 方案 | 授权 | 优点 | 缺点 |
|------|------|------|------|
| **TrueNAS Scale** | 免费 | ZFS企业级安全、KVM虚拟化 | 内存要求高(≥16GB)、硬盘需统一容量 |
| **Unraid** | $59起 | 硬盘混用灵活、扩容方便 | 收费、性能弱于ZFS |
| **OpenMediaVault** | 免费 | 轻量Debian、资源占用低 | 界面一般、ZFS支持弱 |
| **飞牛fnOS** | 免费 | 中文友好、内置穿透 | 生态不如老牌 |
| **CasaOS** | 免费 | 极简、可叠加现有系统 | 功能简单、无RAID |
| **群晖DSM** | 绑定硬件 | 生态最强、套件完善 | 硬件贵、黑群晖风险 |

---

## 媒体服务器软件对比

### 电影/电视剧

| 项目 | Jellyfin | Emby | Plex |
|------|----------|------|------|
| 授权 | 完全免费 | 免费+付费 | 免费+付费 |
| 海报墙 | ✅ 好 | ✅ 精美 | ✅ 最好 |
| 硬件转码 | ✅ 免费Intel核显 | ✅ 需付费 | ✅ 需付费 |
| 外网访问 | 需自配穿透 | 需自配 | 官方中继 |
| 中文支持 | ✅ | ✅ | ✅ |

### 音乐

| 项目 | Jellyfin音乐 | Navidrome |
|------|-------------|-----------|
| 海报墙 | ⚠️ 弱、无歌词 | ✅ 专辑封面+歌词 |
| 资源占用 | 依赖Jellyfin | 极轻量(几十MB) |
| 客户端 | Jellyfin App | 多款专用App |

**推荐组合**：Jellyfin(电影) + Navidrome(音乐)

---

## Docker部署

### Jellyfin

```yaml
# docker-compose.yml
services:
  jellyfin:
    image: jellyfin/jellyfin
    container_name: jellyfin
    ports:
      - "8096:8096"
    volumes:
      - ./jellyfin-config:/config
      - ./jellyfin-cache:/cache
      - /path/to/movies:/media/movies:ro
      - /path/to/tvshows:/media/tvshows:ro
      - /path/to/music:/media/music:ro
    restart: unless-stopped
```

### Navidrome

```yaml
# docker-compose.yml
services:
  navidrome:
    image: deluan/navidrome:latest
    container_name: navidrome
    ports:
      - "4533:4533"
    environment:
      ND_SCANSCHEDULE: "1h"
      ND_LOGLEVEL: "info"
      ND_SESSIONTIMEOUT: "24h"
    volumes:
      - ./navidrome-data:/data
      - /path/to/music:/music:ro
    restart: unless-stopped
```

---

## 访问地址（重要坑）

| 服务 | 正确地址 | 错误地址 |
|------|----------|----------|
| Jellyfin | `http://localhost:8096/web/` | `http://localhost:8096` |
| Navidrome | `http://localhost:4533/app/` | `http://localhost:4533` |

**Jellyfin选服务器时**：填 `localhost` 或 `127.0.0.1`，不是IP地址

---

## 远程访问

| 方案 | 配置复杂度 | 稳定性 | 适用场景 |
|------|-----------|--------|----------|
| Tailscale | 低 | 高 | 已有Tailscale网络 |
| Tailscale Funnel | 中 | 高 | 需公网访问 |
| fnOS FN Connect | 低 | 中 | fnOS系统内置 |

**获取Tailscale IP**：`tailscale ip` 命令，不是猜的

---

## 常见问题

### 访问地址打不开

1. **检查Tailscale IP**：`tailscale ip` 获取正确IP
2. **检查路径**：Jellyfin要 `/web/`，Navidrome要 `/app/`
3. **检查端口**：`ss -tlnp | grep 端口号`

### 海报墙没出来

1. 媒体库要正确配置（控制台 → 媒体库 → 添加）
2. 文件命名要规范
3. 刮削器选TMDB，语言选中文

### 音乐海报墙差

Jellyfin音乐功能弱，建议单独部署Navidrome。

### 电影/媒体库不显示新添加的文件

**根因排查优先级**：

1. **检查Docker挂载**：`docker inspect jellyfin | grep -A20 "Mounts"` — 确认媒体目录已挂载到容器内
2. **检查容器内路径**：`docker exec jellyfin ls /media/movies` — 确认容器内能访问文件
3. **手动扫描**：Jellyfin控制台 → 媒体库 → 扫描媒体库

**常见错误**：部署时忘记挂载媒体目录，Jellyfin配置了媒体库但容器内无文件。

**修复方法**：停止并删除容器，重新运行带正确 `-v` 挂载的命令（配置在 `/config` 挂载卷中，重建不丢失）。

### 端口8096被占用

**排查**：`sudo lsof -i :8096`

**常见占用者**：
- Tailscale Funnel（如果配置了 `tailscale serve` 或 Funnel）
- 其他服务

**解决方案**：
1. 换端口：`-p 8097:8096`（外部访问用8097）
2. 或停用Tailscale对该端口的转发

### 媒体目录挂载缺失（电影不显示）

**症状**：下载了电影，但 Jellyfin 媒体库扫描不到

**排查步骤**：
```bash
# 1. 检查 Docker 挂载
docker inspect jellyfin | grep -A20 "Mounts"

# 2. 检查容器内能否访问
docker exec jellyfin ls /media/movies
```

**根因**：部署时忘记 `-v` 挂载媒体目录

**修复**：重建容器，添加正确的挂载：
```bash
docker stop jellyfin && docker rm jellyfin

docker run -d \
  --name jellyfin \
  -p 8097:8096 \
  -v /path/to/jellyfin-config:/config \
  -v /path/to/jellyfin-cache:/cache \
  -v /path/to/movies:/media/movies \
  -v /path/to/photos:/media/photos \
  jellyfin/jellyfin:latest
```

**注意**：`/config` 卷保留配置，重建不丢失媒体库设置。

### 已删除的文件仍显示在媒体库

**原因**：Jellyfin数据库有缓存，删除文件不会自动移除条目。

**解决**：控制台 → 媒体库 → 扫描媒体库 → **勾选「清理缺失文件」/「清除缺失的媒体」**

单个条目：在电影详情页 → 编辑 → 删除

---

## CD抓轨（Whipper）

### 安装

```bash
sudo apt install -y whipper
```

### 配置

```bash
mkdir -p ~/.config/whipper
```

`~/.config/whipper/whipper.conf`:

```ini
[core]
music_dir = /path/to/music
top_path = %A/%d

[whipper.cdparanoia]
parity = 2

[whipper.command.logger]
whatcd = false
```

### 使用

1. 插入USB光驱，放入CD
2. 运行：`whipper cd rip`
3. 自动完成：识别CD → MusicBrainz获取封面/元数据 → 抓轨FLAC → 存入音乐目录
4. Navidrome自动扫描

### CD信息查不到

```bash
whipper cd rip --unknown  # 手动输入专辑信息
```

---

## 常见安装故障

### dpkg报错 "liblzma.so.5: version XZ_5.4 not found"

**原因**：腾讯会议(wemeet)的liblzma版本冲突，干扰系统dpkg

**修复**：

```bash
sudo mv /opt/wemeet/lib/liblzma.so.5 /opt/wemeet/lib/liblzma.so.5.bak
sudo apt install -y <你要装的包>
```

---

## 文件结构示例

```
/media/
├── movies/
│   ├── 电影名 (年份)/
│   │   └── 电影名.年份.分辨率.编码.mkv
├── tvshows/
│   └── 剧集名/
│       └── Season 01/
│           └── S01E01.mkv
├── music/
│   └── 艺术家/
│       └── 专辑名/
│           ├── 01.歌曲名.flac
│           └── cover.jpg
```
