data = {
        'barang': ['Buku','Pensil','Penghapus','Spidol','Tinta'],
        'harga': (30_000,2000,1000,2500,5000),
        'stok': [20, 10, 60, 70, 90]
}
# 1) Menambahkan barang Buku Gambar, stok nya 100 harga persatuanya 2000
print("{:=^100}".format('Menambahkan barang'))
barang = input("Masukkan Nama barang yang akan di tambahkan \t: ")
harga = int(input("Masukkan harga barang \t\t\t\t:"))
stok = int(input("Masukkan stok barang \t\t\t\t: "))
data['barang'].append(barang)
data['harga']+=(harga,)
data['stok'].append(stok)
# 2)Menampilkan barang
print("{:=^100}".format('Menampilkan barang'))
print()
print("{:-^49}".format(''))
for x in data.keys():
        print("|"f"{x:^15}", end='')
print('|')
print("{:-^49}".format(''))
for y in range (len(data['barang'])):
        print(f"|{data['barang'][y]:<15}| Rp.{data['harga'][y]}\t|{data['stok'][y]:^15}|")
print("{:-^49}".format(''))

#3) Mengubah tipe data stok menjadi set
print("{:=^100}".format('Mengubah tipe data stok menjadi set'))
set = set(data['stok'])
print("Stok dalam bentuk set : ",set)
#4) Mengambil barang dengan stok terbanyak
print("{:=^100}".format('Barang dengan stok terbanyak'))
stok_tertinggi = max(set)
indexnya = data['stok'].index(stok_tertinggi)
print(f"{data['barang'][indexnya]} memiliki stok {stok_tertinggi}")
#5) mengambil harga paling mahal
print("{:=^100}".format('Barang dengan harga termahal'))
harga_tertinggi = max(data['harga'])
indexx = data['harga'].index(harga_tertinggi)
print(f"{data['barang'][indexx]} memiliki harga Rp.{harga_tertinggi}")
#6)mensorting / mengurutkan data
print("{:=^100}".format('Mengurutkan Data'))
sort_barang = sorted(data['barang'])
sort_stok = sorted(data['stok'])
sort_harga = sorted(data['harga'])
print("Barang setelah di urutkan : ")
for a,b in enumerate(sort_barang,1):
        print(f"\t\t{a}.{b}")
print("Harga setelah di urutkan : ")
for e,f in enumerate(sort_harga,1):
        print(f"\t\t{e}.{f}")
print("Stok setelah di urutkan : ")
for c,d in enumerate(sort_stok,1):
        print(f"\t\t{c}.{d}")
#7) mengecek barang apakah ada datanya tidak 
print("{:=^100}".format('Mengurangi stok barang'))
barang = input("Masukkan Nama barang yang telah terjual : ")
if barang in data['barang']:
        index_b = data['barang'].index(barang)
        barang_terjual = int(input("Masukkan jumlah barangnya \t: "))
        #8) mengupdate stok barang
        jml_akhir = data['stok'][index_b]-barang_terjual
        data['stok'][index_b]= jml_akhir
        print("{:=^49}".format('Menampilkan barang Setalah di perbarui'))
        print()
        print("{:-^49}".format(''))
        for x in data.keys():
                print("|"f"{x:^15}", end='')
        print('|')
        print("{:-^49}".format(''))
        for y in range (len(data['barang'])):
                print(f"|{data['barang'][y]:<15}| Rp.{data['harga'][y]}\t|{data['stok'][y]:^15}|")
        print("{:-^49}".format(''))
        print()
        print()
        #9) mengecek apakah stok barang yang telah terjual kurang dari nol tidak
         #menghapus barang jika stoknya kurang dari 0 
        if(data['stok'][index_b]<=0):
                data['barang'].remove(barang)
                list_harga = list(data['harga'])
                list_harga.remove(data['harga'][index_b])
                data['harga'] = list_harga
                stok_ko = data['stok'][index_b]
                data['stok'].remove(stok_ko)
        print("{:=^100}".format('Menampilkan Data Akhir'))
        print("{:-^49}".format(''))
        for x in data.keys():
                print("|"f"{x:^15}", end='')
        print('|')
        print("{:-^49}".format(''))
        for y in range (len(data['barang'])):
                print(f"|{data['barang'][y]:<15}| Rp.{data['harga'][y]}\t|{data['stok'][y]:^15}|")
        print("{:-^49}".format(''))
else:
        print("Maaf, tidak ada barang dengan nama ", barang)





