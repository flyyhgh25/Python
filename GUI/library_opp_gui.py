from datetime import datetime
import json 
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image  
from abc import ABC, abstractmethod
root = tk.Tk()
canvas = tk.Canvas(root, height=12000, width=12000)
canvas.pack(fill='both', expand = True)
root.title('Perpustakaan')
bgi = ImageTk.PhotoImage(Image.open("C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/2449381-249209863.png"))
label1 = Label(image=bgi,borderwidth=0)
label1.image = bgi
label1.place(relx=0, rely=0)
label2 = Label(image=bgi,borderwidth=0)
label2.image = bgi
label2.place(relx=0.5, y=0)
label3 = Label(image=bgi,borderwidth=0)
label3.image = bgi
label3.place(relx=0, rely=0.5)
label4 = Label(image=bgi,borderwidth=0)
label4.image = bgi
label4.place(relx=0.5, rely=0.5)

class Program(ABC):
    @abstractmethod
    def inputData():
        pass
    @abstractmethod
    def tampilData():
        pass
    @abstractmethod
    def editData():
        pass
    @abstractmethod
    def hapusData():
        pass
    @abstractmethod
    def PinjamBuku():
        pass
    @abstractmethod
    def Kembali():
        pass
  
  
class Buku(Program):
    def __init__(self):
        self.buku = []
        self.data_buku = {} 
    def inputData(self):
        main_frame = Frame(root,bd=10,bg=getattr(Auth,'wcolor'),relief='solid', padx=10,pady=10).place(relx=0.5, rely=0.22, relheight=0.7, relwidth=0.5, anchor='n')
        title = tk.Label(root,text="Menambah Buku", font=getattr(Auth,'fontsubtittle'),fg=getattr(Auth,'wcolor'), bg= getattr(Auth,'bcolor'), bd=0)
        title.place(relx=0.50,  relwidth=0.5,rely=0.15, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Kode", bg=getattr(Auth,'bcolor'),font=getattr(Auth,'font'), width=12).place(relx=0.4, rely=0.27, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Pengarang", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.35, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Penerbit", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.43, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="ISBN", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.51,  anchor='n') 
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Bahasa", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.59, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Bentuk Karya", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.67,  anchor='n') 
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Judul", bg=getattr(Auth,'bcolor'),font=getattr(Auth,'font'), width=12).place(relx=0.4, rely=0.75, anchor='n')
        self.k_buku = tk.IntVar()
        self.__kode = Entry(main_frame, textvariable = self.k_buku, font=getattr(Auth,'font'))
        self.__kode.place(relx=0.55, rely=0.27, anchor='n')
        setattr(Buku,'kode',self.__kode)
        self.pengarang = Entry(main_frame, font=getattr(Auth,'font'))
        self.pengarang.place(relx=0.55, rely=0.35, anchor='n')
        self.penerbit = Entry(main_frame, font=getattr(Auth,'font'))
        self.penerbit.place(relx=0.55, rely=0.43, anchor='n')
        self.isbn = Entry(main_frame, font=getattr(Auth,'font'))
        self.isbn.place(relx=0.55, rely=0.51, anchor='n')
        self.bahasa = Entry(main_frame, font=getattr(Auth,'font'))
        self.bahasa.place(relx=0.55, rely=0.59, anchor='n')
        self.bentuk_karya = Entry(main_frame, font=getattr(Auth,'font'))
        self.bentuk_karya.place(relx=0.55, rely=0.67, anchor='n')
        self.judul = Entry(main_frame,font=getattr(Auth,'font') )
        self.judul.place(relx=0.55, rely=0.75, anchor='n')
        self.bukutambah_btn = Button(main_frame, bg=getattr(Auth,'bcolor'), fg=getattr(Auth,'wcolor'), width=30, text='Simpan', font=getattr(Auth,'font'), relief=SOLID,cursor='hand2',command=self.Proses_menambahBuku)
        self.bukutambah_btn.place(relx=0.5, rely=0.82, anchor='n')

    def Proses_menambahBuku(self):
        check_counter=0
        peringatan = ""
        try:
            if self.k_buku.get() == "":
                peringatan = "Kode tidak boleh kosong!"
            else:
                check_counter += 1                
            if self.judul.get() == "":
                peringatan = "Judul tidak boleh kosong!"
            else:
                check_counter += 1
            if self.pengarang.get() == "":
                peringatan = "Pengarang tidak boleh kosong!"
            else:
                check_counter += 1
            if self.penerbit.get() == "":
                peringatan = "Penerbit Tidak boleh kosong !"
            else:
                check_counter += 1
            if self.isbn.get() == "":
                peringatan = "ISBN Tidak boleh kosong !"
            else:
                check_counter += 1
            if self.bahasa.get() == "":
                peringatan = "Bahasa Tidak boleh kosong !"
            else:
                check_counter += 1
            if self.bentuk_karya.get() == "":
                peringatan = "Bentuk Karya Tidak boleh kosong !"
            else:
                check_counter += 1
            if check_counter == 7:
                self.data_buku = {}
                self.data_buku['kode'] = self.k_buku.get()
                self.data_buku['judul'] = self.judul.get()
                self.data_buku['pengarang'] = self.pengarang.get()
                self.data_buku['penerbit'] = self.penerbit.get()
                self.data_buku['isbn'] = self.isbn.get()
                self.data_buku['bahasa'] = self.bahasa.get()
                self.data_buku['bentuk_karya'] = self.bentuk_karya.get()
                self.d_buku = x.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/data_buku.json')
                print(self.d_buku)
                self.d_buku.append(self.data_buku)
                x.opsiWrite('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/data_buku.json',self.d_buku)
                print(self.d_buku)  
                messagebox.showinfo('Sukses', 'Data Buku Telah disimpan')
                x.pilihanAdmin()    
            else:
                    messagebox.showerror('Peringatan', peringatan)
        except TclError:
                messagebox.showerror('Peringatan', "Kode harus berupa angka")
            
    def editData(self):
        main_frame = Frame(root,bd=10,bg=getattr(Auth,'wcolor'),relief='solid', padx=10,pady=10).place(relx=0.5, rely=0.22, relheight=0.7, relwidth=0.5, anchor='n')
        title = tk.Label(root,text="Mengedit Buku", font=getattr(Auth,'fontsubtittle'),fg=getattr(Auth,'wcolor'), bg= getattr(Auth,'bcolor'), bd=0)
        title.place(relx=0.50,  relwidth=0.5,rely=0.15, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Kode", bg=getattr(Auth,'bcolor'),font=getattr(Auth,'font'), width=12).place(relx=0.4, rely=0.27, anchor='n')
        self.k_buku = tk.IntVar()
        self.__kode = Entry(main_frame,textvariable = self.k_buku,font=getattr(Auth,'font') )
        self.__kode.place(relx=0.55, rely=0.27, anchor='n')
        setattr(Buku,'kode',self.__kode)
        def update():
            try:
                self.d_buku = x.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/data_buku.json')
                re = {x:self.d_buku[x]['kode'] for x in range(len(self.d_buku))}
                self.list_value = list(re.values())
                kode = self.k_buku.get()
                if(kode in self.list_value):
                    self.bukuedit_btn.after(100, self.bukuedit_btn.destroy)
                    index_buku = self.list_value.index(kode)
                    Label(main_frame, fg=getattr(Auth,'wcolor'), text="Pengarang", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.35, anchor='n')
                    Label(main_frame, fg=getattr(Auth,'wcolor'), text="Penerbit", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.43, anchor='n')
                    Label(main_frame, fg=getattr(Auth,'wcolor'), text="ISBN", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.51,  anchor='n') 
                    Label(main_frame, fg=getattr(Auth,'wcolor'), text="Bahasa", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.59, anchor='n')
                    Label(main_frame, fg=getattr(Auth,'wcolor'), text="Bentuk Karya", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.67,  anchor='n') 
                    Label(main_frame, fg=getattr(Auth,'wcolor'), text="Judul", bg=getattr(Auth,'bcolor'),font=getattr(Auth,'font'), width=12).place(relx=0.4, rely=0.75, anchor='n')
                    self.pengarang = Entry(main_frame, font=getattr(Auth,'font'))
                    self.pengarang.place(relx=0.55, rely=0.35, anchor='n')
                    placeholder_text = self.d_buku[index_buku]['pengarang']
                    self.pengarang.insert(0, placeholder_text)
                    self.penerbit = Entry(main_frame, font=getattr(Auth,'font'))
                    self.penerbit.place(relx=0.55, rely=0.43, anchor='n')
                    placeholder_text = self.d_buku[index_buku]['penerbit']
                    self.penerbit.insert(0, placeholder_text)
                    self.isbn = Entry(main_frame, font=getattr(Auth,'font'))
                    self.isbn.place(relx=0.55, rely=0.51, anchor='n')
                    placeholder_text = self.d_buku[index_buku]['isbn']
                    self.isbn.insert(0, placeholder_text)
                    self.bahasa = Entry(main_frame, font=getattr(Auth,'font'))
                    self.bahasa.place(relx=0.55, rely=0.59, anchor='n')
                    placeholder_text = self.d_buku[index_buku]['bahasa']
                    self.bahasa.insert(0, placeholder_text)
                    self.bentuk_karya = Entry(main_frame, font=getattr(Auth,'font'))
                    self.bentuk_karya.place(relx=0.55, rely=0.67, anchor='n')
                    placeholder_text = self.d_buku[index_buku]['bentuk_karya']
                    self.bentuk_karya.insert(0, placeholder_text)
                    self.judul = Entry(main_frame,font=getattr(Auth,'font') )
                    self.judul.place(relx=0.55, rely=0.75, anchor='n')
                    placeholder_text = self.d_buku[index_buku]['judul']
                    self.judul.insert(0, placeholder_text)
                    def Proses_editData():
                        self.d_buku[index_buku]['judul'] = self.judul.get()
                        self.d_buku[index_buku]['pengarang'] = self.pengarang.get()
                        self.d_buku[index_buku]['penerbit'] = self.penerbit.get()
                        self.d_buku[index_buku]['isbn']= self.isbn.get()
                        self.d_buku[index_buku]['bahasa']=self.bahasa.get()
                        self.d_buku[index_buku]['bentuk_karya'] =  self.bentuk_karya.get()
                        x.opsiWrite('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/data_buku.json',self.d_buku)
                        messagebox.showinfo('Sukses', 'Telah berhasil mengedit buku')
                        x.pilihanAdmin() 
                    self.bukutambah_btn = Button(main_frame, bg=getattr(Auth,'bcolor'), fg=getattr(Auth,'wcolor'), width=30, text='Simpan', font=getattr(Auth,'font'), relief=SOLID,cursor='hand2',command=Proses_editData)
                    self.bukutambah_btn.place(relx=0.5, rely=0.82, anchor='n')
                else:
                    print(f'Maaf tidak ada buku dengan kode tsb')
                    messagebox.showwarning('Peringatan', 'Maaf tidak ada buku dengan kode tersebut')
            except TclError:
                messagebox.showerror('Peringatan', "Kode harus berupa angka")
        self.bukuedit_btn = Button(main_frame, bg=getattr(Auth,'bcolor'), fg=getattr(Auth,'wcolor'), width=30, text='Edit', font=getattr(Auth,'font'), relief=SOLID,cursor='hand2',command=update)
        self.bukuedit_btn.place(relx=0.5, rely=0.4, anchor='n')
    
    def tampilData(self):
        self.d_buku = x.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/data_buku.json')
        title_frame = tk.Frame(root)
        title_frame.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=0.1, anchor='n')
        title = tk.Label(title_frame,font=getattr(Auth,'fonttittle'),text="Buku Perpustakaan")
        title.place(relx=0.25, relheight=1, relwidth=0.5)
        main_frame = tk.Frame(root, bg=getattr(Auth,'bcolor'), bd=10)
        main_frame.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.8, anchor='n')
        title_frame = tk.Frame(root, bg=getattr(Auth,'bcolor'), bd=10)
        title_frame.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.1, anchor='n')
        index_buku = []
        kode_book = []
        judul_book =[]
        penerbit_book=[]
        pengarang_book=[]
        isbn_book = []
        bahasa_book=[]
        bentuk_karya=[]
        def getDataBuku(books):
            re = {x:self.d_buku[x]['kode'] for x in range(len(books))}
            print(re)
            for no,index in enumerate (books[0].keys(),0):
                print(f'{no} {index}')
                index_buku.append(Label(title_frame,text=f'{index}',width=15,fg=getattr(Auth,'wcolor'), bg='#4161AA'))
                index_buku[no].grid(row=0,column=no,pady=30,padx=10)
            for index in range(len(re)):
                tampil_kode = books[index]['kode']
                tampil_judul = books[index]['judul']
                tampil_pengarang = books[index]['pengarang']
                tampil_penerbit = books[index]['penerbit']
                tampil_isbn = books[index]['isbn']
                tampil_bahasa = books[index]['bahasa']
                tampil_karya = books[index]['bentuk_karya']
                kode_book.append(Label(main_frame,text=f'{tampil_kode}',width=15))
                kode_book[index].grid(row=index,column=0,padx=10,pady=20)
                judul_book.append(Label(main_frame,text=f'{tampil_judul}',width=15))
                judul_book[index].grid(row=index,column=1,padx=10,pady=20)
                pengarang_book.append(Label(main_frame,text=f'{tampil_pengarang}',width=15))
                pengarang_book[index].grid(row=index,column=2,padx=10,pady=20)
                penerbit_book.append(Label(main_frame,text=f'{tampil_penerbit}',width=15))
                penerbit_book[index].grid(row=index,column=3,padx=10,pady=20)
                isbn_book.append(Label(main_frame,text=f'{tampil_isbn}',width=15))
                isbn_book[index].grid(row=index,column=4,padx=10,pady=20)
                bahasa_book.append(Label(main_frame,text=f'{tampil_bahasa}',width=15))
                bahasa_book[index].grid(row=index,column=5,padx=10,pady=20)
                bentuk_karya.append(Label(main_frame,text=f'{tampil_karya}',width=15))
                bentuk_karya[index].grid(row=index,column=6,padx=10,pady=20)
                print(tampil_kode)
                button = tk.Button(root, cursor='hand2', text=f"Kembali", font=40, command=lambda: Auth.pilihanAdmin(self))
                button.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.5)  
        getDataBuku(self.d_buku)


    def hapusData(self):
        rooty = tk.Frame(root, bg= getattr(Auth,'bcolor'), bd=15)
        rooty.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.8, anchor='n') 
        main_frame = Frame(rooty,bd=10,bg=getattr(Auth,'wcolor'),relief='solid', padx=10,pady=10).place(relx=0.5, rely=0.15, relheight=0.3, relwidth=0.5, anchor='n')
        title = tk.Label(root,text="Menghapus Buku",font=getattr(Auth,'fontsubtittle') ,fg=getattr(Auth,'wcolor'), bg= getattr(Auth,'bcolor'), bd=15)
        title.place(relx=0.50,  relwidth=0.5,rely=0.15, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="ID Buku", bg=getattr(Auth,'bcolor'),font=getattr(Auth,'font'), width=12).place(relx=0.4, rely=0.33, anchor='n')
        self.k_buku = tk.IntVar()
        self.__kode = Entry(main_frame,textvariable = self.k_buku,font=getattr(Auth,'font') )
        self.__kode.place(relx=0.55, rely=0.33, anchor='n')
        setattr(Buku,'kode',self.__kode)
        def delete():
            try:
                self.d_buku = x.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/data_buku.json')
                re = {x:self.d_buku[x]['kode'] for x in range(len(self.d_buku))}
                self.list_value = list(re.values())
                global kode
                kode = self.k_buku.get()
                if(kode in self.list_value):
                    index_buku = self.list_value.index(kode)
                    del self.d_buku[index_buku] 
                    x.opsiWrite('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/data_buku.json',self.d_buku)
                    messagebox.showinfo('Sukses', 'Buku telah berhasil dihapus')
                    x.pilihanAdmin() 
                else:
                    print(f'Maaf tidak ada buku dengan kode tersebut')
                    messagebox.showwarning('Peringatan', f'Maaf tidak ada buku dengan kode tersebut')
            except TclError:
                messagebox.showerror('Peringatan', "Kode harus berupa angka")
            except AttributeError:
                messagebox.showerror('Peringatan', "Ada kesalahan pada kode buku")
        self.bukuhapus_btn = Button(main_frame, bg=getattr(Auth,'bcolor'), fg=getattr(Auth,'wcolor'), width=30, text='Hapus', font=getattr(Auth,'font'), relief=SOLID,cursor='hand2',command=delete)
        self.bukuhapus_btn.place(relx=0.5, rely=0.4, anchor='n')
       
