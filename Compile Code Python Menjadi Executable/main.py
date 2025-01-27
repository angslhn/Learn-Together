print("-" * 15)
print(" KALKULATOR")
print(" 1. KALI")
print(" 2. BAGI")
print(" 3. TAMBAH")
print(" 4. KURANG")
print("-" * 15)
opsi = str(input(" PILIHAN = ")).upper()


if opsi == "1" or opsi == "KALI":
    print("-" * 23)
    angka_pertama = int(input(" ANGKA PERTAMA = "))
    angka_kedua = int(input(" ANGKA KEDUA   = "))
    print("-" * 23)
    
    keterangan = "Perkalian"
    hasil = angka_pertama * angka_kedua

    print("")
    print("-" * 55)  
    print(f"Hasilnya Dari {keterangan} Antara {angka_pertama} Dan {angka_kedua} Adalah {hasil}")
    print("-" * 55)
elif opsi == "2" or opsi == "BAGI":
    print("-" * 23)
    angka_pertama = int(input(" ANGKA PERTAMA = "))
    angka_kedua = int(input(" ANGKA KEDUA   = "))
    print("-" * 23)
    
    keterangan = "Pembagian"
    hasil = angka_pertama * angka_kedua
    
    print("")
    print("-" * 55)
    print(f"Hasilnya Dari {keterangan} Antara {angka_pertama} Dan {angka_kedua} Adalah {hasil}")
    print("-" * 55)
elif opsi == "3" or opsi == "TAMBAH":
    print("-" * 23)
    angka_pertama = int(input(" ANGKA PERTAMA = "))
    angka_kedua = int(input(" ANGKA KEDUA   = "))
    print("-" * 23)

    keterangan = "Pertambahan"
    hasil = angka_pertama * angka_kedua

    print("")
    print("-" * 55)    
    print(f"Hasilnya Dari {keterangan} Antara {angka_pertama} Dan {angka_kedua} Adalah {hasil}")
    print("-" * 55)
elif opsi == "4" or opsi == "KURANG":
    print("-" * 23)
    angka_pertama = int(input(" ANGKA PERTAMA = "))
    angka_kedua = int(input(" ANGKA KEDUA   = "))
    print("-" * 23)
    
    keterangan = "Pengurangan"
    hasil = angka_pertama * angka_kedua

    print("")
    print("-" * 55)   
    print(f"Hasilnya Dari {keterangan} Antara {angka_pertama} Dan {angka_kedua} Adalah {hasil}")
    print("-" * 55)
else:
    print("")
    print("-" * 39)
    print(" Pilihan Yang Anda Masukan Tidak Valid!")
    print("-" * 39)

input(" Klik Enter Untuk Keluar Program...")