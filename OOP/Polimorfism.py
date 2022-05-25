class Buku():
    def __init__(self):
        print(f"{'====== MEMASUKKAN DATA BUKU=====':^60}")
        self.penulis = input("Masukkan Penulis Buku \t\t: ")
        setattr(Buku,'penulis',self.penulis)
        self.penerbit = input("Masukkan Penerbit Buku \t\t:")
        setattr(Buku,'penerbit',self.penerbit)
        self.tahun_terbit = input("Masukkan Tahun Terbit Buku \t:")
        setattr(Buku,'tahun_terbit',self.tahun_terbit)

    def jenis(self):
        print('Isi Buku Fiksi/Non Fiksi')
        self.jenis = input("Masukkan Jenis Buku :")
        setattr(Buku,'jenis',self.jenis)
    
    def tampilData(self):
        print(f"Penulis buku \t\t: {getattr(Buku,'penulis')}")
        print(f"Penerbit buku \t\t: {getattr(Buku,'penerbit')}")
        print(f"Tahun Terbit buku\t: {getattr(Buku,'tahun_terbit')}")
        print(f"Jenis Buku \t\t: {getattr(Buku,'jenis')}")

class Novel(Buku):
    def __init__(self):
        print()
        print(f"{'====== BUKU NOVEL=====':^60}")
    def jenis(self):
        print('Isi Jenis Buku Novel Romantis/Komedi/Misteri')
        self.jenis = input("Masukkan Jenis Buku \t:")
        setattr(Buku,'jenis',self.jenis)
    def tampilData(self):
        print(f"{'====== MENAMPILKAN BUKU NOVEL=====':^60}")
        return super().tampilData()

class Pelajaran(Buku):
    def __init__(self):
        print()
        print(f"{'====== BUKU PELAJARAN=====':^60}")
    def jenis(self):
        print('Isi Jenis Buku Social/Bahasa/Science')
        self.jenis = input("Masukkan Jenis Buku \t:")
        setattr(Buku,'jenis',self.jenis)
    def tampilData(self):
        print(f"{'====== MENAMPILKAN BUKU PELAJARAN=====':^60}")
        return super().tampilData()

c = Buku()
c.jenis()
while True:
    opsi = ['Novel  ','Pelajaran','Keluar']
    print()
    print("\t\t\tOPSI")
    print(f"\t\t{'':=^26}")
    for x,y in enumerate(opsi,1):
        print(f"\t\t|| \t{x}.{y}\t||")
    print(f"\t\t{'':=^26}")
    pil = int(input("Masukkan Pilihan : "))
    if pil==1:
        d = Novel()
        d.jenis()
        d.tampilData()
    elif pil==2:
        e = Pelajaran()
        e.jenis()
        e.tampilData()
    else:
        print(f"{'Keluar Program':^50}")
        break

# import math
# class BangunDatar():
#     def __init__(self):
#         print(f"{'====Menghitung Luas dan Keliling Lingkaran Bangun Datar====':^100}")
#         self.keliling = None
#         self.luas = None
#     def HitungLuas(self):
#         self.luas= 0
#         setattr(BangunDatar,'luas',self.luas)
#     def HitungKeliling(self): 
#         self.keliling = 0
#         setattr(BangunDatar,'keliling',self.keliling)
#     def tampilData(self):
#         print("Luas     \t: ",getattr(BangunDatar,'luas'),'cm')
#         print("Keliling \t: ",getattr(Lingkaran,'keliling',self.keliling),'cm')
#         print(f"{'':_^50}")

# class Lingkaran(BangunDatar):
#     def __init__(self):
#         print()
#         print(f"{'======Menghitung Luas dan Keliling Lingkaran=====':^60}")
#         self.jari_jari = float(input("Masukkan jari-jari(cm)\t : "))
#         self.phi = float(input("Masukkan PHI\t\t : "))
#     def HitungLuas(self):
#         self.luas = self.phi*self.jari_jari*self.jari_jari
#         setattr(BangunDatar,'luas',self.luas)
#     def HitungKeliling(self):
#         self.keliling = 2*self.phi*self.jari_jari
#         setattr(BangunDatar,'keliling',self.keliling)
#     def tampilData(self):
#         print(f"{'':_^50}")
#         print()
#         print(f"{'Hasil Luas dan Keliling Lingkaran':^50}")
#         return super().tampilData() 

# class Segitiga(BangunDatar):
#     def __init__(self):
#         print()
#         print(f"{'=====Menghitung Luas dan Keliling segitiga=====':^60}")
#         self.alas = float(input("Masukkan alas segitiga(cm)\t\t: "))
#         self.tinggi = float(input("Masukkan tinggi segitiga(cm)\t\t: "))
#     def HitungLuas(self):
#         self.luas = float(0.5*self.alas*self.tinggi)
#         setattr(BangunDatar,'luas',self.luas)
#     def HitungKeliling(self):
#         self.simir = math.sqrt(pow(0.5*self.alas,2)+pow(self.tinggi,2))
#         self.keliling = float(self.alas+(2*self.simir))
#         setattr(BangunDatar,'keliling',self.keliling)
#     def tampilData(self):
#         print(f"{'':_^50}")
#         print()
#         print(f"{'Hasil Luas dan Keliling Segitiga ':^50}")
#         return super().tampilData() 

# c = BangunDatar()
# c.HitungLuas() 
# c.HitungKeliling()
# while True:
#     opsi = ['Lingkaran','Segitiga','Keluar']
#     print()
#     print("\t\t\tOPSI")
#     print(f"\t\t{'':=^26}")
#     for x,y in enumerate(opsi,1):
#         print(f"\t\t|| \t{x}.{y}\t||")
#     print(f"\t\t{'':=^26}")
#     pil = int(input("Masukkan Pilihan : "))
#     if pil==1:
#         d = Lingkaran()
#         d.HitungLuas()
#         d.HitungKeliling()
#         d.tampilData()
#     elif pil==2:
#         e = Segitiga()
#         e.HitungLuas()
#         e.HitungKeliling()
#         e.tampilData()
#     else:
#         print(f"{'Keluar Program':^50}")
#         break


