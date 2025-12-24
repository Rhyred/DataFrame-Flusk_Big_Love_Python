# Diabetes Melitus Dashboard - Jawa Barat

## 📊 Dashboard Penderita Diabetes Melitus - Jawa Barat

Aplikasi Flask untuk visualisasi dan analisis data penderita Diabetes Melitus di Jawa Barat.

---

## 🎯 Tujuan Proyek

Dashboard ini dibuat untuk:
- ✅ Visualisasi data penderita DM per tahun (2019-2024)
- ✅ Analisis trends dan perubahan data
- ✅ Identifikasi kabupaten/kota dengan kasus tertinggi
- ✅ Kategorisasi penderita berdasarkan jumlah
- ✅ Menyediakan interface yang user-friendly untuk eksplorasi data

---

## 🚀 Fitur Utama

### 1. Dashboard Interaktif
- 📈 Statistik ringkas (total, rata-rata, perubahan)
- 📊 Grafik tren tahunan
- 🔝 Top 10 kabupaten dengan kasus tertinggi
- 🎯 Kategorisasi penderita (Tinggi/Sedang/Rendah)

### 2. Analisis Data
- 📋 Total penderita per tahun (Analisis 14)
- 📊 Rata-rata per kabupaten/kota (Analisis 15)
- 🏆 Identifikasi tertinggi & terendah (Analisis 16)

### 3. Data Lengkap
- 🔍 Filter by tahun, kabupaten/kota, kategori
- 📄 Tabel dengan pagination
- 🔗 Link ke detail per kabupaten/kota

### 4. Detail Per Kota
- 📈 Riwayat penderita per tahun
- 📊 Statistik: total, rata-rata, tertinggi, terendah
- 📉 Perubahan persentase tahunan

---

## 📂 Struktur Folder Lengkap

```
diabetes-dashboard-flask/
│
├── 📄 app.py                       # Main Flask application
├── 📄 config.py                    # Configuration & settings
├── 📄 requirements.txt             # Python dependencies
├── 📄 run.bat                      # Windows launcher script
│
├── 📖 README.md                    # Full documentation
├── 📖 QUICKSTART.md               # Quick setup guide
├── 📖 INSTALLATION.md             # Detailed installation guide
├── 📖 INDEX.md                    # File ini
│
├── 📁 templates/                   # HTML templates
│   ├── index.html                  # Dashboard utama
│   ├── analisis.html               # Halaman analisis
│   ├── data.html                   # Data lengkap dengan filter
│   └── detail_kota.html            # Detail per kabupaten/kota
│
└── 📁 static/                      # Static assets
    ├── 📁 css/
    │   └── style.css               # Stylesheet (Flowbite-inspired)
    │
    └── 📁 images/                  # Generated charts (auto-created)
        ├── trend_tahunan.png
        ├── top_10_2019.png
        └── kategori_2019.png
```

---

## 🛠️ Tech Stack

| Komponen | Teknologi |
|----------|-----------|
| Backend | Flask (Python) |
| Frontend | HTML5 + CSS3 |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| Styling | Custom CSS (Flowbite-inspired) |
| Database | CSV File |

---

## 📋 Data Information

### Dataset
- **Nama**: `dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv`
- **Sumber**: Dinas Kesehatan Jawa Barat
- **Periode**: 2019 - 2024
- **Area**: 27 Kabupaten/Kota di Jawa Barat
- **Format**: CSV dengan kolom: tahun, nama_kabupaten_kota, jumlah_penderita_dm

### Kolom Data
```
tahun                    : Tahun data (int)
nama_kabupaten_kota      : Nama kabupaten atau kota (string)
jumlah_penderita_dm      : Jumlah penderita diabetes melitus (int)
kategori_dm              : Kategori (auto-calculated) - Tinggi/Sedang/Rendah
persentase_tahun         : Persentase kontribusi per tahun (auto-calculated)
```

---

## 🎨 Desain & UI/UX

