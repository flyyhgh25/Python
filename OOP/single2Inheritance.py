import math
class PrismaTrapesium:
    pt=0
    luasAlas = 0
    volume = 0
    def __init__(self,tinggi_trapesium,tinggi_prisma,sisi_sejajar1,sisi_sejajar2):
        self.tinggi_trapesium = tinggi_trapesium,
        self.tinggi_prisma = tinggi_prisma,
        self.sisi_sejajar1=sisi_sejajar1
        self.sisi_sejajar2=sisi_sejajar2
        
    def inputan(self):
        self.tinggi_trapesium=int(input("Masukkan tinggi sisi trapesium  : "))
        self.sisi_sejajar1=int(input("Masukkan sisi sejajar 1\t\t: "))
        self.sisi_sejajar2=int(input("Masukkan sisi sejajar 2\t\t: "))
        self.tinggi_prisma = int(input("Masukkan tinggi prisma\t\t: "))

    def luasAlas(self):
        self.luasAlasTrapesium = float(0.5*self.tinggi_trapesium*(self.sisi_sejajar1+self.sisi_sejajar2))
        return self.luasAlasTrapesium

    def kelilingAlas(self):
        a = self.sisi_sejajar2-self.sisi_sejajar1
        t = self.tinggi_trapesium
        sisi_miring_trapesium = math.sqrt((a*a)+(t*t))
        self.keliling_trapesium =  self.tinggi_trapesium+self.sisi_sejajar1+self.sisi_sejajar2+sisi_miring_trapesium
        return self.keliling_trapesium

    def volumePrismaTrapesium(self):    
        self.volume = float(self.luasAlas()*self.tinggi_prisma)
        print("Volume Prisma Trapesium : ",self.volume,"cm3")

    def luasPermukaanPrismaTrapesium(self):
        lpp = float(2*self.luasAlas()+(self.kelilingAlas()*self.tinggi_prisma))
        print(f" Luas Permukaan Prisma {lpp} cm2")

    def kelilingPrismaTrapesium(self):     
        kt = float((self.keliling_trapesium*2)+ (4*self.tinggi_prisma))
        print(f"Keliling prisma trapesium : {kt} cm")

    def pilihan(self):
        pilihan =int()
        while(pilihan<3):
            d = ['Menghitung Volume Prisma Trapesium','Menghitung Luas Permukaan Prisma Trapesium', 'Menghitung Keliling Prisma Trapesium','Keluar Program']
            print()
            print(f"{'*********PRISMA TRAPESIUM ********':^70}")
            print(f"{'=========PILIHAN============':^70}")
            for q,w in enumerate(d,1):
                print(f"\t\t{q}).{w}")
            x = int(input("Masukkan pilihan : "))
            if(x==1):
                print("\t\tMenghitung Volume Prisma Trapesium ")
                self.inputan()
                self.luasAlas()
                self.volumePrismaTrapesium()
            elif(x==2):
                print("\t\tMenghitung Luas Permukaan Prisma Trapesium ")
                self.inputan()
                self.kelilingAlas()
                self.luasPermukaanPrismaTrapesium()
            elif(x==3):
                print("\t\tMenghitung Keliling Prisma Trapesium ")
                self.inputan()
                self.kelilingAlas()
                self.kelilingPrismaTrapesium()
            else:
                print("Selesai Menggunakan Program!")
                break

x = PrismaTrapesium('','','','')
x.pilihan()
x.tinggi_prisma
x.tinggi_trapesium
x.sisi_sejajar1
x.sisi_sejajar2
