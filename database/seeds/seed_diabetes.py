import sqlite3
import pandas as pd
import os

# --- KONFIGURASI FINAL ---
# Database: project-name/database/app.db
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
DB_PATH = os.path.join(BASE_DIR, 'app.db')
CSV_FILE = 'dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv'

def get_kategori(jumlah):
    if jumlah >= 10000: return "Tinggi"
    elif jumlah >= 5000: return "Sedang"
    else: return "Rendah"

def seed_database():
    print(f"--- SETUP DATABASE LENGKAP (6 TABEL) ---")
    
    # 1. Cek & Baca CSV
    csv_path = os.path.join(os.path.dirname(__file__), CSV_FILE)
    if not os.path.exists(csv_path):
        print(f"[ERROR] CSV tidak ditemukan di: {csv_path}")
        return
    
    print("Membaca CSV & Hitung Statistik...")
    df = pd.read_csv(csv_path)
    
    # Pre-processing data tambahan
    df['kategori_dm'] = df['jumlah_penderita_dm'].apply(get_kategori)
    total_per_tahun = df.groupby('tahun')['jumlah_penderita_dm'].sum().to_dict()
    df['persentase_tahun'] = df.apply(lambda x: (x['jumlah_penderita_dm'] / total_per_tahun[x['tahun']]) * 100, axis=1)

    # 2. Koneksi ke Database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 3. Reset (Hapus 6 tabel lama biar bersih)
    tables = [
        'penderita_dm', 
        'total_per_tahun', 
        'total_per_kabupaten',       # <-- Tabel ke-3 (Total seumur hidup per kota)
        'rata_rata_per_kabupaten',   # <-- Tabel ke-4 (Rata-rata kasus per kota)
        'top_10_per_tahun', 
        'kategori_dm_stats'
    ]
    for t in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {t}")

    # 4. Buat Schema (6 Tabel)
    print("Membuat 6 Tabel...")
    cursor.executescript('''
        CREATE TABLE penderita_dm (
            id INTEGER PRIMARY KEY, nama_kabupaten_kota TEXT, jumlah_penderita_dm INTEGER,
            tahun INTEGER, kategori_dm TEXT, persentase_tahun REAL
        );
        CREATE TABLE total_per_tahun (tahun INTEGER PRIMARY KEY, total_penderita INTEGER);
        CREATE TABLE total_per_kabupaten (nama_kabupaten_kota TEXT PRIMARY KEY, total_penderita INTEGER);
        CREATE TABLE rata_rata_per_kabupaten (nama_kabupaten_kota TEXT PRIMARY KEY, rata_rata_penderita REAL);
        CREATE TABLE top_10_per_tahun (tahun INTEGER, nama_kabupaten_kota TEXT, jumlah_penderita_dm INTEGER);
        CREATE TABLE kategori_dm_stats (tahun INTEGER, kategori_dm TEXT, jumlah INTEGER);
    ''')

    # 5. Seeding Data
    print("Mengisi Data...")
    
    # 1. Data Mentah
    df[['nama_kabupaten_kota', 'jumlah_penderita_dm', 'tahun', 'kategori_dm', 'persentase_tahun']].to_sql('penderita_dm', conn, if_exists='append', index=False)
    
    # 2. Total Per Tahun
    agg_tahun = df.groupby('tahun')['jumlah_penderita_dm'].sum().reset_index(name='total_penderita')
    agg_tahun.to_sql('total_per_tahun', conn, if_exists='append', index=False)

    # 3. Total Per Kabupaten (Semua Tahun)
    agg_kab = df.groupby('nama_kabupaten_kota')['jumlah_penderita_dm'].sum().reset_index(name='total_penderita')
    agg_kab.to_sql('total_per_kabupaten', conn, if_exists='append', index=False)

    # 4. Rata-rata Per Kabupaten
    avg_kab = df.groupby('nama_kabupaten_kota')['jumlah_penderita_dm'].mean().reset_index(name='rata_rata_penderita')
    avg_kab.to_sql('rata_rata_per_kabupaten', conn, if_exists='append', index=False)

    # 5. Top 10 Per Tahun
    top_10 = df.sort_values(['tahun', 'jumlah_penderita_dm'], ascending=[True, False]).groupby('tahun').head(10)
    top_10[['tahun', 'nama_kabupaten_kota', 'jumlah_penderita_dm']].to_sql('top_10_per_tahun', conn, if_exists='append', index=False)

    # 6. Statistik Kategori
    cat_stats = df.groupby(['tahun', 'kategori_dm']).size().reset_index(name='jumlah')
    cat_stats.to_sql('kategori_dm_stats', conn, if_exists='append', index=False)

    conn.commit()
    conn.close()
    print("--- SELESAI: Database 'app.db' dengan 6 tabel siap digunakan! ---")

if __name__ == "__main__":
    seed_database()