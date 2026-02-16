# Analisis Perilaku Transaksi Konsumen Marketplace di Indonesia  
(Studi Kasus Shopee)

## Gambaran Proyek
Proyek ini bertujuan untuk menganalisis perilaku transaksi konsumen marketplace di Indonesia pada periode **event (tanggal kembar)** dan **hari biasa**, dengan menggunakan studi kasus Shopee.

Analisis difokuskan pada perbedaan jumlah transaksi, nilai transaksi rata-rata, intensitas transaksi, penggunaan promo, metode pembayaran, serta perilaku konsumen baru dan lama.

> Catatan: Dataset yang digunakan dalam proyek ini merupakan **data simulasi transaksi konsumen** dan **bukan data internal perusahaan Shopee**.


## Tujuan Analisis
- Membandingkan perilaku transaksi konsumen pada periode event dan hari biasa
- Menganalisis perbedaan nilai transaksi rata-rata dan total revenue
- Mengkaji pengaruh promo terhadap nilai transaksi
- Menganalisis preferensi metode pembayaran konsumen
- Mengidentifikasi perbedaan perilaku konsumen baru dan konsumen lama

---

## Struktur Dataset
### Tabel `konsumen`
- konsumen_id  
- kategori_konsumen (baru / lama)  
- wilayah  
- jumlah_anggota_rumah_tangga  

### Tabel `transaksi`
- transaksi_id  
- konsumen_id  
- tanggal_transaksi  
- jenis_hari (event / hari_biasa)  
- jenis_event (tanggal_kembar / non_event)  
- nilai_transaksi  
- jumlah_item  
- metode_pembayaran  
- promo  

---

## Tools & Teknologi
- PostgreSQL  
- SQL  
- Python (Pandas)  
- Google Colab  

---

## Ringkasan Hasil Analisis
- Jumlah transaksi pada hari biasa lebih tinggi dibandingkan periode event.
- Nilai transaksi rata-rata pada periode event lebih tinggi dibandingkan hari biasa.
- Intensitas transaksi per hari lebih tinggi pada periode event.
- Penggunaan promo meningkat signifikan saat event dan berdampak pada peningkatan nilai transaksi.
- Metode pembayaran e-wallet menjadi pilihan utama selama periode event.
- Konsumen lama merupakan penyumbang revenue terbesar, namun event efektif meningkatkan partisipasi konsumen baru.

---

## Rekomendasi Bisnis
- Event tanggal kembar perlu dipertahankan karena efektif meningkatkan nilai transaksi konsumen.
- Optimalisasi promo berbasis e-wallet pada periode event untuk memaksimalkan pendapatan.
- Strategi akuisisi konsumen baru sebaiknya difokuskan pada periode event.
- Pada hari biasa, perusahaan perlu memperkuat strategi retensi konsumen lama untuk menjaga stabilitas transaksi.

---

## Penulis
Mahasiswa Informatika  
Project Data Analyst (Portofolio)
