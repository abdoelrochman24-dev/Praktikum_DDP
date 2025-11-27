angka_1 = float (input ("masukan angka 1: ")) 
angka_2 = float (input ("masuran angka 2: ")) 
operator = input ("pilih operator (+,-,*/, **):")

if operator == '+' : 
    hasil = angka_1 + angka_2
elif operator == '-':
    hasil = angka_1 - angka_2
elif operator == '*':
    hasil = angka_I * angka_2
elif operator == '/':
    hasil = angka_1 / angka_2
elif operator == '**':
    hasil = angka_1 ** angka_2
else :
    print ("Operator tidak valid")

print ("Angka Pertama:", angka_1)
print ("Angka Kedua:", angka_2)
print ("Operator:", operator)
print ("Hasil:", hasil)    


