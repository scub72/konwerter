import pandas as pd
from tkinter import Frame, X, TOP, LEFT, Y, NW, RIGHT, Label
from GUI.colors_and_theming.ColorPalette import *
from GUI.funkcje_gui.AppButton import AppButton
from tkinter import filedialog
from tkinter import messagebox
from konwerter.KonwerterMagazynSklepSalus import KonwerterMagazynSklepSalus

class AppToolbar:

    def __init__(self, master):
        self.paths = []
        self.labelBuffor = []
        self.createToolbar(master)


    def createToolbar(self, master, theme='primary'):

        self.theme=theme

        self.toolbar = Frame(master)
        self.chooseTheme()

        insertButt = AppButton(self.toolbar, text="Dodaj plik Excel", theme=theme)
        insertButt.bind("<ButtonRelease>", self.importAndDisplayPath)
        insertButt.pack(side=LEFT, padx=5, pady=5)

        exportButt = AppButton(self.toolbar, text="Exportuj plik", theme=theme)
        exportButt.bind("<ButtonRelease>", self.exportCalculations)
        exportButt.pack(side=LEFT, padx=5, pady=5)
        self.toolbar.pack(side=TOP, fill=X)

        self.result_frame = Frame(master)
        title_frame = Frame(self.result_frame)
        self.path_frame = Frame(self.result_frame)

        titlefield = Label(title_frame, text = "Załadowane pliki: ")
        titlefield.pack(side=LEFT, fill=X, padx=5, pady=5, anchor=NW)

        title_frame.pack(side=LEFT, anchor=NW)
        self.path_frame.pack(side=LEFT, anchor=NW)
        self.result_frame.pack(side=TOP, fill=Y, anchor=NW)

        clearButt = AppButton(self.toolbar, text="Wyczyść import", theme=theme)
        clearButt.bind("<ButtonRelease>", self.clearAll)
        clearButt.pack(side=RIGHT, padx=5, pady=5)
        self.toolbar.pack(side=TOP, fill=X)

    """
            Metody
    """

    def definePaths(self, event):
        i = 0
        for index in range(self.labelBuffor.__len__()):

            if self.labelBuffor[index] == event.widget:
                i = index

            index = index+1

        del self.paths[i]
        event.widget.destroy()
        #[print(widget) for widget in self.labelBuffor if widget==event.widget]

    def clearAll(self, event):
        self.paths=[]
        [widget.destroy() for widget in self.labelBuffor ]
        self.labelBuffor=[]

    def importAndDisplayPath(self, event):
        name = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("excel files", "*.xls, *xlsx"), ("all files", "*.*")))
        self.paths.append(name)
        label = Label(self.path_frame, text = name)
        label.bind("<ButtonRelease-1>", self.definePaths)
        label.pack(side=TOP, fill=X, padx=5, pady=5, anchor=NW)
        self.labelBuffor.append(label)

    def exportCalculations(self, event):
        export_path = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
        if export_path != "":
            self.doCalculation(export_path, self.paths)
            success = "Wyeksportowano plik do katalogu:\n" + export_path
            messagebox.showinfo("Eksport udany", success)

        else:
            messagebox.showerror("Błąd", "Nie udało się wyeksportować pliku")


    def doCalculation(self, export_path, paths):

        KonwerterMagazynSklepSalus(export_path, paths).konwertuj()




    """
    Theming
    """

    def chooseTheme(self):

        if self.theme == 'primary':
            self.primaryTheme()

        if self.theme == 'dark':
            self.primaryDarkTheme()

        if self.theme == 'light':
            self.primaryLightTheme()


    def primaryTheme(self):
        self.toolbar["bg"] = PRIMARY_COLOR


    def primaryDarkTheme(self):
        self.toolbar["bg"] = PRIMARY_DARK_COLOR


    def primaryLightTheme(self):
        self.toolbar["bg"] = PRIMARY_DARK_COLOR
