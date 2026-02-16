-- Analisis dasar transaksi event vs hari biasa
SELECT
    jenis_hari,
    COUNT(*) AS jumlah_transaksi,
    ROUND(AVG(nilai_transaksi), 0) AS rata_rata_transaksi
FROM transaksi
GROUP BY jenis_hari;
