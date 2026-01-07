from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
import io
import sys

# Set encoding to UTF-8
if sys.stdout.encoding != 'utf-8':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Gunakan backend non-GUI
matplotlib.use('Agg')

app = Flask(__name__)

# --- Data Preparation ---
try:
    df = pd.read_csv('dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv')
    print("[OK] Dataset loaded.")
except FileNotFoundError:
    print("[ERROR] Dataset file not found!")
    exit()

def prepare_data():
    global df
    def tentukan_kategori(jumlah):
        if jumlah >= 100000:
            return "Tinggi"
        elif jumlah >= 50000:
            return "Sedang"
        else:
            return "Rendah"
    df['kategori_dm'] = df['jumlah_penderita_dm'].apply(tentukan_kategori)
    df['persentase_tahun'] = (df['jumlah_penderita_dm'] / df.groupby('tahun')['jumlah_penderita_dm'].transform('sum')) * 100

prepare_data()

# --- Chart Generation ---
def generate_themed_chart(chart_type, theme='light'):
    is_dark = theme == 'dark'
    
    # Setup warna berdasarkan tema
    text_color = 'white' if is_dark else '#333333'
    bg_color = '#1f2937' if is_dark else '#ffffff' # gray-800
    grid_color = '#374151' if is_dark else '#e5e7eb' # gray-700 / gray-200
    plot_color = '#34D399' # Emerald-400
    pie_colors = ['#EF4444', '#F59E0B', '#10B981'] # Red-500, Amber-500, Emerald-500

    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    fig.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    plt.rcParams.update({
        'text.color': text_color, 'axes.labelcolor': text_color, 
        'xtick.color': text_color, 'ytick.color': text_color, 
        'axes.edgecolor': grid_color
    })

    if chart_type == 'trend_tahunan':
        total_per_tahun = df.groupby('tahun')['jumlah_penderita_dm'].sum()
        ax.plot(total_per_tahun.index.astype(str), total_per_tahun.values, marker='o', linestyle='-', color=plot_color, markersize=8, linewidth=2.5)
        ax.set_title('Tren Total Penderita DM', fontsize=14, color=text_color, pad=20)
        ax.set_xlabel('Tahun', fontsize=12, color=text_color)
        ax.set_ylabel('Total Penderita', fontsize=12, color=text_color)
        ax.grid(True, which='both', linestyle='--', linewidth=0.5, color=grid_color)
    
    elif chart_type == 'kategori_2019':
        df_2019 = df[df['tahun'] == 2019]
        kategori_counts = df_2019['kategori_dm'].value_counts()
        wedges, labels, autotexts = ax.pie(kategori_counts, labels=kategori_counts.index, autopct='%1.1f%%', 
                                          startangle=140, colors=pie_colors, 
                                          textprops={'color': text_color, 'weight': 'bold'}, 
                                          wedgeprops={'edgecolor': bg_color, 'linewidth': 2})
        ax.set_title('Proporsi Kategori DM (2019)', fontsize=14, color=text_color, pad=20)
        plt.setp(autotexts, color='white' if is_dark else 'black', weight="bold", size=10)

    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", facecolor=fig.get_facecolor())
    plt.close(fig)
    buf.seek(0)
    return buf

# --- Main Routes ---
@app.route('/')
def index():
    total_penderita = int(df['jumlah_penderita_dm'].sum())
    total_kota = df['nama_kabupaten_kota'].nunique()
    tahun_terbaru = int(df['tahun'].max())
    total_tahun_terbaru = int(df[df['tahun'] == tahun_terbaru]['jumlah_penderita_dm'].sum())
    tahun_sebelumnya = tahun_terbaru - 1
    total_tahun_sebelumnya = int(df[df['tahun'] == tahun_sebelumnya]['jumlah_penderita_dm'].sum())
    perubahan = ((total_tahun_terbaru - total_tahun_sebelumnya) / total_tahun_sebelumnya * 100) if total_tahun_sebelumnya > 0 else 0
    top_data = df.sort_values(['tahun', 'jumlah_penderita_dm'], ascending=[False, False]).head(5)
    return render_template('index.html', total_penderita=total_penderita, total_kota=total_kota, tahun_terbaru=tahun_terbaru, total_tahun_terbaru=total_tahun_terbaru, perubahan=perubahan, top_data=top_data)

@app.route('/charts/<chart_name>')
def get_chart(chart_name):
    theme = request.args.get('theme', 'light')
    buf = generate_themed_chart(chart_name, theme)
    return send_file(buf, mimetype='image/png')

