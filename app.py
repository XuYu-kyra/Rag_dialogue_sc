from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import asyncio
import threading
from api.weaviate_client import search_sunce
from api.deepseek_client import sunce_qa
from api.tts_client import text_to_speech
from api.config import APP_CONFIG

app = Flask(__name__)

# 确保音频目录存在
os.makedirs(APP_CONFIG['audio_dir'], exist_ok=True)

@app.route('/')
def home():
    """渲染主页"""
    return render_template('index.html')

@app.route('/static/audio/<path:filename>')
def serve_audio(filename):
    """提供音频文件"""
    return send_from_directory(APP_CONFIG['audio_dir'], filename)

@app.route('/api/chat', methods=['POST'])
def chat():
    """处理聊天请求"""
    data = request.json
    question = data.get('message', '')
    
    if not question:
        return jsonify({'error': '问题不能为空'}), 400
    
    try:
        # 搜索相关史料
        retrieved_docs = search_sunce(question)
        
        # 生成孙策的回答
        answer = sunce_qa(question, retrieved_docs)
        
        return jsonify({
            'answer': answer,
            'success': True
        })
    except Exception as e:
        print(f"聊天处理错误: {str(e)}")
        return jsonify({
            'error': '处理您的问题时出现了错误',
            'success': False
        }), 500

@app.route('/api/tts', methods=['POST'])
def tts():
    """处理文字转语音请求"""
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': '文本不能为空'}), 400
    
    try:
        # 在后台线程中处理TTS请求，避免阻塞主线程
        def process_tts():
            nonlocal filename  # 使用nonlocal关键字
            filename = text_to_speech(text)
            if filename:
                print(f"TTS成功: {filename}")
            else:
                print("TTS失败")
        
        filename = None  # 初始化filename
        thread = threading.Thread(target=process_tts)
        thread.daemon = True
        thread.start()
        
        # 等待线程完成
        thread.join()
        
        return jsonify({
            'message': 'TTS请求已接收，正在处理',
            'success': True,
            'audio_file': filename  # 返回音频文件名
        })
    except Exception as e:
        print(f"TTS处理错误: {str(e)}")
        return jsonify({
            'error': '处理TTS请求时出现了错误',
            'success': False
        }), 500

if __name__ == '__main__':
    app.run(
        debug=APP_CONFIG['debug'],
        host=APP_CONFIG['host'],
        port=APP_CONFIG['port']
    ) 