import tkinter as tk
import tkinter.ttk as ttk
import sys
import tkinter.filedialog as tfd
import tkinter.messagebox as msg
import time
from FileImp import FileImp
from GNaiveBayes import GNaiveBayes
from NaiveBayes import NaiveBayes
from Discretizer import Discretizer
from threading import Thread

class Interface:
    def __init__(self, top):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        __bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        __fgcolor = '#000000'  # X11 color: 'black'
        __compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        __ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.' ,background=__bgcolor)
        self.style.configure('.' ,foreground=__fgcolor)
        self.style.configure('.' ,font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', __compcolor), ('active',__ana2color)])

        top.geometry("495x532+663+175")
        top.title("Klasifikasi")
        top.configure(background="#d9d9d9")

        self.FrameDiskritisasi = tk.Frame(top)
        self.FrameDiskritisasi.place(relx=0.061, rely=0.038, relheight=0.254
                , relwidth=0.899)
        self.FrameDiskritisasi.configure(relief='groove')
        self.FrameDiskritisasi.configure(borderwidth="2")
        self.FrameDiskritisasi.configure(relief='groove')
        self.FrameDiskritisasi.configure(background="#d9d9d9")
        self.FrameDiskritisasi.configure(width=445)

        self.ButtonDiskritisasi = tk.Button(self.FrameDiskritisasi)
        self.ButtonDiskritisasi.place(relx=0.045, rely=0.222, height=24, width=97)
        self.ButtonDiskritisasi.configure(activebackground="#ececec")
        self.ButtonDiskritisasi.configure(activeforeground="#000000")
        self.ButtonDiskritisasi.configure(background="#d9d9d9")
        self.ButtonDiskritisasi.configure(disabledforeground="#a3a3a3")
        self.ButtonDiskritisasi.configure(foreground="#000000")
        self.ButtonDiskritisasi.configure(highlightbackground="#d9d9d9")
        self.ButtonDiskritisasi.configure(highlightcolor="black")
        self.ButtonDiskritisasi.configure(pady="0")
        self.ButtonDiskritisasi.configure(text='''Input Data''')
        self.ButtonDiskritisasi.configure(width=97)
        self.ButtonDiskritisasi.configure(command=self.setFileDiskrit)


        self.ProgressBar = ttk.Progressbar(top)
        self.ProgressBar.place(relx=0.37, rely=0.245)
        self.ProgressBar.configure(mode="indeterminate")
        self.ProgressBar.lower(self.FrameDiskritisasi)

        self.AlamatDiskritisasi = tk.Text(self.FrameDiskritisasi)
        self.AlamatDiskritisasi.place(relx=0.315, rely=0.222, relheight=0.278, relwidth=0.593)
        self.AlamatDiskritisasi.configure(background="white")
        self.AlamatDiskritisasi.configure(font="TkTextFont")
        self.AlamatDiskritisasi.configure(foreground="black")
        self.AlamatDiskritisasi.configure(highlightbackground="#d9d9d9")
        self.AlamatDiskritisasi.configure(highlightcolor="black")
        self.AlamatDiskritisasi.configure(insertbackground="black")
        self.AlamatDiskritisasi.configure(selectbackground="#c4c4c4")
        self.AlamatDiskritisasi.configure(selectforeground="black")
        self.AlamatDiskritisasi.configure(state='disabled')
        self.AlamatDiskritisasi.configure(width=264)
        self.AlamatDiskritisasi.configure(wrap='word')

        self.ButtonProsesDiskrit = tk.Button(self.FrameDiskritisasi)
        self.ButtonProsesDiskrit.place(relx=0.315, rely=0.593, height=24, width=127)
        self.ButtonProsesDiskrit.configure(activebackground="#ececec")
        self.ButtonProsesDiskrit.configure(activeforeground="#000000")
        self.ButtonProsesDiskrit.configure(background="#d9d9d9")
        self.ButtonProsesDiskrit.configure(disabledforeground="#a3a3a3")
        self.ButtonProsesDiskrit.configure(foreground="#000000")
        self.ButtonProsesDiskrit.configure(highlightbackground="#d9d9d9")
        self.ButtonProsesDiskrit.configure(highlightcolor="black")
        self.ButtonProsesDiskrit.configure(pady="0")
        self.ButtonProsesDiskrit.configure(text='''Diskritisasi Data''')
        self.ButtonProsesDiskrit.configure(width=127)
        self.ButtonProsesDiskrit.configure(command=self.buttonPressDiskrit)

        self.LabelWaktuDiskrit = tk.Label(top)
        self.LabelWaktuDiskrit.place(relx=0.59, rely=0.24, height=21, width=180)
        self.LabelWaktuDiskrit.configure(background="#d9d9d9")
        self.LabelWaktuDiskrit.configure(disabledforeground="#a3a3a3")
        self.LabelWaktuDiskrit.configure(foreground="#000000")
        self.LabelWaktuDiskrit.lower(self.FrameDiskritisasi)

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.061, rely=0.32, relheight=0.57, relwidth=0.899)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(width=445)

        self.LabelLatih = tk.Label(self.Frame2)
        self.LabelLatih.place(relx=0.045, rely=0.09, height=26, width=41)
        self.LabelLatih.configure(activeforeground="#000000")
        self.LabelLatih.configure(background="#d9d9d9")
        self.LabelLatih.configure(disabledforeground="#a3a3a3")
        self.LabelLatih.configure(font=font10)
        self.LabelLatih.configure(foreground="#000000")
        self.LabelLatih.configure(text='''Latih''')

        self.ButtonDataLatih = tk.Button(self.Frame2)
        self.ButtonDataLatih.place(relx=0.045, rely=0.179, height=24, width=117)
        self.ButtonDataLatih.configure(activebackground="#ececec")
        self.ButtonDataLatih.configure(activeforeground="#000000")
        self.ButtonDataLatih.configure(background="#d9d9d9")
        self.ButtonDataLatih.configure(disabledforeground="#a3a3a3")
        self.ButtonDataLatih.configure(foreground="#000000")
        self.ButtonDataLatih.configure(highlightbackground="#d9d9d9")
        self.ButtonDataLatih.configure(highlightcolor="black")
        self.ButtonDataLatih.configure(pady="0")
        self.ButtonDataLatih.configure(text='''Input Data Latih''')
        self.ButtonDataLatih.configure(width=117)
        self.ButtonDataLatih.configure(command=self.setFileLatih)

        self.AlamatDataLatih = tk.Text(self.Frame2)
        self.AlamatDataLatih.place(relx=0.382, rely=0.179, relheight=0.102
                , relwidth=0.503)
        self.AlamatDataLatih.configure(background="white")
        self.AlamatDataLatih.configure(font="TkTextFont")
        self.AlamatDataLatih.configure(foreground="black")
        self.AlamatDataLatih.configure(highlightbackground="#d9d9d9")
        self.AlamatDataLatih.configure(highlightcolor="black")
        self.AlamatDataLatih.configure(insertbackground="black")
        self.AlamatDataLatih.configure(selectbackground="#c4c4c4")
        self.AlamatDataLatih.configure(selectforeground="black")
        self.AlamatDataLatih.configure(state='disabled')
        self.AlamatDataLatih.configure(width=224)
        self.AlamatDataLatih.configure(wrap='word')

        self.ButtonLatih = tk.Button(self.Frame2)
        self.ButtonLatih.place(relx=0.315, rely=0.418, height=24, width=117)
        self.ButtonLatih.configure(activebackground="#ececec")
        self.ButtonLatih.configure(activeforeground="#000000")
        self.ButtonLatih.configure(background="#d9d9d9")
        self.ButtonLatih.configure(disabledforeground="#a3a3a3")
        self.ButtonLatih.configure(foreground="#000000")
        self.ButtonLatih.configure(highlightbackground="#d9d9d9")
        self.ButtonLatih.configure(highlightcolor="black")
        self.ButtonLatih.configure(pady="0")
        self.ButtonLatih.configure(text='''Latih Data''')
        self.ButtonLatih.configure(width=117)
        self.ButtonLatih.configure(command=self.latihData)

        self.Algorithm = tk.StringVar()
        self.TComboAlgoritma = ttk.Combobox(self.Frame2)
        self.TComboAlgoritma.place(relx=0.382, rely=0.299, relheight=0.063
                , relwidth=0.389)
        self.TComboAlgoritma.configure(textvariable='tes_support.combobox')
        self.TComboAlgoritma.configure(width=173)
        self.TComboAlgoritma.configure(takefocus="")
        self.TComboAlgoritma.configure(values=['Naive Bayes','Gaussian NB'])
        self.TComboAlgoritma.configure(state="readonly")
        self.TComboAlgoritma.configure(textvariable =self.Algorithm)
        self.TComboAlgoritma.bind('<<ComboboxSelected>>', self.checkBoxEnabler)

        self.LabelAlgoritma = tk.Label(self.Frame2)
        self.LabelAlgoritma.place(relx=0.045, rely=0.299, height=21, width=113)
        self.LabelAlgoritma.configure(background="#d9d9d9")
        self.LabelAlgoritma.configure(disabledforeground="#a3a3a3")
        self.LabelAlgoritma.configure(foreground="#000000")
        self.LabelAlgoritma.configure(text='''Algoritma Klasifikasi''')

        self.LabelUji = tk.Label(self.Frame2)
        self.LabelUji.place(relx=0.045, rely=0.567, height=26, width=25)
        self.LabelUji.configure(background="#d9d9d9")
        self.LabelUji.configure(disabledforeground="#a3a3a3")
        self.LabelUji.configure(font=font10)
        self.LabelUji.configure(foreground="#000000")
        self.LabelUji.configure(text='''Uji''')

        self.ButtonDataUji = tk.Button(self.Frame2)
        self.ButtonDataUji.place(relx=0.045, rely=0.657, height=24, width=117)
        self.ButtonDataUji.configure(activebackground="#ececec")
        self.ButtonDataUji.configure(activeforeground="#000000")
        self.ButtonDataUji.configure(background="#d9d9d9")
        self.ButtonDataUji.configure(disabledforeground="#a3a3a3")
        self.ButtonDataUji.configure(foreground="#000000")
        self.ButtonDataUji.configure(highlightbackground="#d9d9d9")
        self.ButtonDataUji.configure(highlightcolor="black")
        self.ButtonDataUji.configure(pady="0")
        self.ButtonDataUji.configure(text='''Input Data Uji''')
        self.ButtonDataUji.configure(width=117)
        self.ButtonDataUji.configure(command=self.setFileUji)

        self.Checker = tk.IntVar()
        self.CheckModelDiskrit = tk.Checkbutton(self.Frame2)
        self.CheckModelDiskrit.place(relx=0.034, rely=0.726, relheight=0.075
                                     , relwidth=0.333)
        self.CheckModelDiskrit.configure(activebackground="#ececec")
        self.CheckModelDiskrit.configure(activeforeground="#000000")
        self.CheckModelDiskrit.configure(background="#d9d9d9")
        self.CheckModelDiskrit.configure(disabledforeground="#a3a3a3")
        self.CheckModelDiskrit.configure(foreground="#000000")
        self.CheckModelDiskrit.configure(highlightbackground="#d9d9d9")
        self.CheckModelDiskrit.configure(highlightcolor="black")
        self.CheckModelDiskrit.configure(justify='left')
        self.CheckModelDiskrit.configure(state='disabled')
        self.CheckModelDiskrit.configure(text='''Gunakan Model Diskrit''')
        self.CheckModelDiskrit.configure(variable=self.Checker)


        self.AlamatDataUji = tk.Text(self.Frame2)
        self.AlamatDataUji.place(relx=0.382, rely=0.657, relheight=0.102
                , relwidth=0.503)
        self.AlamatDataUji.configure(background="white")
        self.AlamatDataUji.configure(font="TkTextFont")
        self.AlamatDataUji.configure(foreground="black")
        self.AlamatDataUji.configure(highlightbackground="#d9d9d9")
        self.AlamatDataUji.configure(highlightcolor="black")
        self.AlamatDataUji.configure(insertbackground="black")
        self.AlamatDataUji.configure(selectbackground="#c4c4c4")
        self.AlamatDataUji.configure(selectforeground="black")
        self.AlamatDataUji.configure(state='disabled')
        self.AlamatDataUji.configure(width=224)
        self.AlamatDataUji.configure(wrap='word')

        self.ButtonUji = tk.Button(self.Frame2)
        self.ButtonUji.place(relx=0.315, rely=0.806, height=24, width=117)
        self.ButtonUji.configure(activebackground="#ececec")
        self.ButtonUji.configure(activeforeground="#000000")
        self.ButtonUji.configure(background="#d9d9d9")
        self.ButtonUji.configure(disabledforeground="#a3a3a3")
        self.ButtonUji.configure(foreground="#000000")
        self.ButtonUji.configure(highlightbackground="#d9d9d9")
        self.ButtonUji.configure(highlightcolor="black")
        self.ButtonUji.configure(pady="0")
        self.ButtonUji.configure(text='''Uji Data''')
        self.ButtonUji.configure(width=117)
        self.ButtonUji.configure(command=self.ujiData)

        self.LabelDiskrit = tk.Label(top)
        self.LabelDiskrit.place(relx=0.101, rely=0.019, height=21, width=101)
        self.LabelDiskrit.configure(background="#d9d9d9")
        self.LabelDiskrit.configure(disabledforeground="#a3a3a3")
        self.LabelDiskrit.configure(font=font11)
        self.LabelDiskrit.configure(foreground="#000000")
        self.LabelDiskrit.configure(text='''DISKRITISASI''')
        self.LabelDiskrit.configure(width=101)

        self.LabelKlasifikasi = tk.Label(top)
        self.LabelKlasifikasi.place(relx=0.101, rely=0.301, height=21, width=109)

        self.LabelKlasifikasi.configure(activeforeground="#000000")
        self.LabelKlasifikasi.configure(background="#d9d9d9")
        self.LabelKlasifikasi.configure(disabledforeground="#a3a3a3")
        self.LabelKlasifikasi.configure(font=font10)
        self.LabelKlasifikasi.configure(foreground="#000000")
        self.LabelKlasifikasi.configure(text='''KLASIFIKASI''')
        self.LabelKlasifikasi.configure(width=109)

        self.LabelModelLatih = tk.Label(top)
        self.LabelModelLatih.place(relx=0.629, rely=0.56, height=21, width=116)
        self.LabelModelLatih.configure(background="#d9d9d9")
        self.LabelModelLatih.configure(disabledforeground="#a3a3a3")
        self.LabelModelLatih.configure(foreground="#000000")
        self.LabelModelLatih.configure(text='''Model Latih Tersedia''')
        self.LabelModelLatih.lower(self.Frame2)

        self.LabelWaktuLatih = tk.Label(top)
        self.LabelWaktuLatih.place(relx=0.61, rely=0.62, height=21, width=140)
        self.LabelWaktuLatih.configure(background="#d9d9d9")
        self.LabelWaktuLatih.configure(disabledforeground="#a3a3a3")
        self.LabelWaktuLatih.configure(foreground="#000000")
        self.LabelWaktuLatih.lower(self.Frame2)

        self.LabelWaktuUji = tk.Label(top)
        self.LabelWaktuUji.place(relx=0.6, rely=0.84, height=21, width=140)
        self.LabelWaktuUji.configure(background="#d9d9d9")
        self.LabelWaktuUji.configure(disabledforeground="#a3a3a3")
        self.LabelWaktuUji.configure(foreground="#000000")
        self.LabelWaktuUji.configure(text= "OMEGALUL3")
        self.LabelWaktuUji.lower(self.Frame2)

        self.LabelAkurasi = tk.Label(top)
        self.LabelAkurasi.place(relx=0.6, rely=0.76, height=21, width=140)
        self.LabelAkurasi.configure(background="#d9d9d9")
        self.LabelAkurasi.configure(disabledforeground="#a3a3a3")
        self.LabelAkurasi.configure(foreground="#000000")
        self.LabelAkurasi.configure(text="OMEGALUL")
        self.LabelAkurasi.lower(self.Frame2)


        self.LabelWaktuApply= tk.Label(top)
        self.LabelWaktuApply.place(relx=0.6, rely=0.80, height=21, width=140)
        self.LabelWaktuApply.configure(background="#d9d9d9")
        self.LabelWaktuApply.configure(disabledforeground="#a3a3a3")
        self.LabelWaktuApply.configure(foreground="#000000")
        self.LabelWaktuApply.configure(text="OMEGALUL2")
        self.LabelWaktuApply.lower(self.Frame2)

        self.ImportedFile = FileImp()
        self.ObjDiskrit = None
        self.NaiveBayes = None
        self.GNB = None
        self.Threadlist = []

    def setFileLatih(self):
        PathLatih = tfd.askopenfilename()
        self.AlamatDataLatih.config(state='normal')
        if PathLatih[-3:]=="csv":
            self.ImportedFile.setAlamatLatih(PathLatih)
            self.AlamatDataLatih.delete(1.0, tk.END)
            self.AlamatDataLatih.insert(1.0, self.ImportedFile.getAlamatLatih())
        elif PathLatih[-3:] != "csv" and PathLatih != "":
            msg.showerror("Terjadi Kesalahan", 'Format dataset salah, file harus berekstensi .csv!')
        self.AlamatDataLatih.config(state='disabled')

    def setFileUji(self):
        PathUji = tfd.askopenfilename()
        self.AlamatDataUji.config(state='normal')
        if PathUji[-3:]=="csv":
            self.ImportedFile.setAlamatUji(PathUji)
            self.AlamatDataUji.delete(1.0, tk.END)
            print(self.ImportedFile.getAlamatUji())
            self.AlamatDataUji.insert(1.0, self.ImportedFile.getAlamatUji())
        elif PathUji[-3:] != "csv" and PathUji != "":
            msg.showerror("Terjadi Kesalahan", 'Format dataset salah, file harus berekstensi .csv!')
        self.AlamatDataUji.config(state='disabled')

    def setFileDiskrit(self):
        PathDiskrit = tfd.askopenfilename()
        self.AlamatDiskritisasi.config(state='normal')
        if PathDiskrit[-3:]=="csv":
            self.ImportedFile.setAlamatDiskrit(PathDiskrit)
            self.AlamatDiskritisasi.delete(1.0, tk.END)
            self.AlamatDiskritisasi.insert(1.0, self.ImportedFile.getAlamatDiskrit())
        elif PathDiskrit[-3:] != "csv" and PathDiskrit != "":
            msg.showerror("Terjadi Kesalahan", 'Format dataset salah, file harus berekstensi .csv!')
        self.AlamatDiskritisasi.config(state='disabled')

    def buttonPressDiskrit(self):
        self.ButtonProsesDiskrit.configure(state='disabled')
        self.ButtonLatih.configure(state='disabled')
        self.ButtonUji.configure(state='disabled')
        try:
            self.ImportedFile.setDataDiskrit()
            self.ObjDiskrit = Discretizer(self.ImportedFile.getDataDiskrit())
            t = Thread(target=self.ObjDiskrit.train, name='thread1', daemon= True, args=(self,))
            t.start()
            self.Threadlist.append(t)
            print(self.Threadlist)
        except:
            msg.showerror("Terjadi Kesalahan", 'Dataset tidak bisa didiskritisasi, pastikan dataset sudah dimasukkan')
            self.ButtonProsesDiskrit.configure(state='normal')
            self.ButtonLatih.configure(state='normal')
            self.ButtonUji.configure(state='normal')
        print(self.ObjDiskrit)

    def latihData(self):
        if(self.Algorithm.get()=="Naive Bayes"):
            try:
                print("NB")
                self.ImportedFile.setDataLatih()
                print(self.ImportedFile.getDataLatih())
                self.NaiveBayes = NaiveBayes(self.ImportedFile.getDataLatih())
                latihstart = time.clock()
                self.NaiveBayes.latih()
                waktu = time.clock()-latihstart
                waktu = round(waktu,2)
                self.LabelWaktuLatih.configure(text="Waktu Latih: "+str(waktu)+" detik")
                self.LabelWaktuLatih.lift(self.Frame2)
                self.LabelModelLatih.lift(self.Frame2)
            except:
                msg.showerror("Terjadi Kesalahan",
                              "Pastikan dataset sudah diinput!")
        elif(self.Algorithm.get()=="Gaussian NB"):
            print(0)
            try:
                print("GNB")
                self.ImportedFile.setDataLatih()
                print(self.ImportedFile.getDataLatih())
                self.GNB = GNaiveBayes(self.ImportedFile.getDataLatih())
                latihstart = time.clock()
                self.GNB.latih()
                waktu = time.clock() - latihstart
                waktu = round(waktu, 2)
                self.LabelWaktuLatih.configure(text="Waktu Latih: " + str(waktu) + " detik")
                self.LabelWaktuLatih.lift(self.Frame2)
                self.LabelModelLatih.lift(self.Frame2)
            except:
                msg.showerror("Terjadi Kesalahan", "Pastikan dataset sudah diinput, dan bersifat numerik atau kontinyu!")
        else:
            msg.showerror("Terjadi Kesalahan", "Harap masukkan data atau pilih algoritma terlebih dahulu")

    def ujiData(self):
        if self.Checker.get() == 0:
            try:
                print(self.Algorithm.get())
                if self.Algorithm.get()=="Gaussian NB":
                    self.ImportedFile.setDataUji()
                    self.GNB.uji(self.ImportedFile.getDataUji(), self, self.ImportedFile)
                elif self.Algorithm.get()=="Naive Bayes":
                    self.ImportedFile.setDataUji()
                    self.NaiveBayes.uji(self.ImportedFile.getDataUji(), self, self.ImportedFile)
                else:
                    msg.showerror("Terjadi Kesalahan",
                                  "Data tidak bisa diuji pastikan data sudah diinput, dan model telah"
                                  "dibuat")
            except:
                msg.showerror("Terjadi Kesalahan", "Data tidak bisa diuji pastikan data sudah diinput, dan model telah"
                                                   "dibuat")

        elif self.Checker.get() == 1:
            try:
                self.ImportedFile.setDataUji()
                """filename = 'dsc2019.sav'
                loaded_dsc = pickle.load(open(filename, 'rb'))"""
                DscUji = Discretizer(self.ImportedFile.getDataUji())
                DscUji.applyUji(self.ObjDiskrit.getsplitvalue(),self)
                print("datadscuji1")
                #a = pd.read_csv('C://Users/halim/Documents/KULIAH/SEMESTER 8/uji344.csv')
                #print(a)
                #print("datadscuji2")
                #print(DscUji.getdf())
                self.NaiveBayes.uji(DscUji.getdf(), self, self.ImportedFile)
            except:
                msg.showerror("Terjadi Kesalahan", "Data tidak bisa diuji pastikan data sudah diinput, bersifat numerik, dan "
                                                   "model latih telah dibuat")

    def saveFile(self, namawindow):
        alamat = tfd.asksaveasfilename(title=namawindow)
        #self.ButtonUji.configure(state='normal')
        #self.ButtonLatih.configure(state='normal')
        return alamat

    def checkBoxEnabler(self, event=None):
        print('ok')
        if event:
            if self.Algorithm.get()=='Naive Bayes' and self.ObjDiskrit is not None:
                print('ok3')
                print(self.Checker)
                self.CheckModelDiskrit.configure(state="normal")
            else:
                self.CheckModelDiskrit.configure(state="disabled")

if __name__ == '__main__':
    root = tk.Tk()
    obj = Interface(root)
    root.mainloop()

