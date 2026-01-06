#tugas1 loop angka
# minta input angka
# tampilkan angka 1 sampai angka yang di input
# jika angka > 10, menampilkan terlalu besar

angka = int(input("Masukkan angka: "))

if angka > 10:
    print("Angka tidak boleh lebih dari 10")
    exit()

for i in range(1, angka + 1):
    print(f"Angka ke - {i}")
    
#tugas2 scan port simulasi , loop scan 1-10
for i in range(1, 11):
    print(f"\nScanning port {i}")
