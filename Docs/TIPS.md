# 💡 Tips & Trik - Dashboard Diabetes Melitus

## 📚 Panduan Penggunaan Dashboard

---

## 🎯 Navigasi Dashboard

### 1️⃣ Dashboard (Home)
**URL**: http://localhost:5000/

**Apa yang bisa dilihat?**
- Total penderita semua tahun
- Jumlah kabupaten/kota di Jawa Barat
- Tahun terbaru dan jumlah penderita
- Perubahan persentase (naik/turun) dari tahun sebelumnya
- Grafik tren tahunan
- Top 10 kabupaten dengan kasus tertinggi
- Top 5 kabupaten tertinggi (tabel)
- Proporsi kategori penderita

**Tips**:
- Hover di card untuk melihat tooltip (jika ada)
- Klik nama kabupaten di "Top 5" untuk melihat detail
- Chart otomatis di-update saat aplikasi startup

---

### 2️⃣ Analisis (Analysis)
**URL**: http://localhost:5000/analisis

**Apa yang bisa dilihat?**
- **Analisis 14**: Total penderita per tahun dengan perubahan %
- **Analisis 15**: Rata-rata penderita per kabupaten/kota
- **Analisis 16**: Kabupaten/kota dengan kasus tertinggi & terendah

**Tips**:
- Analisis 15 udah sorted dari tertinggi ke terendah
- Badge warna menunjukkan kategori penderita:
  - 🔴 Merah (Tinggi) = ≥ 100.000
  - 🟡 Kuning (Sedang) = 50.000-99.999
  - 🟢 Hijau (Rendah) = < 50.000
- Klik nama kabupaten untuk melihat detail time-series

---

### 3️⃣ Data (Data Lengkap)
**URL**: http://localhost:5000/data

**Apa yang bisa dilakukan?**
- Lihat **semua data** penderita (162 records)
- **Filter by Tahun**: Pilih tahun spesifik (2019-2024)
- **Filter by Kabupaten/Kota**: Lihat data kota tertentu
- **Filter by Kategori**: Lihat data Tinggi/Sedang/Rendah
- **Combine filters**: Bisa kombinasi (mis: tahun 2019 + kategori Tinggi)
- **Pagination**: Navigate dengan Previous/Next atau langsung ke halaman

**Tips Filtering**:
```
Contoh kombinasi filter:
1. Tahun: 2019 + Kategori: Tinggi
   → Lihat semua kota dengan kasus tinggi di 2019

2. Kota: KABUPATEN BANDUNG + Kategori: Sedang
   → Lihat tahun mana saja Bandung kategori Sedang

3. Kategori: Rendah
   → Lihat semua kota dengan kasus rendah (semua tahun)
```

**Keyboard Shortcuts** (form submission):
- Isi filter → Click "Filter" atau tekan Enter
- Click "Reset" untuk clear semua filter

---

### 4️⃣ Detail Kabupaten/Kota
**URL**: http://localhost:5000/detail/KABUPATEN%20BOGOR (contoh)

**Apa yang bisa dilihat?**
- **Statistik per Kota**:
  - Total penderita (semua tahun)
  - Rata-rata per tahun
  - Nilai tertinggi & terendah
- **Riwayat per Tahun**: Tabel lengkap tahun ke tahun
- **Perubahan %**: Peningkatan/penurunan setiap tahunnya
- **Kategori**: Badge untuk setiap tahun

**Tips**:
- Perubahan % menunjukkan trend naik (↑) atau turun (↓)
- Berguna untuk melihat progress pemberantasan DM per kota
- Bisa akses dari:
  - Dashboard (Top 5 table)
  - Analisis 15 (Rata-rata table)
  - Data (Detail button)

---

## 🔍 Advanced Tips

### 1. Membaca Chart/Grafik
**Trend Tahunan** (garis):
- Garis naik = kasus meningkat
- Garis turun = kasus menurun
- Kemiringan menunjukkan kecepatan perubahan

**Top 10 Kabupaten** (bar horizontal):
- Bar paling panjang = kasus tertinggi
- Sorting otomatis dari tertinggi ke terendah
- Urutan bar menunjuk ke mana yang perlu perhatian

