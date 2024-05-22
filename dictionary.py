try:
    with open("keuangan.txt", "r") as file:
        data_keuangan = eval(file.read())
except FileNotFoundError:
    data_keuangan = {}

def tampilkan_data():
    print("Data Keuangan:")
    for tanggal, transaksi in data_keuangan.items():
        print(f"{tanggal}:")
        for keterangan, jumlah, tipe in transaksi:
            print(f"  - {keterangan}: Rp {jumlah:} ({tipe})")
        print()

def simpan_data():
    tanggal = input("Tanggal transaksi (dd-mm-yyyy): ")
    keterangan = input("Keterangan transaksi: ")
    jumlah = int(input("Jumlah uang: "))
    tipe = input("Tipe transaksi (pemasukan/pengeluaran): ")
    if tanggal not in data_keuangan:
        data_keuangan[tanggal] = []
    data_keuangan[tanggal].append((keterangan, jumlah, tipe))
    with open("keuangan.txt", "w") as file:
        file.write(str(data_keuangan))
    print("Data berhasil disimpan!")

def hapus_data():
    tanggal = input("Tanggal transaksi yang ingin dihapus (dd-mm-yyyy): ")
    if tanggal in data_keuangan:
        del data_keuangan[tanggal]
        with open("keuangan.txt", "w") as file:
            file.write(str(data_keuangan))
        print("Data berhasil dihapus!")
    else:
        print("Data tidak ditemukan!")

while True:
    print("Menu:")
    print("1. Tampilkan data keuangan")
    print("2. Simpan data keuangan")
    print("3. Hapus data keuangan")
    print("4. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        simpan_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid!")