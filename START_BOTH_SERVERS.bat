@echo off
title FoodieHub - Starting Both Servers

echo ========================================
echo   Starting FoodieHub Application
echo ========================================
echo.

echo [1/2] Starting Backend Server...
echo.
start cmd /k "cd /d %~dp0backend && title Backend Server - Port 8000 && python run_server.py"

timeout /t 3 /nobreak >nul

echo [2/2] Starting Frontend Server...
echo.
start cmd /k "cd /d %~dp0 && title Frontend Server - Port 3002 && npm run dev"

echo.
echo ========================================
echo   Both servers are starting!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3002
echo.
echo Two new windows will open - KEEP THEM OPEN!
echo Close this window when done.
echo ========================================

pause
