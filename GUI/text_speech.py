import pyttsx3
import tkinter as tk
import PyPDF2, pikepdf
root = tk.Tk()

class display():
    def __init__(self):
        canvas = tk.Canvas(root, height=12000, width=12000)
        canvas.pack(fill='both', expand = True)
        root.title('Text Speech')
        self.title_frame = tk.Frame(canvas).place(relheight=0.1,relwidth=0.5,relx=0.3, rely=0.1)
        tk.Label(self.title_frame,font =('Castellar',20,'bold'),fg='black',text="TEXT SPEECH, Let's Speak").place(relx=0.35, rely=0.1)
        self.main_frame = tk.Frame(canvas,bg='#52594F',bd=5,relief='groove').place(relheight=0.7,relwidth=0.5,relx=0.25, rely=0.2)
        
class TextVoice(display):
    def __init__(self):
        self.configure = pyttsx3.init()
        display.__init__(self)
    def Perintah(self):
        tk.Label(self.main_frame,text='Masukkan kalimat yang akan dijadikan suara',font=('Poppin',15),bg='#52594F').place(relx=0.35, rely=0.23)
        self.textD = tk.Text(self.main_frame,font=('Poppin',12))
        self.textD.place(relx=0.30, rely=0.30,relwidth=0.4,relheight=0.2)
        self.audio = tk.Button(self.main_frame,text='Dengarkan audio',bg='black',font=('Poppin',13),width=25,fg='white',command=lambda:self.Dengar()).place(relx=0.31,rely=0.5)
        self.simpan = tk.Button(self.main_frame,text='Simpan audio',bg='black',font=('Poppin',13),width=25,fg='white',command=lambda:self.Simpan()).place(relx=0.507,rely=0.5)
    def Dengar(self):
        self.getText = self.textD.get("1.0", "end-1c")
        self.configure.say(self.getText)
        self.configure.runAndWait()
    def Simpan(self):
        self.new_audio = self.textD.get("1.0", "end-1c")
        self.configure.save_to_file(self.new_audio,'myaudio.mp3')
        self.configure.runAndWait()

class ReadVoice(TextVoice):
    def __init__(self):
        TextVoice.__init__(self)
    def Perintah(self):
        self.buku = 'C:/Users/My Laptop/Downloads/Give and Take.pdf'
        self.textF = self.OpenFile(self.buku)
        self.judul = self.buku.strip().replace("C:/Users/My Laptop/Downloads/","").replace(".pdf","")
        tk.Label(self.main_frame,text=f'Buku {self.judul}',font=('Poppin',15),bg='#52594F').place(relx=0.42, rely=0.55)
        tk.Label(self.main_frame,text=f'Masukkan halaman',font=('Poppin',10),bg='#52594F').place(relx=0.31, rely=0.57)
        self.no_hal = tk.IntVar()
        self.hal = tk.Entry(self.main_frame,textvariable = self.no_hal).place(relx=0.31,rely=0.6,relheight=0.049,relwidth=0.18)
        self.audio = tk.Button(self.main_frame,text='Dengarkan audio',bg='black',font=('Poppin',13),width=25,fg='white',command=lambda:self.Dengar()).place(relx=0.507,rely=0.6)
        self.simpan = tk.Button(self.main_frame,text='Lihat Isi',bg='black',font=('Poppin',13),width=25,fg='white',command=lambda:self.LihatIsi()).place(relx=0.40,rely=0.68)
    def OpenFile(self,file_path):
        self.file_path = file_path
        self.file = open(self.file_path,"rb")
        self.pdf_reader = PyPDF2.PdfFileReader(self.file)
        return self.pdf_reader
    def LihatIsi(self):
        self.page = self.textF.getPage(self.no_hal.get())
        self.text = self.page.extractText()
        print(self.text)
        tk.Label(self.main_frame,text=f'{self.text}',font=('Poppin',5),bg='#52594F',fg='white').place(relx=0.1, rely=0.65,relwidth=0.75,relheight=0.4)
    def Dengar(self):
        self.LihatIsi()
        self.configure.say(self.text)
        self.configure.runAndWait()

x = TextVoice()
x.Perintah()
y = ReadVoice()
y.Perintah()
root.mainloop()