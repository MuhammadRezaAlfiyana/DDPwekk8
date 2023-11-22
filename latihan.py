
#deklarasi 
def profile(nama, alamat, gender, umur, hobi):
    print("Nama saya Muhammad Reza ")
    print("alamat saya di Bogor")
    print("gender saya adlah laki laki")
    print("umur saya adalah 18 tahun")
    print("hobi saya berenang")
profile("muhammad Reza","Bogor","laki-laki","18","berenang")

#no 2
def tentukan_kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif 61 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"

# Contoh penggunaan:
nilai = 70
print(tentukan_kelulusan(nilai))

def cetak_bilangan_ganjil(batas):
    for nilai in range(1, batas + 1, 2):
        print(nilai)

# Contoh penggunaan:
batas_tertinggi = 300
cetak_bilangan_ganjil(batas_tertinggi)