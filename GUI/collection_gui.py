import tkinter as tk
from tkinter import *
main = tk.Tk()
main.title('HERO')
main.geometry("500x500")
isi = Frame(main).pack(side=RIGHT)
header = Frame(main).pack()
listHero = []
class Hero(object):
    def __init__(self, nama=None, alias=None, kelompok=None):
        self.nama = nama
        self.alias = alias
        self.kelompok = kelompok    

    def Awal(self):
        tk.Label()
        tk.Label(header,text='Daftar HERO',bg="blue",pady=4,padx=4,fg="white",font="60").pack(fill=X,side=TOP)
        tk.Label(isi,text='Apakah ingin menambahkan Hero?',width="50",font="50").pack(pady=10)
        self.bt_ok = tk.Button(isi, width="10", bg="grey", text='YES',padx=10,font="50", justify=tk.RIGHT,command=self.inputSatu)
        self.bt_ok.pack(side=tk.RIGHT, fill='both',pady=50)
        self.bt_no = tk.Button(isi, width="10", bg="grey", text='No',padx=10,font="50", justify=tk.LEFT,command=main.destroy)
        self.bt_no.pack(side=tk.LEFT, fill='both',pady=50)
    
    def inputSatu(self):
        tk.Label(isi,text=f' Menambahkan Hero Baru ',bg="brown", width="50",fg="white",font="40").pack(pady=8)
        tk.Label(isi,text=f'Masukkan Nama Hero',width="50",pady=5,padx=10).pack()
        self.nama = tk.Entry(isi,bg="grey",cursor="arrow",width="20")
        self.nama.pack()
        tk.Label(isi,text=f'Masukkan Alias Hero',width="50",pady=5,padx=10).pack()
        self.alias = tk.Entry(isi,bg="grey",cursor="arrow",width="20")
        self.alias.pack()
        tk.Label(isi,text=f'Masukkan Kelompok Hero',width="50",pady=5,padx=10).pack()
        self.kelompok = tk.Entry(isi,bg="grey",cursor="arrow",width="20")
        self.kelompok.pack()
        def SimpanData():
            listHero.append(Hero(self.nama.get(),self.alias.get(),self.kelompok.get()))
            print(listHero)
            self.bt_submit.after(100, self.bt_submit.destroy)
        self.bt_submit = tk.Button(isi, width="40", state=NORMAL, bg="black",fg="white", text='Simpan',command=SimpanData)
        self.bt_submit.pack(pady=20)
       
    def MenampilkanData(self):
        tk.Label(header,text='Daftar LIST HERO',bg="blue",pady=8,padx=7,fg="white",font="70").pack(fill=X,side=TOP)
        tk.Label(header,text=f'Hero Pertama {listHero[0].nama} ',bg="green",pady=5,padx=5,fg="white",font="70").pack(fill=X,side=TOP,padx=50,pady=10)
        for k in listHero:
            tk.Label(isi,text=f'Nama: {k.nama}\nAlias: {k.alias}\nKelompok: {k.kelompok}\n',width="50",bg="purple", fg="white").pack(fill="both",side=TOP,padx=30,pady=15)
       
k = Hero('','','')
k.Awal()
main.mainloop()
k.MenampilkanData()
main.mainloop()


   



