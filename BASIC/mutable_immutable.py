# IMMUTABLE
def PartTuple():
    tuple1 = (1,2,3,4,5)
    print(f"id tuple sebelum diubah : {id(tuple1)}")
    tuple1 += (6,)
    id(f"id tuple setelah diubah : {id(tuple1)}")

    set = {1,5,7,8}
    print(f"id set sebelum diubah : {id(set)}")
    set.add(3)
    print(f"id set setelah diubah : {id(set)}")
    # IMPLEMENTASI
    # # mencetak data tuple 
    tuple3 = (1,2,3,9,9,4)
    print(tuple3[3])
    print(tuple3[-3])
    print(tuple3[1:])
    for x in tuple3:
        print(x, end=' ')
    print()
    print(tuple3.count(9))
    print(tuple3.index(9))
    print(len(tuple3))
    member = 4 in tuple3
    print(member)
    print("Max : ",max(tuple3))
    print("Min : ",min(tuple3))
    # concatination tuple (penambhan)
    tuple3 = (1,2,3,9,9,4)
    tuple3+=(7,)
    tuple3+=(2,0)
    print(tuple3)
    tuple4 = (5,5,2,6,2,7)
    tuple5 = tuple3+tuple4
    print(tuple5)
    # convert data tuple ke dalam variable
    x,y,q,a=(4,2,6,1)
    print(q,y,x)
    # tuple key/value pairs convert kedalam dictionary
    tuple6 = dict([('jan',1),('feb',2),('march',3),])
    print(tuple6)
    print(tuple6['jan'])
    # mutable tuple
    # immutable tidak sepenuhnya immutable
    tuple7 = (1,5,7,[4,5,6,9],9,0,1)
    tuple7[3][3] = 10
    print(tuple7)
    # repetition
    tuple8 = ("Good Morning Everybody")
    repetition = tuple8*5
    print("Perulanganya yaitu : ",repetition)
    tuple9 = ("saya","makan","nasi")
    join_tuple = ' '.join(tuple9)
    print(join_tuple)
    # convert list to tuple
    list = [2,4,6,8]
    tuple10 = tuple(list)
    print(tuple10)
    tuple11 = (1,2,3,4)
    tuple12 = (1,2,3,4)
    print(tuple11==tuple12)
    tuple13 = (2,4,6,7)
    # hapus tuple
    del tuple13
    tuple13=(6,5,6,7)
    print(tuple13)

# (MUTABLE)
def PartSet():
    # SET 
    print("SET")
    set = {1,2,3,4,5}
    for data in set:
        print(data,end='')
    print()
    print(len(set))
    print(3 in set)
    print(3 not in set)
    # issubset 
    a= {1,2,3,4,5,6,7,8,9}
    b={7,9,3,4,10}
    print(b<=a)
    # atau # semua isi data dari set a merupakan keanggotaan dari set b
    print(b.issubset(a))
    # issuperset semua isi data dari set b merupakan keanggotaan dari set a,
    print(a>=b)
    print(b.issuperset(a))
    # set union (menggabungkan semua isi a dan b)
    print("Union :", a.union(b))
    # set intersection (bagian b yang ada di isi a)
    print("Intersection :", a.intersection(b)) 
    # difference # data a yang tidak ada di b
    print("Difference :", a.difference(b))
    # symmetic difference data yang tidak sama pada keduanya
    print("Symmetric :", a.symmetric_difference(b))
    # meng copy element set b ke set c
    a= {1,2,3,4,5,6,7,8,9}
    b={7,9,3,4,10}
    c = b.copy()
    print(c)
    # menambah element set b
    b.add(10)
    print(b)
    # menghapus element set dengan nilai 3
    d= {9,3,5,7}
    d.remove(3)
    print(d)
    print(d.discard(7))
    # menghapus dan mengambil nilai element pertama pada set
    print(d.pop())
    print(d)
    # update set
    e={"nanas","mangga","salak"}
    d.update(e) 
    #memasukkan nilai tersebut dengan gabungan nilai isi di d dan isi di e
    print(d)
    # set.intersection_update(otherset) atau set &= otherset 
    d= {9,3,5,7}
    f = {7,2,1,6}
    d &= (f)  #mengambil isi data dengan nilai yang samaa antara d dan f
    print(d)
    # n set.difference_update(otherset) atau set -= otherset
    j= {9,3,5,7}
    k = {7,2,1,6}
    j -=(k)
    print(j) #  isi data j yang tidak ada dalam f
    l= {9,3,5,7}
    m = {7,2,1,6}
    # menggabungkan semua nilai. tidak ada duplikat
    l ^=(m)
    print(l)
    # menghapus semua element set
    a = {1,2,3,4,5}
    a.clear()
    print(a)


