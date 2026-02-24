import datetime

def cek_saldo(saldo):
    print(f"\nSaldo Anda saat ini: Rp {saldo}")

def setor_uang(saldo, jumlah):
    if jumlah <= 0:
        print("Jumlah setor harus lebih dari 0.")
        return saldo, False
    else:
        saldo += jumlah
        print(f"Setor berhasil. Saldo Anda saat ini: Rp {saldo}")
        return saldo, True

def tarik_uang(saldo, jumlah):
    if jumlah <= 0:
        print("Jumlah tarik harus lebih dari 0.")
        return saldo, False

    elif jumlah > saldo:
        print("Saldo tidak cukup.")
        return saldo, False

    else:
        saldo -= jumlah
        print(f"Tarik berhasil. Saldo Anda saat ini: Rp {saldo}")
        return saldo, True

def transfer_uang(saldo, jumlah):
    if jumlah <= 0:
        print("Jumlah transfer harus lebih dari 0.")
        return saldo, False

    elif jumlah > saldo:
        print("Saldo tidak cukup.")
        return saldo, False

    else:
        saldo -= jumlah
        print(f"Transfer berhasil. Saldo Anda saat ini: Rp {saldo}")
        return saldo, True

def tambah_history(history, jenis, jumlah):
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append(f"{waktu} - {jenis}: Rp {jumlah}")
    return history

def tampilkan_history(history):
    print("\n=== HISTORI TRANSAKSI ===")
    if not history:
        print("Belum ada transaksi.")
    else:
        for transaksi in history:
            print(transaksi)

def cek_limit_tarik(jumlah):
    LIMIT = 1000000

    if jumlah > LIMIT:
        print(f"Limit tarik harian maksimal Rp {LIMIT}")
        return False

    return True

def main():
    saldo = 0
    history = []
    
    while True:
        print("\n===== ATM PYTHON =====")
        print("1. Cek Saldo")
        print("2. Setor Uang")
        print("3. Tarik Uang")
        print("4. Transfer Uang")
        print("5. Histori Transaksi")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            cek_saldo(saldo)
            continue
        
        elif pilihan == "2":
            jumlah = int(input("Masukkan jumlah setor: "))
            saldo, berhasil = setor_uang(saldo, jumlah)
            if berhasil:
                history = tambah_history(history, "Setor", jumlah)
            continue
        
        elif pilihan == "3":
            jumlah = int(input("Masukkan jumlah tarik: "))
            if not cek_limit_tarik(jumlah):
                continue
            saldo, berhasil = tarik_uang(saldo, jumlah)
            if berhasil:
                history = tambah_history(history, "Tarik", jumlah)
            continue

        elif pilihan == "4":
            jumlah = int(input("Masukkan jumlah transfer: "))
            saldo, berhasil = transfer_uang(saldo, jumlah)
            if berhasil:
                history = tambah_history(history, "Transfer", jumlah)
            continue

        elif pilihan == "5":
            tampilkan_history(history)
            continue
        
        elif pilihan == "6":
            print("Terima kasih telah menggunakan ATM Python.")
            break

        else:
            print("Pilihan tidak valid.")
            continue
        
if __name__ == "__main__":
    main()