# 📚 Panduan Penggunaan Dashboard Diabetes

## 🚀 Memulai Aplikasi

### 1. Aktifkan Virtual Environment
```powershell
# Di Windows PowerShell
D:\frontend12\.venv\Scripts\Activate.ps1

# Pindah ke folder aplikasi
cd D:\frontend12\diabetes-dashboard-flask
```

### 2. Jalankan Flask Server
```powershell
python app.py
```

**Output yang diharapkan:**
```
✅ Dataset loaded from: ../dinkes-od_17448_...
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 3. Buka di Browser
```
http://localhost:5000
```

---

## 📊 Navigasi Aplikasi

### Menu Utama
1. **Dashboard** - Ringkasan dan statistik keseluruhan
2. **Analisis** - Analisis mendalam dari 4 perspektif berbeda
3. **Data** - Tabel lengkap dengan filter dan pencarian
4. **Manage** - Kelola data (CRUD operations)

---

## 💡 Panduan Fitur Berdasarkan Halaman

### 1️⃣ DASHBOARD (Home)

**Apa yang bisa dilihat:**
- 4 Kartu Statistik:
  - Total Penderita DM (semua tahun & area)
  - Jumlah Kabupaten/Kota (27 area)
  - Tahun Data Terbaru (2024)
  - Perubahan Penderita YoY

- 3 Visualisasi Data:
  - **Trend Tahunan**: Grafik garis menunjukkan perubahan dari 2019-2024
  - **Top 10 Kabupaten 2019**: Bar chart dengan area dengan kasus tertinggi
  - **Distribusi Kategori**: Pie chart untuk Tinggi/Sedang/Rendah

- Tabel Preview: 5 data dengan jumlah penderita tertinggi

**Navigasi:**
- Klik judul chart untuk informasi lebih lanjut
- Klik baris tabel untuk lihat detail per kabupaten

---

### 2️⃣ ANALISIS

Menampilkan 4 analisis utama dari data:

#### Analisis 14: Total Penderita per Tahun
```
Tahun | Jumlah      | % Perubahan
2019  | 1,234,567   | -
2020  | 1,245,789   | +0.91%
2021  | 1,267,234   | +1.72%
...
```

#### Analisis 15: Rata-rata per Kabupaten
Menampilkan 15 kabupaten dengan rata-rata penderita tertinggi

**Warna Kategori:**
- 🔴 **Merah** (Tinggi): ≥ 100,000
- 🟡 **Oranye** (Sedang): 50,000-99,999
- 🟢 **Hijau** (Rendah): < 50,000

#### Analisis 16: Tertinggi & Terendah
- Top area dengan kasus terbanyak
- Bottom area dengan kasus paling sedikit
- Perbandingan direct

---

### 3️⃣ DATA (Tabel Lengkap)

**Filter Data:**

1. **Filter Tahun**
   - Dropdown list semua tahun (2019-2024)
   - Pilih "Semua Tahun" untuk reset

2. **Filter Kabupaten/Kota**
   - Dropdown list 27 area di Jawa Barat
   - Cari area spesifik

3. **Filter Kategori**
   - Tinggi / Sedang / Rendah
   - Lihat hanya area dengan kategori tertentu

4. **Kombinasi Filter**
   - Tahun 2024 + Kategori Tinggi = Area tinggi di 2024
   - Kota tertentu + Semua Tahun = Timeline satu area

**Pagination:**
- Menampilkan 15 data per halaman
- Tombol: Awal | Sebelumnya | 1 2 3 4... | Selanjutnya | Akhir
- Jump to page: Klik nomor halaman untuk lompat

**Action:**
- Klik **"Detail"** pada baris manapun untuk melihat analisis spesifik kota tersebut

---

### 4️⃣ MANAGE (CRUD Operations)

#### A. TAMBAH DATA BARU (CREATE)

**Langkah-langkah:**
1. Scroll ke form "➕ Tambah Data Baru"
2. Isi field:
   - **Tahun**: Pilih tahun (2010-2099)
   - **Kabupaten/Kota**: Dropdown dengan 27 area
   - **Jumlah Penderita**: Angka (misal: 75000)
3. Klik **✅ Tambah Data**

**Contoh Input:**
```
Tahun: 2024
Kota: Jakarta Pusat
Jumlah: 85000
→ Kategori otomatis: Sedang (karena 50K-100K)
```

**Respons:**
- ✅ Pesan hijau: "Data berhasil ditambahkan!"
- Form reset otomatis
- Data muncul di tabel bawah

---

#### B. LIHAT DATA (READ)

**Tabel Data Terbaru:**
- Otomatis menampilkan semua data di database
- Kolom: No | Tahun | Kabupaten/Kota | Jumlah | Kategori | Aksi

**Informasi Stat Cards:**
- **Total Records**: Jumlah total data
- **Kabupaten/Kota**: Jumlah area unik
- **Tahun Data**: Berapa tahun ada data

---

#### C. EDIT DATA (UPDATE)

**Langkah-langkah:**
1. Cari data yang ingin diedit di tabel
2. Klik tombol **[Edit]** (tombol biru)
3. Modal dialog terbuka dengan form pre-filled
4. Edit field yang ingin diubah:
   - Tahun, Kabupaten/Kota, atau Jumlah Penderita
5. Klik **💾 Simpan Perubahan**

**Contoh Edit:**
```
Sebelum: Sukabumi 2024 - 45000 (Rendah)
Edit Jumlah: 75000
Sesudah: Sukabumi 2024 - 75000 (Sedang) ← Kategori auto-update!
```

**Respons:**
- ✅ Pesan hijau: "Data berhasil diperbarui!"
- Modal tutup otomatis
- Tabel refresh dengan data terbaru

---

#### D. HAPUS DATA (DELETE)

**Langkah-langkah:**
1. Cari data yang ingin dihapus
2. Klik tombol **[Delete]** (tombol merah)
3. Confirmation dialog muncul: "Yakin ingin menghapus data ini?"
4. Klik **OK** untuk konfirmasi hapus

**Perhatian:**
- ⚠️ Penghapusan PERMANENT (tidak bisa di-undo)
- Data hilang dari database selamanya
- Pastikan benar sebelum konfirmasi!

**Respons:**
- ✅ Pesan hijau: "Data berhasil dihapus!"
- Tabel refresh tanpa data yang dihapus
- Nomor otomatis di-reset

---

## 📌 Kategori DM Explanation

Kategori ditentukan otomatis berdasarkan **jumlah penderita**:

| Kategori | Jumlah Penderita | Badge Color |
|----------|------------------|-------------|
| Tinggi | ≥ 100,000 | 🔴 Merah |
| Sedang | 50,000 - 99,999 | 🟡 Oranye |
| Rendah | < 50,000 | 🟢 Hijau |

**Contoh:**
- Input: 125,000 → Kategori: **Tinggi**
- Input: 75,000 → Kategori: **Sedang**
- Input: 35,000 → Kategori: **Rendah**

---

## 🎯 Use Cases & Tips

### Skenario 1: Tambah Data Baru untuk Area Tertentu
```
Tujuan: Tambah data Bandung 2024
1. Ke halaman MANAGE
2. Form → Tahun: 2024, Kota: Bandung, Jumlah: 125000
3. Klik "Tambah Data"
4. Cek tabel untuk verifikasi
```

### Skenario 2: Koreksi Data Salah Input
```
Tujuan: Ubah Depok 2024 dari 50000 → 65000
1. Tabel → Cari baris Depok 2024
2. Klik [Edit]
3. Modal → Ubah Jumlah ke 65000
4. Klik "Simpan Perubahan"
5. Kategori otomatis berubah dari Rendah → Sedang
```

### Skenario 3: Hapus Entry Duplikat
```
Tujuan: Hapus data duplicate
1. Filter data untuk menemukan duplicate
2. Klik [Delete] pada entry yang salah
3. Konfirmasi penghapusan
```

### Skenario 4: Analisis Trend Per Kota
```
Tujuan: Lihat perubahan Sukabumi 2019-2024
1. Ke halaman DATA
2. Filter → Kota: Sukabumi, Tahun: Semua Tahun
3. Klik [Detail] pada salah satu baris
4. Halaman detail menampilkan timeline Sukabumi
```

---

## ⚠️ Perhatian & Best Practices

### ✅ DO (LAKUKAN)
- ✅ Backup data secara berkala
- ✅ Periksa kembali sebelum delete
- ✅ Gunakan kategori yang tepat
- ✅ Dokumentasikan perubahan besar
- ✅ Test di manage page sebelum bagikan

### ❌ DON'T (JANGAN)
- ❌ Jangan hapus data tanpa backup
- ❌ Jangan close browser tanpa save
- ❌ Jangan input angka negatif
- ❌ Jangan ulang submit jika sudah success
- ❌ Jangan edit tahun untuk data lama (buat baru)

---

## 🔧 Troubleshooting

### ❓ Form tidak submit
**Solusi:**
- Pastikan semua field terisi
- Periksa tanda * (required field)
- Lihat console browser (F12) untuk error

### ❓ Data tidak muncul di tabel
**Solusi:**
- Refresh page (F5)
- Periksa loading state
- Buka console untuk error message

### ❓ Kategori salah
**Solusi:**
- Kategori otomatis, pastikan jumlah benar
- Range: Tinggi ≥100K, Sedang 50K-99K, Rendah <50K

### ❓ Tidak bisa edit/delete
**Solusi:**
- Periksa apakah tombol berfungsi
- Lihat notification message
- Refresh halaman dan coba lagi

---

## 📊 Data Export & Backup

### Manual Backup CSV
```
1. Buka folder: D:\frontend12\
2. File: dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv
3. Copy file untuk backup
```

### View Raw Data
```
1. Buka file CSV dengan Excel
2. Semua kolom: tahun, nama_kabupaten_kota, jumlah_penderita_dm, kategori_dm, persentase_tahun
3. Data original + CRUD changes
```

---

## 📞 Support & Help

### Jika Error Terjadi:
1. **Cek Console Browser** (F12 → Console)
2. **Cek Terminal Flask** untuk error message
3. **Restart Flask** jika perlu
4. **Refresh Browser** (Ctrl+F5)

### Terminal Flask
```
# Melihat log real-time
python app.py

# Keterangan:
✅ Dataset loaded → Dataset loaded sukses
ERROR → Ada error, baca pesan
* Detected change in → File berubah, auto-reload
* Restarting with stat → Flask restart (normal)
```

---

## 🎓 Educational Info

### Data yang Ditampilkan
- **Sumber**: Dinas Kesehatan Jawa Barat
- **Periode**: 2019-2024 (6 tahun)
- **Area**: 27 Kabupaten/Kota di Jawa Barat
- **Metrik**: Jumlah penderita Diabetes Melitus

### Pentingnya Data Ini
- Monitoring kesehatan publik regional
- Trend analisis untuk policy making
- Resource allocation planning
- Outbreak prevention

---

## 🎉 Kesimpulan

Dashboard ini memberikan:
- ✅ Visualisasi data yang jelas
- ✅ Analisis mendalam dari berbagai perspektif
- ✅ Kemampuan CRUD untuk manage data
- ✅ Interface yang user-friendly
- ✅ Responsive design untuk berbagai device

**Selamat menggunakan Dashboard Diabetes Mellitus Jawa Barat! 🎯**

---

**Version**: 2.0.1  
**Updated**: 2024  
**Author**: Development Team
