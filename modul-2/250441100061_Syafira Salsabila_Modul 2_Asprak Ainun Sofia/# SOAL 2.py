# SOAL 2
#  Program menghitung harga tiket bioskop 

# Input data
usia = int(input("Masukkan usia:"))
pelajar = input("Apakah kamu pelajar SMA dengan kartu pelajar? (ya/tidak):").lower()
hari = input("Hari apa sekarang?").lower()

# Harga tiket normal
harga_normal = 50000
diskon = 0

# Cek kondisi diskon
if usia < 12:
    diskon = 50
elif pelajar == "ya":
    diskon = 30
elif hari == "selasa":
    diskon = 20
else:
    diskon = 0

# Hitung harga akhir
harga_akhir = harga_normal - (harga_normal * diskon/100) 

# Tampilkan hasil
print("Hasil Perhitungan")
print("Usia:", usia)
print("Pelajar:", pelajar)
print("Hari:", hari)
print("Diskon:", diskon, "%")
print("Harga yang harus dibayarkan:Rp", int(harga_akhir))