@app.route('/analisis')
def analisis():
    total_per_tahun = df.groupby('tahun')['jumlah_penderita_dm'].sum()
    avg_per_kota = df.groupby('nama_kabupaten_kota')['jumlah_penderita_dm'].mean().sort_values(ascending=False)
    total_per_kota = df.groupby('nama_kabupaten_kota')['jumlah_penderita_dm'].sum()
    tertinggi_kota, tertinggi_nilai = total_per_kota.idxmax(), int(total_per_kota.max())
    terendah_kota, terendah_nilai = total_per_kota.idxmin(), int(total_per_kota.min())
    return render_template('analisis.html', total_per_tahun=total_per_tahun.to_dict(), avg_per_kota=avg_per_kota.head(15).to_dict(), tertinggi_kota=tertinggi_kota, tertinggi_nilai=tertinggi_nilai, terendah_kota=terendah_kota, terendah_nilai=terendah_nilai)

@app.route('/data')
def data():
    tahun_param = request.args.get('tahun', type=int)
    kota_param = request.args.get('kota')
    kategori_param = request.args.get('kategori')
    filtered_df = df.copy()
    if tahun_param: filtered_df = filtered_df[filtered_df['tahun'] == tahun_param]
    if kota_param: filtered_df = filtered_df[filtered_df['nama_kabupaten_kota'] == kota_param]
    if kategori_param: filtered_df = filtered_df[filtered_df['kategori_dm'] == kategori_param]
    filtered_df = filtered_df.sort_values(by='jumlah_penderita_dm', ascending=False)
    
    page = request.args.get('page', 1, type=int)
    per_page = 15
    total_rows = len(filtered_df)
    total_pages = (total_rows + per_page - 1) // per_page
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    data_page = filtered_df.iloc[start_idx:end_idx]
    
    tahun_list, kota_list = sorted(df['tahun'].unique()), sorted(df['nama_kabupaten_kota'].unique())
    kategori_list = ['Tinggi', 'Sedang', 'Rendah']
    return render_template('data.html', data=data_page.to_dict('records'), tahun_list=tahun_list, kota_list=kota_list, kategori_list=kategori_list, page=page, total_pages=total_pages, total_rows=total_rows, tahun_param=tahun_param, kota_param=kota_param, kategori_param=kategori_param)

@app.route('/detail/<kota>')
def detail_kota(kota):
    kota_data = df[df['nama_kabupaten_kota'] == kota].sort_values('tahun')
    if kota_data.empty: return ("Data tidak ditemukan", 404)
    total_kota, rata_rata = int(kota_data['jumlah_penderita_dm'].sum()), float(kota_data['jumlah_penderita_dm'].mean())
    tertinggi, terendah = int(kota_data['jumlah_penderita_dm'].max()), int(kota_data['jumlah_penderita_dm'].min())
    return render_template('detail_kota.html', kota=kota, kota_data=kota_data.to_dict('records'), total_kota=total_kota, rata_rata=rata_rata, tertinggi=tertinggi, terendah=terendah)

# --- CRUD & API Routes ---
@app.route('/manage')
def manage():
    tahun_list, kota_list = sorted(df['tahun'].unique()), sorted(df['nama_kabupaten_kota'].unique())
    return render_template('manage.html', tahun_list=tahun_list, kota_list=kota_list, total_records=len(df))

def save_data_to_csv():
    df.to_csv('dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv', index=False)

@app.route('/api/data')
def get_api_data(): return jsonify(df.to_dict('records'))

@app.route('/api/add', methods=['POST'])
def add_data():
    global df
    try:
        new_row = pd.DataFrame([request.form.to_dict()])
        new_row['tahun'] = new_row['tahun'].astype(int)
        new_row['jumlah_penderita_dm'] = new_row['jumlah_penderita_dm'].astype(int)
        df = pd.concat([df, new_row], ignore_index=True)
        prepare_data()
        save_data_to_csv()
        return {"status": "success", "message": "Data berhasil ditambahkan"}
    except Exception as e: return {"status": "error", "message": str(e)}, 400

@app.route('/api/edit/<int:row_id>', methods=['POST'])
def edit_data(row_id):
    global df
    try:
        if not (0 <= row_id < len(df)): return {"status": "error", "message": "ID tidak valid"}, 404
        df.loc[row_id, 'tahun'] = int(request.form.get('tahun'))
        df.loc[row_id, 'nama_kabupaten_kota'] = request.form.get('kota')
        df.loc[row_id, 'jumlah_penderita_dm'] = int(request.form.get('jumlah'))
        prepare_data()
        save_data_to_csv()
        return {"status": "success", "message": "Data berhasil diperbarui"}
    except Exception as e: return {"status": "error", "message": str(e)}, 400

@app.route('/api/delete/<int:row_id>', methods=['POST'])
def delete_data(row_id):
    global df
    try:
        if not (0 <= row_id < len(df)): return {"status": "error", "message": "ID tidak valid"}, 404
        df = df.drop(row_id).reset_index(drop=True)
        save_data_to_csv()
        return {"status": "success", "message": "Data berhasil dihapus"}
    except Exception as e: return {"status": "error", "message": str(e)}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)