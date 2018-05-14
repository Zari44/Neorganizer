from tkinter import *

master = Tk()

for item in [Listbox(master), Listbox(master), Listbox(master), Listbox(master)]:
    item.pack(side = BOTTOM)

mainloop()
