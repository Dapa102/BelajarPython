# latihan membuat data diri kelahiran sederhana
import datetime as dt
nama = input("Masukkan nama anda: ")
if nama == "":
    print("Nama tidak boleh kosong")
    exit()
else:
    print(f"Selamat datang, {nama}")

print("\nMasukkan tanggal lahir anda (tanggal, bulan, tahun)")
Tanggal = int(input("Masukkan tanggal lahir anda\t: "))
Bulan = int(input("Masukkan bulan lahir anda\t: "))
Tahun = int(input("Masukkan tahun lahir anda\t: "))

kelahiran = dt.date(Tahun, Bulan, Tanggal)
hari_sekarang = dt.date.today()
print(f"\nTanggal hari ini adalah: {hari_sekarang}")
umur = hari_sekarang - kelahiran
tahun_umur = umur.days // 365
print(f"\nNama anda adalah: {nama}, anda lahir pada tanggal: {kelahiran}, dan umur anda sekarang adalah: {tahun_umur} tahun")