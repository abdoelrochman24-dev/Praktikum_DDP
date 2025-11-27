# Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
# nilai (80) #lulus
# nilai(60) #gagal

def keterangan_nilai(ipk):
    if ipk >= 80:
        return "Lulus"
    else:
        return "Tidak Lulus"
    
print(keterangan_nilai(80))
print(keterangan_nilai(60)) 
