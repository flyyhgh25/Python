def option():
    print()
    print(f"{'Pilihan':^125}")
    menu = ['Tulis Biodata\t','Tampil Biodata\t','Keluar\t\t']
    print(f"{'':<50}{'':=^24}")
    for no,data in enumerate(menu,1):
        print(f"{'':<50}||{no}. {data}||")
    print(f"{'':<50}{'':=^24}")
    pilihan = int(input("Masukkan pilihan :"))
    return pilihan

def identitas(Nama, TTL, Alamat, email, no_HP):
    with open('C:/Users/My Laptop/Documents/Programming/ISI/PYTHON BASIC/Learn/Kuliah/functio/biodata.txt',"a") as biodata:
        biodata.write(f"Nama \t\t\t:{Nama}\nTempat,Tanggal Lahir \t:{TTL}\nAlamat\t\t\t:{Alamat}\nEmail\t\t\t:{email}\nNo HP\t\t\t:{no_HP}\n")

def pendidikan():
    Universitas = input("Masukkan Universitas \t: ")
    Fakultas = input("Masukkan Fakultas \t: ")
    Program_Studi = input("Masukkan Program Studi \t: ")
    NIM = input("Masukkan NIM \t\t: ")
    with open('C:/Users/My Laptop/Documents/Programming/ISI/PYTHON BASIC/Learn/Kuliah/functio/biodata.txt',"a") as biodata:
        biodata.write(f"Universitas\t\t:{Universitas}\nFakultas\t\t:{Fakultas}\nProgram Studi\t\t:{Program_Studi}\nNIM\t\t\t:{NIM}\n{'':_<100}\n")

def Menu():
    pilihan = int()
    while(pilihan<3):
        pilihan=option()
        if(pilihan==3):
            print("{:^40}".format("**Terimakasih telah menggunakan program kami**"))
            break
        else:
            if(pilihan==1):
                print(f"{'':=^100}")
                print(f"{'Memasukkan Data Identitas':>60}")
                print(f"{'':=^100}")
                nama = input("Masukkan nama\t\t: ")
                TTL = input("Masukkan TTL\t\t: ")
                Alamat = input("Masukkan Alamat\t\t: ")
                email = input("Masukkan Email\t\t: ")
                no_HP = input("Masukkan No HP\t\t: ")
                identitas(nama,TTL,Alamat,email,no_HP)
                print(f"{'':=^100}")
                print(f"{'Memasukkan Data Pendidikan':>60}")
                print(f"{'':=^100}")
                pendidikan()
            elif(pilihan==2):
                with open('C:/Users/My Laptop/Documents/Programming/ISI/PYTHON BASIC/Learn/Kuliah/functio/biodata.txt',"r") as biodata:
                    baca = biodata.read()
                    print(baca)
            else:
                print("Maaf salah menu")
                

Menu()