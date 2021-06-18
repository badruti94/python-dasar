print("Kalkulator Sederhana!!!\n\n")


ang1 = input("Masukan angka 1 : ")
ang2 = input("Masukan angka 2 : ")
print('')
print("Operator : 1 tambah. 2 ambil. 3 bagi. 4 kali")
op = input("Pilih operator : ")


hasil = 0
if op == 1:
    hasil = ang1 + ang2
elif op == 2:
    hasil = ang1 - ang2
elif op == 3:
    hasil = ang1 / ang2
else:
    hasil = ang1 * ang2

print("Hasil : " + str(hasil))