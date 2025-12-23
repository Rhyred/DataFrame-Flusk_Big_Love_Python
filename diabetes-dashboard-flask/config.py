"""
Konfigurasi Dashboard Penderita Diabetes Melitus
"""

import os

# Flask Configuration
DEBUG = True
PORT = 5000
HOST = '127.0.0.1'

# Data Configuration
DATA_FILE = '../dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv'
STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'static')
UPLOAD_FOLDER = os.path.join(STATIC_FOLDER, 'images')

# Pagination
ITEMS_PER_PAGE = 15

# Chart Configuration
CHART_DPI = 100
CHART_FIGSIZE = (10, 6)

# Category Ranges
CATEGORY_RANGES = {
    'Tinggi': (100000, float('inf')),
    'Sedang': (50000, 99999),
    'Rendah': (0, 49999)
}

# Color Configuration
COLORS = {
    'primary': '#3b82f6',
    'success': '#10b981',
    'warning': '#f59e0b',
    'danger': '#ef4444',
    'gray': '#6b7280'
}

# Chart Colors
CHART_COLORS = ['#ef4444', '#f59e0b', '#10b981']

# App Settings
APP_NAME = 'Dashboard Penderita Diabetes Melitus'
APP_SUBTITLE = 'Jawa Barat'
APP_VERSION = '1.0.0'

if __name__ == '__main__':
    print(f"Configuration loaded for {APP_NAME}")
    print(f"Debug mode: {DEBUG}")
    print(f"Port: {PORT}")
