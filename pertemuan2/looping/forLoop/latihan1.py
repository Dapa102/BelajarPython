# membuat loop dari 1 sampai 10 tanpa range
angkaList = [1,2,3,4,5,6,7,8,9,10]

for i in angkaList:
    print(f"ini adalah angka ke - {i}")
print("selesai\n")

# membuat loop dari 1 sampai 10 menggunakan range
angka_range = range
for i in angka_range(1, 11):
    print(f"ini adalah loop yang menggunakan range, angka dimulai dari {i}")
print("selesai\n")

# Melakukan loop dengan cara di input
angka_input = int(input("Masukkan angka: "))

for i in range(1, angka_input + 1):
    print(f"Angka ke - {i}")
print("selesai\n")

# melakukan penjumlahan dengan loop
angka_penjumlahan = int(input("Masukkan bilangan: "))

total = 0
for i in range(1, angka_penjumlahan + 1):
    total += i
print(f"hasil penjumlahan adalah: {total}")
    

# Menampilkan angka dari 1 sampai 20, jika kelipatan 3 akan menampilkan "fizz"
for i in range(1, 21):
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)
print("selesai\n")

# Menampilkan nested loop pola
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()
print("selesai\n")

# Meminta input angka dan menentukan apakah bilangan prima atau bukan
angka = int(input("Masukkan angka: "))
is_prima = True

for i in range(2, angka):
    if angka % i == 0:
        is_prima = False
        break

if is_prima and angka > 1:
    print(f"{angka} adalah bilangan prima")
else:
    print(f"{angka} bukan bilangan prima")
    
# mencoba break
for i in range(1, 11):
    if i == 5:
        break
    print(f"Looping dimulai ke - {i}")
print("Looping selesai")