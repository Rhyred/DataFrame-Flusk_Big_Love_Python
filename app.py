from flask import Flask, render_template, request, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
from datetime import datetime
import io
import base64
import sys

# Set encoding to UTF-8
if sys.stdout.encoding != 'utf-8':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Gunakan backend non-GUI
matplotlib.use('Agg')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'

# Create images folder jika tidak ada
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load dataset - Try multiple paths
dataset_paths = [
    'dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv',
    '../dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv',
    'D:\\frontend12\\dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv',
]

df = None
for path in dataset_paths:
    try:
        df = pd.read_csv(path)
        print("[OK] Dataset loaded from: " + path)
        break
    except FileNotFoundError:
        continue

if df is None:
    print("[ERROR] Dataset tidak ditemukan!")
    print("Current directory: " + os.getcwd())
    print("Coba paths: " + str(dataset_paths))
    raise FileNotFoundError("Dataset tidak ditemukan di path manapun")

# Prepare data
def prepare_data():
    """Persiapan data yang akan digunakan di seluruh aplikasi"""
    global df
    
    # Tambah kategori DM
    def tentukan_kategori(jumlah):
        if jumlah >= 100000:
            return "Tinggi"
        elif jumlah >= 50000:
            return "Sedang"
        else:
            return "Rendah"
    
    df['kategori_dm'] = df['jumlah_penderita_dm'].apply(tentukan_kategori)
    
    # Tambah persentase per tahun
    df['persentase_tahun'] = (
        df['jumlah_penderita_dm'] /
        df.groupby('tahun')['jumlah_penderita_dm'].transform('sum')
    ) * 100

prepare_data()

