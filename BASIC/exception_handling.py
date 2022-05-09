# try:
#     f = open('apa.txt','r')
# except FileNotFoundError:
#     print('File tidak ada')

# try:
#     input=int(input("Masukkan nomor :"))
# except ValueError:
#     print("Maaf anda harus menginputkan nomor")

# multiple
# try:
#     a=[0,1,2]
#     b= int(input("Masukkan nilai: "))
#     c= int(input("Masukkan index list: "))
#     d=a[c]+b
# except ValueError:
#     print("Masukkan bukan integer")
# except IndexError:
#     print("index yang anda masukkan tidak ada")

# raise
# try:
#     a=10*"lima"
#     raise NameError("error type")
# except NameError:
#     print("Tipe data Error")
#     raise

# # implementasi
# try:
#     a=10/0
# except ArithmeticError:
#     print("Operasi aritmatika yang salah")

# try:
#     dic = {"satu":1,"dua":2}
#     print(dic['tiga'])
# except KeyError:
#     print("Key dictionary tidak tersedia")

# Latihan=


def program():
    try:
        nama=[]
        jml_nama = int(input('Berapa jumlah nama yang akan dimasukkan : '))
        for x in range(jml_nama):
            print(f"Nama ke {x} :", end="")
            nam = input(" ")
            nama.append(nam)
        panggil_nama = int(input("Panggil nama dengan index ke : "))
        print(f'Nama pada index ke {panggil_nama} adalah {nama[panggil_nama]}')
    except ValueError:
        print('Inputan harus angka')
    except IndexError:
        print('Index data tersebut tidak ada')
# program()

import tkinter as tk

root = tk.Tk()
w=tk.Label(root,program())
w.pack()

root.mainloop()