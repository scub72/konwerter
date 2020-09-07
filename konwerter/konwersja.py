# -*- coding: utf-8 -*-
import pandas as pd
import tkinter as tk
from datetime import datetime
from tkinter import filedialog

# Stan min.	Stan max.	Dostawcy dostarczą	Odbiorcy odbiorą	Wal. zakupu	C. zakupu netto wal.	Wal. sprzedaży	Producent
pd.set_option('display.max_rows', 1000, 'display.max_columns', 1000)

#
# ------------------------------------------------------------------#
#                       Wczytanie pliku                             #
#-------------------------------------------------------------------#
root = tk.Tk()
root.withdraw()
#file_string = filedialog.askopenfilenames()[0]
file_string = 'pliki_excel/Artykuly_przegladanie_201912132.xlsx'
export_string = 'pliki_excel/export_csv_30_12_2019_580446.csv'

magazyn = pd.read_excel(file_string)
wzor = pd.read_csv(export_string, sep=';')

# ------------------------------------------------------------------#
#                       Obrabianie pliku                            #
#-------------------------------------------------------------------#

# Indeks katalogowy
# nazwa -> Nazwa_produktu_en
# Nazwa c.d. -> Opis
# nazwa (wycinek) -> Kategoria_2_nazwa

#print (magazyn["Indeks katalogowy"].values)
#print (magazyn.columns)
#print (wzor.columns)

wiersz = 0
liczba_wierszy_niezerowych = magazyn.dropna()
frames = []

while wiersz<liczba_wierszy_niezerowych.__len__():

    kolumny_nadpisane = [
        'Nazwa_produktu_en',
         'Nr_katalogowy',
         'Opis',
         'Ilosc_produktow',
         'Cena_zakupu'
         ]

    dane = {
        'Nazwa_produktu_en' : [magazyn['Nazwa'].iloc[wiersz]],
        'Nr_katalogowy' : [magazyn['Indeks katalogowy'].iloc[wiersz]],
        'Opis' : [magazyn['Nazwa c.d.'].iloc[wiersz]],
        'Ilosc_produktow' : [magazyn['Ilość dostępna'].iloc[wiersz]],
        'Cena_zakupu' : [magazyn['Cena sprzedaży netto'].iloc[wiersz]],
    }
    dane_stale={
        'Kategoria_1_nazwa': 'HYDRAULIKA SIŁOWA',
        'Kategoria_1_zdjecie': 'Hydraulika Siłowa.jpg',
        'Kategoria_1_opis': 'elementy',
        'Kategoria_1_meta_tytul': 'HYDRAULIKA SIŁOWA',
        'Kategoria_1_meta_opis': 'HYDRAULIKA SIŁOWA',
        'Kategoria_1_meta_slowa': 'HYDRAULIKA SIŁOWA',
        'Kategoria_1_nazwa_en': 'POWER HYDRAULICS',
        'Kategoria_1_zdjecie': 'Hydraulika Siłowa.jpg',
        'Kategoria_1_meta_tytul_en': 'POWER HYDRAULICS',
        'Kategoria_1_meta_opis_en': 'POWER HYDRAULICS',
        'Kategoria_1_meta_slowa_en': 'POWER HYDRAULICS'
    }

    dane.update(dane_stale)
    tmp = pd.DataFrame(dane, columns=wzor.columns)
    frames.append(tmp)

    wiersz = wiersz + 1

export_df = pd.concat(frames)
print(export_df.info())

export_path = "export/magazyn_export_"+datetime.now().strftime("%d-%m-%Y_%H:%M:%S")+".csv"
export_df.to_csv(export_path,sep=';', index=False)










# ------------------------------------------------------------------#
#                       Eksport do CSV
# ------------------------------------------------------------------#