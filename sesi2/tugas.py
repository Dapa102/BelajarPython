# Membuat to do list
print("=== TO-DO LIST ===")

tugas = []

while True:
    print("1. Tambah Tugas")
    print("2. Lihat Semua Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")
    
    try:
        pilihan = int(input("Masukkan Pilihan: "))
    
    except ValueError:
        print("Input harus angka!\n")
        continue

    if pilihan == 1:
        tugas_baru = input("Masukkan Tugas Baru: ")
        tugas.append(tugas_baru)
        print(f"Tugas {tugas_baru} berhasil ditambahkan\n")

    elif pilihan == 2:
        if len(tugas) == 0:
            print("Belum ada tugas\n")
        else:
            print("\nDaftar Tugas: ")
            for i, t in enumerate(tugas):
                print(f"{i+1}. {t}\n")
    
    elif pilihan == 3:
        print("\nHapus Tugas")
        nomor = int(input("Hapus tugas berdasarkan nomor: "))
        if 1 <= nomor <= len(tugas):
            tugas_terhapus = tugas.pop(nomor-1)
            print(f"Tugas {tugas_terhapus} berhasil dihapus\n")
        else:
            print("Nomor Tugas tidak valid\n")
    
    elif pilihan == 4:
        print("Terima kasih sudah menggunakan aplikasi to-do list")
        break
    
    else:
        print("Pilihan tidak valid\n")
