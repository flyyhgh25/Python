# Caesar Ciper (alphabets shift their order by a fixed number of positions.)
huruf = 'abcdefghijklmnopqrstuvxyz'
def encrypt_caesar(num, text):
    hasil = ' '
    for x in text.lower():
        try:
            i = (huruf.index(x) + num ) %26
            hasil += huruf[i]
        except ValueError:
            hasil +=  x
    return hasil.lower()

num = int(input("Masukkan jumlah inputan : "))
text = input("Masukkan inputan : ")
chiphertext = encrypt_caesar(num,text)
print("Text yang telah di enkode : ", chiphertext)

# DECRIPT

huruf = 'abcdefghijklmnopqrstuvxyz'
def decrypt_caesar(num, text):
    hasil = ' '
    for x in text.lower():
        try:
            i = (huruf.index(x) - num ) %26
            hasil += huruf[i]
        except ValueError:
            hasil +=  x
    return hasil.lower()

num = int(input("Masukkan jumlah inputan 2: "))
text = input("Masukkan inputan2 : ")
chiphertext = decrypt_caesar(num,text)
print("Text yang telah di dekode : ", chiphertext)