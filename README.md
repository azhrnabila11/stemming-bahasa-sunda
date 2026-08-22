# Adaptasi Algoritma Enhanced Confix Stripping (ECS) untuk Stemming Bahasa Sunda

Proyek ini merupakan implementasi dan adaptasi algoritma **Enhanced Confix Stripping (ECS)**—yang awalnya dirancang untuk Bahasa Indonesia—agar dapat memproses morfem dan kata berimbuhan dalam **Bahasa Sunda**. Sistem dikembangkan berbasis web menggunakan *framework* **Django**.

---

##  Fitur Utama
* **Engine ECS Sunda Custom:** Memiliki 48 *rule disambiguator* khusus (Rule 50–90) untuk memproses awalan, akhiran, sisipan (*infix*), dan konfiks Bahasa Sunda (seperti *dipang-*, *-eun*, *-ar-*, dll.).
* **Evaluasi Akurasi Ganda (*Dual Accuracy*):** Membandingkan hasil stemming dan nilai akurasi antara ECS Sunda (Hasil Adaptasi) dengan ECS Indonesia (Sastrawi Asli) secara *real-time*.
* **Multi-Format Input:** Mendukung input teks langsung serta pemrosesan *upload* dokumen dalam format `.txt`, `.docx`, dan `.xlsx`.
* **Ekspor Data:** Fitur untuk mengunduh hasil eksekusi stemming dan evaluasi validasi ke format CSV.

---

##  Perbandingan ECS Indonesia vs. ECS Sunda

| Parameter Perbandingan | ECS Indonesia (Sastrawi) | ECS Sunda (Proyek Ini) |
| :--- | :--- | :--- |
| **Basis Kamus** | Kamus Bahasa Indonesia | Kamus Bahasa Sunda (Wikikamus) |
| **Jumlah Rule** | Rule 1–42 (Morfologi Indonesia) | 48 Rule Disambiguasi Baru (Morfologi Sunda) |
| **Cakupan Imbuhan** | *me-*, *ber-*, *-kan*, *-i*, dll. | *dipang-*, *-eun*, *-ana*, *-ar-*, *-in-*, dll. |
| **Penanganan Sisipan** | Tidak didukung | Didukung (contoh: *-ar-*, *-in-*) |

---

##  Teknologi yang Digunakan
* **Language:** Python 3.x
* **Framework:** Django 5.x
* **NLP Libraries:** NLTK, PySastrawi (Architecture base)
* **File Parsers:** `python-docx`, `pandas`, `openpyxl`
* **Frontend:** HTML5, CSS3, Bootstrap

---

##  Sumber Data & Kamus Acuan

Validasi kata dasar dan pembersihan data pada sistem ini memanfaatkan dataset terbuka (*open source*) berikut:

1. **Kamus Dasar Sunda (`db_kamus_sunda`):**
   * **Sumber:** [Wikikamus Bahasa Sunda / Wiktionary](https://id.wiktionary.org/)
   * **Deskripsi:** Ekstraksi entri leksikal kata dasar Bahasa Sunda yang digunakan sebagai acuan *dictionary lookup* saat proses stripping imbuhan.

2. **Kamus Stopword Sunda (`db_stopwords`):**
   * **Sumber:** Repositori GitHub [`Javanese-and-Sundanese-Stopword`]([https://github.com/Bimarakajati/Javanese-and-Sundanese-Stopword](https://github.com/bimarakajati/Javanese-and-Sundanese-Stopwords) oleh **Bimarakajati**.
   * **Deskripsi:** Terdiri dari 750 kata tugas (*stopword*) Bahasa Sunda untuk menyaring kata-kata non-esensial pada tahap *filtering preprocessing*.

---

