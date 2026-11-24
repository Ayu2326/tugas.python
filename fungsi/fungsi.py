def sapa(nama):
    """
    Fungsi ini menyapa nama yang diberikan.
    """
    print(f"Halo, {nama}!")
    
# Memanggil fungsi
sapa("Andi")
sapa("Siti")

def tambah(angka1, angka2):
    """
    Fungsi ini mengembalikan jumlah dari dua angka.
    """
    return angka1 + angka2

# Memanggil fungsi dan menyimpan hasilnya
hasil_penjumlahan = tambah(10, 5)
print(f"Hasil penjumlahan: {hasil_penjumlahan}")