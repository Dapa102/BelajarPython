# Pengulangan 5 kali
for i in range(5):
    print(f"Halo ke- {i+1}")

# Loop melewati list
buah = ["Apel", "Jeruk", "Mangga"]

for item in buah:
    print(f"\nSaya suka {item}")

# input banyak barang pakai list
harga_barang = []
print(" ")
jumlah = int(input("Mau input berapa barang? "))

for i in range(jumlah):
    harga = int(input(f"Harga barang ke- {i+1}\t: Rp. "))
    harga_barang.append(harga)

total = sum(harga_barang)
print(f"Total belanja anda adalah : Rp.{total}")

# cari harga termahal
harga = [1, 2, 3]

termahal = max(harga)
termurah = min(harga)

print(f"\nHarga termahal adalah : Rp.{termahal}")
print(f"Harga termurah adalah : Rp.{termurah}")