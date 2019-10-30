import unittest
import readConfig
from common import common
from common import configHttp
from common import ConnectDB

rc = readConfig.ReadConfig()
cf = configHttp.ConfigHttp()
cd = ConnectDB.Mongo_DB()


class BR(unittest.TestCase):
    def setUp(self):
        self.url = rc.get_http("baseurl")
        self.header = eval(rc.get_http("header"))
        self.database = rc.get_mongo("database")
        self.mongo_client = cd.get_mongoConnect()

    def request_url(self):
        self.data = {"context": {"id_card_number": "341124199108145313","mobile": "18552272190","name": "高学朋","decision_time":"2019-06-28 22:35:47", "usage":"offline"},}
        self.element_id = common.Read_xlrd.get_xls("百融因子20190620.xlsx", "bairong")
        print(self.element_id)

    def get_mongo_data(self):
        pass

    def tearDown(self):
        cd.close_mongoDB()


if __name__ == '__main__':
    unittest.main()


