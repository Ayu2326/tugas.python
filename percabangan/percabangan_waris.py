#Studi Kasus - Hukum Waris Sederhana
#Sebuah keluarga meninggalkan warisan sebesar Rp 120.000.000

#Aturan Hukum Waris Sederhana
#1. Jika Ahli Waris adalah anak laki - laki, mendapat 2 bagian
#2. Jika Ahli Waris adalah anak perempuan, mendapat 1 bagian
#3. Program meminta jumlah anak laki - laki dan jumlah anak perempuan 
#4. Program menghitung bagian masing - masing ahli waris

print("===Program Pembagian Waris Sederhana===")
warisan = int(input("Masukkan Jumlah Harta Warisan : Rp "))
lk = int(input("Jumlah anak laki - laki : "))
pr = int(input("Jumlah anak perempuan : "))

#menghitung jumlah bagian
bagian_lk = lk*2
bagian_pr = pr*1
total_bagian = bagian_lk + bagian_pr

#percabangan waris
if total_bagian > 0:
    nilai_bagian = warisan / total_bagian
    
print("\n=== HASIL PEMBAGIAN")
if lk > 0:
    print("Setiap anak laki - laki mendapat Rp",int(nilai_bagian*2))
    
if pr > 0:
    print("Setiap anak perempuan mendapat Rp",int(nilai_bagian))

else:
    print("tidak ada ahli waris")