def generate_chart(chart_type, filename):
    """Generate dan simpan chart sebagai gambar"""
    plt.figure(figsize=(10, 6))
    
    if chart_type == 'trend_tahunan':
        total_per_tahun = df.groupby('tahun')['jumlah_penderita_dm'].sum()
        plt.plot(total_per_tahun.index, total_per_tahun.values, marker='o', linewidth=2, markersize=8)
        plt.title('Tren Total Penderita DM di Jawa Barat', fontsize=14, fontweight='bold')
        plt.xlabel('Tahun', fontsize=12)
        plt.ylabel('Jumlah Penderita DM', fontsize=12)
        plt.grid(True, alpha=0.3)
        
    elif chart_type == 'top_10_2019':
        df_2019 = df[df['tahun'] == 2019]
        top_10 = df_2019.sort_values(by='jumlah_penderita_dm', ascending=False).head(10)
        plt.barh(top_10['nama_kabupaten_kota'], top_10['jumlah_penderita_dm'], color='steelblue')
        plt.title('10 Kabupaten/Kota Tertinggi Penderita DM (2019)', fontsize=14, fontweight='bold')
        plt.xlabel('Jumlah Penderita', fontsize=12)
        plt.gca().invert_yaxis()
        
    elif chart_type == 'kategori_2019':
        df_2019 = df[df['tahun'] == 2019]
        kategori_counts = df_2019['kategori_dm'].value_counts()
        colors = ['#ef4444', '#f59e0b', '#10b981']
        plt.pie(kategori_counts.values, labels=kategori_counts.index, autopct='%1.1f%%',
                colors=colors, startangle=90)
        plt.title('Proporsi Kategori Penderita DM Tahun 2019', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    filepath = f'static/images/{filename}'
    plt.savefig(filepath, dpi=100, bbox_inches='tight')
    plt.close()
    return filepath

# Routes
@app.route('/')
def index():
    """Dashboard utama"""
    # Statistik utama
    total_penderita = int(df['jumlah_penderita_dm'].sum())
    total_kota = df['nama_kabupaten_kota'].nunique()
    tahun_terbaru = int(df['tahun'].max())
    
    # Total per tahun terbaru
    total_tahun_terbaru = int(df[df['tahun'] == tahun_terbaru]['jumlah_penderita_dm'].sum())
    
    # Perubahan dari tahun sebelumnya
    tahun_sebelumnya = tahun_terbaru - 1
    total_tahun_sebelumnya = int(df[df['tahun'] == tahun_sebelumnya]['jumlah_penderita_dm'].sum())
    perubahan = ((total_tahun_terbaru - total_tahun_sebelumnya) / total_tahun_sebelumnya * 100) if total_tahun_sebelumnya > 0 else 0
    
    # Top 5 tertinggi semua tahun
    top_5_kota = df.groupby('nama_kabupaten_kota')['jumlah_penderita_dm'].sum().nlargest(5)
    
    # Tren tahunan
    total_per_tahun = df.groupby('tahun')['jumlah_penderita_dm'].sum()
    
    # Top 10 data terbaru untuk tabel
    top_data = df.sort_values('tahun', ascending=False).head(10)
    
    # Generate charts
    generate_chart('trend_tahunan', 'trend_tahunan.png')
    generate_chart('top_10_2019', 'top_10_2019.png')
    generate_chart('kategori_2019', 'kategori_2019.png')
    
    return render_template('index.html',
                         total_penderita=total_penderita,
                         total_kota=total_kota,
                         tahun_terbaru=tahun_terbaru,
                         total_tahun_terbaru=total_tahun_terbaru,
                         perubahan=perubahan,
                         top_5_kota=top_5_kota.to_dict(),
                         total_per_tahun=total_per_tahun.to_dict(),
                         top_data=top_data)

@app.route('/analisis')
def analisis():
    """Halaman analisis detail"""
    # Analisis 14: Total per tahun
    total_per_tahun = df.groupby('tahun')['jumlah_penderita_dm'].sum()
    
    # Analisis 15: Rata-rata per kota
    avg_per_kota = df.groupby('nama_kabupaten_kota')['jumlah_penderita_dm'].mean().sort_values(ascending=False)
    
    # Analisis 16: Tertinggi dan terendah
    total_per_kota = df.groupby('nama_kabupaten_kota')['jumlah_penderita_dm'].sum()
    tertinggi_kota = total_per_kota.idxmax()
    tertinggi_nilai = int(total_per_kota.max())
    terendah_kota = total_per_kota.idxmin()
    terendah_nilai = int(total_per_kota.min())
    
    return render_template('analisis.html',
                         total_per_tahun=total_per_tahun.to_dict(),
                         avg_per_kota=avg_per_kota.head(15).to_dict(),
                         tertinggi_kota=tertinggi_kota,
                         tertinggi_nilai=tertinggi_nilai,
                         terendah_kota=terendah_kota,
                         terendah_nilai=terendah_nilai)

@app.route('/data')
def data():
    """Halaman data lengkap dengan filter"""
    tahun_param = request.args.get('tahun', type=int)
    kota_param = request.args.get('kota')
    kategori_param = request.args.get('kategori')
    
    filtered_df = df.copy()
    
    # Filter berdasarkan parameter
    if tahun_param:
        filtered_df = filtered_df[filtered_df['tahun'] == tahun_param]
    if kota_param:
        filtered_df = filtered_df[filtered_df['nama_kabupaten_kota'] == kota_param]
    if kategori_param:
        filtered_df = filtered_df[filtered_df['kategori_dm'] == kategori_param]
    
    # Sorting
    filtered_df = filtered_df.sort_values(by='jumlah_penderita_dm', ascending=False)
    
    # Pagination
    page = request.args.get('page', 1, type=int)
    per_page = 15
    total_rows = len(filtered_df)
    total_pages = (total_rows + per_page - 1) // per_page
    
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    
    data_page = filtered_df.iloc[start_idx:end_idx]
    
    # Daftar unik untuk filter
    tahun_list = sorted(df['tahun'].unique())
    kota_list = sorted(df['nama_kabupaten_kota'].unique())
    kategori_list = ['Tinggi', 'Sedang', 'Rendah']
    
    return render_template('data.html',
                         data=data_page.to_dict('records'),
                         tahun_list=tahun_list,
                         kota_list=kota_list,
                         kategori_list=kategori_list,
                         page=page,
                         total_pages=total_pages,
                         total_rows=total_rows,
                         tahun_param=tahun_param,
                         kota_param=kota_param,
                         kategori_param=kategori_param)

@app.route('/detail/<kota>')
def detail_kota(kota):
    """Halaman detail per kabupaten/kota"""
    kota_data = df[df['nama_kabupaten_kota'] == kota].sort_values('tahun')
    
    if kota_data.empty:
        return "Data tidak ditemukan", 404
    
    # Statistik kota
    total_kota = int(kota_data['jumlah_penderita_dm'].sum())
    rata_rata = float(kota_data['jumlah_penderita_dm'].mean())
    tertinggi = int(kota_data['jumlah_penderita_dm'].max())
    terendah = int(kota_data['jumlah_penderita_dm'].min())
    
    return render_template('detail_kota.html',
                         kota=kota,
                         kota_data=kota_data.to_dict('records'),
                         total_kota=total_kota,
                         rata_rata=rata_rata,
                         tertinggi=tertinggi,
                         terendah=terendah)

# ============= CRUD Routes =============

@app.route('/manage')
def manage():
    """Halaman manage data (CRUD)"""
    tahun_list = sorted(df['tahun'].unique())
    kota_list = sorted(df['nama_kabupaten_kota'].unique())
    
    return render_template('manage.html',
                         tahun_list=tahun_list,
                         kota_list=kota_list,
                         total_records=len(df))

@app.route('/api/data')
def get_data():
    """Get data as JSON"""
    return jsonify(df.to_dict('records'))

@app.route('/api/add', methods=['POST'])
def add_data():
    """Tambah data baru"""
    global df
    try:
        tahun = int(request.form.get('tahun'))
        kota = request.form.get('kota')
        jumlah = int(request.form.get('jumlah'))
        
        # Tentukan kategori
        if jumlah >= 100000:
            kategori = "Tinggi"
        elif jumlah >= 50000:
            kategori = "Sedang"
        else:
            kategori = "Rendah"
        
        # Tambah ke dataframe
        new_row = pd.DataFrame({
            'tahun': [tahun],
            'nama_kabupaten_kota': [kota],
            'jumlah_penderita_dm': [jumlah],
            'kategori_dm': [kategori],
            'persentase_tahun': [0]  # Will be calculated later
        })
        
        df = pd.concat([df, new_row], ignore_index=True)
        
        # Save to CSV
        save_data_to_csv()
        
        return {"status": "success", "message": "Data berhasil ditambahkan"}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 400

def save_data_to_csv():
    """Save dataframe to CSV"""
    global df
    try:
        # Get the CSV path
        dataset_paths = [
            'dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv',
            '../dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv',
            'D:\\frontend12\\dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv',
        ]
        
        # Try to save to the first path that exists or the second one as default
        for path in dataset_paths:
            if os.path.exists(path):
                df.to_csv(path, index=False)
                print(f"✅ Data saved to: {path}")
                return
        
        # If no path exists, save to the second one (relative path)
        df.to_csv(dataset_paths[1], index=False)
        print(f"✅ Data saved to: {dataset_paths[1]}")
    except Exception as e:
        print(f"❌ Error saving data: {e}")

@app.route('/api/edit/<int:row_id>', methods=['POST'])
def edit_data(row_id):
    """Edit data"""
    global df
    try:
        if row_id < 0 or row_id >= len(df):
            return {"status": "error", "message": "ID tidak valid"}, 404
        
        tahun = int(request.form.get('tahun'))
        kota = request.form.get('kota')
        jumlah = int(request.form.get('jumlah'))
        
        # Tentukan kategori
        if jumlah >= 100000:
            kategori = "Tinggi"
        elif jumlah >= 50000:
            kategori = "Sedang"
        else:
            kategori = "Rendah"
        
        # Update row
        df.loc[row_id, 'tahun'] = tahun
        df.loc[row_id, 'nama_kabupaten_kota'] = kota
        df.loc[row_id, 'jumlah_penderita_dm'] = jumlah
        df.loc[row_id, 'kategori_dm'] = kategori
        
        # Save to CSV
        save_data_to_csv()
        
        return {"status": "success", "message": "Data berhasil diperbarui"}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 400

@app.route('/api/delete/<int:row_id>', methods=['POST'])
def delete_data(row_id):
    """Hapus data"""
    global df
    try:
        if row_id < 0 or row_id >= len(df):
            return {"status": "error", "message": "ID tidak valid"}, 404
        
        df = df.drop(row_id).reset_index(drop=True)
        
        # Save to CSV
        save_data_to_csv()
        
        return {"status": "success", "message": "Data berhasil dihapus"}
    except Exception as e:
        return {"status": "error", "message": str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
