from datetime import datetime
import json
garis_batas = "{:=^73}".format('')
garis_batas2 = f"{'':=^65}" 
# Data Buku
data_buku = {
    'id_buku':(1234,567,890,7655),
    'buku':['Laskar Pelangi','Sang Pemimpi','Bulan','Bintang'],
    'penulis':['Andrea Hirata','Andrea Hirata','Tere Liye','Tere Liye']
}
# Data User terdaftar
data_user = {
    'id':[1,2,3,4,5],
    'nama':['Laras','Siska','Avi','Kento','Ahmad'],
    'alamat':{
        'negara':('Indonesia','Korea','Switzerland','Jepang','Mesir'),
        'provinsi':('Jawa tengah','Soul','Bern','Tokyo','kairo')
    },
    'role':['admin','operator','operator','operator']
}
# Data buku yang dipinjam
nama_peminjam = []
daftar_pinjaman = []
tanggal_pinjam = []
nb = []
pb = []
data = {
'nama_peminjam':nama_peminjam,
'daftar_pi':daftar_pinjaman,
'tanggal_pi':tanggal_pinjam,
'nama_buku': nb,
'penulis': pb,
}

def opsiWriteRead(path,mode,data_yang_ditambah):
    with open(f'{path}',f'{mode}') as data_file:
        json.dump(data_yang_ditambah,data_file)

def pendahuluan():
    print("{:=^98}".format(''))
    print("|{0:^96}|".format("Meminjam dan Mengembalikan Buku"))
    print("{:=^98}".format(''))
    print()

# Menampilkan semua data User yang telah terdaftar
def pemilik(data):
        print("{:^100}".format("User yang Terdaftar"))
        print(f"{'':=^97}")
        for index in data.keys():
            print('|',f"{index:^24}", end="\t")
        print('|')
        print(f"{'':=^97}")
        for x in range(len(data['id'])):     
            print(f"|{data['id'][x]:^24}\t|{data['nama'][x]:^24}\t|{data['alamat']['provinsi'][x]:<12}|{data['alamat']['negara'][x]:>18}|")
        print(f"{'':=^97}")
        opsiWriteRead('C:/Users/My Laptop/Documents/Programming/ISI/PYTHON BASIC/Program/user.json','w',data)
        print()

# Menampilkan semua data Buku yang terdaftar
def buku(data):  
        print("{:^100}".format("Daftar Buku"))
        print(f"{'':^5}{'':=^77}")
        for index in data.keys():
            print(f"{'':<5}|{index:^20}", end=" ") 
        print('|')
        print(f"{'':^5}{'':=^77}")
        for x in range(len(data['id_buku'])):      
            print(f"{'':<5}|{data['id_buku'][x]:^26}|{data['buku'][x]:^26}|{data['penulis'][x]:^21}|")
        print(f"{'':^5}{'':=^77}")
        opsiWriteRead('C:/Users/My Laptop/Documents/Programming/ISI/PYTHON BASIC/Program/buku.json','w',data_buku)
        print()

# Menampilkan peraturan peminjaman dan pengembalian buku
def peraturan():
    rule = ['Hanya Boleh meminjam maksimal 3 buku', 'Lama maksimal meminjam adalah 1 minggu', 'Jika waktu peminjaman melebihi batas maka :']
    denda = ['Terlambat pada minggu pertama  = Rp.5000','Terlambat pada minggu kedua  = Rp.7000', 'Terlambat pada minggu ketiga = Rp.9000', 'Terlambat pada minggu ke empat = Rp.11.000']      
    print("Rule : ")
    for a, b in enumerate(rule,1):
        print(f"\t{a}.{b}")
    print("\t\t{:_^51}".format(''))
    print("\t\t|\{:_^47}/|".format(''))
    for x, y in enumerate(denda,1):
        print(f"\t\t| |{x}.{y}\t| |")
    print("\t\t\{:_^49}/".format(''))
    print()
    print(f"\tNote : Terlambat lebih dari satu bulan, maka tidak boleh meminjam buku selama waktu waktu yang ditentukan")

