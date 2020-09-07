from tkinter import *
from GUI.colors_and_theming.ColorPalette import *
from GUI.funkcje_gui.AppButton import AppButton

"""
root = Tk()

primaryPalette = AppButton(root, text='Primary', borderwidth=0, theme='primary')
primaryPalette.pack(fill=X)
primaryDarkPalette = AppButton(root, text='Primary Dark', borderwidth=0, theme='dark')
primaryDarkPalette.pack(fill=X)
primaryLightPalette = AppButton(root, text='Primary Light', borderwidth=0, theme='light')
primaryLightPalette.pack(fill=X)

root.mainloop()

"""

czesc_dolna_path = r'C:\Users\skubala\Desktop\PTM enea\Część Dolna.xlsx'

print(czesc_dolna_path.split(sep="\\")[-1])