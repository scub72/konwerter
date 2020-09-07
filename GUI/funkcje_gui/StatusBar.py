from tkinter import Label, BOTTOM, X, SUNKEN, W

class StatusBar:

    def __init__(self, master):
        self.createStatusBar(master)

    def createStatusBar(self, master):
        status = Label(master, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