def PartDictionary():
    # mendefinisikan dict
    dictt = {'a': 'alpha','b':'beta','o':'omega'}
    print(dictt)
    # menambahkan dict kosong
    dicttt={}
    dicttt['a'] ='alpha',
    dicttt['b']='beta',
    dicttt['o'] = 'omega'
    # contructor
    dictionary = dict(a='alpha',b='beta',o='omega')
    print(dictionary)
    dec = dict([('a','alpha'),('b','beta'),('o','omega')])
    print(dec)
    dicts = dict(zip(['a','b','o'],['alpha','beta','omega']))
    print(dicts)
    # mencetak data
    print(dicts['a'])
    for data in dictt:
        print(data,end=' ')
    print()
    for index,data in dictt.items():
        print("index ke %s adalah %s"%(index,data))
    for index in dictt.keys():
        print("index ke %s"%(index))
    for data in dictt.values():
        print("data %s"%(data))
    # len
    print(len(dictt))
    member = "b" in dictt.keys()
    print(member)
    member = "omega" in dictt.values()
    print(member)
    member = "d" in dictt.keys()
    print(member)
    member = "omegot" not in dictt.values()
    print(member)
    # copy dict
    new_dict = dictt.copy()
    print(id(dictt))
    print(id(new_dict))
    new_dict['a']="Helloow"
    print(new_dict)
    print(id(new_dict))
    # mengubah niai element dict
    dictt['b'] = 'octal'
    print(dictt)
    # reset nilai
    newest = dict.fromkeys(new_dict,"Heyoo")
    print(newest)
    # mengambil element
    element_beta = new_dict.pop('a')
    print(element_beta)
    print(new_dict)
    # penggabungan dictionary
    new_dict={'c':'penta'}
    dictt.update(new_dict)
    print(dictt)
    # delte element
    del dictt['o']
    print(dictt)
    # latihan
    ujian = {
        'Mady':8,
        'Roger':5,
        'Paul':5,
        'Lucy':7
    }
    print("{:^50}".format('1) Nilai Ujian UTS Konsep Pemrograman Hari Pertama'))
    for x,y in ujian.items():
        print("{:>25} = {}".format(x,y))
        
    ujian_susulan = {
        'Ken':8,
        'Andrea':7,
        'Smith':6
    }
    print("{:^40}".format('2) Nilai Ujian UTS Konsep Pemrograman Hari Kedua'))
    for x,y in ujian_susulan.items():
        print("{:>25} = {}".format(x,y))
    ujian.update(ujian_susulan)
    new_data = ujian
    print("{:^50}".format('3) Nilai Ujian UTS Konsep Pemrograman Hari Pertama dan  Kedua'))
    for x,y in new_data.items():
        print("{:>25} = {}".format(x,y))
    new_data['Roger'] = 8
    new_data['Smith'] = 8
    new_data['Paul'] = 8
    print("{:^50}".format('4) Nilai Ujian UTS Konsep Pemrograman Setalah dilakukan Remidial'))
    for x,y in new_data.items():
        print("{:>25} = {}".format(x,y))
    print("{:^10}".format('5) Nilai Ujian 8 ke atas'))
    print('\t\t{:_^17}'.format(''))
    print('\t\t|%s\t|%s\t|'%('Nama','Nilai'))
    print('\t\t{:+^17}'.format(''))
    for x,y in new_data.items():
        if(y>=8):
            print('\t\t|%s\t|%s\t|'%(x,y))
    print('\t\t{:=^17}'.format(''))

def PartList():
    # menampilkan isi list yang mempunyai index tertentu
    list = [1,2,3,4,3,3,5]
    print(list[3])

    # menampilkan semua list
    for x in list:
        print(x)
    print(list.count(3))

    # cek index isi list
    print(list.index(2))

    # cek banyaknya anggota list
    print(len(list))

    # cek anggota list
    member = 5 in list
    print(member)
    notmember = 5 not in list
    print(notmember)

    # nilai maximal dan minimal
    max = max(list)
    min = min(list)
    print(f"Max:{max} Min:{min}")

    # menambahkan list
    list+=[6,]
    print(list)

    # penambahan pada index tertentu
    list.insert(5,9)
    print(list)

    # penambahan index paling akhir
    list.append(10)
    print(list)

    # penggabungan list
    list1 = [3,5,6,7,7]
    penggabungan = list+list1
    print(penggabungan)

    # penggabungan 2 list lebih dengan extend
    list.extend(list1)
    print(list)
    list.extend('slow')
    print(list)

    # convert list
    x,y,k = [3,4,5]
    print(f"{x},{y},{k}")

    # merubah ddata
    list2 = [3,5,6,[6,8,3],0,9]
    list2[3][1]=10
    print(list2)

    # repetititon and join
    list3 = ['GM Everybody']
    repeat = ' '.join(list3*4)
    print(repeat)

    # convert list ke tuple
    list4 = [2,4,5,6]
    tuple = tuple(list4)
    print(tuple)

    # operator perbandingan
    list1 = [1,2,3,4,5]
    list2 = [1,2,3,4,5]
    print(list1==list2)

    # mengahus data list
    list1.remove(2)
    print(list1)

    # mengambil element/data list
    list1.pop() #index terakhir
    list1.pop(2) #index ke 2
    # mengurutkan
    print(sorted(list4))
    print(sorted(list4,reverse=True))

    # copy list
    list = [1,4,3,5,2]
    id(list)
    list_new = list
    id(list_new)
    list_copy = list.copy()
    id(list_copy)
    print(list_new)
    print(list_copy)
    # hapus semua element list
    list_new.clear()
    print(list_new)





