import tkinter as tk
master=tk.Tk()
master.title("SEGETIGA")
tk.Label(master,text="Alas").grid(row=0)
tk.Label(master,text="Tinggi").grid(row=1)
tk.Label(master,text="Sisi miring").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

def luas_segitiga():
	txt_alas = int(e1.get())
	txt_tinggi =int(e2.get())
	luas_segitiga =1/2*txt_alas*txt_tinggi
	tk.Label(master,text=f"Luas:{luas_segitiga}").grid(row=4, columnspan=2)
	# tk.Label(master, text=txt_tinggi).grid(row=5, columnspan=2)
    
bt_luas = tk.Button(master, text='Luas', command=luas_segitiga)
bt_luas.grid(row=6, column=0, sticky=tk.W, pady=7)



def keliling_segitiga():
	txt_alas =int(e1.get())
	txt_tinggi =int(e2.get())
	txt_sisi_miring =int(e3.get())
	keliling_segitiga = txt_alas + txt_tinggi + txt_sisi_miring
	tk.Label(master, text=f"Keliling:{keliling_segitiga}").grid(row=4, columnspan=2)
	# tk.Label(master, text=txt_tinggi).grid(row=5, columnspan=2)
	# tk.Label(master, text=txt_sisi_miring).grid(row=6, columnspan=2)

bt_keliling = tk.Button(master, text='Keliling', command=keliling_segitiga)
bt_keliling.grid(row=7, column=0, sticky=tk.W, pady=8)

# def inputan_hasil():
# 	txt_alas = "Alas : %s"%(e1.get())
# 	txt_tinggi = "Tinggi : %s"%(e2.get())
# 	txt_sisi_miring = "Sisi miring : %s"%(e3.get())
# 	keliling_segitiga = txt_alas + txt_tinggi + txt_sisi_miring
# 	tk.Label(master, text=txt_alas).grid(row=4, columnspan=2)
# 	tk.Label(master, text=txt_tinggi).grid(row=5, columnspan=2)
# 	tk.Label(master, text=txt_sisi_miring).grid(row=6, columnspan=2)

# bt_hasil = tk.Button(master, text='Tampilkan inputan dan hasil', command=inputan_hasil)
# bt_hasil.grid(row=8, column=0, sticky=tk.W, pady=9)
master.mainloop()