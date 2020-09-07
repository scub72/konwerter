from tkinter import Menu

class AppMenu:

    def __init__(self, master):
        self.createMenu(master)

    def createMenu(self, master):

        menu = Menu(master)
        master.config(menu=menu)

        subMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="New project", command=self.defaultCommand())
        subMenu.add_command(label="new", command=self.defaultCommand())
        subMenu.add_separator()
        subMenu.add_command(label="exit", command=quit)
        editMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="New project", command=self.defaultCommand())
        editMenu.add_command(label="new", command=self.defaultCommand())

    def defaultCommand(self):
        print("define the default command")