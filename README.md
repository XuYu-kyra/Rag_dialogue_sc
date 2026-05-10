# RAG Dialogue System for Historical Character Interaction

This project is a Flask-based prototype for a dialogue and speech demo centered on a historical character. It combines a web interface, backend orchestration, large language model calls, text-to-speech generation, and vector retrieval components.

The repository is intended as a local prototype and demonstration environment for:
- text and speech question answering
- retrieval-augmented generation workflows
- integration with external LLM, TTS, and vector database services

## Project Structure

```text
sunce_chat/
├─ app.py                # Flask entry point
├─ api/                  # External service clients (LLM, TTS, vector DB)
│  ├─ config.py
│  ├─ deepseek_client.py
│  ├─ tts_client.py
│  └─ weaviate_client.py
├─ templates/
│  └─ index.html         # Front-end page template
├─ static/
│  ├─ css/style.css
│  ├─ js/chat.js
│  └─ audio/             # Generated audio files
├─ requirements.txt
└─ README.md
```

## Features

- Web-based chat interface built with Flask
- Role-oriented dialogue generation for a historical character
- External large language model integration
- Text-to-speech generation for spoken responses
- Vector database support for retrieval-augmented responses

## Getting Started

### 1. Prepare the environment

- Python 3.9 or later is recommended
- Git is optional but useful for version control

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python app.py
```

By default, the application starts at `http://127.0.0.1:5000`.

## Configuration

Some external services require API keys or connection settings. Review and adjust these files as needed:

- `api/config.py`
- `api/deepseek_client.py`
- `api/tts_client.py`
- `api/weaviate_client.py`

A common approach is to use environment variables for sensitive information.

Example:

```bash
export DEEPSEEK_API_KEY="your_api_key_here"
export TTS_API_KEY="your_tts_key_here"
export WEAVIATE_ENDPOINT="http://localhost:8080"
python app.py
```

## Demo Assets

- Audio example: `static/audio/`
- Video demo: `static/final.mp4`

If you want to create a GIF preview locally, you can use `ffmpeg`:

```bash
ffmpeg -i demo.mp4 -vf "fps=10,scale=800:-1:flags=lanczos" -y frames_%04d.png
ffmpeg -i frames_%04d.png -vf "palettegen=stats_mode=full" -y palette.png
ffmpeg -i frames_%04d.png -i palette.png -lavfi "paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle" -y demo.gif
```

## Common Issues

- Port already in use: change the port in `app.py` or stop the conflicting process
- Dependency installation fails: upgrade `pip` and retry
- Audio playback fails: check whether generated audio files exist in `static/audio/`

## Development Notes

- Add a `.gitignore` to exclude `.venv/`, `__pycache__/`, `*.pyc`, and generated audio files
- Store API keys in environment variables instead of committing them

Example `.gitignore` snippet:

```gitignore
.venv/
__pycache__/
*.pyc
static/audio/*.wav
.DS_Store
.vscode/
.idea/
```

## License

No license is currently specified. If you plan to open-source this project, add an appropriate `LICENSE` file such as MIT or Apache-2.0.
