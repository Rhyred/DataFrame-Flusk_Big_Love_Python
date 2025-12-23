@echo off
REM Script untuk menjalankan Flask Dashboard - Windows

echo ============================================
echo Dashboard Penderita Diabetes Melitus
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python tidak ditemukan di system!
    echo Pastikan Python sudah terinstall dan ditambahkan ke PATH
    pause
    exit /b 1
)

echo Checking dependencies...
echo.

REM Check if requirements.txt exists
if not exist "requirements.txt" (
    echo ERROR: requirements.txt tidak ditemukan!
    pause
    exit /b 1
)

REM Install requirements
echo Installing packages from requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Gagal menginstall packages!
    pause
    exit /b 1
)

echo.
echo ============================================
echo ✅ Semua dependencies terinstall
echo ============================================
echo.

REM Run the application
echo Starting Flask application...
echo Dashboard akan berjalan di: http://localhost:5000
echo.
echo Tekan CTRL+C untuk menghentikan aplikasi
echo.

python app.py

pause
