import tkinter as tk
def utama():
    global master
    master = tk.Tk()
    master.title("Program Biodata")
    tk.Label(master,text="Nama Depan").grid(row=0)
    tk.Label(master,text="Nama tengah").grid(row=1)
    tk.Label(master,text="Nama Belakang").grid(row=2)
    global e1,e2,e3
    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    tk.Button(master,command=show_data,text="Show").grid(row=3,column=0,sticky="w")
    master.mainloop()

def show_data():
    tk.Label(master,text=f"Nama Lengkap : {e1.get()} {e2.get()} {e3.get()}").grid(row=4)

utama()



