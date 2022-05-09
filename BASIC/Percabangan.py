def ifNeseted():
    nilai_mtk = int(input("Masukkan nilai mtk : "))
    nilai_indo = int(input("Masukkan nilai indo : "))
    if(nilai_mtk<80):
        print("Nilai Matematika anda : ",nilai_mtk,"\n (dibawah KKM)")
        print("Anda harus mengikuti remidian MTK")
        if(nilai_indo<=75):
            print("Nilai B.Indo anda : ",nilai_indo,"\n (dibawah KKM)")
            print("Anda harus mengikuti remidian B.Indonesia")
            if(nilai_mtk or nilai_indo):
                print("Anda harus mengulang semuanya")
            else:
                print("Anda tidak ikut remidial mtk")
        else:
            print("Anda tidak ikut remidial indo")
    else:
        print("Selamat Anda tidak ikut remidial mtk dan Indo ")

    
     # if bersarang
    if((x%2) ==1):
        if(x>10):
            print("x diatas 10")
        elif(x==3):
            print('x adalah 3')
        else:
            print('x dibawah 10')

    x = int(input("Masukkan x: "))
    print(('Bilangan genap','Bilangan ganjil')[((x%2)==1)])

def PercabanganIFElse():
    angka1 = int(input("Masukkan angka pertama : "))
    angka2 = int(input("Masukan angka ke dua : "))

    # menghitung angka maksimal
    angka_max = max(angka1,angka2)
    print("Angka Maksimalnya : ",angka_max)
    # cara lain
    if(angka1>=angka2):
        angka_max = angka1
    else:
        angka_max = angka2
    # menghitung keliling lingkaran
    print("Opsi : \n 1.Masukkan angka 1 untuk menghitung keliling lingkaran \n 2.Masukkan angka 2 untuk menghitung luas lingkaran")
    pil = int(input("Masukkan angka pilihan : "))
    phi = 3.14
    if(pil==1):
        jari_jari = int(input("Masukkan jari-jarinya : "))
        keliling = 2*phi*jari_jari
        print("Kelilingnya yaitu : ", keliling)
    elif(pil==2):
        jari_jari = int(input("Masukkan jari-jarinya : "))
        luas = phi*jari_jari*jari_jari
        print("Luasnya yaitu : ", luas)
    else :
        print("Maaf pilihan tidak tersedia")
    
    if(float(x).is_integer())!=True:
        print('Bukan bilangan bulat')
    elif(x%2)==1:
        print("Bilangan Ganjil")
    else:
        print('Bilangan Genap')


def ifTunggal():
    # if tunggal
    x=3
    if(x%2)==1:
        print('Bilangan Ganjil')
    if(x==3):
        print('Angka 3')

    if(float(x).is_integer())!=True:         
        print('Bukan bilangan bulat')
    # else:
    #     print("Bilangan Bulat")
    elif(x%2)==1:
        print("Bilangan Ganjil")
    else:
        print("Bilangan Genap")
   
    # ternary if
    if x%2==1:   
        print('Bilangan Ganjil')
    else:
        print('Bilangan Genap')
    # ternary nya ada 3 cara (biasa, ternary, dan dictionary)
    x=3
    print("Bilangan Ganjil" if(x%2==1) else "Bilangan Genap")
    # menggunakan tuple
    print(("Bilangan genap","Bilangan ganjil")[((x%2)==1)])
    # menggunakan dictionary
    print({True:"Bilangan ganjil", False:"Bilangan genap"} [(x%2)==1])
    # menggunakan lambda  
    print((lambda:"Bilangan genap", lambda:"Bilangan ganjil")[(x%2)==1]())
    # if and or
    if((x%2)==1) and (x==3):
        print('x adalah bilangan ganjil')
    if((x%2)==1) or (x==3):
        print('x adlah bilangan ganjil')






            


    