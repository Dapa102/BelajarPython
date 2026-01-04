# tugas 1 , membuat variable dengan tipe data string, integer, dan boolean
target_ip = "192.168.1.1"
target_port = 80
status_aktif = True

print(f"Tipe data dari {target_ip} adalah {type(target_ip)}")
print(f"Tipe data dari {target_port} adalah {type(target_port)}")
print(f"Tipe data dari {status_aktif} adalah {type(status_aktif)}")

# tugas 2, melakukan input dari user
username_user = str(input("Masukkan username anda: "))
umur_user = int(input("Masukkan umur anda: "))
login_aktif = True

print(f"Selamat datang {username_user}")
print(f"Tipe data username anda adalah: {type(username_user)}")
print(f"Umur anda adalah: {umur_user}")
print(f"Tipe data umur anda adalah: {type(umur_user)}")
print(f"Status login aktif: {login_aktif}")
print(f"Tipe data status login anda adalah: {type(login_aktif)}")