def pil():
    opsi = ['Simpan biodata\t','Tampilkan semua biodata','Keluar program\t']
    a=f"{'':>20}"
    print(f"{a}{'':_>29}")
    print(f"{a}|{'Daftar Pilihan':^27}|")
    print(f"{a}{'':=>29}")
    for x,y in enumerate(opsi,1):
        print(f"{a}|{x}.{y}\t|")
    print(f"{a}{'':=>29}")
    pilihan = int(input("Masukkan pilihan : "))
    return pilihan

def simpanBiodata(nama,tanggal_lahir,asal):
    with open('C:/Users/My Laptop/Documents/Programming/ISI/PYTHON BASIC/Learn/Kuliah/functio/database.txt','a') as data:
        data.write(f"{'':_^35}\nNama\t\t:  {nama}\nTanggal Lahir\t:{tanggal_lahir}\nAsal Daerah\t:{asal}\n{'':_^35}\n")

def tampilBiodata():
    dataOpen = open('C:/Users/My Laptop/Documents/Programming/ISI/PYTHON BASIC/Learn/Kuliah/functio/database.txt','r')
    x = dataOpen.read()
    a=f"{'':>20}"
    print(f"{x}")
    dataOpen.close()

def Main():
    option=int()
    while(option<5):
        option=pil()
        if(option==3):
            print("Good bye.. Terimakasih telah menggunakan program kami..")
            break 
        else:
            if(option==1):
                nama = input("Masukkan nama \t\t: ")
                tanggal_lahir = input("Masukkan tanggal lahir  : ")
                asal = input("Masukkan asal\t\t: ")
                simpanBiodata(nama,tanggal_lahir,asal)
            elif(option==2):
                tampilBiodata()
            else:
                print("Maaf pilihan anda tidak masuk dalam daftar pilihan ")
                break
Main()