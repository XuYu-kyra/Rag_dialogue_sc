# Central configuration. Secrets and machine-specific paths come from environment variables.
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

WEAVIATE_CONFIG = {
    'http_host': os.getenv('WEAVIATE_HTTP_HOST', '127.0.0.1'),
    'http_port': int(os.getenv('WEAVIATE_HTTP_PORT', '8080')),
    'api_key': os.getenv('WEAVIATE_API_KEY', 'test-secret-key'),
}

DEEPSEEK_CONFIG = {
    'api_key': os.getenv('DEEPSEEK_API_KEY'),
    'base_url': os.getenv('DEEPSEEK_BASE_URL', 'https://api.deepseek.com'),
}

TTS_CONFIG = {
    'api_url': os.getenv('TTS_API_URL', 'http://127.0.0.1:9880/tts'),
    'ref_audio_path': os.getenv(
        'TTS_REF_AUDIO_PATH',
        str(PROJECT_ROOT / 'GPT_SoVITS' / 'liuyinxia_2_resample_68.wav'),
    ),
    'params': {
        'text_lang': 'zh',
        'prompt_lang': 'zh',
        'top_k': 5,
        'top_p': 1,
        'temperature': 1,
        'text_split_method': 'cut0',
        'batch_size': 1,
        'batch_threshold': 0.75,
        'split_bucket': True,
        'speed_factor': 1.0,
        'seed': -1,
        'parallel_infer': True,
        'repetition_penalty': 1.35,
    },
}

APP_CONFIG = {
    'debug': os.getenv('FLASK_DEBUG', '0') == '1',
    'host': os.getenv('FLASK_HOST', '127.0.0.1'),
    'port': int(os.getenv('FLASK_PORT', '5000')),
    'audio_dir': os.getenv('AUDIO_DIR', str(PROJECT_ROOT / 'static' / 'audio')),
}