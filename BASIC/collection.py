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
        print(f"{'':=^57}")
        print(f"|Nama\t\t|Alias\t\t|Kelompok\t\t|")
        print(f"{'':=^57}")
        for k in self.listHero:
            print(f"|{k.nama}\t\t|{k.alias}\t\t|{k.kelompok}\t\t|")
        print(f"{'':=^57}")
        def panggilHero(pahlawan):
            assert(pahlawan.kelompok == "Avengers"), "Hero tidak bisa dipanggil."
            return print("Avengers Berkumpul!")   
        try:
            panggilHero(self.listHero[0])
        except AssertionError as error:
            print(error)
            print('Hero bukan bagian dari Avengers!')
        else:
            k = self.listHero[0].kelompok
            print("Hero bagian dari",k+'!')
        finally:
            print('Resume:')
            print(f"{'':=^57}")
            print(f"|Nama\t\t|Alias\t\t|Kelompok\t\t|")
            print(f"{'':=^57}")
            print(f"|{self.listHero[0].nama}\t\t|{self.listHero[0].alias}\t\t|{self.listHero[0].kelompok}\t\t|")
            print(f"{'':=^57}")

l = Hero('','','')
l.inputHero()
l.MenampilkanData()

