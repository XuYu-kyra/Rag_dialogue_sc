<<<<<<< HEAD
# sunce_chat
=======
# Rag_dialogue_sc

一个基于 Flask 的简易对话与语音演示项目，包含：
- Web 前端页面（`templates/index.html` + `static/`）
- 后端服务（`app.py`）
- 第三方服务客户端封装（`api/`：如大模型、TTS、向量库等）

适合作为本地原型与演示：文本/语音问答、调用外部大模型与语音合成服务等。

---

## 目录结构
```
sunce_chat/
├─ app.py                # Flask 入口
├─ api/                  # 外部服务客户端（LLM、TTS、向量库等）
│  ├─ config.py
│  ├─ deepseek_client.py
│  ├─ tts_client.py
│  └─ weaviate_client.py
├─ templates/
│  └─ index.html         # 前端页面模板
├─ static/
│  ├─ css/style.css
│  ├─ js/chat.js
│  └─ audio/             # 生成的音频文件
├─ requirements.txt      # 依赖
└─ README.md
```

---

## 快速开始（Windows）

### 1) 准备环境
- 安装 Python 3.9+（建议 3.10/3.11）
- 安装 Git（用于推送到 GitHub，可选）

### 2) 进入项目
如果你已经在本地有本项目，可直接进入目录：
```powershell
cd .\sunce_chat
```

### 3) 创建并激活虚拟环境
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
如果执行策略限制导致无法激活，可先运行：
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 4) 安装依赖
```powershell
pip install -r requirements.txt
```

> 如需 CUDA/音频相关依赖，请根据你的硬件/驱动在安装前设置好环境。

### 5) 运行项目
```powershell
python app.py
```
默认会在 `http://127.0.0.1:5000` 启动。打开浏览器访问即可。

---

## 配置说明
部分外部服务（如大模型、TTS、向量数据库）需要 API Key 或连接信息。请查看并按需修改：
- `api/config.py`
- `api/deepseek_client.py`
- `api/tts_client.py`
- `api/weaviate_client.py`

常见做法：
- 使用环境变量存放敏感信息（API Key、URL 等）
- 在 PowerShell 中设置环境变量（示例）：
```powershell
$env:DEEPSEEK_API_KEY = "your_api_key_here"
$env:TTS_API_KEY = "your_tts_key_here"
$env:WEAVIATE_ENDPOINT = "http://localhost:8080"
```
然后运行：
```powershell
python app.py
```

---

<<<<<<< HEAD
=======
### 本仓库实际展示（TTS 音频）


[下载/试听（sunce_1744476113_b6a7f359.wav）](sunce_chat/static/audio/sunce_1744476113_b6a7f359.wav)

---

   
### 本仓库实际展示

- 仓库内视频直链（建议用浏览器直接下载/观看）：

[下载/观看 MP4（demo.mp4）](sunce_chat/static/final.mp4)

生成 GIF（本地有 ffmpeg 的示例命令）：
```powershell
# 先将 mp4 转为 10fps 的中间帧
ffmpeg -i demo.mp4 -vf "fps=10,scale=800:-1:flags=lanczos" -y frames_%04d.png
# 合成为 gif（简单方式）
ffmpeg -i frames_%04d.png -vf "palettegen=stats_mode=full" -y palette.png
ffmpeg -i frames_%04d.png -i palette.png -lavfi "paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle" -y demo.gif
```

---

## 常见问题
- 端口被占用：修改 `app.py` 中的端口，或结束占用该端口的进程。
- 依赖安装失败：升级 pip 或单独安装有问题的包。
```powershell
python -m pip install --upgrade pip
```
- 无法播放音频：检查 `static/audio/` 是否有生成的音频文件，浏览器控制台是否报错。

---

## 开发建议
- 建议添加 `.gitignore`（忽略 `.venv/`、`__pycache__/`、`*.pyc`、`static/audio/*.wav` 等大文件或临时文件）。
- 将密钥放环境变量，不要提交到仓库。

示例 `.gitignore` 片段：
```
# Python
.venv/
__pycache__/
*.pyc

# Audio cache
static/audio/*.wav

# OS / IDE
.DS_Store
.vscode/
.idea/
```

---

## 许可证
未指定许可证时默认保留所有权利。若需开源，请添加合适的 `LICENSE` 文件（如 MIT、Apache-2.0）。
