from tkinter import filedialog
from openpyxl import *
from pearson import *

class Neorganizer:

    def __init__(self):
        self.community_members = []


    def loadCommunityWorkbook(self):
        FILEOPENOPTIONS = dict(filetypes=[(('Xls','*.xls'),('Xlsx','*.xlsx')),('All files','*.*')])
        community_workbook_path = filedialog.askopenfilename(**FILEOPENOPTIONS)
        if (community_workbook_path != ''):
            wb = load_workbook(filename=community_workbook_path, read_only=True)
            ws = wb.active


        for row in ws.rows:
            pearson_info = []
            for cell in row[:5]:
                pearson_info.append(cell.value)
            pearson = Pearson(pearson_info)
            self.community_members.append(pearson)

        self.printCommunityMembers()

    def printCommunityMembers(self):
        for community_member in self.community_members:
            community_member.print()

    # def donothing(self):
    #     filewin = tk.Toplevel()
    #     button = tk.Button(filewin, text="Do nothing button")
    #     button.pack()
