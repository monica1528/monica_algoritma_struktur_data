def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    total_gaji = 0
    for _ in range(hari_kerja):
        if jam_kerja_per_hari > 8:
            lembur = jam_kerja_per_hari - 8
            total_gaji += (8 * tarif_per_jam) + (lembur * tarif_per_jam * 1.5)
        else:
            total_gaji += jam_kerja_per_hari * tarif_per_jam
    return total_gaji
jam_kerja_minimal = int(input("Masukkan jam kerja minimal:"))
tarif = float(input("Masukkan tarif per jam: "))
jam_kerja = int(input("Masukkan jam kerja per hari: "))
hari = int(input("Masukkan jumlah hari kerja: "))

gaji_bulanan = hitung_gaji(tarif, jam_kerja, hari)
print(f"Total gaji bulanan: Rp {gaji_bulanan:.2f}")