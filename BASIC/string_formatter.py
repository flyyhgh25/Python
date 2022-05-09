
print("I has {} ballons.".format(5))
mystring = "I love {0} because he is very {2} and {1}!"
print(mystring.format("Cha eun wo", "funny", "cool"))

# percent format
# {0:.1f} untuk membulatkan angka
# {0:.1f} angka tidak dibulatkan. di ambil angka terakhir
# {0:.0f}  hasil int buat float
print("I ate {0:.1f} percent of a sate!".format(75.784452))
print("I ate {0:.3f} percent of a sate!".format(75.784452))
print("I ate {0:.0f} percent of a sate!".format(75.784452))

# < will left-align the text in a field, ^ will center the text in the field, and > will right-align it.

print("I have {0:<4} red {1:^16}!".format(5,"ballons"))
print("{:*^40}".format("Sammy"))
print("{:*^60}".format("Sammy is nice cool, good, diligent"))

print("Sammy ate {0:8.0f} percent of a pizza!".format(7105.765367))
print("Sammy ate {0:20.1f} percent of a pizza!".format(75.765367))

a = int(input("Masukkan nomor 1 : "))
b = int(input("Masukkan nomor 2 : "))
hasil = 1/2*a*b
print("Hasil : {0:.0f} ".format(hasil))