class Pearson:
    "Class for all community members"

    def __init__(self, spreadsheet_row):
        self.pearson_info = spreadsheet_row
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
        self.info_list = [self.name_and_surname, self.phone, self.email, self.address]

    def print(self):
        print ("Pearson: " + self.name_and_surname + ", phone: " + self.phone + ", address: " + self.address + ", email: " + self.email)

    def printName(self):
        print ("Pearson: " + self.name_and_surname)

    def getString(self):
        return self.name_and_surname + "\t" + self.phone + "\t" + self.address + "\t" + self.email

    def getInfoList(self):
        return [self.name_and_surname, self.phone, self.email, self.address]
