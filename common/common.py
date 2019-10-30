from xlrd import open_workbook
import os
import readConfig


proDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# localReadConfig = readConfig.ReadConfig()


class Read_xlrd(object):
    def __init__(self):
        self.xls_cls = []
        self.xls_cls_2 = []

    def get_xls(self, xls_name, sheet_name):
        self.xls_path = os.path.join(proDir, "TestData", xls_name)
        print(self.xls_path)
        self.file = open_workbook(self.xls_path, "rb")
        self.sheet = self.file.sheet_by_name(sheet_name)
        self.sheet_nrows_context = self.sheet.col_values(0)
        self.sheet_nrows_context2 = self.sheet.col_values(1)
        for each in self.sheet_nrows_context:
            self.xls_cls.append(each)
        for one in self.sheet_nrows_context2:
            self.xls_cls_2.append(one[12:])
        return self.xls_cls, self.xls_cls_2


if __name__ == '__main__':
    x = Read_xlrd()
    file = x.get_xls("testdata20190620.xlsx","bairong")
    print(file)
    print(type(file))
    print(len(file))


