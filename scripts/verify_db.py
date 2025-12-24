import sqlite3
import os

DB = os.path.join(os.path.dirname(__file__), '..', 'diabetes_jabar.db')
DB = os.path.abspath(DB)

if not os.path.exists(DB):
    print('Database not found at', DB)
    print('Run setup_database.py first to create the DB from CSV.')
    raise SystemExit(1)

conn = sqlite3.connect(DB)
cursor = conn.cursor()

print('Tables and row counts:')
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
for (t,) in cursor.fetchall():
    cursor.execute(f"SELECT COUNT(*) FROM {t}")
    print(f" - {t}: {cursor.fetchone()[0]} rows")

print('\nSample from penderita_dm:')
cursor.execute('SELECT nama_kabupaten_kota, jumlah_penderita_dm, tahun FROM penderita_dm LIMIT 5')
for row in cursor.fetchall():
    print(' ', row)

conn.close()
