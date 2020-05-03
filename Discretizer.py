import math as mt
import numpy as np
import time


class Discretizer:

    def __init__(self, data):
         self.__df = data.copy()
         self.__allcolumns = []
         self.__uniqueClass = np.empty([1, 1])
         self.__splitter = {}
         self.__splitValue = []

    def train(self, interface):
        traintimestart = time.clock()
        interface.ProgressBar.lift(interface.FrameDiskritisasi)
        interface.ProgressBar.start()
        self.__allcolumns = list(self.__df)
        '''MENDAPATKAN BANYAK KELAS UNIK DALAM DF'''
        self.__uniqueClass = self.getUniqueClass(self.__df)
        i = 0
        while i < len(self.__allcolumns)-1:
            print(i)
            self.__splitter = {}
            '''KOLOM while i < 1: 'KOLOM '''
            self.__df = self.__df.sort_values(self.__allcolumns[i])
            self.__df = self.__df.reset_index(drop=True)
            df = self.__df.iloc[:, [i, -1]]
            self.splitting(df, self.__uniqueClass)
            applier = list(self.__splitter.values())
            applier.sort()
            self.__splitValue.append(applier)

            '''print(i)
            print('SPLITTER')
            print(self.splitter)'''
            self.apply(applier, i)

            i += 1
        self.__df = self.__df.reset_index(drop=True)
        prosestime = time.clock()-traintimestart
        prosestime = round(prosestime,2)
        interface.LabelWaktuDiskrit.configure(text = "Waktu Proses: "+str(prosestime)+" detik")
        interface.LabelWaktuDiskrit.lift(interface.FrameDiskritisasi)
        alamat = interface.saveFile("Simpan Dataset Hasil Diskritisasi")
        self.__df.to_csv(alamat + ".csv", index=False)
        interface.ButtonProsesDiskrit.configure(state='normal')
        interface.ButtonUji.configure(state='normal')
        interface.ButtonLatih.configure(state='normal')
        interface.ProgressBar.stop()
        interface.ProgressBar.lower(interface.FrameDiskritisasi)

        print(self.__df)
        print(self.__splitValue)

    def getUniqueClass(self, df):
        allcolumns = list(df)
        KolomKelas = allcolumns[-1]
        UniqueClass = df.__getattr__(KolomKelas).unique()
        return UniqueClass

    def getdf(self):
        return self.__df

    def getsplitvalue(self):
        return self.__splitValue

    def splitting(self, df, UniqueClass):
        '''MENGHITUNG PROB TIAP KELAS'''
        ClassProb = self.hitungProbKelas(df, UniqueClass)
        '''MENGHITUNG ENTROPY KELAS'''
        ClassEntropy = self.hitungEntropy(UniqueClass, ClassProb)
        PotSplitGain = {}
        j = 0
        while j < (len(df) - 1):
            '''BARIS 10 DATA len(df)'''
            try:
                if df.iat[j, -1] != df.iat[j + 1, -1]:
                    if df.iat[j, 0] != df.iat[j + 1, 0]:
                        '''calculate entropy & calculate the gain'''
                        s1 = df.iloc[:j + 1]
                        s2 = df.iloc[(j + 1):]
                        s1UniqueClass = self.getUniqueClass(s1)
                        s2UniqueClass = self.getUniqueClass(s2)
                        s1ProbKelas = self.hitungProbKelas(s1, s1UniqueClass)
                        s2ProbKelas = self.hitungProbKelas(s2, s2UniqueClass)
                        s1Entropy = self.hitungEntropy(s1UniqueClass, s1ProbKelas)
                        s2Entropy = self.hitungEntropy(s2UniqueClass, s2ProbKelas)
                        splitEntropy = ((len(s1) / len(df)) * s1Entropy) + ((len(s2) / len(df)) * s2Entropy)
                        Gain = ClassEntropy - splitEntropy
                        PotSplitGain.update({j: Gain})
            except IndexError:
                print('INDEX ERROR')

            j += 1

        if PotSplitGain != {}:
            MaxGain = max(PotSplitGain, key=PotSplitGain.get)
            s1 = df.iloc[:MaxGain + 1]
            s2 = df.iloc[(MaxGain + 1):]
            s1UniqueClass = self.getUniqueClass(s1)
            s2UniqueClass = self.getUniqueClass(s2)
            s1ProbKelas = self.hitungProbKelas(s1, s1UniqueClass)
            s2ProbKelas = self.hitungProbKelas(s2, s2UniqueClass)
            s1Entropy = self.hitungEntropy(s1UniqueClass, s1ProbKelas)
            s2Entropy = self.hitungEntropy(s2UniqueClass, s2ProbKelas)
            splitEntropy = ((len(s1) / len(df)) * s1Entropy) + ((len(s2) / len(df)) * s2Entropy)
            Gain = ClassEntropy - splitEntropy
            DeltaATS = mt.log2(mt.pow(3, len(UniqueClass)) - 2) - ((len(UniqueClass) * ClassEntropy) -
                                                                   (len(s1UniqueClass) * s1Entropy) -
                                                                   (len(s2UniqueClass) * s2Entropy))
            MinimalGain = (mt.log2(len(df) - 1) / len(df)) + (DeltaATS / len(df))

            if Gain > MinimalGain:
                self.__splitter.update({MaxGain: df.iat[MaxGain, 0]})
                'print(self.splitter)'
                self.splitting(s1, s1UniqueClass)
                self.splitting(s2, s2UniqueClass)

    def hitungProbKelas(self, df, UniqueClass):
        classprob = {}
        k = 0
        'MENGHITUNG PROB TIAP KELAS'
        while k < len(UniqueClass):
            tempprob = len(df.loc[df.iloc[:, -1] == UniqueClass[k]]) / len(df)
            classprob.update({UniqueClass[k]: tempprob})
            k += 1
        return classprob

    def hitungEntropy(self, UniqueClass, ClassProb):
        l = 0
        entropy = 0
        while l < len(UniqueClass):
            entropy = entropy + (ClassProb[UniqueClass[l]] * mt.log2(ClassProb[UniqueClass[l]]))
            l += 1
        entropy = -entropy
        return entropy

    def apply(self, applier, i):
        'print(type(applier[0]))'
        'print(applier)'
        j = 0
        k = 0
        #loop bnyak split
        while k < len(applier):
            'print(j)'
            while j < len(self.__df):
                if self.__df.iat[j, i] <= applier[k]:
                    if k != 0:
                        self.__df.iloc[j:j + 1, i:i + 1] = str(applier[k - 1]) + "<=X<=" + str(applier[k])
                    elif k == 0:
                        self.__df.iloc[j:j + 1, i:i + 1] = 'Inf<=X<=' + str(applier[k])

                else:

                    if k == (len(applier) - 1):
                        while j < len(self.__df):
                            self.__df.iloc[j:j + 1, i:i + 1] = str(applier[k]) + "<=X<=Inf"
                            j += 1
                    break

                j += 1
            k += 1

    def applyUji(self, splitValue, interface):
        applystart = time.clock()
        self.__allcolumns = list(self.__df)
        i = 0
        while i <len(splitValue):
            self.__df = self.__df.sort_values(self.__allcolumns[i])
            self.__df = self.__df.reset_index(drop=True)
            applier  = splitValue[i]
            print(i)
            print(splitValue[i])
            self.apply(applier, i)
            i+=1
        print(self.__df)
        waktu = time.clock() - applystart
        waktu = round(waktu, 2)
        interface.LabelWaktuApply.configure(text="Waktu Apply: " + str(waktu) + " detik")
        interface.LabelWaktuApply.lift(interface.Frame2)
        alamat = interface.saveFile("Simpan Dataset Hasil Diskritisasi Uji")
        self.__df.to_csv(alamat + ".csv", index=False)



'''
dsc = Discretizer('C:/Users/halim/Documents/KULIAH/SEMESTER 7/Dataset Numerik/avila/avila/avila-tr2.csv')
dsc.train()
dscuji = Discretizer('C:/Users/halim/Documents/KULIAH/SEMESTER 7/Dataset Numerik/avila/avila/avila-ts.csv')
dscuji.ApplyUji(dsc.splitValue)
print(dscuji.df)
dscuji.df.to_csv(r'C://Users/halim/Documents/KULIAH/SEMESTER 8/uji1.csv',index=False)

filename = 'dsc2019.sav'
pickle.dump(dsc, open(filename, 'wb'))

loaded_dsc = pickle.load(open(filename,'rb'))'''