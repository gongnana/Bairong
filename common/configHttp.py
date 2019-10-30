import requests
import readConfig
import json
from common import common


localreadConfig = readConfig.ReadConfig()


class ConfigHttp:
    def __init__(self):
        self.baseurl = localreadConfig.get_http("baseurl")
        self.port = localreadConfig.get_http("port")
        self.headers = localreadConfig.get_http("header")
        self.timeout = localreadConfig.get_http("timeout")
        self.url = self.baseurl + self.port

    def send_request(self, url, headers, data):
        self.data = data
        self.datalist = json.loads(data)
        self.headers = headers
        self.url = url
        res = requests.post(self.url, headers=self.headers, json=self.datalist, timeout=None)
        return res


if __name__ == '__main__':
    read_element_list = common.Read_xlrd()
    element_list_id = read_element_list.get_xls(r"F:\MyProject\Bairong\TestData\百融因子20190620.xlsx", "bairong")
    data = json.dumps({"context": {"id_card_number": "320681198911086645","mobile": "18721550656","name": "郭佳凤",
                                   "decision_time":"2019-06-28 22:35:47","usage":"offline"},"element_id_list":["bairong_als_796"]})
    cfig = ConfigHttp()
    headers = eval(cfig.headers)
    response = cfig.send_request(cfig.baseurl, headers=headers, data=data)
    print(response.text)
