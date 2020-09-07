from tkinter import Button
from tkinter import filedialog
from GUI.colors_and_theming.ColorPalette import *



class AppButton(Button):
    """
            :param master:
            :param theme: 'primary', 'dark', 'light'
    """

    def __init__(self, master, theme='primary', **kwargs):
        Button.__init__(self, master, kwargs)
        self.path = "Default"
        self.theme = theme
        self['borderwidth'] = 0
        self.chooseTheme()


    def openFile(self, event):
        name = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("excel files", "*.xls, *xlsx"), ("all files", "*.*")))
        return name



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
        self["bg"] = PRIMARY_COLOR
        self["fg"] = PRIMARY_TEXT_COLOR
        self["activebackground"] = SECONDARY_COLOR
        self["highlightbackground"] = SECONDARY_TEXT_COLOR

    def primaryDarkTheme(self):
        self["bg"] = PRIMARY_DARK_COLOR
        self["fg"] = PRIMARY_TEXT_COLOR
        self["activebackground"] = SECONDARY_DARK_COLOR
        self["highlightbackground"] = SECONDARY_TEXT_COLOR

    def primaryLightTheme(self):
        self["bg"] = PRIMARY_LIGHT_COLOR
        self["fg"] = PRIMARY_TEXT_COLOR
        self["activebackground"] = SECONDARY_LIGHT_COLOR
        self["highlightbackground"] = SECONDARY_TEXT_COLOR