# Peminjaman buku 
def pinjam():
        print()
        print("{:=^98}".format(''))
        print("|{0:^96}|".format("Meminjam Buku"))
        print("{:=^98}".format(''))
        nama_p = input("Masukkan Nama Peminjam\t\t\t: ")
        file_json = open('C:/Users/My Laptop/Documents/Programming/ISI/PYTHON BASIC/Program/data_pinjalllllm.json')
        parsing_data = json.loads(file_json.read())
        if(nama_p in data_user['nama']):
            if(len(parsing_data['nama_peminjam'])<2):
                nama_peminjam.append(nama_p)    
            if(nama_p in parsing_data['nama_peminjam'] or len(parsing_data['nama_peminjam'])<1):
                a=1
                jumlah_pinjam = int(input("Masukkan jumlah buku yang ingin dipinjam: "))
                if(jumlah_pinjam<=3):
                    jumlah_pinjam+=1   
                    while(a<jumlah_pinjam):
                        meminjam = int(input("Masukkan id buku yang ingin dipinjam \t: "))
                        if meminjam in data_buku['id_buku']:
                            index_buku = data_buku['id_buku'].index(meminjam)
                            nama_buku = data_buku['buku'][index_buku]
                            penulis_buku = data_buku['penulis'][index_buku]
                            daftar_pinjaman.append(meminjam)
                            nb.append(nama_buku)
                            pb.append(penulis_buku)
                            tanggal = datetime.today()
                            t_pinjam = tanggal.strftime('%d-%m-%Y')
                            tanggal_pinjam.append(t_pinjam)
                            opsiWriteRead('C:/Users/My Laptop/Documents/Programming/ISI/PYTHON BASIC/Program/data_pinjam.json','w',data)
                            print()
                            deskripsi()
                        else:
                            print()
                            print("{0:^64}".format("**Maaf Data tidak tersedia**"))
                        if(a == 4): 
                            print("{0:^64}".format("**Maaf Maksimal meminjam buku hanya 3 buah buku**"))
                            break
                        a+=1  
                else:
                    print("{0:^64}".format("**Maaf Maksimal meminjam buku hanya 3 buah buku **"))
            else:
                    print("{0:^64}".format("**Maaf Ada kesalahan user yang meminjam. Coba cek ulang lagi **"))
        else:
            print("{0:^64}".format("**Maaf Anda belum punya akun**"))
        print()

# pengembalian buku
def kembali():
        print()
        print("{:=^98}".format(''))
        print("|{0:^96}|".format("Mengembalikan Buku"))
        print("{:=^98}".format(''))
        nama_p = input("Masukkan Nama Peminjam \t : ")
        file_json = open('C:/Users/My Laptop/Documents/Programming/ISI/PYTHON BASIC/Program/data_pinjam.json')
        parsing_data = json.loads(file_json.read())
        if(nama_p in parsing_data["nama_peminjam"]):
            deskripsi()
            jml_buku_pinjam = len(parsing_data['daftar_pi'])
            if(jml_buku_pinjam>=1):
                for x in parsing_data["nama_peminjam"]:
                    print(f"{x} meminjam buku sebanyak {jml_buku_pinjam} buah buku")  
                jml_kembali = int(input("Masukkan jumlah buku yang ingin dikembalikan : "))
                if(jml_kembali>jml_buku_pinjam):
                    print(f"Maaf Anda hanya meminjam {jml_buku_pinjam} buah buku")
                else:
                    x=1
                    while(x<=jml_kembali):
                        id_buku = int(input("Masukkan ID buku pinjaman : "))
                        if id_buku in parsing_data['daftar_pi']:
                            index = parsing_data['daftar_pi'].index(id_buku)
                            print(garis_batas2)
                            print(f"|{'ID Buku':^15}|{'Tanggal Pinjam':^15}|{'Nama Buku':^15}|{'Penulis':^15}|")     
                            print(garis_batas2)
                            print(f"|{parsing_data['daftar_pi'][index]:^15}|{parsing_data['tanggal_pi'][index]:^15}|{parsing_data['nama_buku'][index]:^15}|{parsing_data['penulis'][index]:^15}|")     
                            print(garis_batas2)
                            tanggal_pinjaman = parsing_data['tanggal_pi'][index]
                            tanggal_k = input("Masukkan tanggal kembali (d-m-Y): ")
                            format_t = "%d-%m-%Y"
                            print("Tanggal meminjam : ", tanggal_pinjaman)
                            tdelta = datetime.strptime(tanggal_k,format_t) - datetime.strptime(tanggal_pinjaman,format_t)
                            jml_hari = tdelta.days
                            print("Jumlah waktu meminjam : ",jml_hari,"hari")
                            denda_awal = 0
                            total_denda = 0
                            if(jml_hari>=7):
                                denda_akhir1 = denda_awal + 5000
                                total_denda = denda_akhir1
                                if(jml_hari>=14):
                                    denda_akhir2 = denda_akhir1 + 2000
                                    total_denda = denda_akhir2
                                    if(jml_hari>=21):
                                        denda_akhir3 = denda_akhir2 + 2000
                                        total_denda = denda_akhir3
                                        if(jml_hari>=30):
                                            denda_akhir4 = denda_akhir3 +2000
                                            total_denda = denda_akhir4
                                            hari_tp = jml_hari-30
                                            print(f"Maaf Anda terlambat mengembalikan buku selama lebih dari 30 hari. Anda tidak boleh meminjam buku selama {hari_tp} hari")             
                                print(f"Maaf Anda terlambat mengembalikan buku,Anda akan dikenakan denda sebesar Rp.{total_denda} ")
                            else:
                                print("{0:^64}".format("==Terimakasih telah mengembalikan buku dengan tepat waktu=="))

                            del parsing_data['daftar_pi'][index]
                            del parsing_data['tanggal_pi'][index]
                            del parsing_data['nama_buku'][index]
                            del parsing_data['penulis'][index]

                            opsiWriteRead('C:/Users/My Laptop/Documents/Programming/ISI/PYTHON BASIC/Program/data_pinjam.json','w',parsing_data)
                            if(len(parsing_data['penulis'])<1):
                                del parsing_data['nama_peminjam'][0]
                            opsiWriteRead('C:/Users/My Laptop/Documents/Programming/ISI/PYTHON BASIC/Program/data_pinjam.json','w',parsing_data)

                        else:
                            print("{0:_^64}".format("Maaf Anda belum pernah meminjam buku itu"))
                        x+=1
                    print()
        else:
            print("{0:^64}".format("**Maaf Anda belum meminjam buku**"))
    
