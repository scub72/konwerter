# pyinstaller --noconsole --onefile  --noupx --icon=ExportXC.ico -n ExportExcel -F  MainWindow.py

from tkinter import Frame, Tk
from GUI.funkcje_gui.AppToolbar import AppToolbar


root = Tk()
root.title("Obliczanie ilości detali")
root.geometry("630x300")


appToolbar = AppToolbar(root)
main_frame = Frame(root)
main_frame.pack()

root.mainloop()