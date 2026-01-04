import datetime as dt

hari_ini = dt.datetime.now() # menampilkan tahun, bulan, tanggal, jam, menit, detik
print(hari_ini)

hari_ini = dt.datetime.now().day # menampilkan hanya tanggal
print(f"Hari ini tanggal: {hari_ini}")