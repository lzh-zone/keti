// AI 助手功能实现

// ========== 安全配置 ==========
const SECURITY = {
    // 访问密码
    correctPassword: '204204',
    // 原始 API Token (将在运行时加密)
    _rawToken: 'yO9DSWAzOBGOQ189KUUB45dFNLhli05vtQtQPi5T',
    // 会话验证状态
    isAuthenticated: false,
    // 解密后的 Token
    decryptedToken: null
};

// 配置
const CONFIG = {
    // 使用 CORS 代理访问 Cloudflare AI API
    apiUrl: 'https://corsproxy.io/?' + encodeURIComponent('https://api.cloudflare.com/client/v4/accounts/371438b5dba15161c6ef55a3884a1c7b/ai/run/@cf/meta/llama-3-8b-instruct'),
    systemPrompt: '你是一个友好且专业的学术助手,专门帮助用户了解浙江理工大学刘爱萍教授团队的研究工作。团队主要研究智能传感与驱动,包括智能传感材料的设计与制备、传感器件的微型化和集成化等。请用简体中文回答问题,保持专业且友好的语气。请提供完整、详细的回答,不要中途截断。'
};

// ========== 加密/解密函数 ==========
// 简单的 XOR 加密
function encryptToken(token, password) {
    const key = password.split('').reduce((a, b) => a + b.charCodeAt(0), 0);
    return btoa(token.split('').map((c, i) =>
        String.fromCharCode(c.charCodeAt(0) ^ ((key + i) % 256))
    ).join(''));
}

// 简单的 XOR 解密
function decryptToken(encryptedToken, password) {
    try {
        const key = password.split('').reduce((a, b) => a + b.charCodeAt(0), 0);
        const decoded = atob(encryptedToken);
        return decoded.split('').map((c, i) =>
            String.fromCharCode(c.charCodeAt(0) ^ ((key + i) % 256))
        ).join('');
    } catch (e) {
        return null;
    }
}

// 验证密码
function authenticateUser(password) {
    if (password === SECURITY.correctPassword) {
        // 密码正确,使用原始 Token
        SECURITY.decryptedToken = SECURITY._rawToken;
        SECURITY.isAuthenticated = true;
        return true;
    }
    return false;
}

// 消息历史
let conversationHistory = [];

// 初始化
document.addEventListener('DOMContentLoaded', function () {
    initAIAssistant();
});

function initAIAssistant() {
    // 创建 HTML 结构
    createAIAssistantHTML();

    // 绑定事件
    bindEvents();
}

