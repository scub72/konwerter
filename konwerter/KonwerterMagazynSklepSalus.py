
from konwerter.pliki_excel.WIERSZ_EKSPORTU import WIERSZ_EKSPORTU
import pandas as pd


class KonwerterMagazynSklepSalus:
    def __init__(self, export_path, paths):
        self.paths = paths[0]
        self.export_path = export_path
        self.kolumny = WIERSZ_EKSPORTU.keys()


    def magazyn(self):
        magazyn = pd.read_excel(self.paths)
        return magazyn.dropna()


    def konwertuj(self):

        wiersz = 0
        liczba_wierszy_niezerowych = self.magazyn().__len__()
        frames = []
        magazyn = self.magazyn()

        while wiersz < liczba_wierszy_niezerowych:

            dane = {
                'Nazwa_produktu_en': [magazyn['Nazwa'].iloc[wiersz]],
                'Nr_katalogowy': [magazyn['Indeks katalogowy'].iloc[wiersz]],
                'Opis': [magazyn['Nazwa c.d.'].iloc[wiersz]],
                'Ilosc_produktow': [magazyn['Ilość dostępna'].iloc[wiersz]],
                'Cena_zakupu': [magazyn['Cena sprzedaży netto'].iloc[wiersz]],
            }
            dane_stale = {
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
            tmp = pd.DataFrame(dane, columns=self.kolumny)
            frames.append(tmp)

            wiersz = wiersz + 1

        export_df = pd.concat(frames)
        print(export_df.info())

        #export_path = "export/magazyn_export_" + datetime.now().strftime("%d-%m-%Y_%H:%M:%S") + ".csv"

        try:
            export_df.to_csv(self.export_path+".csv", sep=';', index=False)
            # print("Wyeksportowano przeliczone dane")
        except:
            # print("Wystąpił Błąd eksportu dla pliku: ", self.paths)
            messagebox.showerror("Wystąpił Błąd eksportu dla pliku: ", self.paths)


