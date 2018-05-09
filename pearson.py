class Pearson:
    "Class for all community members"

    def __init__(self, spreadsheet_row):
        self.pearson_info = spreadsheet_row
        print (self.pearson_info)
        self.name_and_surname = ''
        self.name = ''
        self.surname = ''
        self.phone = ''
        self.address = ''
        self.email = ''
        self.parseInfo()

    def parseInfo(self):
        self.name_and_surname = self.pearson_info[0]
        self.phone = str(self.pearson_info[1])
        self.email = self.pearson_info[2]
        self.address = self.pearson_info[3]

    def print(self):
        print ("Pearson: " + self.name_and_surname + ", phone: " + self.phone + ", address: " + self.address + ", email: " + self.email)