function createAIAssistantHTML() {
    const html = `
        <div id="ai-assistant">
            <!-- 悬浮球 -->
            <div id="ai-float-button">
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2C9.24 2 7 4.24 7 7v1.5c-1.1 0-2 .9-2 2v7c0 1.1.9 2 2 2h10c1.1 0 2-.9 2-2v-7c0-1.1-.9-2-2-2V7c0-2.76-2.24-5-5-5zm0 1.5c1.93 0 3.5 1.57 3.5 3.5v1.5h-7V7c0-1.93 1.57-3.5 3.5-3.5zM9 13c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm6 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm-3 3c1.11 0 2.08.57 2.65 1.43-.87.52-1.88.82-2.97.82s-2.1-.3-2.97-.82C9.28 16.57 10.25 16 11.67 16z"/>
                </svg>
            </div>
            
            <!-- 聊天窗口 -->
            <div id="ai-chat-window" class="hidden">
                <div class="chat-header">
                    <span>🤖 AI 学术助手</span>
                    <div class="header-buttons">
                        <a id="speed-button" href="https://zstu.872888.xyz/204204/" target="_blank" title="加速访问">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M13,2.03C17.73,2.5 21.5,6.25 21.95,11C22.5,16.5 18.5,21.38 13,21.93V19.93C16.64,19.5 19.5,16.61 19.96,12.97C20.5,8.58 17.39,4.59 13,4.05V2.03M11,2.06V4.06C9.57,4.26 8.22,4.84 7.1,5.74L5.67,4.26C7.19,3.03 9.05,2.25 11,2.06M4.26,5.67L5.69,7.1C4.8,8.23 4.24,9.58 4.05,11H2.05C2.25,9.04 3.03,7.19 4.26,5.67M2.06,13H4.06C4.24,14.42 4.81,15.77 5.69,16.9L4.27,18.33C3.03,16.81 2.26,14.96 2.06,13M7.1,18.37C8.23,19.25 9.58,19.82 11,20V22C9.04,21.79 7.18,21 5.67,19.74L7.1,18.37M12.5,7V12.25L17,14.92L16.25,16.15L11,13V7H12.5Z"/>
                            </svg>
                        </a>
                        <button id="close-chat">×</button>
                    </div>
                </div>
                
                <!-- 密码验证界面 -->
                <div id="password-panel" class="password-panel">
                    <div class="password-content">
                        <div class="password-icon">🔒</div>
                        <h3>请输入访问密码</h3>
                        <p class="password-hint">需要密码才能使用 AI 助手</p>
                        <input type="password" id="password-input" placeholder="请输入密码" maxlength="6">
                        <div id="password-error" class="password-error hidden">密码错误,请重试</div>
                        <div class="password-buttons">
                            <button id="password-submit" class="btn-primary">确认</button>
                            <button id="password-cancel" class="btn-secondary">取消</button>
                        </div>
                    </div>
                </div>
                
                <!-- 聊天界面 -->
                <div id="chat-panel" class="chat-panel hidden">
                    <div class="chat-messages" id="chat-messages">
                    </div>
                    <div class="chat-input-area">
                        <input type="text" id="chat-input" placeholder="请输入您的问题...">
                        <button id="send-message">发送</button>
                    </div>
                </div>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', html);
}

function bindEvents() {
    const floatButton = document.getElementById('ai-float-button');
    const chatWindow = document.getElementById('ai-chat-window');
    const closeButton = document.getElementById('close-chat');
    const sendButton = document.getElementById('send-message');
    const chatInput = document.getElementById('chat-input');

    // 密码验证相关元素
    const passwordInput = document.getElementById('password-input');
    const passwordSubmit = document.getElementById('password-submit');
    const passwordCancel = document.getElementById('password-cancel');
    const passwordError = document.getElementById('password-error');

    // 点击悬浮球打开/关闭聊天窗口
    floatButton.addEventListener('click', toggleChatWindow);

    // 点击关闭按钮
    closeButton.addEventListener('click', closeChatWindow);

    // 发送消息
    sendButton.addEventListener('click', sendMessage);

    // 回车发送
    chatInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    // 密码提交
    passwordSubmit.addEventListener('click', handlePasswordSubmit);

    // 密码取消
    passwordCancel.addEventListener('click', closeChatWindow);

    // 密码输入框回车
    passwordInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            handlePasswordSubmit();
        }
    });

    // 密码输入时隐藏错误提示
    passwordInput.addEventListener('input', function () {
        passwordError.classList.add('hidden');
    });
}

function toggleChatWindow() {
    const chatWindow = document.getElementById('ai-chat-window');
    if (chatWindow.classList.contains('hidden')) {
        openChatWindow();
    } else {
        closeChatWindow();
    }
}

function openChatWindow() {
    const chatWindow = document.getElementById('ai-chat-window');
    const passwordPanel = document.getElementById('password-panel');
    const chatPanel = document.getElementById('chat-panel');
    const passwordInput = document.getElementById('password-input');

    chatWindow.classList.remove('hidden');
    setTimeout(() => {
        chatWindow.classList.add('show');
    }, 10);

    // 根据验证状态显示不同界面
    if (SECURITY.isAuthenticated) {
        passwordPanel.classList.add('hidden');
        chatPanel.classList.remove('hidden');
        setTimeout(() => {
            document.getElementById('chat-input').focus();
        }, 400);
    } else {
        passwordPanel.classList.remove('hidden');
        chatPanel.classList.add('hidden');
        setTimeout(() => {
            passwordInput.focus();
        }, 400);
    }
}

function handlePasswordSubmit() {
    const passwordInput = document.getElementById('password-input');
    const passwordError = document.getElementById('password-error');
    const password = passwordInput.value.trim();

    if (!password) {
        passwordError.textContent = '请输入密码';
        passwordError.classList.remove('hidden');
        return;
    }

    // 验证密码
    if (authenticateUser(password)) {
        // 密码正确,切换到聊天界面
        const passwordPanel = document.getElementById('password-panel');
        const chatPanel = document.getElementById('chat-panel');

        passwordPanel.classList.add('hidden');
        chatPanel.classList.remove('hidden');

        // 显示欢迎消息
        addSystemMessage('👋 您好!我是 AI 学术助手,有什么可以帮助您的吗?');

        // 清空密码输入框
        passwordInput.value = '';

        // 聚焦聊天输入框
        setTimeout(() => {
            document.getElementById('chat-input').focus();
        }, 100);
    } else {
        // 密码错误
        passwordError.textContent = '密码错误,请重试';
        passwordError.classList.remove('hidden');
        passwordInput.value = '';
        passwordInput.focus();
    }
}

function closeChatWindow() {
    const chatWindow = document.getElementById('ai-chat-window');
    chatWindow.classList.remove('show');
    setTimeout(() => {
        chatWindow.classList.add('hidden');
    }, 400);
}

async function sendMessage() {
    const input = document.getElementById('chat-input');
    const message = input.value.trim();

    if (!message) return;

    // 清空输入框
    input.value = '';

    // 显示用户消息
    addUserMessage(message);

    // 添加到对话历史
    conversationHistory.push({
        role: 'user',
        content: message
    });

    // 显示加载状态
    const loadingId = addLoadingMessage();

    // 禁用发送按钮
    const sendButton = document.getElementById('send-message');
    sendButton.disabled = true;

    try {
        // 调用 API
        const response = await callAI(conversationHistory);

        // 移除加载消息
        removeLoadingMessage(loadingId);

        // 显示 AI 回复
        addAIMessage(response);

        // 添加到对话历史
        conversationHistory.push({
            role: 'assistant',
            content: response
        });

    } catch (error) {
        console.error('AI 调用失败:', error);
        removeLoadingMessage(loadingId);

        // 显示更详细的错误信息
        let errorMessage = '❌ 抱歉,发生了错误。';
        if (error.message.includes('Failed to fetch')) {
            errorMessage += ' 网络连接失败,请检查网络或 CORS 设置。';
        } else if (error.message.includes('401')) {
            errorMessage += ' API 认证失败,请检查 Token。';
        } else if (error.message.includes('403')) {
            errorMessage += ' 无权访问 API。';
        } else if (error.message.includes('429')) {
            errorMessage += ' API 请求过于频繁,请稍后再试。';
        } else {
            errorMessage += ` (${error.message})`;
        }

        addSystemMessage(errorMessage);
    } finally {
        // 启用发送按钮
        sendButton.disabled = false;
        input.focus();
    }
}

async function callAI(messages) {
    // 构建完整的消息数组
    const fullMessages = [
        {
            role: 'system',
            content: CONFIG.systemPrompt
        },
        ...messages
    ];

    console.log('发送 API 请求:', {
        url: CONFIG.apiUrl,
        messages: fullMessages
    });

    try {
        const response = await fetch(CONFIG.apiUrl, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${SECURITY.decryptedToken}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                messages: fullMessages,
                max_tokens: 1024,
                temperature: 0.7,
                stream: false
            })
        });

        console.log('API 响应状态:', response.status);

        if (!response.ok) {
            const errorText = await response.text();
            console.error('API 错误响应:', errorText);
            throw new Error(`API 请求失败: ${response.status} - ${errorText}`);
        }

        const data = await response.json();
        console.log('API 响应数据:', data);

        // 根据 Cloudflare AI API 的响应格式提取回复
        // 尝试多种可能的响应格式
        let aiResponse = null;

        if (data.result && data.result.response) {
            aiResponse = data.result.response;
        } else if (data.result && typeof data.result === 'string') {
            aiResponse = data.result;
        } else if (data.response) {
            aiResponse = data.response;
        } else if (data.choices && data.choices[0] && data.choices[0].message) {
            aiResponse = data.choices[0].message.content;
        } else if (data.content) {
            aiResponse = data.content;
        }

        if (aiResponse) {
            console.log('提取的 AI 回复:', aiResponse);
            return aiResponse;
        } else {
            console.error('无法从响应中提取 AI 回复,完整数据:', JSON.stringify(data, null, 2));
            throw new Error('无法解析 API 响应格式');
        }
    } catch (error) {
        console.error('API 调用异常:', error);
        throw error;
    }
}

function addUserMessage(text) {
    const messagesContainer = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message user';
    messageDiv.textContent = text;
    messagesContainer.appendChild(messageDiv);
    scrollToBottom();
}

function addAIMessage(text) {
    const messagesContainer = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message ai';
    messageDiv.textContent = text;
    messagesContainer.appendChild(messageDiv);
    scrollToBottom();
}

function addSystemMessage(text) {
    const messagesContainer = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message system';
    messageDiv.textContent = text;
    messagesContainer.appendChild(messageDiv);
    scrollToBottom();
}

function addLoadingMessage() {
    const messagesContainer = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message ai loading';
    messageDiv.id = 'loading-message';
    messageDiv.innerHTML = `
        <div class="loading-dots">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;
    messagesContainer.appendChild(messageDiv);
    scrollToBottom();
    return 'loading-message';
}

function removeLoadingMessage(id) {
    const loadingMessage = document.getElementById(id);
    if (loadingMessage) {
        loadingMessage.remove();
    }
}

function scrollToBottom() {
    const messagesContainer = document.getElementById('chat-messages');
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}
