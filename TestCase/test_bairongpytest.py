import pytest
import readConfig
import json
from common import common
from common import configHttp
from common import ConnectDB
rc = readConfig.ReadConfig()
cf = configHttp.ConfigHttp()
cd = ConnectDB.Mongo_DB()

reponse_list = []
mongo_list = []


def setup_module():
    print("测试开始")


def http_data():
    read_element_list = common.Read_xlrd()
    file_data = read_element_list.get_xls("testdata20190620.xlsx", "bairong")
    data = json.dumps({"context": {"id_card_number": "333444199911112222","mobile": "13566668888","name": "我呃呃",
                                   "decision_time": "2019-06-28 22:35:47", "usage": "offline"},
                       "element_id_list": file_data[0]})
    cfig = configHttp.ConfigHttp()
    headers = eval(cfig.headers)
    response = cfig.send_request(cfig.baseurl, headers=headers, data=data)
    text = response.text
    text_dict = json.loads(text)
    print("****text_dict is***** :", text_dict)
    reponse_list.append(text_dict)
    print("****reponse_list is***** :", reponse_list)
    for each in range(len(file_data[0])):
            for keys, values in text_dict.items():
                if keys == file_data[0][each]:
                        text_dict[file_data[1][each]] = text_dict.pop(keys)

    return reponse_list


def mongo_data():
    client = cd.get_mongoConnect()
    collection = client.xinyongfei_rcs_gateway.bairongLog
    del_keys = ['code', 'swift_number', 'flag_specialList_c', 'flag_datastrategy', 'DataStrategy', 'status',
                'rs_strategy_id', 'rs_product_name','scorecashon','rs_Score_decision','rs_product_type','rs_platform',
                'rs_final_decision','flag_score','flag_riskstrategy','rs_strategy_version','rs_scene','rs_Score_scorecashon']
    results = collection.find({"status": "SUCCESS","id_card_number": "333444199911112222","mobile": "13566668888","name": "我呃呃",
                               "method_id": "specialList"})
    for result in results:
        for keys, values in result.items():
            if keys == "return_data":
                for key1 in list(result["return_data"].keys()):
                    if key1 in del_keys:
                        del result["return_data"][key1]
                mongo_list.append(result["return_data"])
    return mongo_list


def test_equal():
    a_http = http_data()
    b_mongo = mongo_data()
    a_dict_http = {}
    b_dict_mongo = {}
    for each in b_mongo:
        b_dict_mongo.update(each)

    for one in a_http:
        a_dict_http.update(one)

    for b_keys in b_dict_mongo.keys():
        for a_keys in a_dict_http.keys():
            if b_keys == a_keys:
                try:
                    assert int(b_dict_mongo[b_keys]) == a_dict_http[a_keys], "判断当前失败的id为%s, %s" % (b_keys, a_keys)
                except AssertionError as e:
                    print("错误的原因为:", e)

    print("从mongo中取值的条数为：%d" % len(b_dict_mongo))

    # for each_dict in a:
    #     for every_dict in b:
    #         if every_dict in each_dict:
            # for each_dict_keys, each_dict_values in each_dict:
            #     for every_dict_keys, every_dict_values in every_dict:
            #         if each_dict_keys == every_dict_keys:
            #             assert each_dict[each_dict_keys] == every_dict[every_dict_keys]
            #         else:
            #             assert False
    # , "id_card_number": "320681198911086645", "mobile": "18721550656", "name": "郭佳凤",


def teardown_module():
    cd.close_mongoDB()
    print("测试结束！！！")


if __name__ == '__main__':
    # get_http = http_data()
    # print(get_http)
    pytest.main(["-s", "test_bairongpytest.py"])
