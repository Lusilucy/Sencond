import unittest
from HTMLTestRunner_PY3.HTMLTestRunner_PY3 import HTMLTestRunner

"""方法4：匹配某个目录下所有以***命名规则的文件，执行文件下所有测试用例"""
if __name__ == '__main__':
    report_title = "我的unittest测试报告"
    desc = "这是一个描述信息：用于展示修改样式后的HTMLTestRunner"
    report_file = "./result.html"

    test_dir = "./testcases"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="demo*.py")
    # unittest.TextTestRunner(verbosity=2).run(discover)

    with open(report_file, "wb") as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)
