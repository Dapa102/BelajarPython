import datetime as dt

hari_ini = dt.datetime.now() # menampilkan tahun, bulan, tanggal, jam, menit, detik
print(hari_ini)

tanggal = dt.date(2006, 5, 4) # Mengatur tanggal sesuai dengan apa yang kita mau
print ("Tanggal lahir saya adalah: ", tanggal)
print(f"Hari saya ultah adalah hari = {tanggal:%A}")

hari = dt.date.today() # menampilkan tanggal hari ini
print(hari)
print(f"Hari ini adalah hari = {hari:%A}")

print ("Masukkan tanggal, tahun, bulan") # input tanggal lahir user
tanggal = int(input("Tanggal \t= "))
bulan = int(input("Bulan \t\t= "))
tahun = int(input("Tahun \t\t= "))

tanggal_lahir = dt.date(tahun, bulan, tanggal) 
print(f"Tanggal lahir anda adalah = {tanggal_lahir}") # menampilkan tanggal lahir user
print(f"Hari lahir nya adalah = {tanggal_lahir:%A}") # menampilkan hari lahir user

hari_sekarang = dt.date.today() # menampilkan tanggal hari ini
print(f"Hari ini adalah tanggal = {hari_sekarang}")
umur = hari_sekarang - tanggal_lahir
umur_tahun = umur.days // 365
print(f"Umur anda adalah = {umur_tahun} tahun")