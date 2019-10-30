import configparser


class ReadConfig:
    def __init__(self):
        self.init = configparser.ConfigParser()
        self.init.read("F:/MyProject/Bairong/config.ini")

    def get_http(self, name):
        return self.init.get("HTTP", name)

    def get_mongo(self, name):
        return self.init.get("MONGO", name)


