saldo = 100000

while saldo > 0:
    beli = int(input("Mau penarikan saldo berapa?  "))
    saldo -= beli

    if saldo >= 0:
        print(f"Sisa saldo anda adalah {saldo}")
        print("Penarikan saldo selesai")
    else:
        print("Saldo anda tidak cukup")
        print("Silahkan cek kembali saldo anda")
        break

