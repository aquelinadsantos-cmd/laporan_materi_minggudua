

# input dari pengguna
gaji = float(input("Masukkan gaji per jam (Rp): "))  # meminta pengguna untuk input Gaji per jam
jam = float(input("Masukkan jam kerja per minggu: "))  # untuk input Jam kerja per minggu

# Hitung total pendapatan sebelum pajak 14%
total = gaji * jam * 5  # 5 minggu liburan
print("Pendapatan sebelum pajak:", total)

# Hitung pajak 14%
pajak = total * (14 /100)  
total_setelah_pajak = total - pajak
print("Pendapatan setelah pajak:", total_setelah_pajak)

#  Hitung belanja baju dan aksesoris 10%
baju = total_setelah_pajak * (10/100)
print("Uang beli baju & aksesoris:", baju)

# Hitung belanja alat tulis 1%
alat = total_setelah_pajak * (1/100)
print("Uang beli alat tulis:", alat)

#  Hitung sisa uang setelah belanja
sisa = total_setelah_pajak - baju - alat
print("Sisa uang setelah belanja:", sisa)

#  Hitung sedekah 25%
sedekah = sisa * (25/100)
print("Uang yang disedekahkan:", sedekah)

#  Bagi sedekah 30% untuk anak yatim dan 70% untuk dhuafa
sedekah_anak_yatim = sedekah * (30/100)
sedekah_dhufan = sedekah * (70/100)
print("Uang untuk anak yatim:",  sedekah_anak_yatim)
print("Uang untuk kaum dhuafa:", sedekah_dhufan)
