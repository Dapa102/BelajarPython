# Kalkulator belanja unlimited
print("=== Kalkulator Belanja ===")

while True:
    harga_barang = []

    banyak_barang = int(input("Berapa barang yang ingin dibeli? "))

    for i in range(banyak_barang):
        harga = int(input(f"Harga barang ke- {i+1}\t: Rp."))
        harga_barang.append(harga)
    
    total = sum(harga_barang)
        
    if total >= 100000:
        diskon = total * 0.1
    else:
        diskon = 0
        
    total_bayar = total - diskon
    
    print("\n=== STRUK BELANJA ===")
    for i, harga in enumerate(harga_barang, start=1):
        print(f"Barang ke- {i}\t: Rp.{harga:,.0f}")
    
    print(f"\nTotal\t\t: Rp.{total:,.0f}")
    print(f"Diskon 10%\t: Rp.{diskon:,.0f}")
    print(f"Total Bayar\t: Rp.{total_bayar:,.0f}")
    
    belanja_lagi = input("\nBelanja Lagi? (y/n): ")
    if belanja_lagi.lower() == "n":
        print("Terima kasih dan sampai jumpa")
        break