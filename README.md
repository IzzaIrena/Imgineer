# Imgineer

# 🖼️ Aplikasi Pengolahan Citra Digital dengan Tkinter & OpenCV
Repositori ini berisi aplikasi GUI berbasis Python (Tkinter) untuk melakukan berbagai operasi pengolahan citra digital, seperti grayscale, thresholding, histogram, edge detection, erosi, serta operasi aritmatika dan logika.

## 🗂️ Struktur Cabang (Branch)
Branch main
Isi: Antarmuka GUI utama
File: main.py

Branch grayscale-biner-histogram
Isi: Fitur Grayscale, Biner, Histogram
File: citra_grayscale_biner_histogram.py

Branch edge-erosi
Isi: Fitur Edge Detection dan Erosi
File: citra_edge_erosi.py

Branch aritmatika-logika
Isi: Fitur Operasi Aritmatika dan Logika
File: citra_aritmatika_logika.py

## 📌 Deskripsi Fitur
### 🔹 `main.py` (GUI Utama)
- Tampilan GUI dengan tombol untuk mengakses fitur.
- Load dan tampilkan gambar.
- Integrasi fungsi dari file lain (jika digabung).
  
### 🔹 Grayscale, Biner, Histogram (`grayscale-biner-histogram`)
- Konversi ke **Grayscale**.
- Thresholding ke **Biner (Binary)**.
- Menampilkan **Histogram RGB**.

### 🔹 Edge Detection & Erosi (`edge-erosi`)
- Deteksi tepi dengan metode **Canny**.
- **Erosi** menggunakan dua jenis elemen struktur:
  - Kotak penuh (3x3)
  - Cross (struktur plus)

### 🔹 Aritmatika & Logika (`aritmatika-logika`)
- Penambahan brightness secara **aritmatika** (`cv2.add`).
- Operasi logika **NOT** (inversi warna).

---

## ⚙️ Teknologi
- Python 3.x
- OpenCV
- NumPy
- Matplotlib
- Pillow (untuk Tkinter image)

---

## 🚀 Cara Menjalankan
1. Pastikan semua dependensi terinstal:
   ```bash
   pip install opencv-python numpy matplotlib pillow
