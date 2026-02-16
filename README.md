# Analisis Perilaku Transaksi Konsumen Marketplace di Indonesia  
(Studi Kasus Shopee)

## Gambaran Proyek
Proyek ini bertujuan untuk menganalisis perilaku transaksi konsumen marketplace di Indonesia pada periode **event (tanggal kembar)** dan **hari biasa**, dengan menggunakan studi kasus Shopee dari sudut pandang konsumen.

Analisis difokuskan pada perbedaan jumlah transaksi, nilai transaksi rata-rata, intensitas transaksi per hari, penggunaan promo, metode pembayaran, serta perilaku konsumen baru dan konsumen lama.

> Dataset yang digunakan merupakan **data simulasi transaksi konsumen** yang merepresentasikan aktivitas belanja di marketplace Shopee.

---

## Tujuan Analisis
- Membandingkan perilaku transaksi konsumen pada periode event dan hari biasa
- Menganalisis perbedaan nilai transaksi rata-rata dan total pendapatan (revenue)
- Mengkaji pengaruh promo terhadap nilai transaksi
- Menganalisis preferensi metode pembayaran konsumen
- Mengidentifikasi perbedaan perilaku konsumen baru dan konsumen lama

---

## Dataset
Dataset disusun menggunakan **Google Spreadsheet** dan terdiri dari dua sheet:

- **Sheet 1 – konsumen**  
  Berisi data karakteristik konsumen (baru/lama, wilayah, jumlah anggota rumah tangga).

- **Sheet 2 – transaksi**  
  Berisi data transaksi konsumen pada periode event dan hari biasa.

**Tautan Dataset (Google Spreadsheet):**  
(https://docs.google.com/spreadsheets/d/1SiE7-swTTGAihEoF0ta_jw5CK-_3zLzIhieUWWFsbuA/edit?usp=sharing)


## Tools yang dipakai
- PostgreSQL (Database & SQL Analysis)
- SQL
- Python (Google Colab – simulasi data)
- Google Spreadsheet

---

## Metodologi Singkat
1. Data simulasi transaksi konsumen dibuat menggunakan Python.
2. Data disusun dan divalidasi melalui Google Spreadsheet.
3. Data diimpor ke PostgreSQL untuk analisis.
4. Analisis dilakukan menggunakan query SQL terstruktur.
5. Hasil analisis diinterpretasikan menjadi insight dan rekomendasi bisnis.

---

## Ringkasan Hasil Analisis
- Jumlah transaksi pada hari biasa lebih tinggi dibandingkan periode event.
- Nilai transaksi rata-rata pada periode event lebih tinggi dibandingkan hari biasa.
- Intensitas transaksi per hari lebih tinggi pada periode event.
- Penggunaan promo meningkat signifikan selama event dan berdampak pada peningkatan nilai transaksi.
- Metode pembayaran e-wallet menjadi metode paling dominan pada periode event.
- Konsumen lama merupakan penyumbang revenue terbesar, sementara event efektif meningkatkan partisipasi konsumen baru.

---

## Rekomendasi Bisnis
- Event tanggal kembar perlu dipertahankan karena terbukti meningkatkan nilai transaksi konsumen.
- Optimalisasi promo berbasis e-wallet selama event untuk memaksimalkan pendapatan.
- Strategi akuisisi konsumen baru sebaiknya difokuskan pada periode event.
- Pada hari biasa, perusahaan perlu memperkuat strategi retensi konsumen lama untuk menjaga stabilitas transaksi.

---

## Penulis
Ilyas Yasin Nurulah
