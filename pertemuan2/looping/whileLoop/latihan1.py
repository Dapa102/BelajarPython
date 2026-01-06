# Belajar while loop
import datetime as dt

while True:
    angka = int(input("Masukkan angka: "))
    if angka > 0:
        print("tolong masukkan angka 0")
    elif angka == 0:
        print("nah gitu masukkin 0")
        break
    else:
        print("angka negatif, coba lagi")
print("selesai\n")

# Belajar security sederhana
password_benar = "admin123"
percobaan = 0

while percobaan < 3:
    password = input("Masukkan password: ")
    if password == password_benar:
        print("Akses diterima")
        waktu = dt.datetime.now()
        print(f"Anda berhasil login pada waktu: {waktu:%H:%M:%S}\n")
        break
    else:
        print("password salah")
    percobaan += 1

if percobaan == 3:
    print("akses diblockir\n")



    