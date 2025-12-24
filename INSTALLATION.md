# 📋 Panduan Instalasi Lengkap - Dashboard Diabetes Melitus

## 🖥️ Persyaratan Sistem

- **Operating System**: Windows 7 ke atas (atau Linux/Mac)
- **Python**: 3.8 atau lebih baru
- **RAM**: Minimal 2 GB
- **Storage**: 500 MB untuk aplikasi + dependencies
- **Browser**: Chrome, Firefox, Safari, atau Edge (terbaru)

---

## 📥 Step 1: Install Python

### Windows
1. Kunjungi: https://www.python.org/downloads/
2. Download **Python 3.10 atau lebih baru**
3. Double-click installer
4. **PENTING**: Centang checkbox **"Add Python to PATH"**
5. Click "Install Now"
6. Tunggu hingga selesai

### Verifikasi Instalasi
Buka Command Prompt/PowerShell dan ketik:
```bash
python --version
```
Jika muncul versi Python, instalasi berhasil! ✅

---

## 📂 Step 2: Setup Folder Project

### Opsi A: Gunakan Folder yang Sudah Ada
Folder sudah disiapkan di: `d:\frontend12\diabetes-dashboard-flask`

### Opsi B: Buat Folder Baru (Manual)
1. Buat folder baru, misalnya: `C:\Users\YourName\diabetes-dashboard`
2. Copy semua file dari `d:\frontend12\diabetes-dashboard-flask` ke folder baru
3. Pastikan struktur seperti ini:
```
diabetes-dashboard-flask/
├── app.py
├── config.py
├── requirements.txt
├── run.bat
├── README.md
├── QUICKSTART.md
├── templates/
└── static/
```

---

## 📦 Step 3: Install Dependencies

### Opsi A: Menggunakan run.bat (MUDAH)
1. Buka File Explorer
2. Navigasi ke folder `diabetes-dashboard-flask`
3. Double-click **`run.bat`**
4. Tunggu hingga selesai install (muncul file di `static/images/`)

### Opsi B: Manual dengan Command Prompt
1. Buka Command Prompt / PowerShell as Administrator
2. Navigasi ke folder:
   ```bash
   cd d:\frontend12\diabetes-dashboard-flask
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

**Tunggu hingga semua package terinstall** (biasanya 2-5 menit)

Output yang benar:
```
Successfully installed Flask-2.3.3 pandas-2.0.3 matplotlib-3.7.2 ...
```

---

## 📊 Step 4: Persiapan Dataset

Dataset harus berada di folder parent:
```
d:\frontend12\dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv
```

**Verifikasi:**
- File harus bernama **exact** seperti di atas (case-sensitive untuk Linux)
- File format: **CSV** dengan columns: `tahun`, `nama_kabupaten_kota`, `jumlah_penderita_dm`

---

## 🚀 Step 5: Jalankan Aplikasi

### Opsi A: Double-click run.bat (RECOMMENDED)
1. Double-click **`run.bat`**
2. Tunggu hingga muncul pesan: "Running on http://127.0.0.1:5000"
3. Buka browser, ketik: **http://localhost:5000**

### Opsi B: Terminal Manual
```bash
# Navigasi ke folder
cd d:\frontend12\diabetes-dashboard-flask

