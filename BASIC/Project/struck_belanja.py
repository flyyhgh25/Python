from datetime import datetime
data = {
        'barang': ['Buku','Pensil','Penghapus','Spidol','Tinta','Rautan','Bolpoin','Penggaris'],
        'harga': (30_000,2000,1000,2500,5000,2000,2000,5000),
    }
barang_t = []
jumlah = []
harga_tot = []
items = {
    'Nama Barang' : barang_t,
    'Harga' : harga_tot,
}
def garis_batas():
    a=''
    garis_batas = print("{:=^50}".format(a))
    return garis_batas

def namaToko():
    toko = [
        {
            "nama":"TOKO Alat Tulis",
            "alamat": "Wonosobo, Jawa Tengah",
            "no_telp": "(021) 023456 123",
        }
    ]

    for x in toko:
        print(f"{toko[0]['nama']:^50}\n {toko[0]['alamat']:^50}\n {toko[0]['no_telp']:^50}\n")

def keterangan():
    tanggal = datetime.today()
    format = '%d %B %Y %H:%M:%S'
    get_date = tanggal.strftime(format)
    print(f"Date\t : {get_date}\nGuest\t : - \nCashier\t : Default")

def belanja():
    print("Ket : Ketikkan stop jika sudah selesai")
    a=0
    barang=''
    while(a!=barang):
        barang_i = input("Masukkan barang :")
        if barang_i in data['barang']:
            barang_t.append(barang_i)
            jml = int(input("Masukkan jumlah : "))
            jumlah.append(jml)
            idx = data['barang'].index(barang_i)
            tot = data['harga'][idx] * jml
            # print(f"Total : {tot} ")
            harga_tot.append(tot)
            print(harga_tot)
        else:
            print(f"Maaf {barang_i} tidak tersedia")
        if(barang_i=="stop"):
            break
        a+=1

def hasil():
    for x in items.keys():
        print(f"{x}",end='\t\t')
    print('')
    for y in range(len(items['Nama Barang'])):
        print(f"{items['Nama Barang'][y]}\t\t\t {items['Jumlah'][y]} \t\t {items['Harga'][y]}")
    
    for x in items['Harga']:
        all_total  = x
        print(all_total)

belanja()

namaToko()
garis_batas()
keterangan()
garis_batas()
hasil()