import unittest
import HTMLTestRunner
import time

discover = unittest.defaultTestLoader.discover("TestCase/", pattern="test_bairong.py")

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = "Test_Report/" + now + "_test_result.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="接口测试报告", description="用例执行情况", verbosity=2)
    runner.run(discover)
    fp.close()

