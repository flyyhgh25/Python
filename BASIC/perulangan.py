def PerulanganWhile():
    nama=''
    awal= 0
    a='python'
    while(awal,nama!=a):
        nama = input("Masukkan nama : ")
        if(nama==a):
            print ("goodbye python")
            break
        print("Nama saya ", nama)
    awal+=1

    banyak_pasien = int(input("Masukkan banyaknya pasien : "))
    pasien = 0
    while(pasien<=banyak_pasien):
        nama_pasien = input("Masukkan nama pasien : ")
        if(nama_pasien == 'ronald'):
            pass
            print("pasien belum datang")
        pasien+=1
    print("\n")

def PerulanganFor():
    for i in range(0,1000):
        nama = input("Masukkan nama : ")
        if(nama=='a'):
            print("goodbye python")
            break
        print("Nama saya ", nama)

    banyak_pasien = int(input("Masukkan banyaknya pasien : "))
    pasien = 0
    for x in range(pasien,banyak_pasien):
        nama_pasien = input("Masukkan nama pasien : ")
        if(nama_pasien == 'ronald'):
            print("Pasien",nama_pasien,"belum datang")
            continue
        print('Pasien', nama_pasien,' sudah datang')
    
    # random
    print("\N{Sauropod}"*10)
    dinosaur = "\N{T-Rex}"*7
    greening = "\N{Grinning Face}"*3
    gerrening_stars = "\N{Grinning Face with Star Eyes}"*3
    for x in dinosaur:
        print(f"{x}  {greening}{gerrening_stars}  {x}")
    print("\N{Sauropod}"*10)



   
    


# kata = "python"
# awal = 0
# nama=''
# while(awal,nama!=kata):
#     nama = input("Silahkan masukkan nama : ")
#     if(nama == "python"):
#         print("goodbye python")
#         break
#     print("Nama saya ", nama)
#     awal+=1

