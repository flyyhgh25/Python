class Pegawai:
    def __init__(self):
        self.nip = input('Masukkan NIP :')
        setattr(Pegawai,'nip',self.nip)
        self.nama = input('Masukkan Nama :')
        setattr(Pegawai,'nama',self.nama)
        self.jabatan = input('Masukkan Jabatan (sekretaris/manajer):')
        setattr(Pegawai,'jabatan',self.jabatan)
        self.gaji_pokok = float(input('Masukkan Gaji Pokok :'))
        setattr(Pegawai,'gaji_pokok',self.gaji_pokok)
        self.tunjangan  = float(input('Masukkan Tunjangan :'))
        setattr(Pegawai,'tunjangan',self.tunjangan)
        self.pajak = float(input('Masukkan Pajak :'))
        setattr(Pegawai,'pajak',self.pajak)
    
    def Ubah_Jabatan(self):
        self.jabatan = input('Ubah Jabatan :')
    def Ubah_Gaji_Pokok(self):
        self.gaji_pokok = float(input('Ubah Gaji Pokok :'))
    def Gaji_Bersih(self):
        self.x = getattr(Pegawai,'gaji_pokok')-getattr(Pegawai,'pajak')+getattr(Pegawai,'tunjangan')
        setattr(Pegawai,'x',self.x)
        return getattr(Pegawai,'x')

    def tampilData(self):
        print("NIP : ",getattr(Pegawai,'nip' ))
        print("Nama : ",getattr(Pegawai,'nama'))
        print("Jabatan : ",getattr(Pegawai,'jabatan'))
        print("Gaji Pokok : ",getattr(Pegawai,'gaji_pokok'))
        print("Tunjangan : ",getattr(Pegawai,'tunjangan'))
        print("Pajak :",getattr(Pegawai,'pajak'))
        # print("Gaji Bersih : ",self.Gaji_Bersih())
    

class Sekretaris(Pegawai):
    def __init__(self):
        self.upah_lembur = float(input('Masukkan Upah Lembur Pegawai :'))

    def Ubah_Upah(self):
        self.upah_lembur = float(input('Ubah Upah Lembur Pegawai:'))
    
    def Gaji_Bersih(self):
        Pegawai.Gaji_Bersih(self)
        print("Gaji Bersihnya : ", Pegawai.Gaji_Bersih(self))
    
    def tampilData(self):
        Pegawai.tampilData(self)
        print("Upah : ",self.upah_lembur)

class Manajer(Pegawai):
    def __init__(self):
        self.bonus = float(input('Masukkan Bonus Manajer :'))
    
    def Ubah_Bonus(self):
        self.bonus = float(input('Ubah Bonus Manajer :'))
    
    def Gaji_Bersih(self):
        print("Gaji Bersihya : ", Pegawai.Gaji_Bersih(self))
    
    def tampilData(self):
        Pegawai.tampilData(self)
        print("Bonus : ",self.bonus)
    
class Main:
    while True:
        print("---------------------------------------------")
        print("=================DATA PEGAWAI===================")
        print("---------------------------------------------")
        np =Pegawai()
        np.Gaji_Bersih()
        menuy = input("Apakah ingin mengubah Jabatan?(y/t) : ")
        if(menuy=="y"):
            np.Ubah_Jabatan()
            if(np.jabatan=="sekretaris"):
                print("---------------------------------------------")
                print("===================SEKRETARIS======================")
                print("---------------------------------------------")
                sek = Sekretaris()   
                pillk = ['Ubah Gaji Pokok', 'Ubah Upah','tidak']
                for x,y in enumerate(pillk,1):
                    print(f"{x}). {y}")
                menu1 = int(input("Masukkan pilihan   : "))
                if(menu1==1):
                    np.Ubah_Gaji_Pokok()
                    sek.Gaji_Bersih()
                    sek.tampilData()
                    break
                elif(menu1==2):
                    sek.Ubah_Upah()
                    sek.Gaji_Bersih()
                    sek.tampilData()
                    break
                else:
                    sek.Gaji_Bersih()
                    sek.tampilData()
                    break
            elif(np.jabatan=="manajer"):
                print("---------------------------------------------")
                print("===================MANAJER======================")
                print("---------------------------------------------")
                se = Manajer()
                pillkk = ['Ubah Gaji Pokok', 'Ubah Bonus','tidak']
                for x,y in enumerate(pillkk,1):
                    print(f"{x}). {y}")
                menu1 = int(input("Masukkan pilihan   : "))
                if(menu1==1):
                    np.Ubah_Gaji_Pokok()
                    se.Gaji_Bersih()
                    se.tampilData()
                    break
                elif(menu1==2):
                    se.Ubah_Bonus()
                    se.Gaji_Bersih()
                    se.tampilData()
                    break
                else:
                    se.Gaji_Bersih()
                    se.tampilData()
                break
        else:
            if(np.jabatan=="sekretaris"):
                print("---------------------------------------------")
                print("===================SEKRETARIS======================")
                print("---------------------------------------------")
                sek = Sekretaris()   
                pill = ['Ubah Gaji Pokok', 'Ubah Upah','tidak']
                for x,y in enumerate(pill,1):
                    print(f"{x}). {y}")
                menu1 = int(input("Masukkan pilihan ?  : "))
                if(menu1==1):
                    np.Ubah_Gaji_Pokok()
                    sek.Gaji_Bersih()
                    sek.tampilData()
                    break
                elif(menu1==2):
                    sek.Ubah_Upah()
                    sek.Gaji_Bersih()
                    sek.tampilData()
                    break
                else:
                    sek.Gaji_Bersih()
                    sek.tampilData()
                break
            elif(np.jabatan=="manajer"):
                print("---------------------------------------------")
                print("===================MANAJER======================")
                print("---------------------------------------------")
                se = Manajer()
                pill = ['Ubah Gaji Pokok', 'Ubah Bonus','tidak']
                for x,y in enumerate(pill,1):
                    print(f"{x}). {y}")
                menu1 = int(input("Masukkan pilihan   : "))
                if(menu1==1):
                    np.Ubah_Gaji_Pokok()
                    se.Gaji_Bersih()
                    se.tampilData()
                    break
                elif(menu1==2):
                    se.Ubah_Bonus()
                    se.Gaji_Bersih()
                    se.tampilData()
                    break
                else:
                    se.Gaji_Bersih()
                    se.tampilData()
                break