import requests
import os
import time
import uuid
from .config import TTS_CONFIG, APP_CONFIG

def text_to_speech(text):
    """
    将文本转换为语音
    
    :param text: 要转换的文本
    :return: 音频文件路径
    """
    # 准备参数
    params = TTS_CONFIG['params'].copy()
    params['text'] = text
    params['ref_audio_path'] = TTS_CONFIG['ref_audio_path']
    
    # 生成唯一文件名
    filename = f"sunce_{int(time.time())}_{uuid.uuid4().hex[:8]}.wav"
    output_path = os.path.join(APP_CONFIG['audio_dir'], filename)
    
    try:
        # 发送请求
        response = requests.get(TTS_CONFIG['api_url'], params=params)
        
        # 检查响应
        if response.status_code == 200:
            # 保存音频文件
            with open(output_path, "wb") as f:
                f.write(response.content)
            return filename
        else:
            print(f"TTS错误: {response.text}")
            return None
            
    except Exception as e:
        print(f"TTS发生错误: {str(e)}")
        return None 