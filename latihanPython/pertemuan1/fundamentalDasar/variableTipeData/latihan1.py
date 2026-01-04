# belajar variable dan mencetak tipe data nya
x = 4
y = x + 4
print (y)
print(f"Nilai y adalah: {y}, dan tipe datanya adalah {type(y)}")

# latihan menjumlahkan dua bilangan yang di input
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
hasil = bilangan1 + bilangan2
print (f"hasil dari {bilangan1} + {bilangan2} adalah {hasil}, kemudian tipe datanya adalah {type(hasil)}")

# latihan tipe data
data_string = "Hello world" # tipe data string
print ("Data: ", data_string)
print ("Tipe data: ", type(data_string))

data_integer = 100 # tipe data integer
print ("Data: ", data_integer)
print ("Tipe data: ", type(data_integer))

data_float = 10.0 # tipe data float
print ("Data: ", data_float)
print ("Tipe data: ", type(data_float))

data_boolean = True # tipe data boolean
print ("Data: ", data_boolean)
print ("Tipe data: ", type(data_boolean))