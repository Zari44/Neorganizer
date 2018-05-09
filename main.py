import tkinter as tk
# from tkinter import filedialog
# from openpyxl import *
from neorganizer import *

def donothing():
   filewin = tk.Toplevel(root)
   button = tk.Button(filewin, text="Do nothing button")
   button.pack()

if __name__ == '__main__':
   root = tk.Tk()
   neorganizer = Neorganizer()

   menubar = tk.Menu(root)
   filemenu = tk.Menu(menubar, tearoff=0)

   filemenu.add_command(label="New", command=donothing)
   filemenu.add_command(label="Load community", command=neorganizer.loadCommunityWorkbook)
   filemenu.add_command(label="Open", command=donothing)
   filemenu.add_command(label="Save", command=donothing)
   filemenu.add_command(label="Save as...", command=donothing)
   filemenu.add_command(label="Close", command=donothing)

   filemenu.add_separator()

   filemenu.add_command(label="Exit", command=root.quit)
   menubar.add_cascade(label="File", menu=filemenu)
   editmenu = tk.Menu(menubar, tearoff=0)
   editmenu.add_command(label="Undo", command=donothing)

   editmenu.add_separator()

   editmenu.add_command(label="Cut", command=donothing)
   editmenu.add_command(label="Copy", command=donothing)
   editmenu.add_command(label="Paste", command=donothing)
   editmenu.add_command(label="Delete", command=donothing)
   editmenu.add_command(label="Select All", command=donothing)

   menubar.add_cascade(label="Edit", menu=editmenu)
   helpmenu = tk.Menu(menubar, tearoff=0)
   helpmenu.add_command(label="Help Index", command=donothing)
   helpmenu.add_command(label="About...", command=donothing)
   menubar.add_cascade(label="Help", menu=helpmenu)

   root.config(menu=menubar)
   root.mainloop()
