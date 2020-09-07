import pandas as pd
import os

def export_sheet(export_df, export_path, export_sheet_name):

    try:
        # eksport danych do pliku z funkcją "a" - append
        if os.path.isfile(export_path):
            mode = "a"
        else:
            mode = "w"

        with pd.ExcelWriter(export_path, mode=mode) as excelWriter:
            export_df.to_excel(excelWriter, sheet_name=export_sheet_name, index=False)
        print("Wyeksportowano przeliczone dane")
    except:
        print("Wystąpił Błąd eksportu dla pliku: ", export_sheet_name)
