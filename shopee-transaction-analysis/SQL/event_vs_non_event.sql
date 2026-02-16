-- Perbandingan intensitas transaksi dan revenue
SELECT
    jenis_hari,
    COUNT(*) AS total_transaksi,
    COUNT(DISTINCT tanggal_transaksi) AS jumlah_hari,
    ROUND(
        COUNT(*)::numeric / COUNT(DISTINCT tanggal_transaksi),
        2
    ) AS transaksi_per_hari,
    SUM(nilai_transaksi) AS total_revenue
FROM transaksi
GROUP BY jenis_hari;
