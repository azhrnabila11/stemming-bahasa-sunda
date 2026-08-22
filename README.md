# Sundanese Stemmer Web Application (Modified ECS Algorithm)

Aplikasi web pemroses teks dan *stemming* Bahasa Sunda berbasis **Django** yang mengimplementasikan modifikasi algoritma **Enhanced Confix Stripping (ECS)**. Sistem ini dirancang untuk mengembalikan kata berimbuhan bahasa Sunda ke bentuk dasarnya menggunakan aturan disambiguasi morfologi Sunda terstruktur (Rule 50–90).

---

## 🚀 Fitur Utama

- **Modifikasi Algoritma ECS Sunda:** Pemotongan imbuhan berantai (*iterative stripping*) yang disesuaikan dengan karakteristik morfologi lokal, termasuk penanganan alomorf, konfiks, dan sisipan (*infix*).
- **Aturan Disambiguasi Terstruktur (Rule 50–90):** Mengintegrasikan himpunan aturan khusus untuk meminimalkan masalah *over-stemming* dan *under-stemming*.
- **Preservasi Karakter Aksensuasi (`é`/`É`):** Tahap *text cleansing* khusus untuk mempertahankan vokal beraksen Sunda agar tidak mengubah makna kata dasar.
- **Pemrosesan Dokumen Multi-Format:** Mampu mengolah dokumen teks berukuran besar dalam format `.txt`, `.docx`, dan `.xlsx`.
- **Pengukuran Kinerja Sistem:** Menampilkan analisis tingkat akurasi dan kecepatan waktu eksekusi (*running time*) pemrosesan secara otomatis.
- **Manajemen Basis Data Dinamis:** Terintegrasi dengan database kamus kata dasar dan *stopwords* bahasa Sunda yang dapat diperbarui.
- **Ekspor Data:** Fitur pengunduhan hasil ekstraksi *stemming* ke dalam format `.csv`.

---

## 🛠️ Teknologi yang Digunakan

- **Backend:** Python 3.11+, Django Framework
- **Data Processing:** Pandas, NLTK, `python-docx`
- **Database:** SQLite3 / PostgreSQL
- **Frontend:** HTML5, CSS3, JavaScript

---

## ⚙️ Panduan Instalasi Lokal

### 1. Prasyarat
Pastikan Python versi 3.10+ dan `git` sudah terpasang di sistem kamu.

### 2. Klon Repositori
```bash
git clone [https://github.com/username/project_skripsi.git](https://github.com/username/project_skripsi.git)
cd project_skripsi