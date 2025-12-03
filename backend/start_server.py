#!/usr/bin/env python3
"""
Backend server startup script - keeps the server running
"""
import uvicorn

if __name__ == "__main__":
    print("🚀 Starting FastAPI server...")
    print("📍 Server will run on: http://localhost:8000")
    print("📖 API docs at: http://localhost:8000/docs")
    print("⚠️  Press Ctrl+C to stop the server")
    print("-" * 60)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes
        log_level="info"
    )
