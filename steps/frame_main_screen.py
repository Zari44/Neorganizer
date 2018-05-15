# from tkinter import filedialog
# from openpyxl import *
# from Gui import *
from neorganizer import *
import tkinter as tk
import tkinter.ttk as ttk

def destroy_frame(widget):
    widget.destroy()

if __name__ == '__main__':

   root = tk.Tk()
   root.geometry("500x200")
   root.resizable()

   frame = tk.Frame()
   tk.Label(frame, text='Label').pack()
   frame.pack()

   frame2 = tk.Frame().pack()
   button = tk.Button(frame2, text="Destroy", command= lambda : destroy_frame(frame))
   button.pack()

   tk.Label(text="one").pack()

   separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
   separator.pack(fill=tk.X, padx=5, pady=5)

   tk.Label(text="two").pack()

   root.mainloop()
