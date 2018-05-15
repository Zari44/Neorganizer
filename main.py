# from tkinter import filedialog
# from openpyxl import *
# from Gui import *
from neorganizer import *
import tkinter as tk
import tkinter.ttk as ttk

if __name__ == '__main__':

   root = tk.Tk()
   root.geometry("700x300")
   root.resizable()
   root.title("Neorganizer")

   neorganizer = Neorganizer(root)
   menubar = tk.Menu(root)
   filemenu = tk.Menu(menubar, tearoff=0)

   filemenu.add_command(label="Load community", command=neorganizer.loadCommunityWorkboodAndPrintContent)
   filemenu.add_command(label="Pick new circles", command=neorganizer.pickNewCircles)

   filemenu.add_separator()
   filemenu.add_command(label="Exit", command=root.quit)
   menubar.add_cascade(label="File", menu=filemenu)

   # editmenu = tk.Menu(menubar, tearoff=0)
   # editmenu.add_command(label="Undo", command=donothing)
   # editmenu.add_separator()

   # editmenu.add_command(label="Cut", command=donothing)
   # editmenu.add_command(label="Copy", command=donothing)
   # editmenu.add_command(label="Paste", command=donothing)
   # editmenu.add_command(label="Delete", command=donothing)
   # editmenu.add_command(label="Select All", command=donothing)

   # menubar.add_cascade(label="Edit", menu=editmenu)
   # helpmenu = tk.Menu(menubar, tearoff=0)
   # helpmenu.add_command(label="Help Index", command=donothing)
   # helpmenu.add_command(label="About...", command=donothing)
   # menubar.add_cascade(label="Help", menu=helpmenu)

   root.config(menu=menubar)
   root.mainloop()
