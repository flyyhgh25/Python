class Mahasiswa:
    def __init__(self,nama,nim,alamat,jenis_kelamin,status):
        self.__nim = input("Masukkan NIM : ")
        setattr(Mahasiswa,'__nim',self.__nim)
        self.nama =  input("Masukkan Nama : ")
        self.alamat =  input("Masukkan Alamat : ")
        self.jenis_kelamin =  input("Masukkan Jenis Kelamin : ")
        self.status = input("Masukkan Status : ")
    def __tampilData(self):
        print("Namanya : ", self.nama)
        print("Alamatnya : ", self.alamat)
        print("Jenis Kelaminya : ", self.jenis_kelamin)
        print("Statusnya : ", self.status)

class Pendidikan(Mahasiswa):
    def __init__(self,nama, nim, alamat, jenis_kelamin, status):
        Mahasiswa.__init__(self,nama, nim, alamat, jenis_kelamin, status)
 
    def __fk(self):
        
        self.nama_universitas = input("Masukkan Nama Universsitas : ")
        self.prodi = input("Masukkan Prodi : ")
        self.fakultas = input("Masukkan Fakultas : ")
    
    def TampilAll(self):
        print()
        print("NIMnya : ", getattr(Mahasiswa,'__nim'))
        self._Mahasiswa__tampilData()
        print("Nama universitasnya :",self.nama_universitas)
        print("Nama prodinya :",self.prodi)
        print("Nama Fakultasnya :",self.fakultas)
    
biodata1 = Pendidikan('','','','','')
biodata1._Pendidikan__fk()
biodata1.TampilAll()

    