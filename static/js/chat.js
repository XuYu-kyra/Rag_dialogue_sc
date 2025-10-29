// 全局变量
let currentAudio = null;
let isProcessing = false;

// DOM元素
const chatMessages = document.querySelector('.chat-messages');
const messageInput = document.querySelector('#message-input');
const sendButton = document.querySelector('#send-button');
const audioPlayer = document.querySelector('#audio-player');
const audioSource = document.querySelector('#audio-source');

// 初始化
document.addEventListener('DOMContentLoaded', () => {
    // 添加欢迎消息
    addMessage('sunce', '你好啊！我是江东孙策。');
    
    // 事件监听器
    sendButton.addEventListener('click', handleSend);
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    });
});

// 处理发送消息
async function handleSend() {
    if (isProcessing) return;
    
    const message = messageInput.value.trim();
    if (!message) return;
    
    // 清空输入框
    messageInput.value = '';
    
    // 添加用户消息
    addMessage('user', message);
    
    // 显示加载动画
    showTypingIndicator();
    
    try {
        isProcessing = true;
        
        // 发送请求到后端
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });
        
        const data = await response.json();
        
        if (!data.success) {
            throw new Error(data.error);
        }
        
        // 移除加载动画
        removeTypingIndicator();
        
        // 添加孙策回复
        addMessage('sunce', data.answer);
        
        // 生成语音
        await generateSpeech(data.answer);
        
    } catch (error) {
        console.error('Error:', error);
        removeTypingIndicator();
        addMessage('system', '抱歉，发生了一些错误。请稍后再试。');
    } finally {
        isProcessing = false;
    }
}

// 添加消息到聊天界面
function addMessage(sender, text) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    
    const now = new Date();
    const time = now.toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' });

    // 为用户消息创建不同的HTML结构
    if (sender === 'user') {
        messageDiv.innerHTML = `
            <div class="message-content">
                <div class="message-header">
                    <span class="message-sender">你</span>
                    <span class="message-time">${time}</span>
                </div>
                <div class="message-text">${text}</div>
            </div>
            <div class="avatar"></div>
        `;
    } else if (sender === 'system') {
        messageDiv.innerHTML = `
            <div class="message-content">
                <div class="message-header">
                    <span class="message-sender">系统</span>
                    <span class="message-time">${time}</span>
                </div>
                <div class="message-text">${text}</div>
            </div>
        `;
    } else {
        // 孙策的消息，添加点赞和倒赞按钮
        messageDiv.innerHTML = `
            <div class="avatar"></div>
            <div class="message-content">
                <div class="message-header">
                    <span class="message-sender">孙策</span>
                    <span class="message-time">${time}</span>
                </div>
                <div class="message-text">${text}</div>
                <div class="feedback-buttons">
                    <button class="feedback-button like-button" title="点赞">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" fill="none" stroke="currentColor" stroke-width="2"/>
                        </svg>
                    </button>
                    <button class="feedback-button dislike-button" title="倒赞">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M12 2.65l1.45 1.32C18.6 8.64 22 11.72 22 15.5c0 3.08-2.42 5.5-5.5 5.5-1.74 0-3.41-.81-4.5-2.09C10.91 20.19 9.24 21 7.5 21 4.42 21 2 18.58 2 15.5c0-3.78 3.4-6.86 8.55-11.54L12 2.65z" fill="none" stroke="currentColor" stroke-width="2"/>
                        </svg>
                    </button>
                </div>
            </div>
        `;
        
        // 添加点击事件处理
        setTimeout(() => {
            const likeButton = messageDiv.querySelector('.like-button');
            const dislikeButton = messageDiv.querySelector('.dislike-button');
            
            if (likeButton && dislikeButton) {
                likeButton.addEventListener('click', function() {
                    handleFeedback(messageDiv, 'like');
                });
                
                dislikeButton.addEventListener('click', function() {
                    handleFeedback(messageDiv, 'dislike');
                });
            }
        }, 0);
    }

    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// 处理点赞和倒赞
function handleFeedback(messageDiv, type) {
    const likeButton = messageDiv.querySelector('.like-button');
    const dislikeButton = messageDiv.querySelector('.dislike-button');
    
    if (type === 'like') {
        if (likeButton.classList.contains('liked')) {
            // 取消点赞
            likeButton.classList.remove('liked');
        } else {
            // 点赞
            likeButton.classList.add('liked');
            dislikeButton.classList.remove('disliked'); // 移除倒赞
        }
    } else {
        if (dislikeButton.classList.contains('disliked')) {
            // 取消倒赞
            dislikeButton.classList.remove('disliked');
        } else {
            // 倒赞
            dislikeButton.classList.add('disliked');
            likeButton.classList.remove('liked'); // 移除点赞
        }
    }
    
    // 这里可以添加发送反馈到服务器的代码
    // sendFeedbackToServer(messageDiv.dataset.messageId, type);
}

// 显示加载动画
function showTypingIndicator() {
    const indicator = document.createElement('div');
    indicator.className = 'message sunce';
    indicator.innerHTML = `
        <div class="typing-indicator">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;
    indicator.id = 'typing-indicator';
    chatMessages.appendChild(indicator);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// 移除加载动画
function removeTypingIndicator() {
    const indicator = document.getElementById('typing-indicator');
    if (indicator) {
        indicator.remove();
    }
}

// 生成语音
async function generateSpeech(text) {
    try {
        const response = await fetch('/api/tts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });
        
        const data = await response.json();
        
        if (!data.success) {
            throw new Error(data.error);
        }
        
        // 播放音频
        if (data.audio_file) {
            playAudio(data.audio_file);
        }
        
    } catch (error) {
        console.error('TTS Error:', error);
    }
}

// 播放音频
function playAudio(audioFile) {
    // 停止当前播放的音频
    if (currentAudio) {
        currentAudio.pause();
        currentAudio = null;
    }
    
    // 更新音频源并播放
    audioSource.src = `/static/audio/${audioFile}`;
    audioPlayer.load();
    
    // 确保音频加载完成后播放
    audioPlayer.oncanplaythrough = () => {
        audioPlayer.play().catch(error => {
            console.error('播放音频失败:', error);
        });
        currentAudio = audioPlayer;
        
        // 显示音频播放器
        audioPlayer.parentElement.style.display = 'flex';
    };
} 