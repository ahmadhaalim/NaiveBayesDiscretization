import numpy as np
import math as mt
import time
import pandas as pd

class GNaiveBayes:
    def __init__(self, data):
        self.__datalatih = data.copy()
        self.__meanClass = {}
        self.__stdClass = {}
        self.__uniqueClass = np.empty([1, 1])
        self.__classprob = {}

    def latih(self):

        print(self.__datalatih)
        '''GaussianNB.fit(self.datalatih)'''
        allcolumns = list(self.__datalatih)
        KolomKelas = allcolumns[-1]
        self.__uniqueClass = self.__datalatih.__getattr__(KolomKelas).unique()
        i = 0

        while i < len(self.__uniqueClass):
            print(self.__uniqueClass[i])
            tempprob = len(self.__datalatih.loc[self.__datalatih.iloc[:, -1] == self.__uniqueClass[i]]) / len(self.__datalatih)
            self.__classprob.update({self.__uniqueClass[i]: tempprob})
            i += 1

        i = 0
        j = 0

        while i < len(self.__uniqueClass):
            tdf = self.__datalatih.loc[self.__datalatih.iloc[:, -1] == self.__uniqueClass[i]]
            while j < (len(self.__datalatih.columns) - 1):
                mean = tdf.iloc[:, j].mean()
                standardeviasi = tdf.iloc[:, j].std()
                self.__meanClass.update({(self.__uniqueClass[i], self.__datalatih.columns[j]): mean})
                self.__stdClass.update({(self.__uniqueClass[i], self.__datalatih.columns[j]): standardeviasi})
                j += 1
            j = 0
            i += 1
        print("LATIH SELESAI")
        print(self.__stdClass)


    def uji(self, data):
        ujistart = time.clock()
        i = 0
        datauji = data.copy()
        datapredik = datauji.copy()
        datapredik['PREDIKSI'] = 'NaN'
        totalprob = {}

        while i < len(datauji):
            j = 0
            while j < len(self.__uniqueClass):
                k = 0
                pxctotal = 1
                while k < len(datauji.columns) - 1:

                    x = datauji.iat[i, k]

                    try:
                        epower = (-(mt.pow((x - self.__meanClass[self.__uniqueClass[j], datauji.columns[k]]), 2) / (
                                2 * mt.pow(self.__stdClass[self.__uniqueClass[j], datauji.columns[k]], 2))))
                        pxc = (1 / (mt.sqrt(2 * mt.pi) * self.__stdClass[self.__uniqueClass[j], datauji.columns[k]])) * mt.pow(mt.e,
                                                                                                                               epower)
                    except ZeroDivisionError:
                        epower = (-(mt.pow(x - self.__meanClass[self.__uniqueClass[j], datauji.columns[k]], 2) / (
                                2 * 0.00001)))
                        pxc = (1 / (mt.sqrt(2 * mt.pi) * 0.00001)) * mt.pow(mt.e, epower)
                        """
                        print(self._stdClass[self._uniqueClass[j], datauji.columns[k]])
                        print(self._uniqueClass[j] + " " + datauji.columns[k])
                        """
                    pxctotal = pxctotal * pxc
                    k += 1
                totalprob.update({self.__uniqueClass[j]: (pxctotal * self.__classprob[self.__uniqueClass[j]])})

                j += 1

            m = 0
            big = 0
            while m < len(totalprob):
                if big < totalprob[self.__uniqueClass[m]]:
                    big = totalprob[self.__uniqueClass[m]]
                    datapredik.at[i, 'PREDIKSI'] = self.__uniqueClass[m]
                m += 1

            i += 1
        waktu = time.clock() - ujistart
        waktu = round(waktu, 2)
        tabelcf = pd.DataFrame(0, self.__uniqueClass, self.__uniqueClass)
        print(tabelcf)
        i = 0
        while i < len(datapredik):
            tabelcf.at[datapredik.iat[i, -1], datapredik.iat[i, -2]] = tabelcf.at[
                                                                           datapredik.iat[i, -1], datapredik.iat[
                                                                               i, -2]] + 1
            i += 1
        # Total sum per row:
        tabelcf.loc['Total', :] = tabelcf.sum(axis=0)
        # Total sum per column:
        tabelcf.loc[:, 'Total'] = tabelcf.sum(axis=1)
        i = 0
        TPTN = 0
        while i < (len(tabelcf) - 1):
            TPTN = TPTN + tabelcf.iat[i, i]
            i += 1
        accuracy = TPTN / len(datauji)
        tesa = accuracy*100
        tesa = "{0:.2f}".format(tesa)
        print("Accuracy= {}".format(accuracy))
        print(tabelcf)





# trainfile = pd.read_csv('C:/Users/halim/Documents/KULIAH/SEMESTER 7/Dataset Numerik/avila/avila/avila-tr.csv')
# GNB = GNaiveBayes(trainfile)
# GNB.latih()
# testfile = pd.read_csv('C:/Users/halim/Documents/KULIAH/SEMESTER 7/Dataset Numerik/avila/avila/avila-ts.csv')
# GNB.uji(testfile)



