# coding=utf-8
import pandas as pd
import string
import os




pd.set_option('display.max_columns', 10000)

path = r'C:\Users\skubala\PycharmProjects\Analysis\Analysis\Harmonogram na dzień 07.06.2019.xlsx'
header=['tydzien', 'dzien', 'pily', 'laser', 'zaginarki']
df = pd.read_excel(path, skiprows=0, header=0)

df.zaginarki[1]=df.zaginarki[0]
i=0

t1=[]
tab = [t1.append(x) for x in df.zaginarki.values]

for i in range(tab.__len__()):
    if tab[i] == "NaN":
        tab[i] = tab[i-1]
    i=i+1

print(tab)