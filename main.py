import tkinter as tk
# from tkinter import filedialog
# from openpyxl import *
from neorganizer import *
from Gui import *
# from TkTreectrl import *
# import Multilistbox

def donothing():
   filewin = tk.Toplevel(root)
   button = tk.Button(filewin, text="Do nothing button")
   button.pack()

if __name__ == '__main__':

   root = tk.Tk()
   root.geometry("700x300")
   root.resizable()
   root.title("Neorganizer")
   listBox = tk.Text(root, width=100, height=100, bg='white', state=tk.DISABLED)
   listBox.grid(row=0, column=0, sticky=tk.W)
   listBox.pack()
   # textFrame.insert(END,"siema")
   neorganizer = Neorganizer(root, listBox)
   menubar = tk.Menu(root)
   filemenu = tk.Menu(menubar, tearoff=0)

   filemenu.add_command(label="Load community", command=neorganizer.loadCommunityWorkboodAndPrintContent)
   filemenu.add_command(label="Pick new circles", command=neorganizer.pickNewCircles)
   # filemenu.add_command(label="Save", command=donothing)
   # filemenu.add_command(label="Save as...", command=donothing)
   # filemenu.add_command(label="Close", command=donothing)

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
