#Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
# print(is_genap(4))  # Output: True
# print(is_genap(7))  # Output: False
 

def is_genap(bilangan_bulat):
    if bilangan_bulat % 2 == 0:
        return True
    else:
        return False
print(is_genap(4))  
print(is_genap(7))   