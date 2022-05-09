x = 1
y=int(input("Masukkan jumlah mahasiswa: "))
y+=1
nomor_list =[]
nama_list = []
alamat_list = []
prodi_list=[]
while(x<y): 
    print(f"{x:=^100}")
    nomor_list.append(x)
    nama = input("Masukkan nama : ")
    nama_list.append(nama)
    alamat = input("Masukkan Alamat : ")
    alamat_list.append(alamat)
    prodi = input("Masukkan Prodi : ")
    prodi_list.append(prodi)
    x+=1
datas = {
    'nomor' : nomor_list,
    'nama' : nama_list,
    'alamat' :alamat_list,
    'prodi' :prodi_list
}
k =''
print(f"{k:=^97}")
for index in datas.keys():
    print("|",f"{index:^20}", end='\t')
print('|')
print(f"{k:=^97}")
for x in range(len(datas['nomor'])):
    print(f"|{datas['nomor'][x]:<20}\t|{datas['nama'][x]:<20}\t|{datas['alamat'][x]:<20}\t|{datas['prodi'][x]:<20}\t|")
print(f"{k:=^97}")