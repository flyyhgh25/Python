from abc import ABC, abstractclassmethod
class Orang(ABC):
    abstractclassmethod
    def __init__(self):
        self.nama = None
        self.umur = None
        self.jenis_kelamin = None
    # @abstractmethod
    def inputOrang(self):
        self.nama = input("Masukkan nama\t\t:")
        self.umur = input("Masukkan umur\t\t:")
        self.jenis_kelamin = input("Masukkan jenis kelamin\t:")

class Mahasiswa():
    def __init__(self):
        self.__nim = None
    def inputMahasiswa(self):
        self.__nim = input("Masukkan NIM\t\t:")
        setattr(Mahasiswa,'__nim',self.__nim)
    def ubahNim(self):
        self.__nim = input("Masukkan NIM\t\t:")
        setattr(Mahasiswa,'__nim',self.__nim)
    def tampil(self):
        nimnya = getattr(Mahasiswa,"__nim") 
        print("NIM\t\t :", nimnya)
 
class Identitas(Orang,Mahasiswa):
    def __init__(self):
        self.alamat = 'Tegalsari'
        Orang.__init__(self)
    def MahasiswaTa(self):
        Mahasiswa.__init__(self)
    def ubahNama(self):
        self.nama = input("Masukkan nama\t\t:")
    def __ubahUmur(self):
        self.umur = input("Masukkan Umur\t\t:")
    def tampilData(self):
        print("Nama\t\t :",self.nama)
        print("Umur\t\t :",self.umur)
        print("Jenis Kelamin\t : ",self.jenis_kelamin)
        Mahasiswa.tampil(self)

identity = Identitas()
identity.inputOrang()
identity.inputMahasiswa()
identity.MahasiswaTa()
identity.tampilData()

# class Dosen():
#      def __init__(self):
#         self.__nidn = None
#         setattr(Dosen,'__nidn',self.__nidn)
#         self.mengajar = None
#      def inputDosen(self):
#         self.__nidn = input("Masukkan NIDN \t\t:")
#         setattr(Dosen,'__nidn',self.__nidn)
#         self.mengajar = input("Masukkan mengajar \t:") 
#      def __ubahNIDN(self):
#         self.__nim = input("Masukkan NIDN\t\t:")
#         setattr(Dosen,'__nidn',self.__nidn)
#      def __tampilDosen(self):
#         nidn = getattr(Dosen,"__nidn") 
#         print("NIDN\t\t :", nidn)

# class Universitas:
#     def __init__(self):
#         self.universitas = None
#         self.fakultas = None  
#     def __ubahUniv(self):
#         self.universitas = input("Masukkan Universitas\t:") 
#     def tampilUniv(self):
#         print("Universitas\t :",self.universitas )
#         print("Fakultas \t :", self.fakultas)  
#     def inputUniv(self):
#         self.universitas = input("Masukkan Universitas\t:")
#         self.fakultas = input("Masukkan Fakultas\t:")     

# class Identitas(Orang,Dosen,Universitas,Mahasiswa):
#     def __init__(self):
#         Orang.__init__(self)
#         Universitas.__init__(self)
#     def MahasiswaTa(self):
#         Mahasiswa.__init__(self)
#     def DosenTa(self):
#         Dosen.__init__(self)
#     def ubahNama(self):
#         self.nama = input("Masukkan nama\t\t:")
#     def __ubahUmur(self):
#         self.umur = input("Masukkan Umur\t\t:")

# identity = Identitas()
# identity.inputOrang()
# identity.inputUniv()

# while True:
#     pil = ['Mahasiswa', 'Dosen','Keluar']
#     print()
#     print("Pilihan")
#     for x,y in enumerate(pil,1):
#         print(f"{x}. {y}")
#     role = int(input("Masukkan role : "))
#     print()
#     if(role==1):       
#         print()
#         print(f"{'Memasukkan Data Mahasiswa':^50}")
#         identity.inputMahasiswa()
#         print()
#         que1 = input("Apakah ingin mengubah Nama ? (y/n):")
#         if(que1=="y"):
#             identity.ubahNama()
#         else : 
#             print("Tidak ada perubahan data Nama")
#         que2 = input("Apakah ingin mengubah Universitas ? (y/n):")
#         if(que2=="y"):
#             identity._Universitas__ubahUniv()
#         else : 
#             print("Tidak ada perubahan data Universitas")
#         que3 = input("Apakah ingin mengubah NIM ? (y/n) :")
#         if(que3=="y"):
#                 identity.ubahNim()
#         else : 
#             print("Tidak ada perubahan data NIM")
#         que4 = input("Apakah ingin mengubah Umur ? (y/n) :")
#         if(que4=="y"):
#                 identity._Identitas__ubahUmur()
#         else : 
#             print("Tidak ada perubahan data Umur")

