# coding=utf-8
import pandas as pd
import string
import os




pd.set_option('display.max_columns',10000)


path = r'\\ARCHIWUM\Uwagi konstrukcyjne\Rejestr wadliwych przewodow hydraulicznych\01 - Rejestr wadliwych przewodow hydraulicznych-2018.07.13.xlsx'
path2 = r'C:\Users\skubala\Desktop\przew\c3\b3.xlsx'
header=['Montaz_ID', 'Serwis_ID', 'Data', 'Typ_podestu', 'Nr_fab_podestu', 'Zlecenie', 'Data_wydania_po_naprawie',
       'Data_zgloszenia_usterki', 'Stan_licznika_MTH_w_dniu_usterki', 'Oznaczenie_przewodu', 'Lokalizacja_przewodu','Przyczyna_wymiany', 'Str_nieszczelna_typ_koncowki',
       'Str_nieszczelna_srednica_zakucia', 'Str_szczelna_typ_koncowki','Str_szczelna_srednica_zakucia', 'Srednica_nominalna_zakucia_wg_tabeli',
       'Dzial_zglaszajacy', 'Decyzja_o_wykorzystaniu_lub_utylizacji', 'Potwierdzenie_wykonania','Uwagi']

df = pd.read_excel(path, skiprows=2, header=None, names=header)
df_serwis = df[df['Montaz_ID'] == '-------']
df_montaz = df[df['Serwis_ID'] == '-------']

#print(df_serwis[['Typ_podestu', 'Przyczyna_wymiany', 'Oznaczenie_przewodu', 'Lokalizacja_przewodu', 'Przyczyna_wymiany', 'Potwierdzenie_wykonania', 'Uwagi']])


#print(df_serwis.info())
#print(df_serwis)

path2 = string.replace(path2, " ", "%20")
print(path2)
df = pd.read_excel(path2, skiprows=2, header=None, names=header)



