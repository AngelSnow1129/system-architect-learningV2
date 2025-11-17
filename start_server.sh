#!/bin/bash

echo "========================================"
echo "  系统架构设计师学习平台"
echo "========================================"
echo ""
echo "正在启动本地服务器..."
echo ""

# 检查Python是否安装
if command -v python3 &> /dev/null; then
    echo "使用Python3启动服务器..."
    echo "服务器地址: http://localhost:8000"
    echo "主页地址: http://localhost:8000/web/"
    echo ""
    echo "按 Ctrl+C 停止服务器"
    echo "========================================"
    echo ""
    
    # 尝试自动打开浏览器
    if command -v xdg-open &> /dev/null; then
        xdg-open http://localhost:8000/web/ &
    elif command -v open &> /dev/null; then
        open http://localhost:8000/web/ &
    fi
    
    python3 -m http.server 8000
elif command -v python &> /dev/null; then
    echo "使用Python启动服务器..."
    echo "服务器地址: http://localhost:8000"
    echo "主页地址: http://localhost:8000/web/"
    echo ""
    echo "按 Ctrl+C 停止服务器"
    echo "========================================"
    echo ""
    
    # 尝试自动打开浏览器
    if command -v xdg-open &> /dev/null; then
        xdg-open http://localhost:8000/web/ &
    elif command -v open &> /dev/null; then
        open http://localhost:8000/web/ &
    fi
    
    python -m http.server 8000
else
    echo "Python未安装，尝试直接打开主页..."
    echo ""
    if [ -f "web/index.html" ]; then
        if command -v xdg-open &> /dev/null; then
            xdg-open web/index.html
        elif command -v open &> /dev/null; then
            open web/index.html
        else
            echo "无法自动打开浏览器，请手动打开 web/index.html"
        fi
    else
        echo "错误：找不到 web/index.html 文件"
        echo "请确保文件结构完整"
    fi
    read -p "按任意键退出..."
fi
