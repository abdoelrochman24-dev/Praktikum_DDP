# Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
# print(celcius_ke_fahrenheit(0))    # Output: 32.0
# print(celcius_ke_fahrenheit(100))  # Output: 212.0


def celcius_ke_fahrenheit (celcius):
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))