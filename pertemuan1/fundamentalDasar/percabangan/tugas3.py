# tugas3 deteksi service berdasarkan port

port = int(input("Masukkan port: "))
if port == 80:
    print("HTTP Service")
elif port == 22:
    print("SSH Service")
elif port == 443:
    print("HTTPS Service")
else:
    print("Service tidak dikenal")
    