import readConfig
import pymongo


localReadConfig = readConfig.ReadConfig()


class Mongo_DB:
    def get_mongoConnect(self):
        self.host = localReadConfig.get_mongo("host")
        self.username = localReadConfig.get_mongo("username")
        self.password = localReadConfig.get_mongo("password")
        self.port = localReadConfig.get_mongo("port")
        self.client = pymongo.MongoClient("mongodb://"
                                          + self.username
                                          + ":"
                                          + self.password
                                          + "@"
                                          + self.host
                                          + ":"
                                          + self.port)


        return self.client

    def close_mongoDB(self):
        self.client.close()


if __name__ == '__main__':
    db_connect = Mongo_DB()
    client = db_connect.get_mongoConnect()
    collection = client.xinyongfei_rcs_gateway.bairongLog
    results = collection.find({"status": "SUCCESS",
                               "method_id": "specialList"})
    del_keys = ['code','swift_number','flag_specialList_c','flag_datastrategy','DataStrategy', 'status','rs_strategy_id','rs_product_name']
    final_result = []
    print(type(results))
    for result in results:
        for keys, values in result.items():
            if keys == "return_data":
                for key1 in list(result["return_data"].keys()):
                    if key1 in del_keys:
                        del result["return_data"][key1]
                print(result["return_data"])






        # for keys, values in result.items():
        #     if keys == "result":
        #         print(result[keys])
    # for result in results:
    #     for keys, values in result.items():
    #         if keys == "return_data":
    #             for key, value in values.items():
    #                 if key not in ['code','swift_number','flag_specialList_c','flag_datastrategy','DataStrategy']:
    #                     final_result.append(values[key])





    db_connect.close_mongoDB()
