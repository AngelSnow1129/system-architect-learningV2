// Marked.js 备用加载方案
// 如果CDN加载失败，尝试从其他CDN加载

(function() {
    // 检查marked是否已加载
    if (typeof marked !== 'undefined') {
        console.log('✅ Marked.js 已加载');
        return;
    }

    console.warn('⚠️ Marked.js 未从主CDN加载，尝试备用CDN...');

    // 备用CDN列表
    const fallbackCDNs = [
        'https://cdn.jsdelivr.net/npm/marked@9.1.6/marked.min.js',
        'https://unpkg.com/marked@9.1.6/marked.min.js',
        'https://cdnjs.cloudflare.com/ajax/libs/marked/9.1.6/marked.min.js'
    ];

    let currentIndex = 0;

    function loadNextCDN() {
        if (currentIndex >= fallbackCDNs.length) {
            console.error('❌ 所有CDN都加载失败');
            showError();
            return;
        }

        const script = document.createElement('script');
        script.src = fallbackCDNs[currentIndex];
        
        script.onload = function() {
            console.log('✅ Marked.js 从备用CDN加载成功:', fallbackCDNs[currentIndex]);
        };

        script.onerror = function() {
            console.warn('❌ CDN加载失败:', fallbackCDNs[currentIndex]);
            currentIndex++;
            loadNextCDN();
        };

        document.head.appendChild(script);
    }

    function showError() {
        const contentDiv = document.getElementById('markdown-content');
        if (contentDiv) {
            contentDiv.innerHTML = `
                <div style="text-align: center; padding: 50px; color: #f5576c;">
                    <h2>😕 无法加载Markdown解析库</h2>
                    <p>所有CDN都无法访问，请检查网络连接</p>
                    <p style="color: #999; font-size: 0.9em;">
                        可能的原因：<br>
                        1. 网络连接问题<br>
                        2. 防火墙或代理设置<br>
                        3. CDN服务暂时不可用
                    </p>
                    <button onclick="location.reload()" style="
                        padding: 10px 20px;
                        background: #667eea;
                        color: white;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        margin-top: 20px;
                    ">重新加载</button>
                </div>
            `;
        }
    }

    // 延迟1秒后开始尝试备用CDN
    setTimeout(loadNextCDN, 1000);
})();
