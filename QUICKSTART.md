# 🚀 Quick Start Guide - Dashboard Diabetes Melitus

## ⚡ Cara Menjalankan (Windows)

### Opsi 1: Menggunakan Script Run (Rekomendasi)
1. Buka folder `diabetes-dashboard-flask`
2. Double-click file **`run.bat`**
3. Tunggu hingga selesai install dependencies
4. Buka browser ke: **http://localhost:5000**

### Opsi 2: Manual Menggunakan Terminal
1. Buka Command Prompt (cmd) atau PowerShell
2. Navigasi ke folder diabetes-dashboard-flask:
   ```
   cd d:\frontend12\diabetes-dashboard-flask
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Jalankan aplikasi:
   ```
   python app.py
   ```
5. Buka browser ke: **http://localhost:5000**

---

## 📁 Struktur Proyek

```
diabetes-dashboard-flask/
│
├── app.py                           # Aplikasi Flask utama
├── requirements.txt                 # Daftar dependencies Python
├── run.bat                         # Script untuk menjalankan (Windows)
├── README.md                       # Dokumentasi lengkap
├── QUICKSTART.md                   # File ini
│
├── templates/                      # Folder template HTML
│   ├── index.html                 # Dashboard utama
│   ├── analisis.html              # Halaman analisis (14-16)
│   ├── data.html                  # Halaman data dengan filter
│   └── detail_kota.html           # Detail per kabupaten/kota
│
└── static/                         # Folder assets statis
    ├── css/
    │   └── style.css              # Stylesheet (Flowbite-style)
    └── images/                     # Folder chart yang di-generate otomatis
        ├── trend_tahunan.png
        ├── top_10_2019.png
        └── kategori_2019.png
```

---

## 🎯 Halaman-Halaman Utama

### 1️⃣ Dashboard (Home)
- **URL**: http://localhost:5000/
- **Isi**:
  - Statistik ringkas (total penderita, jumlah kota, tahun terbaru)
  - Grafik tren tahunan
  - Top 10 kabupaten/kota (2019)
  - Proporsi kategori penderita

### 2️⃣ Analisis
- **URL**: http://localhost:5000/analisis
- **Isi**:
  - Analisis 14: Total per tahun dengan perubahan
  - Analisis 15: Rata-rata per kabupaten/kota
  - Analisis 16: Tertinggi & terendah

### 3️⃣ Data Lengkap
- **URL**: http://localhost:5000/data
- **Fitur**:
  - Tabel semua data penderita
  - Filter by tahun, kabupaten/kota, kategori
  - Pagination (15 baris per halaman)
  - Link ke detail kabupaten/kota

### 4️⃣ Detail Kabupaten/Kota
- **URL**: http://localhost:5000/detail/<nama_kota>
- **Contoh**: http://localhost:5000/detail/KABUPATEN%20BOGOR
- **Isi**:
  - Statistik per kota (total, rata-rata, tertinggi, terendah)
  - Riwayat penderita per tahun
  - Perubahan persentase

---

## 🛠️ Troubleshooting

### ❌ Error: "Python tidak ditemukan"
**Solusi**: Install Python dari https://www.python.org/downloads/
- Pastikan checkbox "Add Python to PATH" dicentang saat install

### ❌ Error: "ModuleNotFoundError: No module named 'flask'"
**Solusi**: Install ulang dependencies:
```bash
pip install -r requirements.txt
```

### ❌ Error: "Dataset tidak ditemukan"
**Solusi**: Pastikan file CSV ada di folder parent:
```
d:\frontend12\dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv
```

### ❌ Port 5000 sudah terpakai
**Solusi**: Edit file `app.py` baris terakhir:
```python
# Ubah dari:
app.run(debug=True, port=5000)

# Menjadi:
app.run(debug=True, port=5001)  # atau port lain yang available
```

---

## 📊 Data & Fitur

### Dataset
- **File**: `dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv`
- **Tahun**: 2019-2024
- **Area**: Jawa Barat (27 kabupaten/kota)
- **Kolom**: tahun, nama_kabupaten_kota, jumlah_penderita_dm
- **Tambahan** (auto-generated): kategori_dm, persentase_tahun

### Kategori Penderita
- 🔴 **Tinggi**: ≥ 100.000 penderita
- 🟡 **Sedang**: 50.000 - 99.999 penderita
- 🟢 **Rendah**: < 50.000 penderita

---

## 🎨 Desain

- **Framework CSS**: Custom CSS (Flowbite-inspired)
- **Tanpa JavaScript**: Pure HTML + CSS
- **Responsif**: Cocok untuk mobile dan desktop
- **Color Scheme**: Blue (#3b82f6) sebagai primary color

---

## 💡 Tips & Trik

### Mengakses Data Spesifik
Gunakan filter di halaman Data:
- Filter by Tahun: Lihat data tahun tertentu
- Filter by Kota: Lihat detail kota tertentu
- Filter by Kategori: Lihat kota dengan kategori tertentu

### Query URL Manual
```
/data?tahun=2019&kategori=Tinggi
/detail/KABUPATEN BANDUNG
```

### Generate Chart Ulang
Chart otomatis di-generate saat aplikasi startup. Jika ingin refresh:
1. Hentikan aplikasi (CTRL+C)
2. Hapus folder `static/images/`
3. Jalankan ulang aplikasi

---

## 🔧 Pengembangan Lanjutan

### Menambah Fitur
Edit file `app.py` untuk menambah route dan logika bisnis baru.

### Mengubah Style
Edit file `static/css/style.css` untuk custom styling.

### Menambah Template
Buat file `.html` baru di folder `templates/` dan tambah route di `app.py`.

---

## 📚 Referensi

- **Flask Documentation**: https://flask.palletsprojects.com/
- **Pandas Documentation**: https://pandas.pydata.org/
- **Matplotlib Documentation**: https://matplotlib.org/
- **Flowbite Components**: https://flowbite.com/

---

## ❓ FAQ

**Q: Bisa gak diubah warna tema?**  
A: Bisa! Edit file `style.css`, ubah nilai di `:root` color variables.

**Q: Gimana caranya share dashboard ke orang lain?**  
A: Bisa dengan host di server atau gunakan ngrok untuk temporary sharing.

**Q: Bisa gak export data ke Excel?**  
A: Bisa dengan menambah library `openpyxl` dan route export di `app.py`.

---

## 📞 Support

Jika ada pertanyaan atau masalah, silakan cek ulang:
1. Python sudah terinstall
2. Semua dependencies terinstall
3. Dataset file ada di tempat yang benar
4. Port 5000 tidak terpakai

---

**Selamat menggunakan Dashboard! 🎉**

*Dashboard ini dibuat berdasarkan data Dinas Kesehatan Jawa Barat menggunakan Flask (Python).*
