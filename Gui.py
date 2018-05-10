import tkinter as tk

class Gui:

    def __init__(self):
        self.root = tk.Tk
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)