# PINJAM KEMBALI BUKU
class Pinjam(Program):
    def __init__(self):
        self.pinjam = []
        self.d_pinjam = {}
        global kode_buku
    def tampilBuku(self):
        self.d_buku = x.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/data_buku.json')
        title_frame = tk.Frame(root)
        title_frame.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=0.1, anchor='n')
        title = tk.Label(title_frame,font=getattr(Auth,'fonttittle'),text="Buku Perpustakaan")
        title.place(relx=0.25, relheight=1, relwidth=0.5)
        main_frame = tk.Frame(root, bg=getattr(Auth,'bcolor'), bd=10)
        main_frame.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.8, anchor='n')
        title_frame = tk.Frame(root, bg=getattr(Auth,'bcolor'), bd=10)
        title_frame.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.1, anchor='n')
        index_buku = []
        kode_book = []
        judul_book =[]
        penerbit_book=[]
        pengarang_book=[]
        isbn_book = []
        bahasa_book=[]
        bentuk_karya=[]
        def getDataBuku(books):
            re = {x:self.d_buku[x]['kode'] for x in range(len(books))}
            print(re)
            for no,index in enumerate (books[0].keys(),0):
                print(f'{no} {index}')
                index_buku.append(Label(title_frame,text=f'{index}',width=15,fg=getattr(Auth,'wcolor'), bg='#4161AA'))
                index_buku[no].grid(row=0,column=no,pady=30,padx=10)
            for index in range(len(re)):
                tampil_kode = books[index]['kode']
                tampil_judul = books[index]['judul']
                tampil_pengarang = books[index]['pengarang']
                tampil_penerbit = books[index]['penerbit']
                tampil_isbn = books[index]['isbn']
                tampil_bahasa = books[index]['bahasa']
                tampil_karya = books[index]['bentuk_karya']
                kode_book.append(Label(main_frame,text=f'{tampil_kode}',width=15))
                kode_book[index].grid(row=index,column=0,padx=10,pady=20)
                judul_book.append(Label(main_frame,text=f'{tampil_judul}',width=15))
                judul_book[index].grid(row=index,column=1,padx=10,pady=20)
                pengarang_book.append(Label(main_frame,text=f'{tampil_pengarang}',width=15))
                pengarang_book[index].grid(row=index,column=2,padx=10,pady=20)
                penerbit_book.append(Label(main_frame,text=f'{tampil_penerbit}',width=15))
                penerbit_book[index].grid(row=index,column=3,padx=10,pady=20)
                isbn_book.append(Label(main_frame,text=f'{tampil_isbn}',width=15))
                isbn_book[index].grid(row=index,column=4,padx=10,pady=20)
                bahasa_book.append(Label(main_frame,text=f'{tampil_bahasa}',width=15))
                bahasa_book[index].grid(row=index,column=5,padx=10,pady=20)
                bentuk_karya.append(Label(main_frame,text=f'{tampil_karya}',width=15))
                bentuk_karya[index].grid(row=index,column=6,padx=10,pady=20)
                print(tampil_kode)
                button = tk.Button(root, cursor='hand2', text=f"Kembali", font=40, command=lambda: Auth.pilihanUser(self))
                button.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.5)  
        getDataBuku(self.d_buku)

    def PinjamBuku(self):
        main_frame = Frame(root,bd=10,bg=getattr(Auth,'wcolor'),relief='solid', padx=10,pady=10).place(relx=0.5, rely=0.23, relheight=0.6, relwidth=0.5, anchor='n')
        title = tk.Label(root,text="Pinjam Buku", font=getattr(Auth,'fontsubtittle'),fg=getattr(Auth,'wcolor'), bg= getattr(Auth,'bcolor'), bd=15)
        title.place(relx=0.50,  relwidth=0.5,rely=0.15, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Nama Peminjam", bg=getattr(Auth,'bcolor'),font=getattr(Auth,'font'), width=20).place(relx=0.4, rely=0.3, anchor='n')
        self.nama_peminjam = Entry(main_frame,font=getattr(Auth,'font'))
        placeholder_text = Auth.username.get()
        self.nama_peminjam.insert(0, placeholder_text)
        self.nama_peminjam.place(relx=0.60, rely=0.3, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Kode Buku", bg=getattr(Auth,'bcolor'),font=getattr(Auth,'font'), width=20).place(relx=0.4, rely=0.38, anchor='n')
        self.k_buku = tk.IntVar()
        self.__kode_buku = Entry(main_frame,font=getattr(Auth,'font'),textvariable=self.k_buku)
        self.__kode_buku.place(relx=0.60, rely=0.38, anchor='n')
        setattr(Pinjam,'kode_buku',self.__kode_buku)
        self.denda = ['Terlambat pada minggu pertama  = Rp.5000',
                'Terlambat pada minggu kedua  = Rp.7000', 
                'Terlambat pada minggu ketiga = Rp.9000', 
                'Terlambat pada minggu ke empat = Rp.11.000']  
        denda_frame = Frame(root, bg='#483D8B', bd=5)
        denda_frame.place(relx=0.5, rely=0.55, relwidth=0.30, relheight=0.23, anchor='n')
        for w,k in enumerate(self.denda,4):
            Label(denda_frame,text=k,width=52,pady=9).grid(row=w,column=1)
     
        def proses_pinjam():
            try:
                self.d_buku = x.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/data_buku.json')
                re = {x:self.d_buku[x]['kode'] for x in range(len(self.d_buku))}
                self.list_value = list(re.values())
                kode_buku = self.k_buku.get()
                if(kode_buku in self.list_value):
                    self.d_pinjam = {}
                    self.pinjam = []
                    index_buku = self.list_value.index(kode_buku)
                    print(index_buku)
                    self.d_pinjam['nama_peminjam'] = self.nama_peminjam.get()
                    self.d_pinjam['kode_buku']  = self.d_buku[index_buku]['kode'] 
                    self.d_pinjam['judul']  = self.d_buku[index_buku]['judul']
                    self.d_pinjam['pengarang ']  = self.d_buku[index_buku]['pengarang']
                    self.d_pj = x.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/p_buku.json') 
                    kb = {x:self.d_pj[x]['kode_buku'] for x in range(len(self.d_pj))}
                    self.list_kb = list(kb.values())
                    assert(self.d_buku[index_buku]['kode'] not in self.list_kb), 'Buku sudah dipinjam'
                    tanggal = datetime.today()
                    t_pinjam = tanggal.strftime('%d-%m-%Y')
                    self.d_pinjam['tanggal_pinjam'] = t_pinjam
                    self.d_pj = x.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/p_buku.json') 
                    self.d_pj.append(self.d_pinjam)
                    x.opsiWrite('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/p_buku.json',self.d_pj)
                    print(self.pinjam)  
                    messagebox.showinfo('Sukses', 'Buku berhasil dipinjam')
                    x.pilihanUser()    
                else:
                    print("Maaf tidak ada buku dengan kode")
                    messagebox.showwarning('Peringatan', f"Maaf tidak ada buku dengan kode tersebut")
            except TclError:
                messagebox.showerror('Peringatan', "Kode harus berupa angka")
            except AssertionError as error:
                    print(error)
                    messagebox.showinfo('Peringatan', f'Buku sedang dipinjam')
        self.bukupinjam_btn = Button(main_frame, bg=getattr(Auth,'bcolor'), fg=getattr(Auth,'wcolor'), width=30, text='Pinjam', font=getattr(Auth,'font'), relief=SOLID,cursor='hand2',command=proses_pinjam)
        self.bukupinjam_btn.place(relx=0.5, rely=0.45, anchor='n')       

             
    def Kembali(self):
        main_frame = Frame(root,bd=10,bg=getattr(Auth,'wcolor'),relief='solid', padx=10,pady=10).place(relx=0.5, rely=0.23, relheight=0.6, relwidth=0.5, anchor='n')
        title = tk.Label(root,text="Kembali Buku", font=getattr(Auth,'fontsubtittle'),fg=getattr(Auth,'wcolor'), bg= getattr(Auth,'bcolor'), bd=15)
        title.place(relx=0.50,  relwidth=0.5,rely=0.15, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Kode Buku Peminjam", bg=getattr(Auth,'bcolor'),font=getattr(Auth,'font'), width=20).place(relx=0.4, rely=0.3, anchor='n')
        self.k_buku = tk.IntVar()
        self.kode_buku = Entry(main_frame,font=getattr(Auth,'font'),textvariable = self.k_buku )
        self.kode_buku.place(relx=0.60, rely=0.3, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Tanggal (d-m-y)", bg=getattr(Auth,'bcolor'),font=getattr(Auth,'font'), width=20).place(relx=0.4, rely=0.38, anchor='n')
        self.tgl = Entry(main_frame,font=getattr(Auth,'font') )
        self.tgl.place(relx=0.60, rely=0.38, anchor='n')
        self.denda = ['Terlambat pada minggu pertama  = Rp.5000',
                'Terlambat pada minggu kedua  = Rp.7000', 
                'Terlambat pada minggu ketiga = Rp.9000', 
                'Terlambat pada minggu ke empat = Rp.11.000']  
        denda_frame = Frame(root, bg='#483D8B', bd=5)
        denda_frame.place(relx=0.5, rely=0.55, relwidth=0.30, relheight=0.23, anchor='n')
        for w,k in enumerate(self.denda,4):
            Label(denda_frame,text=k,width=52,pady=9).grid(row=w,column=1)

        def proses_kembali():
            try:
                self.p_buku = x.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/p_buku.json')
                re = {x:self.p_buku[x]['kode_buku'] for x in range(len(self.p_buku))}
                self.list_value = list(re.values())
                print(self.tgl.get())
                self.kode_buku = self.k_buku.get()
                index_buku = self.list_value.index(self.kode_buku)
                if( self.kode_buku  in self.list_value):
                    self.d_pj = x.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/p_buku.json')
                    self.isi_buku = {x:self.d_pj[x]['kode_buku'] for x in range(len(self.d_pj))}
                    print(self.isi_buku)
                    self.list_value = list(self.isi_buku.values())
                    print(self.list_value)
                    index_pinjam = self.list_value.index(self.kode_buku )
                    format_t = "%d-%m-%Y"
                    tanggal_p = self.p_buku[index_pinjam]['tanggal_pinjam']
                    tanggal_k = self.tgl.get()
                    tdelta = datetime.strptime( tanggal_k,format_t) - datetime.strptime(tanggal_p,format_t)
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
                                    messagebox.showinfo('Peringatan', f"Maaf Anda terlambat mengembalikan buku selama lebih dari 30 hari. Anda tidak boleh meminjam buku selama {hari_tp} hari")
                                    print()   
                                
                        print(f"Maaf Anda terlambat mengembalikan buku,Anda akan dikenakan denda sebesar Rp.{total_denda} ")
                        messagebox.showinfo('Peringatan',f"Maaf Anda terlambat mengembalikan buku,Anda akan dikenakan denda sebesar Rp.{total_denda} ")
                    else:
                        messagebox.showinfo('Sukses',"Terimakasih telah mengembalikan buku dengan tepat waktu")
                    del self.d_pj[index_buku]
                    x.opsiWrite('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/p_buku.json',self.d_pj)
                    messagebox.showinfo('Sukses', 'Buku telah berhasil dikembalikan')
                    x.pilihanUser() 

                else:
                    # print("Maaf tidak ada buku dengan kode")
                    messagebox.showwarning('Peringatan',f'Maaf Tidak ada buku dengan kode tersebut')
            except KeyError:
                 messagebox.showerror('Error',f'Ada kesalahan penyimpanan')
            except ValueError:
                 messagebox.showerror('Error',f'Ada kesalahan list')
        self.bukukembali_btn = Button(main_frame, bg=getattr(Auth,'bcolor'), fg=getattr(Auth,'wcolor'), width=30, text='Kembali', font=getattr(Auth,'font'), relief=SOLID,cursor='hand2',command=proses_kembali)
        self.bukukembali_btn.place(relx=0.51, rely=0.45, anchor='n')  
   
    
class Auth(Buku,Pinjam):      
    def __init__(self):
        self.users = []
        self.d_users = {}
        self.font= ('Comic', 15)
        self.font_title= ('Rockwell', 20)
        self.font_subtittle = ('Helvetica',17,'bold italic')
        setattr(Auth,'fonttittle',self.font_title)
        setattr(Auth,'font',self.font)
        setattr(Auth,'fontsubtittle',self.font_subtittle)
        self.wcolor = 'white'
        setattr(Auth,'wcolor',self.wcolor)
        self.b_color = '#2C26D1'
        setattr(Auth,'bcolor',self.b_color)
    def opsiWrite(self,path,data_yang_ditambah):
        self.path =path
        self.data_yang_ditambah = data_yang_ditambah
        with open(f'{self.path}','w',encoding='utf-8') as data_file: 
            json.dump(self.data_yang_ditambah,data_file,ensure_ascii=False, indent=2)
    def OpsiRead(self,path):
        self.path = path
        with open(self.path, encoding="utf-8") as data_file:
            return json.load(data_file)
    def Register(self):
        rooty = tk.Frame(root, bg= getattr(Auth,'bcolor'), bd=15)
        rooty.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.8, anchor='n') 
        # title
        title_frame = tk.Frame(rooty, bd=0,bg= getattr(Auth,'bcolor'))
        title_frame.place(relx=0.5, rely=0.02, relwidth=0.8, relheight=0.1, anchor='n')
        title = tk.Label(title_frame,text="REGISTER", font=getattr(Auth,'fontsubtittle'),fg=getattr(Auth,'wcolor'), bg= getattr(Auth,'bcolor'), bd=0)
        title.place(relx=0.25,  relwidth=0.5)
        # main
        main_frame = Frame(rooty,bd=10,bg=getattr(Auth,'wcolor'),relief='solid', padx=10,pady=10).place(relx=0.5, rely=0.1, relheight=0.6, relwidth=0.5, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Username", bg=getattr(Auth,'bcolor'),font=getattr(Auth,'font'), width=12).place(relx=0.4, rely=0.3, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Alamat", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.38, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Role", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.46, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Password", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.54,  anchor='n') 
        self.__username = Entry(main_frame,font=getattr(Auth,'font') )
        self.__username.place(relx=0.55, rely=0.3, anchor='n')
        setattr(Auth,'username',self.__username)
        self.alamat = Entry(main_frame, font=getattr(Auth,'font'))
        self.alamat.place(relx=0.55, rely=0.38, anchor='n')
        opsi_frame = LabelFrame(main_frame)
        opsi_frame.place(relx=0.55, rely=0.46, anchor='n')
        self.role = StringVar()
        self.role.set('admin')
        self.admin_rb= Radiobutton(opsi_frame, variable=self.role,text='Admin',value='admin',font=getattr(Auth,'font'))
        self.admin_rb.pack(side=LEFT)
        self.user_rb= Radiobutton(opsi_frame, variable=self.role, text='User',value='user',font=getattr(Auth,'font'))
        self.user_rb.pack( side=LEFT)
        self.password = Entry(main_frame, font=getattr(Auth,'font'),show='*')
        self.password.place(relx=0.55, rely=0.54, anchor='n')
        self.register_btn = Button(main_frame, bg=getattr(Auth,'bcolor'), fg=getattr(Auth,'wcolor'), width=30, text='Register', font=getattr(Auth,'font'), relief=SOLID,cursor='hand2',command=self.proses_register)
        self.register_btn.place(relx=0.5, rely=0.6, anchor='n')

    def proses_register(self):
        #validasi form 
        try:
            check_counter=0
            peringatan = ""
            if self.username.get() == "":
                peringatan = "Username tidak boleh kosong!"
            else:
                check_counter += 1
                
            if self.alamat.get() == "":
                peringatan = "Alamat tidak boleh kosong!"
            else:
                check_counter += 1

            if self.role.get() == "":
                peringatan = "Role tidak boleh kosong!"
            else:
                check_counter += 1
            
            if  self.password.get() == "":
                peringatan = "Password Tidak boleh kosong !"
            else:
                check_counter += 1

            if check_counter == 4:        
                self.d_users['username'] = self.username.get()
                self.d_users['password'] = self.password.get()
                self.d_users['alamat'] = self.alamat.get()
                self.d_users['role'] = self.role.get()
                self.d_user = self.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/d_user.json')
                print(self.d_user)
                re = {x:self.d_user[x]['username'] for x in range(len(self.d_user))}
                self.list_value = list(re.values())
                username = self.username.get()
                assert(username not in self.list_value), 'Username sudah ada'
                self.d_user.append(self.d_users)
                self.opsiWrite('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/d_user.json',self.d_user)
                print('Selamat anda berhasil menambah akun')
                messagebox.showinfo('Sukses', 'Akun berhasil ditambahkan')
                self.akun =  self.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/d_user.json')
                isi_pengguna = {x:self.akun[x]['username'] for x in range(len(self.akun))}
                print(isi_pengguna)
                self.list_value = list(isi_pengguna.values())
                self.index_user = self.list_value.index(self.username.get())
                self.Middleware()
            else:
                messagebox.showerror('Peringatan', peringatan)
        except AssertionError as error:
                    print(error)
                    messagebox.showinfo('Peringatan', error)
    
    def login(self):
        rooty = tk.Frame(root, bg= getattr(Auth,'bcolor'), bd=15)
        rooty.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.8, anchor='n') 
        # title
        title_frame = tk.Frame(rooty, bd=5,bg= getattr(Auth,'bcolor'))
        title_frame.place(relx=0.5, rely=0.03, relwidth=0.8, relheight=0.1, anchor='n')
        title = tk.Label(title_frame,text="LOGIN", font=getattr(Auth,'fontsubtittle'),fg=getattr(Auth,'wcolor'), bg= getattr(Auth,'bcolor'), bd=15)
        title.place(relx=0.25,  relwidth=0.5)
        main_frame = Frame(rooty,bd=10,bg=getattr(Auth,'wcolor'),relief='solid', padx=10,pady=10).place(relx=0.5, rely=0.15, relheight=0.5, relwidth=0.5, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Username", bg=getattr(Auth,'bcolor'),font=getattr(Auth,'font'), width=12).place(relx=0.4, rely=0.35, anchor='n')
        Label(main_frame, fg=getattr(Auth,'wcolor'), text="Password", bg= getattr(Auth,'bcolor'),font=getattr(Auth,'font'),width=12).place(relx=0.4, rely=0.45,  anchor='n') 
        self.__username = Entry(main_frame,font=getattr(Auth,'font') )
        self.__username.place(relx=0.55, rely=0.35, anchor='n')
        setattr(Auth,'username',self.__username)
        self.password = Entry(main_frame, font=getattr(Auth,'font'),show='*')
        self.password.place(relx=0.55, rely=0.45, anchor='n')
        self.login_btn = Button(main_frame, width=30, text='Login', bg=getattr(Auth,'bcolor'), fg=getattr(Auth,'wcolor'),font=getattr(Auth,'font'), relief=SOLID,cursor='hand2',command=self.prosesLogin)
        self.login_btn.place(relx=0.5, rely=0.55, anchor='n')

     
    def prosesLogin(self):
        check_counter=0
        peringatan = ""
        if self.username.get() == "":
            peringatan = "Username tidak boleh kosong!"
        else:
            check_counter += 1
        if  self.password.get() == "":
            peringatan = "Password Tidak boleh kosong !"
        else:
            check_counter += 1
        if check_counter == 2:     
            print(check_counter) 
            self.akun =  self.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/d_user.json')
            isi_pengguna = {x:self.akun[x]['username'] for x in range(len(self.akun))}
            print(isi_pengguna)
            self.list_value = list(isi_pengguna.values())
            if(self.username.get() in self.list_value):
                self.index_user = self.list_value.index(self.username.get())
                pwd_user = self.akun[self.index_user]['password']
                if(self.password.get() == pwd_user):
                    # print('Selamat Anda sudah bisa masuk')
                    messagebox.showinfo('Sukses', 'Selamat Anda Berhasil Masuk')
                    self.Middleware()
                else:
                    messagebox.showwarning('Peringatan', 'Maaf passwod salah')    
            else:
                messagebox.showwarning('Peringatan', f'Maaf tidak ada user dengan nama {self.username.get()}')
        else:
                messagebox.showerror('Peringatan', peringatan)

    def pilihanAdmin(self):
        pil1 = ['Menambahkan buku', 'Mengedit Buku', 'Menghapus Buku','Menampilkan Buku','Menampilkan Data User','Menampilkan Data Pinjam','Logout']
        # main
        rooty = tk.Frame(root, bg= getattr(Auth,'bcolor'), bd=15)
        rooty.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.8, anchor='n') 
        # title
        title_frame = tk.Frame(root)
        title_frame.place(relx=0.5, rely=0.05, relwidth=0.8, relheight=0.1, anchor='n')
        title = tk.Label(title_frame,font=getattr(Auth,'fonttittle'),text="Perpustakaan")
        title.place(relx=0.25, relheight=1, relwidth=0.5)
        # title
        title_frame = tk.Frame(rooty, bd=15,bg= getattr(Auth,'bcolor'))
        title_frame.place(relx=0.5, rely=0.03, relwidth=0.8, relheight=0.1, anchor='n')
        title = tk.Label(title_frame,text=f"Menu Admin ({self.username.get()})", font=getattr(Auth,'fontsubtittle'),fg=getattr(Auth,'wcolor'), bg= getattr(Auth,'bcolor'), bd=5)
        title.place(relx=0.25,  relwidth=0.5)
        #input buku
        self.frame = tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=5)
        self.frame.place(relx=0.5, rely=0.15, relwidth=0.5, relheight=0.1, anchor='n')
        button = tk.Button(self.frame, cursor='hand2', text=f"{pil1[0]}", font=40, command=lambda: self.inputData())
        button.place(relx=0.25, relheight=1, relwidth=0.5) 
        #edit buku
        lower_frame = tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=5)
        lower_frame.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.1, anchor='n')
        button2 = tk.Button(lower_frame, cursor='hand2',text=f"{pil1[1]}", font=40, command=lambda: self.editData())
        button2.place(relx=0.25, relheight=1, relwidth=0.5)    
        # hapus bukua
        lower_frame2 = tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=5)
        lower_frame2.place(relx=0.5, rely=0.35, relwidth=0.5, relheight=0.1, anchor='n')
        button2 = tk.Button(lower_frame2, cursor='hand2', text=f"{pil1[2]}", font=40, command=lambda: self.hapusData())
        button2.place(relx=0.25, relheight=1, relwidth=0.5)
        # tampil buku  
        lower_frame3 = tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=5)
        lower_frame3.place(relx=0.5, rely=0.45, relwidth=0.5, relheight=0.1, anchor='n')
        button3 = tk.Button(lower_frame3,cursor='hand2', text=f"{pil1[3]}", font=40, command=lambda: Buku.tampilData(self))
        button3.place(relx=0.25, relheight=1, relwidth=0.5)
        # tampil User
        lower_frame3 = tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=5)
        lower_frame3.place(relx=0.5, rely=0.55, relwidth=0.5, relheight=0.1, anchor='n')
        button3 = tk.Button(lower_frame3,cursor='hand2', text=f"{pil1[4]}", font=40, command=lambda: self.tampilData())
        button3.place(relx=0.25, relheight=1, relwidth=0.5)  
            # tampil Pinjam
        lower_frame3 = tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=5)
        lower_frame3.place(relx=0.5, rely=0.65, relwidth=0.5, relheight=0.1, anchor='n')
        button3 = tk.Button(lower_frame3,cursor='hand2', text=f"{pil1[5]}", font=40, command=lambda: self.tampilDataPinjam())
        button3.place(relx=0.25, relheight=1, relwidth=0.5)  
        #keluar (menu)
        lower_frame4 = tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=5)
        lower_frame4.place(relx=0.5, rely=0.75, relwidth=0.5, relheight=0.1, anchor='n')
        button4 = tk.Button(lower_frame4, cursor='hand2', text=f"{pil1[6]}", font=40, command=lambda: self.LoginRegister())
        button4.place(relx=0.25, relheight=1, relwidth=0.5)  
    def tampilData(self):
        self.d_user = self.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/d_user.json')        # title
        title_frame = tk.Frame(root)
        title_frame.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=0.1, anchor='n')
        title = tk.Label(title_frame,font=getattr(Auth,'fonttittle'),text="Data User")
        title.place(relx=0.25, relheight=1, relwidth=0.5)
        main_fram = tk.Frame(root, bg=getattr(Auth,'bcolor'), bd=10)
        main_fram.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.8, anchor='n')
        main_frame = tk.Frame(main_fram, bg=getattr(Auth,'bcolor'), bd=10)
        main_frame.place(relx=0.59, rely=0.05, relwidth=0.8, relheight=0.8, anchor='n')
        title_frame = tk.Frame(main_fram, bg=getattr(Auth,'bcolor'), bd=0)
        title_frame.place(relx=0.6, rely=0, relwidth=0.8, relheight=0.1, anchor='n')
        index_user=[]
        username = []
        alamat = []
        password =[]
        role=[]
        def getDataUser(users):
            re = {x:self.d_user[x]['username'] for x in range(len(users))}
            print(re)
            for no,index in enumerate (users[0].keys(),0):
                print(f'{no} {index}')
                index_user.append(Label(title_frame,text=f'{index}',width=15,fg=getattr(Auth,'wcolor'), bg='#4161AA'))
                index_user[no].grid(row=0,column=no,pady=30,padx=10)
            for index in range(len(re)):
                tampil_username = users[index]['username']
                tampil_alamat = users[index]['alamat']
                tampil_password = users[index]['password']
                tampil_role = users[index]['role']
                username.append(Label(main_frame,text=f'{tampil_username}',width=15))
                username[index].grid(row=index,column=0,padx=10,pady=20)
                alamat.append(Label(main_frame,text=f'{tampil_alamat}',width=15))
                alamat[index].grid(row=index,column=1,padx=10,pady=20)
                password.append(Label(main_frame,text=f'{tampil_password}',width=15))
                password[index].grid(row=index,column=2,padx=10,pady=20)
                role.append(Label(main_frame,text=f'{tampil_role}',width=15))
                role[index].grid(row=index,column=3,padx=10,pady=20)
                button = tk.Button(root, cursor='hand2', text=f"Kembali", font=40, command=lambda: Auth.pilihanAdmin(self))
                button.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.5)  
        getDataUser(self.d_user)
    
    def tampilDataPinjam(self):
        self.d_pinjam = self.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/p_buku.json')       
        title_frame = tk.Frame(root)
        title_frame.place(relx=0.5, rely=0.05, relwidth=0.5, relheight=0.1, anchor='n')
        title = tk.Label(title_frame,font=getattr(Auth,'fonttittle'),text="Data Peminjaman")
        title.place(relx=0.25, relheight=1, relwidth=0.5)
        main_fram = tk.Frame(root, bg=getattr(Auth,'bcolor'), bd=10)
        main_fram.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.8, anchor='n')
        main_frame = tk.Frame(main_fram, bg=getattr(Auth,'bcolor'), bd=10)
        main_frame.place(relx=0.59, rely=0.05, relwidth=0.8, relheight=0.8, anchor='n')
        title_frame = tk.Frame(main_fram, bg=getattr(Auth,'bcolor'), bd=0)
        title_frame.place(relx=0.6, rely=0, relwidth=0.8, relheight=0.1, anchor='n')
        index_pinjam=[]
        nama_peminjam = []
        kode_buku = []
        judul =[]
        pengarang=[]
        tanggal_pinjam = []
        def getDataPinjam(pinjam):
            re = {x:self.d_pinjam[x]['nama_peminjam'] for x in range(len(pinjam))}
            print(re)
            for no,index in enumerate (pinjam[0].keys(),0):
                print(f'{no} {index}')
                index_pinjam.append(Label(title_frame,text=f'{index}',width=15,fg=getattr(Auth,'wcolor'), bg='#4161AA'))
                index_pinjam[no].grid(row=0,column=no,pady=30,padx=10)
            for index in range(len(re)):
                tampil_nama_peminjam = pinjam[index]['nama_peminjam']
                tampil_kode_buku = pinjam[index]['kode_buku']
                tampil_judul = pinjam[index]['judul']
                tampil_pengarang = pinjam[index]['pengarang ']
                tampil_tanggal_pinjam = pinjam[index]['tanggal_pinjam']
                nama_peminjam.append(Label(main_frame,text=f'{tampil_nama_peminjam}',width=15))
                nama_peminjam[index].grid(row=index,column=0,padx=10,pady=20)
                kode_buku.append(Label(main_frame,text=f'{tampil_kode_buku}',width=15))
                kode_buku[index].grid(row=index,column=1,padx=10,pady=20)
                judul.append(Label(main_frame,text=f'{tampil_judul}',width=15))
                judul[index].grid(row=index,column=2,padx=10,pady=20)
                pengarang.append(Label(main_frame,text=f'{tampil_pengarang}',width=15))
                pengarang[index].grid(row=index,column=3,padx=10,pady=20)
                tanggal_pinjam.append(Label(main_frame,text=f'{tampil_tanggal_pinjam}',width=15))
                tanggal_pinjam[index].grid(row=index,column=4,padx=10,pady=20)
                button = tk.Button(root, cursor='hand2', text=f"Kembali", font=40, command=lambda: Auth.pilihanAdmin(self))
                button.place(relx=0.25, rely=0.9, relheight=0.05, relwidth=0.5)  
        getDataPinjam(self.d_pinjam)

    def pilihanUser(self):
        pil1 = ['Meminjam Buku', 'Mengembalikan Buku','Daftar Buku','Logout']
        # main
        rooty = tk.Frame(root, bg= getattr(Auth,'bcolor'), bd=15)
        rooty.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.8, anchor='n') 
        # title
        title_frame = tk.Frame(rooty, bd=15,bg= getattr(Auth,'bcolor'))
        title_frame.place(relx=0.5, rely=0.02, relwidth=0.8, relheight=0.1, anchor='n')
        title = tk.Label(title_frame,text=f"Menu User ({self.username.get()})", font=getattr(Auth,'fontsubtittle'),fg=getattr(Auth,'wcolor'), bg= getattr(Auth,'bcolor'), bd=5)
        title.place(relx=0.25,  relwidth=0.5)
        #Pinja Buku
        self.frame = tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=15)
        self.frame.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.1, anchor='n')
        button = tk.Button(self.frame, cursor='hand2',text=f"{pil1[0]}", font=40, command=lambda: self.PinjamBuku())
        button.place(relx=0.25, relwidth=0.5) 
        #Kembali Buku
        lower_framet= tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=15)
        lower_framet.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.1, anchor='n')
        button2 = tk.Button(lower_framet,cursor='hand2', text=f"{pil1[1]}", font=40, command=lambda: self.Kembali())
        button2.place(relx=0.25,  relwidth=0.5)   
        #Lihat Buku
        lower_fra= tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=15)
        lower_fra.place(relx=0.5, rely=0.35, relwidth=0.8, relheight=0.1, anchor='n')
        button3 = tk.Button(lower_fra,cursor='hand2', text=f"{pil1[2]}", font=40, command=lambda: self.tampilBuku())
        button3.place(relx=0.25,  relwidth=0.5)  
        
        #Keluar
        lower_framets= tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=15)
        lower_framets.place(relx=0.5, rely=0.45, relwidth=0.8, relheight=0.1, anchor='n')
        button4 = tk.Button(lower_framets,cursor='hand2', text=f"{pil1[3]}", font=40, command=lambda: self.LoginRegister())
        button4.place(relx=0.25,  relwidth=0.5)  
        image_frame = tk.Frame(rooty)
        image_frame.pack()
        image_frame.place(relx=0.5, rely=0.55, anchor='n')
        img = ImageTk.PhotoImage(Image.open("C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/bacab.png"))
        label = Label(image_frame, image = img,borderwidth=0)
        label.image= img
        label.pack() 
                  
    def Middleware(self):
        try:
            self.akun =  self.OpsiRead('C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/d_user.json')
            if(self.akun[self.index_user]['role'] == 'admin'):
                self.pilihanAdmin()
            else:
                self.pilihanUser()
        except FileNotFoundError:
            messagebox.showerror('Peringatan', 'Maaf file penyimpanan tidak ada')
    def KeluarProgram(self):
        konfirmasi = messagebox.askyesno('Konfirmasi', 'Apakah kamu yakin ingin keluar?')
        if konfirmasi == True:
            messagebox.showinfo('keluar..', 'Terima kasih telah menggunakan aplikasi kami ^-^')
            root.destroy()
        else:
            messagebox.showinfo('stay..', 'Terimakasih tetap menggunakan aplikasi kami ^-^')

    def LoginRegister(self):
        try:  
            # title
            title_frame = tk.Frame(root)
            title_frame.place(relx=0.5, rely=0.05, relwidth=0.8, relheight=0.1, anchor='n')
            title = tk.Label(title_frame,font=getattr(Auth,'fonttittle'),text="Perpustakaan")
            title.place(relx=0.25, relheight=1, relwidth=0.5)
            # main
            rooty = tk.Frame(root, bg= getattr(Auth,'bcolor'), bd=15)
            rooty.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.8, anchor='n') 
            # title
            title_frame = tk.Frame(rooty, bd=5,bg= getattr(Auth,'bcolor'))
            title_frame.place(relx=0.5, rely=0.01, relwidth=0.8, relheight=0.1, anchor='n')
            title = tk.Label(title_frame,text="Menu", font=getattr(Auth,'fontsubtittle'),fg=getattr(Auth,'wcolor'), bg= getattr(Auth,'bcolor'), bd=15)
            title.place(relx=0.25,  relwidth=0.5)
            #register
            self.frame = tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=15)
            self.frame.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.1, anchor='n')
            button = tk.Button(self.frame, cursor='hand2',text="Register", font=40, command=lambda: self.Register())
            button.place(relx=0.25, relwidth=0.5) 
            #login
            lower_framet= tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=15)
            lower_framet.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.1, anchor='n')
            button2 = tk.Button(lower_framet,cursor='hand2', text="Login", font=40, command=lambda: self.login())
            button2.place(relx=0.25,  relwidth=0.5)   
            #login
            lower_frame = tk.Frame(rooty, bg= getattr(Auth,'bcolor'), bd=15)
            lower_frame.place(relx=0.5, rely=0.35, relwidth=0.8, relheight=0.1, anchor='n')
            button3 = tk.Button(lower_frame, cursor='hand2',text="Keluar", font=40, command=lambda:self.KeluarProgram())
            button3.place(relx=0.25, relwidth=0.5)  
            image_frame = tk.Frame(rooty)
            image_frame.pack()
            image_frame.place(relx=0.5, rely=0.45, anchor='n')
            img = ImageTk.PhotoImage(Image.open("C:/Users/My Laptop/Documents/Programming/PYTHON/PYTHON BASIC/Challege/bbook.png"))
            label = Label(image_frame, image = img,borderwidth=0)
            label.image= img
            label.pack()
        except FileNotFoundError:
            messagebox.showerror('Peringatan', 'Maaf file penyimpanan tidak ada')
            print("{0:^64}".format("**Maaf file penyimpanan tidak ada **"))            
try:
    x = Auth()
    x.LoginRegister()
    root.mainloop()
except TypeError:
    print('Abstract method belum diimplementasikan!')
    messagebox.showerror('Error', 'Abstract method belum diimplementasikan!')