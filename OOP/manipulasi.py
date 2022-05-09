class Mahasiswa:
    jmlMhs=0
    def __init__(self,nama,prodi,nim,kelamin,fakultas):
        self.nama = nama
        self.prodi = prodi
        self.nim = nim
        self.kelamin = kelamin
        self.fakultas = fakultas
        Mahasiswa.jmlMhs+=1
    def tampilJml(self):
        print("total Mahasiswa: ",Mahasiswa.jmlMhs)
    def tampilProfil(self):
        print("Nama : ", self.nama)
        print("Prodi : ", self.prodi)
        print("NIM : ", self.nim)
        print("Kelamin : ", self.kelamin)
        print("Fakultas : ",self.fakultas)
        print()


mhs1 = Mahasiswa('Adi','Teknik','2121039','','')
nama = input(" Nama:")
prodi = input(" Prodi:")
nim = input("NIM :")
jk = input("Kelamin :")
fk = input("Fakultas :")
setattr(mhs1,"nama",nama)
setattr(mhs1,"prodi",prodi)
setattr(mhs1,"nim",nim)
setattr(mhs1,"kelamin",jk)
setattr(mhs1,"fakultas",fk)
print()
print("Namanya :",getattr(mhs1,'nama'))
print("Prodinya :",getattr(mhs1,'prodi'))
print("NIMnya :",getattr(mhs1,'nim'))
print("Jenis Kelaminya :",getattr(mhs1,'kelamin'))
print("Fakultas :",getattr(mhs1,'fakultas'))
delattr(mhs1,'nama')
delattr(mhs1,'prodi')
delattr(mhs1,'nim')
delattr(mhs1,'kelamin')
delattr(mhs1,'fakultas')
print()
print("Namanya :",hasattr(mhs1,'nama'))
print("Prodinya :",hasattr(mhs1,'prodi'))
print("NIMnya :",hasattr(mhs1,'nim'))
print("Jenis Kelaminya :",hasattr(mhs1,'kelamin'))
print("Fakultas :",hasattr(mhs1,'fakultas'))
print()
# mhs1.tampilProfil()
mhs1.tampilJml()




class Sepeda():
    rem="berhenti"
    jarak_awal=0
    waktu_awal=0
    spd = 0
    def __init__(self,warna,merk,roda):
        self.warna = warna,
        self.merk = merk,
        self.roda = roda
    def jalan(self):
        Sepeda.rem ="jalan"
        print(f"\t\tSepeda {Sepeda.rem} ............................")
    def stop(self):
        Sepeda.rem ="berhenti"
        print(f"\t\tSepeda {Sepeda.rem} ............................")

    def kecepatan(self,jarak,waktu):
        if(Sepeda.rem=="jalan"):
            jarak= Sepeda.jarak_awal+getattr(Sepeda,'jarak')
            print(f"\t\tSepeda telah berjalan pada jarak {jarak} km")
            waktu = Sepeda.waktu_awal+waktu
            print(f"\t\tSepeda telah telah menempuh waktu selama {waktu} jam")
            self.v =float(jarak/waktu) 
        else:
            self.v = 0
        print("\t\tKecepatan Sepeda : ", self.v, "km/jam")

    def delAtribut(self):
        print("\t__Hapus Atribut Sepeda__")
        delattr(Sepeda,'warna')
        delattr(Sepeda,'merk')
        
    def hasAtribut(self):
        print("\t__Cek Atribut Sepeda__")
        print(f"Warna sepeda  {hasattr(Sepeda,'warna')}")
        print(f"Merk sepeda  {hasattr(Sepeda,'merk')}")

    def getAtribut(self):
        print("\t__Detail Sepeda__")
        print(f"Warna sepeda  {getattr(Sepeda,'warna')}")
        print(f"Merk sepeda  {getattr(Sepeda,'merk')}")

    def setAtribut(self):
        Sepeda.spd+=1
        print()
        print(f"\t=== Sepeda {Sepeda.spd} ===")
        self.warna = input("Masukkan warna sepeda : ")
        self.merk = input("Masukkan merk sepeda : ")
        self.roda = int(input("Masukkan roda sepeda : "))  
        setattr(Sepeda,'warna',self.warna)
        setattr(Sepeda,'merk',self.merk)
 
sepeda2 = Sepeda('','','')
sepeda2.setAtribut()
sepeda2.getAtribut()
sepeda2.delAtribut()
sepeda2.hasAtribut()
