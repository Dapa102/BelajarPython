barang1 = int(input("Masukkan barang 1: "))
barang2 = int(input("Masukkan barang 2: "))
barang3 = int(input("Masukkan barang 3: "))
total = barang1 + barang2 + barang3

if total >= 100000:
    diskon = total * 0.1
    total_bayar = total - diskon
else:
    diskon = 0
    total_bayar = total

print(f"Total Belanja \t\t: {total:,.0f}")
print(f"Diskon 10% \t\t: {diskon:,.0f}")
print(f"Yang harus dibayar \t: {total_bayar:,.0f}")