**Kategori** (pie chart):
- Ukuran slice = proporsi kategori
- Persentase menunjukkan pembagian

---

### 2. Data Interpretation

**Jika Tahun 2019 vs 2024 Meningkat Drastis**:
- Indikasi: Peningkatan kasus DM yang signifikan
- Action: Perlu intensifikasi program pengendalian

**Jika Ada Kota Kategori "Tinggi"**:
- Indikasi: Area dengan beban kesehatan DM berat
- Action: Prioritas untuk program intervensi

**Jika Rata-rata Tinggi di Analisis 15**:
- Indikasi: Kota konsisten tinggi sepanjang tahun
- Action: Butuh strategi jangka panjang

---

### 3. Membandingkan Data

**Perbandingan Antar Tahun**:
Gunakan filter untuk membandingkan tahun berbeda:
1. Cek tahun 2019 → catat kota tertinggi
2. Cek tahun 2024 → bandingkan dengan 2019
3. Lihat di Analisis 14 perubahan totalnya

**Perbandingan Antar Kota**:
1. Ke halaman Data
2. Filter kota A → lihat data
3. Ubah filter ke kota B → bandingkan

**Perbandingan Kategori**:
1. Ke Analisis 15 (rata-rata)
2. Lihat mana saja kategori Tinggi
3. Bandingkan dengan Sedang & Rendah

---

### 4. Export Data (Manual)

Jika ingin export data yang sedang dilihat:

**Opsi 1: Copy-Paste Tabel**
1. Select tabel → Ctrl+C
2. Paste ke Excel/Google Sheets

**Opsi 2: Screenshoot**
1. Print (Ctrl+P) → Save as PDF
2. atau Screenshot dengan snipping tool

**Opsi 3: Akses Source Data**
1. Buka file CSV langsung di Excel/Spreadsheet

---

## 📊 Use Cases / Skenario Penggunaan

### Skenario 1: Presentasi Ke Pimpinan
**Tujuan**: Tunjukkan trend DM di Jawa Barat

**Steps**:
1. Buka Dashboard (home) → tunjukkan statistik utama
2. Tunjukkan grafik tren tahunan → jelaskan trend
3. Buka Analisis → tunjukkan Top 5 kota tertinggi
4. Simpulkan action items

---

### Skenario 2: Analisis Mendalam Satu Kota
**Tujuan**: Understand trend DM di KABUPATEN BOGOR

**Steps**:
1. Ke halaman Data
2. Filter: Kota = "KABUPATEN BOGOR"
3. Lihat detail untuk setiap tahun
4. Atau langsung ke /detail/KABUPATEN%20BOGOR
5. Analisis tren per tahun, hitung growth rate

---

### Skenario 3: Identifikasi Area Kritis
**Tujuan**: Temukan kota mana yang butuh fokus

**Steps**:
1. Ke halaman Analisis
2. Lihat Analisis 16 → catat kota tertinggi (KARAWANG)
3. Ke Analisis 15 → cek rata-rata (KARAWANG mungkin top)
4. Filter kategori "Tinggi" di halaman Data
5. Identifikasi pattern → buat action plan

---

### Skenario 4: Monitoring Progress Tahunan
**Tujuan**: Track progress dari tahun ke tahun

**Steps**:
1. Ke Dashboard → lihat perubahan tahun terbaru
2. Ke Analisis 14 → lihat tren tahunan
3. Ke /detail/<kota> → lihat progress per kota
4. Bandingkan dengan baseline tahun lalu

---

## ⚡ Keyboard & Browser Tips

### Navigation Shortcuts
```
Ctrl+L              → Kursor ke address bar (ketik URL)
F5 atau Ctrl+R      → Refresh page
Ctrl+F              → Find text di halaman
Ctrl+P              → Print / Save as PDF
Alt+Left Arrow      → Back button
Alt+Right Arrow     → Forward button
```

### Form Tips
```
Tab                 → Move ke field berikutnya
Enter               → Submit form (jika di input terakhir)
Shift+Tab           → Move ke field sebelumnya
```

