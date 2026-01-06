# latihan simulasi login menggunakan if else
import datetime as dt

time = dt.datetime.now()
print(f"Waktu sekarang: {time:%Y-%m-%d %H:%M:%S}")
pemimpin = "John Corner"
password_pemimpin = "SecurePassword111"
username = input("Masukkan username anda: ")
password = input("Masukkan password anda: ")

if username == pemimpin and password == password_pemimpin:
    print(f"Login berhasil, selamat datang {pemimpin}")
else:
    print("Login gagal, username atau password salah")