def Implementasi():
       # CARA SIMPLE
        Tweedledoom = {
            "tanggal_lahir" : ('1861-10-23'),
            "kemampuan" : ['Bersyair','Menyanyi','Suka Berpura-pura']
        }
        Tweedledee = {
            "tanggal_lahir" : ('1861-10-23'),
            "kemampuan" : ['Bersyair','Menyanyi','Suka Berpura-pura']
        }
        print("Profile Tweedledoom")
        print("Tanggal Lahir Tweedledoom : ", Tweedledoom['tanggal_lahir'])
        print('Kemampuan : ')
        for x in Tweedledoom['kemampuan']:
            print('\t~ ',x)
        print("{0:=^120}".format(''))

        print("Profile Tweedledee")
        print("Tanggal Lahir Tweedledee : ", Tweedledee['tanggal_lahir'])
        print('Kemampuan : ')
        for x in Tweedledee['kemampuan']:
            print('\t~ ',x)

        # b
        Tweedledee['kemampuan'][0] = "Memanah"
        print("Profile Tweedledee")
        print("Tanggal Lahir Tweedledee : ", Tweedledee['tanggal_lahir'])
        print('Kemampuan : ')
        for x in Tweedledee['kemampuan']:
            print('\t~ ',x)
        #  kemampuan[0] = 'Memanah'
        # print("Tanggal Lahir : ", tanggal_lahir)
        # print('Kemampuan : ')
        # for x in kemampuan:
        #     print('\t~ ',x)

        # CARA RIBET
        profile = {
            "Tweedledoom" : {
                "tanggal_lahir" : ('1861-10-23'),
                "kemampuan" : ['Bersyair','Menyanyi','Suka Berpura-pura']
                },
            "Tweedledee" : {
                "tanggal_lahir" : ('1861-10-23'),
                "kemampuan" : ['Bersyair','Menyanyi','Suka Berpura-pura']
                }
        }
        print("{0:=^120}".format('Profile Tweedledom'))
        print(f"Tanggal Lahir \t: {profile['Tweedledoom']['tanggal_lahir']}") 
        print("Kemampuan \t: ")
        for x,y in enumerate(profile['Tweedledoom']['kemampuan'],1):
            print(f"\t\t {x}.{y}")
        print()
        print("{0:=^120}".format('Profile Tweedledee'))
        print(f"Tanggal Lahir \t: {profile['Tweedledee']['tanggal_lahir']}") 
        print("Kemampuan \t: ")
        for x in profile['Tweedledee']['kemampuan']:
            print(f"\t\t  ✔{x}")
        # mengganti bersyair menjadi memanah
        profile['Tweedledee']['kemampuan'][0] = "Memanah"
        print()
        print("{0:=^120}".format('Profile Tweedledee'))
        print(f"Tanggal Lahir \t: {profile['Tweedledee']['tanggal_lahir']}") 
        print("Kemampuan \t: ")
        for x in profile['Tweedledee']['kemampuan']:
            print(f"\t\t  ✔{x}")

        print("{0:=^120}".format('A'))
        hari_pertama = {'keju','tepung','garam','gula','coklat'}
        hari_kedua = {'garam','gula','coklat','kecap'}
        print("pembelian hari pertama :", hari_pertama)
        print('pembelian hari kedua : ',hari_kedua)
        print("{0:=^120}".format('B'))
        hari_kedua.add('keju')
        print("Pembelian hari kedua setelah penambahan keju : ", hari_kedua)
        print("{0:=^120}".format('C'))
        sama = hari_pertama.intersection(hari_kedua)
        print("Barang yang sama pada pembelian hari pertama dan pembelian hari kedua :", sama)
        print("{0:=^120}".format('D'))
        beda = hari_pertama.difference(hari_kedua)
        print("Barang yang dibeli di hari pertama akan tetapi tidak dibeli pada hari kedua :", beda)
        print("{0:=^120}".format('E'))
        h_g = hari_pertama.remove('garam')
        print("Pembelian hari pertama setelah garam dihapus :", hari_pertama)
        print("{0:=^120}".format('F','K'))
        f = hari_kedua.difference(hari_pertama)
        print("Barang yang dibeli pada hari kedua akan tetapi tidak dibeli di hari pertama :", f)
        print("{0:=^120}".format('G'))
        h = hari_kedua.symmetric_difference(hari_pertama)
        print("Barang  yang tidak sama pada pembelian hari pertama dan pembelian hari kedua:", h)
        print("{0:=^120}".format('H'))
        print('Barang yang dibeli pada hari pertama :')
        for i,x in enumerate(hari_pertama,1):
            print('\t',i, x)
        print("{0:=^120}".format('I'))
        print('Barang yang dibeli pada hari kedua :')
        for j,k in enumerate(hari_kedua,1):
            print('\t',j, k)
























