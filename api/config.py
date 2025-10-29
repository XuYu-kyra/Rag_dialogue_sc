# 配置文件
import os

# Weaviate配置
WEAVIATE_CONFIG = {
    'http_host': '127.0.0.1',
    'http_port': 8080,
    'api_key': 'test-secret-key'
}

# DeepSeek配置
DEEPSEEK_CONFIG = {
    'api_key': 'sk-bc4c38af14ae4822928e258c6128e44a',
    'base_url': 'https://api.deepseek.com'
}

# TTS配置
TTS_CONFIG = {
    'api_url': 'http://127.0.0.1:9880/tts',
    'ref_audio_path': 'GPT_SoVITS/liuyinxia_2_resample_68.wav',
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
        'repetition_penalty': 1.35
    }
}

# 应用配置
APP_CONFIG = {
    'debug': True,
    'host': '0.0.0.0',
    'port': 5000,
    'audio_dir': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'audio')
} 