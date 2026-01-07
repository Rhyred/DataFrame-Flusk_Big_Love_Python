#!/bin/bash
# Dashboard Startup Script

echo "🚀 Starting Professional DM Dashboard..."
echo ""
echo "📋 Checking Python..."
python --version

echo ""
echo "📦 Activating virtual environment..."
source .venv/Scripts/activate || .\.venv\Scripts\activate

echo ""
echo "🎨 Starting Flask Server..."
python app.py

echo ""
echo "✅ Dashboard is now running!"
echo "📱 Open http://localhost:5000 in your browser"
echo ""
echo "Press Ctrl+C to stop the server"
