# latihan simulasi level akses menggunakan if elif else
import datetime as dt

level_akses = input("Masukkan jabatan anda (admin/user): ")
if level_akses == "admin":
    print("Admin memiliki akses penuh ke sistem")
elif level_akses == "user":
    print("User memiliki akses terbatas ke sistem")
else:
    print("Akses ditolak, anda bukan siapa siapa")

time = dt.datetime.now()
print(f"Anda login pada: {time:%Y-%m-%d %H:%M:%S}")