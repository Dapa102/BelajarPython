# tugas2 mengecek status port

port_status = input("Masukkan status port (open/closed): ")
if port_status == "open":
    print("Port dapat diakses")
elif port_status == "closed": 
    print("Port tidak dapat diakses")
else:
    print("Status tidak valid")