@echo off
echo 正在启动本地服务器...
echo.
echo 服务器将在 http://localhost:8000 运行
echo 按 Ctrl+C 可以停止服务器
echo.
python -m http.server 8000
