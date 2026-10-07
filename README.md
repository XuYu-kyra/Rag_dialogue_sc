# RAG Dialogue System for Historical Character Interaction

[English](#english) · [中文](#中文)

## English

This Flask prototype lets a user chat with a historically grounded “Sun Ce” character. It combines multilingual semantic retrieval, prompt-controlled generation, short conversation memory, and text-to-speech so that the result feels like an interactive character rather than a raw question-answer endpoint.

### The story

Historical role-play has two competing requirements: the answer should be engaging, but it should not drift away from the available sources. I designed the request path so retrieval happens before generation. The model receives ranked source snippets and speaker metadata, while the prompt anchors identity, tone, and rules for uncertainty.

### What I built

- A Flask web UI and JSON API with `/api/chat` and `/api/tts` endpoints.
- A Weaviate semantic-search client using `paraphrase-multilingual-MiniLM-L12-v2` embeddings and top-k retrieval from the `SunCeDocs` collection.
- A DeepSeek client with a role-specific prompt, source context, and up to five turns of in-memory conversation history.
- A TTS adapter that writes generated audio into the configured static audio directory and serves it back to the browser.
- A simple front end for text interaction and audio playback, plus local demo assets for explaining the system.

### Request flow

```text
question -> multilingual embedding -> Weaviate top-k sources
         -> identity/style/grounding prompt -> DeepSeek response
         -> optional TTS -> browser playback
```

### Quick start

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows:    .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

The app listens on `http://127.0.0.1:5000` by default. Configure API keys, Weaviate connection details, TTS endpoint, and audio paths in `api/config.py` or, preferably, through environment-backed configuration before deployment.

### Engineering trade-offs and limits

The prototype keeps conversation history in process memory and uses a synchronous local request path for predictable demos. Retrieval quality depends on the indexed corpus, and role-play output is not a substitute for historical scholarship. A production version would add persistent sessions, timeouts/retries, source citations in the UI, secret management, content moderation, and evaluation for groundedness and latency.

## 中文

这是一个 Flask 历史人物对话原型：用户可以与“孙策”角色聊天，系统先从 Weaviate 中检索相关史料，再把史料片段、说话人信息、身份设定和短期对话历史交给 DeepSeek 生成，最后可选地调用 TTS 播放语音。

### 项目故事

历史角色扮演同时要求“有趣”和“不能脱离史料”。因此我把检索放在生成之前：每次请求先用多语句向量找到 `SunCeDocs` 中的相关文本，再通过 prompt 约束身份、语气、白话表达和不确定信息的处理方式，而不是让模型无依据地自由发挥。

### 我的工作

- 使用 Flask 搭建网页和 JSON API，提供 `/api/chat` 与 `/api/tts`；
- 使用 `paraphrase-multilingual-MiniLM-L12-v2` 生成 embedding，并通过 Weaviate 做 top-k 语义检索；
- 封装 DeepSeek 调用，组织史料上下文、身份锚定、风格规则和最多五轮进程内对话历史；
- 封装 TTS 接口，把生成的音频写入静态目录并返回浏览器播放；
- 组织前端聊天、音频播放和演示素材，形成从问题到语音回答的完整链路。

### 快速运行

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

默认地址是 `http://127.0.0.1:5000`。部署前请配置 DeepSeek、Weaviate 和 TTS 的凭据与地址，推荐使用环境变量而不是把密钥写入代码。

### 边界与下一步

当前版本把对话历史保存在进程内，适合本地演示；检索质量依赖索引语料，角色回答也不能替代历史研究。产品化还需要持久化会话、超时重试、界面引用来源、密钥管理、内容安全和 groundedness/延迟评测。
