-- Analisis perilaku konsumen baru dan lama
SELECT
    t.jenis_hari,
    k.kategori_konsumen,
    COUNT(*) AS jumlah_transaksi,
    ROUND(AVG(t.nilai_transaksi), 0) AS rata_rata_transaksi
FROM transaksi t
JOIN konsumen k
  ON t.konsumen_id = k.konsumen_id
GROUP BY t.jenis_hari, k.kategori_konsumen
ORDER BY t.jenis_hari, jumlah_transaksi DESC;
