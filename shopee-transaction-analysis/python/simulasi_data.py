from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import random  
from datetime import datetime, timedelta

#MEMBUAT DATA KONSUMEN
random.seed(42)

jumlah_konsumen = 200
konsumen = []

for i in range(1, jumlah_konsumen + 1):
    konsumen.append({
        "konsumen_id": i,
        "kategori_konsumen": random.choice(["baru", "lama"]),
        "wilayah": random.choice(["Jakarta", "Bandung", "Surabaya", "Medan", "Makassar"]),
        "jumlah_anggota_rumah_tangga": random.randint(2, 5)
    })

df_konsumen = pd.DataFrame(konsumen)
df_konsumen




#MEMBUAT DATA TRANSAKSI
jumlah_transaksi = 1200
transaksi = []

tanggal_event = [
    "2024-01-01", "2024-02-02", "2024-03-03", "2024-04-04",
    "2024-05-05", "2024-06-06", "2024-07-07", "2024-08-08",
    "2024-09-09", "2024-10-10", "2024-11-11", "2024-12-12"
]

for i in range(1, jumlah_transaksi + 1):
    is_event = random.random() < 0.4
    tanggal = random.choice(tanggal_event) if is_event else (
        datetime(2024, 1, 1) + timedelta(days=random.randint(1, 364))
    ).strftime("%Y-%m-%d")

    transaksi.append({
        "transaksi_id": i,
        "konsumen_id": random.randint(1, 200),
        "tanggal_transaksi": tanggal,
        "jenis_hari": "event" if is_event else "hari_biasa",
        "jenis_event": "tanggal_kembar" if is_event else "non_event",
        "nilai_transaksi": random.randint(150000, 800000) if is_event else random.randint(20000, 250000),
        "jumlah_item": random.randint(2, 8) if is_event else random.randint(1, 4),
        "metode_pembayaran": random.choice(["e-wallet", "COD", "transfer"]),
        "promo": True if is_event else random.random() < 0.3
    })

df_transaksi = pd.DataFrame(transaksi)
df_transaksi