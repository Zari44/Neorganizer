from tkinter import filedialog
from openpyxl import *
from pearson import *
import tkinter as tk
import tkinter.ttk as ttk

class Neorganizer:

    def __init__(self, root, text_frame):
        self.community_members = []
        self.loaded = False
        self.root = root
        self.text_frame = text_frame


    def loadCommunityWorkboodAndPrintContent(self):
        worksheet = self.loadCommunityWorkbook()
        if(self.parseWorkSheet(worksheet)):
            self.displayCommunityMembers()


    def loadCommunityWorkbook(self):
        FILEOPENOPTIONS = dict(filetypes=[(('Xls','*.xls'),('Xlsx','*.xlsx')),('All files','*.*')])
        community_workbook_path = filedialog.askopenfilename(**FILEOPENOPTIONS)
        if (community_workbook_path != ''):
            wb = load_workbook(filename=community_workbook_path, read_only=True)
            ws = wb.active
            self.loaded = True
        return ws


    def parseWorkSheet(self, ws):
        for row in ws.rows:
            pearson_info = []
            for cell in row[:4]:
                pearson_info.append(cell.value)
            pearson = Pearson(pearson_info)
            self.community_members.append(pearson)
        return True


    def printCommunityMembers(self):
        for community_member in self.community_members:
            community_member.print()


    def displayCommunityMembers(self):
        if self.loaded:
            r = 0
            for pearson in self.community_members:
                r = r + 1
                c = 0
                for info in pearson.getInfoList():
                    c = c + 1
                    tk.Label(self.text_frame, text=info, bg = 'snow').grid(row=r,column=c, sticky=tk.W)
                    ttk.Separator(self.text_frame, orient=tk.VERTICAL).grid(column=c+1, row=r, rowspan=len(self.community_members), sticky='ns')
                    # self.text_frame.grid_columnconfigure(4,minsize=125)
                # tk.Label(self.text_frame, pearson.getString()+"\n").grid()
                # self.text_frame.insert(tk.END,pearson.getString()+"\n")
        else:
            filewin = tk.Toplevel(self.root)
            label = tk.Label(filewin, text="\nLoad community first")
            button = tk.Button(filewin, text="Ok", command=filewin.destroy)
            filewin.geometry("150x75")
            filewin.title("Warning!")
            label.pack()
            button.pack()