- **Design Pattern**: Dashboard Admin Style (mirip Flowbite)
- **Color Scheme**:
  - Primary: Blue (#3b82f6)
  - Success: Green (#10b981)
  - Warning: Amber (#f59e0b)
  - Danger: Red (#ef4444)

- **Responsif**: Cocok untuk desktop, tablet, mobile
- **No JavaScript**: Pure HTML + CSS (form submission only)
- **Accessibility**: Semantic HTML, good contrast, readable fonts

---

## 🎓 Kategori Penderita DM

Data penderita dikategorikan berdasarkan jumlah:

| Kategori | Range | Warna |
|----------|-------|-------|
| 🔴 Tinggi | ≥ 100.000 | Red (#ef4444) |
| 🟡 Sedang | 50.000 - 99.999 | Amber (#f59e0b) |
| 🟢 Rendah | < 50.000 | Green (#10b981) |

---

## 🌐 Routes & URLs

| Route | Method | Halaman | Fungsi |
|-------|--------|---------|--------|
| `/` | GET | Dashboard | Overview & statistik |
| `/analisis` | GET | Analisis | Analisis 14-16 |
| `/data` | GET | Data | Tabel data lengkap |
| `/data` | GET (params) | Data Filtered | Filter by tahun/kota/kategori |
| `/detail/<kota>` | GET | Detail Kota | Riwayat per kabupaten |

### Query Parameters untuk /data
```
tahun=2019          → Filter by tahun
kota=KABUPATEN%20BOGOR  → Filter by kabupaten/kota
kategori=Tinggi     → Filter by kategori
page=2              → Halaman pagination
```

---

## 💻 Instalasi & Setup

### Quick Start (Windows)
```bash
1. Double-click run.bat
2. Buka http://localhost:5000
```

### Manual Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Jalankan aplikasi
python app.py

# 3. Akses di browser
# http://localhost:5000
```

Untuk panduan lengkap, lihat [INSTALLATION.md](INSTALLATION.md)

---

## 📖 Dokumentasi Lengkap

| File | Isi |
|------|-----|
| [README.md](README.md) | Dokumentasi lengkap aplikasi |
| [QUICKSTART.md](QUICKSTART.md) | Panduan cepat & tips |
| [INSTALLATION.md](INSTALLATION.md) | Panduan instalasi detail |
| [INDEX.md](INDEX.md) | File ini - Overview struktur |

---

## 🔧 Kustomisasi

### Mengubah Warna
Edit `static/css/style.css`:
```css
:root {
    --primary: #3b82f6;        /* Ubah warna primary */
    --success: #10b981;        /* Ubah warna success */
    --warning: #f59e0b;        /* Ubah warna warning */
    --danger: #ef4444;         /* Ubah warna danger */
}
```

### Menambah Fitur Baru
1. Edit `app.py` untuk menambah route
2. Buat template `.html` baru di `templates/`
3. Tambah style di `static/css/style.css`
4. Restart aplikasi

### Mengubah Port
Edit baris terakhir `app.py`:
```python
app.run(debug=True, port=5001)  # Ubah 5000 ke port lain
```

---

## 🐛 Troubleshooting

| Error | Solusi |
|-------|--------|
| Python not found | Install Python dan add to PATH |
| Module not found | Jalankan `pip install -r requirements.txt` |
| Dataset not found | Pastikan CSV ada di folder parent |
| Port already in use | Ganti port di app.py atau kill process |
| Chart tidak muncul | Pastikan matplotlib terinstall |

Lihat [INSTALLATION.md](INSTALLATION.md) untuk troubleshooting lengkap.

---

## 📊 Analisis Data yang Tersedia

### Analisis 14: Total per Tahun
Menampilkan total jumlah penderita DM untuk setiap tahun dengan tren perubahan.

**Insight**: Identifikasi tahun dengan kenaikan/penurunan kasus terbesar.

### Analisis 15: Rata-rata per Kota
Menampilkan rata-rata penderita DM per kabupaten/kota (basis semua tahun).

**Insight**: Identifikasi area dengan rata-rata kasus tertinggi.

### Analisis 16: Tertinggi & Terendah
Menampilkan kabupaten/kota dengan total kasus tertinggi dan terendah (semua tahun).

**Insight**: Perbandingan area dengan beban kesehatan DM tertinggi vs terendah.

---

## 🚀 Deployment

Untuk production deployment, lihat catatan di [README.md](README.md):
- Ubah `debug=False`
- Gunakan production WSGI server (Gunicorn, uWSGI)
- Setup environment variables
- Implementasi security measures

---

## 📝 License & Credit

- **Data Source**: Dinas Kesehatan Jawa Barat
- **Framework**: Flask (https://flask.palletsprojects.com/)
- **Libraries**: Pandas, Matplotlib, NumPy
- **Design Inspiration**: Flowbite Admin Dashboard

---

## 👨‍💻 Pengembangan Berkelanjutan

Fitur yang bisa ditambahkan di masa depan:
- 📈 Interactive charts (Plotly, Chart.js)
- 💾 Database integration (SQLite, PostgreSQL)
- 👤 User authentication & login
- 📥 Data export (CSV, PDF, Excel)
- 🔔 Real-time notifications
- 📱 Mobile app version
- 🤖 Predictive analytics

---

## 🎯 Next Steps

1. **Baca [INSTALLATION.md](INSTALLATION.md)** untuk setup yang tepat
2. **Jalankan dengan `run.bat`** atau `python app.py`
3. **Explore dashboard** di http://localhost:5000
4. **Coba semua fitur**: filter, detail view, dll
5. **Customize sesuai kebutuhan** (warna, feature, dll)

---

## 📞 Support & Contact

Jika ada pertanyaan atau issues:
1. Cek dokumentasi di file README/QUICKSTART/INSTALLATION
2. Verifikasi instalasi dengan checklist di INSTALLATION.md
3. Periksa error message di terminal dengan teliti

---

**Dashboard Penderita Diabetes Melitus - Jawa Barat v1.0.0**

Dibuat dengan ❤️ menggunakan Flask & Python

*Last Updated: 2024*
