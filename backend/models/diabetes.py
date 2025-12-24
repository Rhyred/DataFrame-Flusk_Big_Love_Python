from backend.models.base import db

# 1. Model Data Utama (Untuk List Lengkap/Search)
class PenderitaDM(db.Model):
    __tablename__ = 'penderita_dm'
    id = db.Column(db.Integer, primary_key=True)
    nama_kabupaten_kota = db.Column(db.String(100))
    jumlah_penderita_dm = db.Column(db.Integer)
    tahun = db.Column(db.Integer)
    kategori_dm = db.Column(db.String(20))
    persentase_tahun = db.Column(db.Float)

# 2. Model Ringkasan (Untuk Grafik Dashboard)
class TotalPerTahun(db.Model):
    __tablename__ = 'total_per_tahun'
    tahun = db.Column(db.Integer, primary_key=True)
    total_penderita = db.Column(db.Integer)

# 3. Model Top 10 (Untuk Tabel "Highest Cases")
class Top10PerTahun(db.Model):
    __tablename__ = 'top_10_per_tahun'
    # Composite PK trick karena tabel ini hasil sortiran
    tahun = db.Column(db.Integer, primary_key=True) 
    nama_kabupaten_kota = db.Column(db.String(100), primary_key=True)
    jumlah_penderita_dm = db.Column(db.Integer)