# coding=utf-8
# -*- coding: utf-8 -*-
from Eksport_GUI.Kosz.exportToExcel import export_sheet


from Eksport_GUI.Kosz.excelPrzewody import excelPrzewody as ep

# Ścieżki importu plików
czesc_dolna_path = r'C:\Users\skubala\Desktop\PTM enea\Część Dolna.xlsx'
kolumna_path = r'C:\Users\skubala\Desktop\PTM enea\Kolumna.xlsx'
wysiegnik_path = r'C:\Users\skubala\Desktop\PTM enea\Wysięgnik.xlsx'

# Ścieżki eksportu plików
export_path = r'C:\Users\skubala\Desktop\PTM enea\Test_export.xlsx'

# Część dolna
cd = ep(czesc_dolna_path, export_path, "BOM", "Część Dolna")
cd.export_sheet(cd.optymalizuj_tabele())


# Kolumna
k = ep(kolumna_path, export_path, "BOM", "Kolumna")
k.export_sheet(k.optymalizuj_tabele())


# Wysięgnik
w = ep(wysiegnik_path, export_path, "BOM", "Wysięgnik")
w.export_sheet(w.optymalizuj_tabele())

dfc = cd.df.append(k.df, sort=False).append(w.df, sort=False)

dfc = dfc.drop(columns=['Struktura zestawienia BOM','Ilość jednostkowa', 'ILOŚĆ', 'Numer katalogowy', 'Opis', 'WER'])

export_sheet(dfc, export_path, "Zbiorczy")

