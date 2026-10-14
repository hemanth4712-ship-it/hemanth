#!/usr/bin/env python3
"""
Smart Dairy Farm Management System - Runner Script
Starts the FastAPI application and serves both the REST API and the modern Web UI.
"""
import os
import sys
import uvicorn

# Ensure the backend directory is in the Python search path
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "127.0.0.1")
    
    print("\n" + "="*65)
    print(" 🐄 SMART DAIRY FARM MANAGEMENT SYSTEM (గోకులం డైరీ) 🐄 ")
    print("="*65)
    print(f" • Modern Web UI : http://localhost:{port}/")
    print(f" • Swagger APIs  : http://localhost:{port}/docs")
    print(f" • ReDoc Specs   : http://localhost:{port}/redoc")
    print(f" • Demo Account  : farmer@dairy.in / farmer123")
    print("="*65 + "\n")
    
    uvicorn.run("app.main:app", host=host, port=port, reload=True)
