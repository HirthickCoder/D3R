"""
Keep-alive server script - prevents VS Code terminal from killing the server
"""
import uvicorn
import sys
import os

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Starting FastAPI Backend Server")
    print("=" * 60)
    print("\n📍 Server running on: http://localhost:8000")
    print("📖 API Documentation: http://localhost:8000/docs")
    print("🔗 Test endpoint: http://localhost:8000/api/menu/")
    print("\n⚠️  IMPORTANT: Keep this window open!")
    print("   Press Ctrl+C to stop the server\n")
    print("=" * 60)
    print()
    
    try:
        # Run with reload enabled for development
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info",
            access_log=True
        )
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        input("Press Enter to exit...")
        sys.exit(1)
