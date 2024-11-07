from flask import Flask, render_template, request, jsonify, redirect, url_for, send_from_directory
import csv
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

# Fungsi untuk memeriksa ekstensi file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('home.html')

# Rute untuk halaman CV
@app.route('/cv')
def cv():
    return render_template('cv.html')

# Halaman Portofolio
@app.route('/portofolio')
def portofolio():
    return render_template('portofolio.html')

# Halaman Biodata
@app.route('/biodata')
def biodata():
    return render_template('biodata.html')

# Halaman Instagram
@app.route('/instagram')
def instagram():
    return redirect("https://www.instagram.com/najwazayr_")

# Route untuk halaman Foto Diri
@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    result = None
    if request.method == 'POST':
        n = int(request.form['number'])
        sequence = [1, 1]
        for i in range(2, n):
            sequence.append(sequence[-1] + sequence[-2])
        result = sequence[:n]
    return render_template('fibonacci.html', result=result)

# Route untuk menampilkan data CSV dalam format JSON
@app.route('/data', methods=['GET'])
def get_csv_data():
    data = []
    try:
        with open('data.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        return jsonify({"error": "File CSV tidak ditemukan"}), 404
    return jsonify(data)

# List untuk menyimpan hasil input
submitted_data = []

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Ambil data dari form dan simpan di list
        submitted_data.append(request.form['data'])
    
    # Kirim list data yang sudah disubmit ke template
    return render_template('form.html', data=submitted_data)

if __name__ == "__main__":
    app.run(debug=True)