# deskripsi buku apa saja yang sedang dipinjam
def deskripsi():
        file_json = open('C:/Users/My Laptop/Documents/Programming/ISI/PYTHON BASIC/Program/data_pinjam.json')
        parsing_data = json.loads(file_json.read())
        print("{:^50}".format("Deskripsi Buku"))
        print(garis_batas2)
        print(f"|{'Daftar Pinjam':^15}|{'Tanggal Pinjam':^15}|{'Nama Buku':^15}|{'Penulis':^15}", end='')
        print('|')
        print(garis_batas2)
        for x in range(len(parsing_data['daftar_pi'])):
            print(f"|{parsing_data['daftar_pi'][x]:^15}|{parsing_data['tanggal_pi'][x]:^15}|{parsing_data['nama_buku'][x]:^15}|{parsing_data['penulis'][x]:^15}|")     
        print(garis_batas2)

# fungsi Main Menampilkan semua menu pilihan
def lihatDaftar():
    pendahuluan()
    pemilik(data_user)
    buku(data_buku)
    peraturan()

def MenuUtama():
    try: 
        print()
        print()
        pilihan=int()
        while(pilihan<4):   
            print("{:^120}".format("Menu"))
            menu = ['Lihat Daftar\t','Meminjam Buku','Mengembalikan Buku','Keluar\t']
            print(f"{'':^47}{'':_^26}")
            a='|'
            for x,y in enumerate(menu,1):
                print(f"{a:>48} {x}){y}\t|")
            print(f"{'':^47}{'':=^26}")
            pil=int(input("Masukkan pilahan : "))
            pilihan=pil
            if(pil==4):
                print("{0:^64}".format("==Terimakasih telah menggunakan program kami=="))
                break
            else:
                if(pil==1):
                    lihatDaftar()
                    print(f"{'':=^150}")
                elif(pil==2):
                    pinjam()
                    print(f"{'':=^150}")
                elif(pil==3):
                    kembali()
                    print(f"{'':=^150}")
                else:
                    print("{0:^64}".format("**Salah pilih menu**"))
                    break
    except TypeError:
         print("{0:^64}".format("**Maaf Anda kesalahan type nya **"))
    except ValueError:
        print("{0:^64}".format("**Maaf Anda harus menginputkan angka **"))
    except KeyError:
         print("{0:^64}".format("**Maaf ada kesalahan pada key nya **"))
    except IndexError:
        print("{0:^64}".format("**Maaf Index data User ada yang melebihi batas/tidak sesuai **"))
    except FileNotFoundError:
        print("{0:^64}".format("**Maaf file penyimpanan tidak ada **"))


MenuUtama()