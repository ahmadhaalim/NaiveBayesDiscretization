import numpy as np
import time

class NaiveBayes:
    def __init__(self, data):
        self.__datalatih = data.copy()
        self.__uniqueClass = np.empty([1, 1])
        self.__classprob = {}
        self.__pxc ={}

    def latih(self):
        allcolumns = list(self.__datalatih)
        KolomKelas = allcolumns[-1]
        self.__uniqueClass = self.__datalatih.__getattr__(KolomKelas).unique()
        # CLASS LOOP
        i = 0
        while i < len(self.__uniqueClass):
            tempdf = self.__datalatih.loc[self.__datalatih.iloc[:, -1] == self.__uniqueClass[i]]
            tempdf = tempdf.reset_index(drop=True)
            tempprob = len(tempdf) / len(self.__datalatih)
            self.__classprob.update({self.__uniqueClass[i]: tempprob})
            dictcolumn = {}
            #COLUMN LOOP
            j = 0
            while j<len(allcolumns)-1:
                UniqueValues = self.__datalatih.__getattr__(allcolumns[j]).unique()
                #UNIQUE COLUMN VALUE LOOP
                tempdf2 = tempdf.iloc[:, [j, -1]]
                dictvalue = {}
                k = 0
                while k< len(UniqueValues):
                    tempdf3 = tempdf2.loc[tempdf2[allcolumns[j]]==UniqueValues[k]]
                    tempdf3 = tempdf3.reset_index(drop=True)
                    valueprob = len(tempdf3)/len(tempdf)
                    dictvalue.update({UniqueValues[k]:valueprob})
                    k+=1

                dictcolumn.update({j:dictvalue})
                j+=1
            self.__pxc.update({self.__uniqueClass[i]:dictcolumn})
            #[CLASS][COLUMNS][VALUE]
            i += 1


    def uji(self, data, interface, ImportedFile):
        ujistart = time.clock()
        datauji = data.copy()
        print("datauji")
        print(datauji)
        datapredik = datauji.copy()
        datapredik['PREDIKSI'] = 'NaN'
        allcolumns = list(datauji)
        #row
        i=0
        #print(len(datapredik))
        while i < len(datapredik):
            #print('baris'+str(i))
            probkelas = {}
            #class
            j=0
            while j<len(self.__uniqueClass):
                #print('kelas'+str(j))
                probpxc = []
                #column
                k=0
                while k<len(allcolumns)-1:
                    #print(self.UniqueClass[j],k,datapredik.iat[i,k])
                    #print('kolom' + str(k))
                    try:
                        print(self.__pxc[self.__uniqueClass[j]][k][datapredik.iat[i, k]])
                        probpxc.append(self.__pxc[self.__uniqueClass[j]][k][datapredik.iat[i, k]])
                        #prob.update({self.UniqueClass[j]:self.pxc[self.UniqueClass[j]][k][datapredik.iat[i,j]]})
                    except KeyError:
                        print("error")
                        probpxc.append(0)
                    k+=1
                #hitung prob pxc
                hasil = 1
                for x in probpxc:
                    hasil = hasil * x
                #hitung probabilitas satu baris ke suatu kelas
                prob = hasil * self.__classprob[self.__uniqueClass[j]]
                #menyimpan probabilitas kelas tertentu yang kemudian dibandingkan
                probkelas.update({self.__uniqueClass[j]:prob})
                j+=1
            predictrow = max(probkelas,key=probkelas.get)

            datapredik.at[i,'PREDIKSI']=predictrow
            i+=1

        waktu = time.clock() - ujistart
        waktu = round(waktu, 2)
        interface.LabelWaktuUji.configure(text="Waktu Uji: " + str(waktu) + " detik")
        interface.LabelWaktuUji.lift(interface.Frame2)
        print("datapredik")
        print(datapredik)
        ImportedFile.createTableCF(datauji, datapredik, self.__uniqueClass, interface)



"""
data = pd.read_csv('C:/Users/halim/Documents/KULIAH/SEMESTER 8/DATASET/latih1.csv')
tes = NaiveBayes(data)
tes.Latih()
data2 = pd.read_csv('C:/Users/halim/Documents/KULIAH/SEMESTER 8/DATASET/uji1.csv')
tes.Uji(data2)
"""
