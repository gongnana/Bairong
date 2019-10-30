from common import ConnectDB
from bson.objectid import ObjectId
from xlrd import open_workbook
import os


connect = ConnectDB.Mongo_DB()
client = connect.get_mongoConnect()
collection = client.xinyonfei_gateway.BairongLog
test_list = []
test_data = {}
prodir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def Read_xlsx(xls_name, sheet_name):
    file_list = []
    xls_path = os.path.join(prodir, "TestData", xls_name)
    file = open_workbook(xls_path, "rb")
    sheet = file.sheet_by_name(sheet_name)
    sheet_ncol_content = sheet.col_values(0)
    for each in sheet_ncol_content:
        file_list.append(each)
    return file_list


file = Read_xlsx("test2.xlsx", "test")


for i in range(1, 500):
    test_list.append(i)

for i in range(len(file)):
    test_data[file[i]] = test_list[i]


def test_modify():
    col = collection.find_one_and_update({"_id": ObjectId("5d0c924fc567d66e3c588235")},
                                         {"$set": {"return": test_data}})
    return col


if __name__ == '__main__':
    test_demo = test_modify()
    print(test_demo)
    print(test_data)
