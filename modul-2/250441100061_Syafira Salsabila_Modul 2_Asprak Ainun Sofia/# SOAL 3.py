# SOAL 3
# Program menghitung biaya parkir mall

lama_parkir = int(input("Masukkan lama parkir (jam):"))
vip = input("Apakah Anda member VIP? (ya/tidak): ").lower()

if vip == "ya":
    total = 0
else:
    if lama_parkir <= 2:
        total = 5000
    else:
        total = 5000 + (lama_parkir - 2) * 3000
    if total > 20000:
        total = 20000

print("Hasil Perhitungan")
print("Lama parkir:", lama_parkir, "jam")
print("Status VIP:", vip)
print("Total biaya parkir: Rp", total)
