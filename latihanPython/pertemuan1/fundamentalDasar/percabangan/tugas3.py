# Membuat input untuk tanggal, bulan, lahir
import datetime as dt

print("Masukkan tanggal, bulan, tahun lahir anda") # input tanggal lahir user
tanggal = int(input("Tanggal lahir anda \t= "))
bulan = int(input("Bulan lahir anda \t= "))
tahun = int(input("Tahun lahir anda \t= "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah = {tanggal_lahir}")
print(f"Hari kelahiran anda adalah = {tanggal_lahir:%A}")

hari_sekarang = dt.date.today() # untuk menghitung umur
print(f"Hari ini adalah tanggal = {hari_sekarang}")
umur = hari_sekarang - tanggal_lahir
umur_tahun = umur.days //365
print(f"Umur anda adalah = {umur_tahun} tahun")