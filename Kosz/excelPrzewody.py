# coding=utf-8
# -*- coding: utf-8 -*-
from tkinter import messagebox

import pandas as pd
import numpy as np
import os

pd.set_option('display.max_columns', 10000)

class excelPrzewody:

    def __init__(self, import_path, export_path, import_sheet_name, export_sheet_name):

        self.sep = "."
        self.import_path = import_path
        self.import_sheet_name = import_sheet_name
        self.export_path = export_path
        self.export_sheet_name = export_sheet_name
        self.df = pd.DataFrame()
        self.oblicz_ilosc()

    def oblicz_ilosc(self):
        """
        Typy poziomów:      [0, 1, 2, 3, 4]
        Mnożnik:            [0, 0, 0, 0, 0]

        :return:
        """

        try:
            self.df = pd.read_excel(self.import_path, sheet_name=self.import_sheet_name)
            # print("Wczytano plik")
        except:
            # print("Błąd wczytywania pliku: ", self.import_path)
            messagebox.showerror("Błąd wczytywania pliku: ", self.import_path)

        # Pobranie danych z tabeli do obróbki
        self.setSep()
        poziom = self.df["Pozycja"].apply(lambda x: x.count(self.sep)).get_values()
        ilosc = self.df["ILOŚĆ"].get_values()

        ilosc_docelowa = []
        typy_poziomow = np.unique(poziom)
        mnoznik = np.zeros(typy_poziomow.__len__())

        for i in range(0, self.df.__len__()):

            for j in range(0, typy_poziomow.__len__()):

                # warunki
                zgodnosc_poziomow = (poziom[i] == typy_poziomow[j])
                poziom_zero = (poziom[i] == 0)
                powrot_poziom_nizej = (poziom[i] < poziom[i-1])
                poziom_wyzej = (poziom[i] > poziom[i-1])
                ten_sam_poziom = (poziom[i] == poziom[i-1])

                if poziom_zero & zgodnosc_poziomow:
                    # print("poziom zero: ",mnoznik)
                    mnoznik = np.zeros(typy_poziomow.__len__())
                    mnoznik[poziom[j]] = ilosc[i]
                    ilosc_docelowa.append(ilosc[i])

        #            print(i, poziom[i], "==", poziom[i-1])
        #            print("\t", mnoznik)

                elif powrot_poziom_nizej & zgodnosc_poziomow:


                    mnoznik[typy_poziomow[j]] = mnoznik[poziom[j-1]] * ilosc[i]
                    # print("poziom w gore: ", mnoznik)
                    print(self.df.Pozycja[i],mnoznik)
                    """
                     roznica_poziomow = poziom[i-1]-poziom[i]
                    for x in range(0, mnoznik.__len__()):
                        if x > roznica_poziomow:
                            mnoznik[x] = 1
                    """
                    ilosc_docelowa.append(mnoznik[typy_poziomow[j]])


        #            print(i, poziom[i], "<", poziom[i-1])
        #            print("\t", mnoznik)


                elif poziom_wyzej & zgodnosc_poziomow:
                    mnoznik[typy_poziomow[j]] = ilosc_docelowa[i-1]
                    ilosc_docelowa.append(ilosc_docelowa[i-1] * ilosc[i])

        #            print(i, poziom[i], ">", poziom[i-1])
        #            print("\t", mnoznik)


                elif ten_sam_poziom & zgodnosc_poziomow:
                    oblicz = mnoznik[typy_poziomow[j-1]] * ilosc[i]
                    print(oblicz)
                    ilosc_docelowa.append(oblicz)
                    mnoznik[typy_poziomow[j]]= oblicz
        #            print(i, poziom[i], "==", poziom[i-1])
        #            print("\t", mnoznik)

                j = j+1

            i = ++i

        self.df['Poziom'] = poziom
        self.df['Ilość przeliczona'] = ilosc_docelowa
        self.df['Ilość przeliczona'] = self.df['Ilość przeliczona'].apply(lambda x: int(x))
        self.df['Zespół'] = self.export_sheet_name



    def export_sheet(self):


        export_df = self.optymalizuj_tabele()

        try:
            # eksport danych do pliku z funkcją "a" - append
            if os.path.isfile(self.export_path):
                mode = "a"
            else:
                mode = "w"
            with pd.ExcelWriter(self.export_path+'.xlsx', mode=mode) as excelWriter:
                export_df.to_excel(excelWriter, sheet_name=self.export_sheet_name, index=False)
            print("Wyeksportowano przeliczone dane")
        except:
                print("Wystąpił Błąd eksportu dla pliku: ", self.import_path)

    def optymalizuj_tabele(self):
        # optymalizacja kolumn
        return self.df.drop(columns=['Struktura zestawienia BOM','Ilość jednostkowa', 'ILOŚĆ', 'Numer katalogowy', 'Opis', 'WER'])

    def setSep(self):

        sep_list = [",", ".", ":", "-", "/", r"\\"]

        for i in range(sep_list.__len__()):
            sep = sep_list[i]
            poz = self.df["Pozycja"].apply(lambda x: x.count(sep)).get_values()
            sum = poz.sum()

            if sum != 0:
                self.sep = sep
                # print("Separator poziomów: ", sep)







