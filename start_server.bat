@echo off
chcp 65001 >nul
echo ========================================
echo   系统架构设计师学习平台
echo ========================================
echo.
echo 正在启动本地服务器...
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo 使用Python启动服务器...
    echo 服务器地址: http://localhost:8000
    echo 主页地址: http://localhost:8000/web/
    echo.
    echo 按 Ctrl+C 停止服务器
    echo ========================================
    echo.
    start http://localhost:8000/web/
    python -m http.server 8000
) else (
    echo Python未安装，尝试直接打开主页...
    echo.
    if exist "web\index.html" (
        start web\index.html
    ) else (
        echo 错误：找不到 web\index.html 文件
        echo 请确保文件结构完整
    )
    pause
)
