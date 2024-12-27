def cetak_pola(baris):
    for i in range(1, baris + 1):
        print("*" * i)

# Input jumlah baris
jumlah_baris = int(input("Masukkan jumlah baris: "))
cetak_pola(jumlah_baris)