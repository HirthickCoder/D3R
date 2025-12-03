@echo off
echo ========================================
echo Starting FastAPI Backend Server
echo ========================================
echo.
echo Server will run on: http://localhost:8000
echo API docs at: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

uvicorn main:app --reload --host 0.0.0.0 --port 8000

pause