### Mobile Tips (jika akses dari handphone)
- Swipe left/right untuk scroll table
- Tap pada nama kabupaten untuk detail
- Filter button ada di atas table
- Pagination di bawah table

---

## 🎯 Checklist Penggunaan Pertama

- [ ] Akses Dashboard (home) → pastikan semua stat card muncul
- [ ] Akses Analisis → pastikan tabel teisi data
- [ ] Akses Data → coba filter tahun, kota, kategori
- [ ] Akses Detail → klik salah satu kabupaten
- [ ] Scroll halaman → pastikan responsive
- [ ] Baca semua badge warna → understand kategori

---

## ❓ FAQ

**Q: Gimana cara lihat data untuk tahun tertentu?**  
A: Ke halaman Data → Filter Tahun → Pilih tahun → Click Filter

**Q: Gimana cara lihat detail kota?**  
A: Ke halaman Data → klik "Detail" button, atau langsung di URL: /detail/NAMA_KOTA

**Q: Bagaimana cara filter multiple criteria?**  
A: Isi semua filter (tahun, kota, kategori) → Click "Filter"

**Q: Warna badge apa artinya?**  
A: Merah=Tinggi (≥100k), Kuning=Sedang (50k-99k), Hijau=Rendah (<50k)

**Q: Data sampai tahun berapa?**  
A: Data tersedia dari 2019 sampai 2024

**Q: Berapa jumlah kabupaten/kota di Jawa Barat?**  
A: 27 kabupaten/kota (bisa lihat di Dashboard card "Kabupaten/Kota")

**Q: Gimana cara export data?**  
A: Screenshot atau copy-paste tabel ke Excel (fitur export resmi bisa ditambah)

---

## 🚀 Pro Tips

1. **Bookmark Halaman Favorit**
   - Bookmark Dashboard untuk akses cepat
   - Bookmark /detail/<kota> untuk monitoring rutin

2. **Print ke PDF**
   - Ctrl+P → Ubah destination ke "Save as PDF"
   - Gunakan untuk laporan atau dokumentasi

3. **Kombinasi Filter Efisien**
   - Gunakan 1-2 filter saja (jangan ketig)
   - Lebih spesifik = hasil lebih jelas

4. **Cross-Check Data**
   - Lihat dari beberapa perspektif (Dashboard → Analisis → Detail)
   - Pastikan insight konsisten dari berbagai view

5. **Monitor Trends**
   - Cek Analisis 14 secara berkala
   - Track perubahan tahun ke tahun
   - Identifikasi inflection points

---

## 🎓 Learning Path

**Day 1: Explore**
- [ ] Jelajahi semua halaman
- [ ] Pahami struktur data
- [ ] Lihat semua chart/tabel

**Day 2: Analyze**
- [ ] Baca Analisis 14-16 dengan seksama
- [ ] Buat notes tentang findings
- [ ] Identifikasi area kritis

**Day 3: Interpret**
- [ ] Buat kesimpulan dari data
- [ ] Bandingkan antar periode/area
- [ ] Rencanakan action items

**Day 4+: Monitor**
- [ ] Setup routine checking
- [ ] Track progress
- [ ] Update insights berkala

---

## 💬 Sharing & Collaboration

### Share Halaman Tertentu
Bisa copy-paste URL dan share ke colleague:
```
http://localhost:5000/
http://localhost:5000/analisis
http://localhost:5000/data?tahun=2019&kategori=Tinggi
http://localhost:5000/detail/KABUPATEN%20BANDUNG
```

### Share Finding
1. Screenshot halaman
2. Annotate dengan findings/notes
3. Share ke team via email/chat

### Export untuk Meeting
1. Print halaman jadi PDF (Ctrl+P)
2. Buat summary dari data
3. Present dengan confidence! 💪

---

**Happy Analyzing! 📊✨**

Untuk pertanyaan lebih lanjut, cek README.md atau INSTALLATION.md

---

*Dashboard Penderita Diabetes Melitus Jawa Barat - Tips & Tricks v1.0*
