from xlrd import open_workbook


class Read_xlxs:
    def __init__(self, file):
        self.file = file
        self.test_data = []

    def read_file(self, sheetname):
        self.data = open_workbook(self.file)
        self.table = self.data.sheet_by_name(sheetname)
        self.nrows = self.table.nrows
        # self.table_content = self.table.col_values(1, 1, 2)
        self.table_row = self.table.col_values(0)

    def get_file(self):
        for each in self.table_row:
            self.test_data.append(each)
        return self.test_data


if __name__ == '__main__':
    file = Read_xlxs(r"F:\MyProject\Bairong\TestData\testdata20190620.xlsx")
    file.read_file("bairong")
    print(file.get_file())
