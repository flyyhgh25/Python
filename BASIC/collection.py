class Hero(object):
    def __init__(self, nama=None, alias=None, kelompok=None):
        self.nama = nama
        self.alias = alias
        self.kelompok = kelompok
    def inputHero(self):
        self.listHero = []
        jml = int(input("Masukkan jumlah hero yang akan ditambahkan : "))
        for x in range(jml):
            print()
            print(f"=== Menambahkan Hero {x+1} ===")
            self.nama = input('Masukkan nama : ')
            self.alias = input('Masukkan alias : ')
            self.kelompok = input('Masukkan kelompok : ')
            self.listHero.append(Hero(self.nama,self.alias,self.kelompok))
    def MenampilkanData(self):
        print(self.listHero)
        print(f"=== Daftar superhero ===")
        print ("Hero pertama:", self.listHero[0].nama,"\n")
        for k in self.listHero:
            print("Nama: {}\nAlias: {}\nKelompok: {}\n".format(k.nama, k.alias, k.kelompok))

k = Hero('','','')
k.inputHero()
k.MenampilkanData()

