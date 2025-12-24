@echo off
REM Dashboard Startup Script for Windows

echo.
echo 🚀 Starting Professional DM Dashboard...
echo.

REM Check Python
echo 📋 Checking Python...
python --version
echo.

REM Activate virtual environment
echo 📦 Activating virtual environment...
call .venv\Scripts\activate.bat
echo.

REM Start Flask server
echo 🎨 Starting Flask Server...
python app.py

echo.
echo ✅ Dashboard is now running!
echo 📱 Open http://localhost:5000 in your browser
echo.
echo Press Ctrl+C to stop the server
pause