# Jalankan aplikasi
python app.py
```

**Output yang benar:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

---

## 🌐 Step 6: Akses Dashboard

1. Buka browser (Chrome, Firefox, Edge, dll)
2. Ketik di address bar: **http://localhost:5000**
3. Selamat! Dashboard siap digunakan 🎉

---

## 🎯 Halaman yang Tersedia

| Halaman | URL | Deskripsi |
|---------|-----|-----------|
| Dashboard | http://localhost:5000/ | Overview & statistik |
| Analisis | http://localhost:5000/analisis | Analisis detail data |
| Data | http://localhost:5000/data | Tabel data lengkap |

---

## 🛑 Menghentikan Aplikasi

Tekan **CTRL + C** di terminal/command prompt

Output:
```
Shutting down...
```

---

## ✅ Checklist Instalasi

- [ ] Python 3.8+ terinstall
- [ ] Command `python --version` berjalan
- [ ] Folder `diabetes-dashboard-flask` ada di tempat yang benar
- [ ] File `requirements.txt` ada
- [ ] Semua dependencies terinstall (`pip list` untuk verify)
- [ ] Dataset CSV ada di folder parent
- [ ] Folder `static/images/` ada (otomatis dibuat saat run pertama)
- [ ] Aplikasi berjalan di http://localhost:5000

---

## 🔧 Troubleshooting

### ❌ Problem: "Python is not recognized"

**Penyebab**: Python tidak ditambahkan ke PATH

**Solusi**:
1. Uninstall Python
2. Install ulang dan **CENTANG "Add Python to PATH"**
3. Restart computer
4. Buka terminal baru dan coba lagi

---

### ❌ Problem: "No module named 'flask'"

**Penyebab**: Dependencies belum terinstall

**Solusi**:
```bash
# Pastikan berada di folder yang benar
cd d:\frontend12\diabetes-dashboard-flask

# Install ulang
pip install -r requirements.txt
```

---

### ❌ Problem: "FileNotFoundError: [Errno 2] No such file or directory: '../dinkes-od_...csv'"

**Penyebab**: Dataset file tidak ditemukan

**Solusi**:
1. Pastikan file CSV ada di: `d:\frontend12\`
2. Nama file **exact** seperti di requirements
3. Cek bahwa path relatif `../` menunjuk ke folder parent yang benar

---

### ❌ Problem: "Port 5000 is already in use"

**Penyebab**: Port 5000 sudah dipakai aplikasi lain

**Solusi**:
```bash
# Edit app.py, ubah port di baris terakhir:
app.run(debug=True, port=5001)  # Ganti 5000 dengan port lain

# Atau gunakan command line:
python app.py --port 5001
```

---

### ❌ Problem: "Chart tidak muncul / blank images"

**Penyebab**: Chart belum di-generate

**Solusi**:
1. Pastikan matplotlib terinstall: `pip install matplotlib`
2. Tunggu beberapa saat saat akses dashboard pertama kali
3. Refresh browser (CTRL + F5)

---

## 📝 Catatan Penting

1. **First Run**: Saat pertama kali dijalankan, aplikasi akan:
   - Load dataset CSV
   - Generate chart images (bisa memakan beberapa detik)
   - Membuat folder `static/images/` otomatis

2. **Debug Mode**: Aplikasi berjalan dalam mode debug, artinya:
   - Setiap perubahan file Python otomatis reload
   - Error messages lebih detail
   - Tidak untuk production!

3. **Izin File**: Pastikan folder punya write permission untuk generate chart

---

## 🎓 Verifikasi Instalasi

Setelah aplikasi jalan, test setiap halaman:

```
✅ http://localhost:5000/          → Dashboard dengan 4 stat cards
✅ http://localhost:5000/analisis   → Tabel analisis 14-16
✅ http://localhost:5000/data       → Tabel data dengan filter
✅ http://localhost:5000/detail/KABUPATEN%20BOGOR → Detail kota
```

Jika semua berjalan, **instalasi BERHASIL!** 🎉

---

## 📚 File Penting & Penjelasannya

| File | Fungsi |
|------|--------|
| `app.py` | Main application, routes, dan logic |
| `config.py` | Konfigurasi global aplikasi |
| `requirements.txt` | Daftar Python packages yang diperlukan |
| `run.bat` | Script untuk menjalankan (Windows) |
| `templates/*.html` | Template halaman web |
| `static/css/style.css` | Stylesheet |
| `static/images/` | Folder untuk chart yang di-generate |

---

## 🆘 Butuh Bantuan?

1. Cek QUICKSTART.md untuk tips cepat
2. Baca README.md untuk dokumentasi lengkap
3. Verifikasi semua langkah di checklist di atas
4. Cek error message di terminal dengan teliti

---

## 🎉 Selamat!

Jika berhasil sampai sini, dashboard Anda sudah siap digunakan! 

Nikmati analisis data penderita Diabetes Melitus Jawa Barat! 📊

---

**Dibuat dengan ❤️ - Dashboard Diabetes Melitus v1.0.0**
