import pandas as pd
class FileImp:
    def __init__(self):
        self.__alamatLatih = ""
        self.__alamatUji = ""
        self.__alamatDiskrit = ""
        self.__dataLatih = None
        self.__dataUji = None
        self.__dataDiskrit = None

    def setAlamatLatih(self, Alamat):
        self.__alamatLatih = Alamat

    def setAlamatUji(self, Alamat):
        self.__alamatUji = Alamat

    def setAlamatDiskrit(self, Alamat):
        self.__alamatDiskrit = Alamat

    def setDataLatih(self):
        self.__dataLatih = pd.read_csv(self.__alamatLatih).round(6)

    def setDataUji(self):
        self.__dataUji = pd.read_csv(self.__alamatUji).round(6)

    def setDataDiskrit(self):
        self.__dataDiskrit = pd.read_csv(self.__alamatDiskrit).round(6)

    def getDataLatih(self):
        return self.__dataLatih

    def getDataUji(self):
        return self.__dataUji

    def getDataDiskrit(self):
        return self.__dataDiskrit

    def getAlamatLatih(self):
        return self.__alamatLatih

    def getAlamatUji(self):
        return self.__alamatUji

    def getAlamatDiskrit(self):
        return self.__alamatDiskrit

    def createTableCF(self, datauji, datapredik, UniqueClass, interface):
        tabelcf = pd.DataFrame(0, UniqueClass, UniqueClass)
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
        interface.LabelAkurasi.configure(text="Akurasi: "+tesa+"%")
        interface.LabelAkurasi.lift(interface.Frame2)
        print("Accuracy= {}".format(accuracy))
        print(tabelcf)
        alamathasilpredik = interface.saveFile("Simpan Data Hasil Klasifikasi")
        datapredik.to_csv(alamathasilpredik + ".csv", index=False)
        alamatmatrixakurasi = interface.saveFile("Simpan Data Confusion Matrix dan Akurasi")
        tabelcf["AKURASI"] = ""
        tabelcf.iat[0, -1] = accuracy
        tabelcf.to_csv(alamatmatrixakurasi + ".csv")