#         print()
#         print(f"{'Menampilkan Data Mahasiswa':^50}")
#         identity.tampilData()
#         identity._Mahasiswa__tampilMahasiswa()
#         identity.tampilUniv()

#     elif(role==2):
#         print()
#         print(f"{'Memasukkan Data Dosen':^50}")
#         identity.inputDosen()
#         print()
#         que1 = input("Apakah ingin mengubah Nama ? (y/n):")
#         if(que1=="y"):
#             identity.ubahNama()
#         else : 
#             print("Tidak ada perubahan data Nama")
#         que2 = input("Apakah ingin mengubah Universitas ? (y/n):")
#         if(que2=="y"):
#             identity._Universitas__ubahUniv()
#         else : 
#             print("Tidak ada perubahan data Universitas")
#         que3 = input("Apakah ingin mengubah NIDN ? (y/n) :")
#         if(que3=="y"):
#                  identity._Dosen__ubahNIDN()
#         else : 
#             print("Tidak ada perubahan data NIDN")
#         que4 = input("Apakah ingin mengubah Umur ? (y/n) :")
#         if(que4=="y"):
#                 identity._Identitas__ubahUmur()
#         else : 
#             print("Tidak ada perubahan data Umur")
#         print(f"{'Menampilkan Data Dosen':^50}")
#         identity.tampilData()
#         identity._Dosen__tampilDosen()
#         identity.tampilUniv()
#         print("Mengajar\t : ",identity.mengajar)
#     else:
#         print("Berhasil Keluar!")
#         break


# class PemilikSaham:
#     def __init__(self):
#         self.ID_PemilikSaham = None
#         self.Nama_PemilikSaham = None
#         self.JumlahInvestasi = None
    
#     def Input_dataPemilikSaham(self):
#         print(f"{'Memasukkan Data Pemilik Saham ':^50}")
#         self.ID_PemilikSaham = input("Masukkan ID Pemilik Saham \t:")
#         self.Nama_PemilikSaham = input("Masukkan Nama Pemilik Saham \t:")
#         self.JumlahInvestasi = input("Masukkan JUmlah Investasi \t:")

#     def Tampil_dataPemilikSaham(self):
#         print(" ID pemilk saham \t: ", self.ID_PemilikSaham)
#         print(" Nama pemilik saham \t: ",self.Nama_PemilikSaham)
#         print(" Jumlah Investasi \t: ",self.JumlahInvestasi)

# class PemainSepakBola:
#     def __init__(self):
#         self.ID_Pemain = None
#         self.Nama_Pemain = None
#         self.Posisi = None
    
#     def Input_dataPemain(self):
#         print(f"{'Memasukkan Data Pemain Sepak Bola ':^50}")
#         self.ID_Pemain = input("Masukkan ID Pemain \t:")
#         self.Nama_Pemain = input("Masukkan Nama Pemain \t:")
#         self.Posisi = input("Masukkan Posisi \t:")

#     def Tampil_dataPemain(self):
#         print(" ID pemain \t\t: ", self.ID_Pemain)
#         print(" Nama pemain \t\t: ",self.Nama_Pemain)
#         print(" Posisi      \t\t: ",self.Posisi)

# class ClubSepakBola(PemilikSaham,PemainSepakBola):
#     def __init__(self):
#         self.ID_Club = None
#         self.Nama_Club = None
#         self.Nama_Pelatih = None
#     def Input_dataClub(self):
#         print(f"{'Memasukkan Data CLUB Sepak Bola':^50}")
#         self.ID_Club = input("Masukkan ID Club \t: ")
#         self.Nama_Club = input("Masukkan Nama Club \t: ")
#         self.Nama_Pelatih = input("Masukkan Nama Pelatih \t: ")
#     def Tampil_dataClub(self):
#         print(" ID Club     \t\t: ", self.ID_Club)
#         print(" Nama Club   \t\t: ",self.Nama_Club)
#         print(" Nama Pelatih\t\t: ",self.Nama_Pelatih)


# club1 = ClubSepakBola()
# club1.Input_dataPemilikSaham()
# club1.Input_dataPemain()
# club1.Input_dataClub()
# print()
# print()
# print(f"{'Menampilkan Data':^50}")
# club1.Tampil_dataPemilikSaham()
# club1.Tampil_dataPemain()
# club1.Tampil_dataClub()

  


