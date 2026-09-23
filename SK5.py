#function untuk menghitung biaya pemesanan hotel
#parameter jenis kamar dan durasi menginap
#percabangan untuk menentukan tarif kamar
def hitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar == "standard":
        tarif = 200000
    elif jenis_kamar == "deluxe":
        tarif = 350000
    else:
        return 0
#Hitung total biaya berdasarkan jumlah malam menginap
#return untuk mengembalikan total biaya pemesanan
    total_biaya = tarif * lama_menginap
    return total_biaya

#Panggil function dengan data jenis kamar dan lama menginap yang diperoleh dari tanggal check-in dan check-out
def tampilkan_pesanan(jenis_kamar, check_in, check_out, lama_menginap):
    total_biaya = hitung_biaya(jenis_kamar, lama_menginap)

    if total_biaya == 0:
        print("jenis kamar tidak tersedia.")
    else:
        print("PEMESANAN HOTEL")
        print("jenis kamar       :", jenis_kamar)
        print("tanggal check-in  :", check_in)
        print("tanggal check-out :", check_out)
        print("lama menginap     :", lama_menginap, "malam")
        print("total biaya       : Rp", total_biaya)

#Tampilkan jenis kamar, tanggal check-in dan check-out, lama menginap, dan total biaya pemesanan hotel.
jenis_kamar = input("masukkan jenis kamar (standard/deluxe): ")
check_in = input("masukkan tanggal check-in: ")
check_out = input("masukkan tanggal check-out: ")
lama_menginap = int(input("masukkan lama menginap (malam): "))

tampilkan_pesanan(jenis_kamar, check_in, check_out, lama_menginap)