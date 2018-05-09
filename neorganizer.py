from tkinter import filedialog
from openpyxl import *
from pearson import *

class Neorganizer:

    def __init__(self):
        self.community_members = []

    def loadCommunityWorkboodAndPrintContent(self):
        worksheet = self.loadCommunityWorkbook()
        if(self.parseWorkSheet(worksheet)):
            self.printCommunityMembers()



    def loadCommunityWorkbook(self):
        FILEOPENOPTIONS = dict(filetypes=[(('Xls','*.xls'),('Xlsx','*.xlsx')),('All files','*.*')])
        community_workbook_path = filedialog.askopenfilename(**FILEOPENOPTIONS)
        if (community_workbook_path != ''):
            wb = load_workbook(filename=community_workbook_path, read_only=True)
            ws = wb.active
        return ws


    def parseWorkSheet(self, ws):
        for row in ws.rows:
            pearson_info = []
            for cell in row[:4]:
                pearson_info.append(cell.value)
            pearson = Pearson(pearson_info)
            self.community_members.append(pearson)
        self.simplePrintCommunityMembers()
        return True

    def simplePrintCommunityMembers(self):
        for community_member in self.community_members:
            community_member.print()

    def printCommunityMembers(self):
        for row in range(4):
            for column in range(len(self.community_members)):
                pass
