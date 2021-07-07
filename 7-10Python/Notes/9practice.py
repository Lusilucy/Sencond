# TODO Python 进阶✅
"""pip✅"""
# pip3.8 install ** -i http://pypi.douban.com/simple/ --trust-host pypi.douban.com
# pip3.8 freeze > requirements.txt

"""os✅"""
# import os
#
# print(os.path)
# print("--------")
# if not os.path.exists("./Hello"):
#     os.mkdir("./Hello")
#     with open("./Hello/text.txt", "w") as f:
#         f.write("Hello World!")
# else:
#     if os.path.exists("./Hello/text.txt"):
#         os.remove("./Hello/text.txt")
#     os.removedirs("./Hello")
#
# print("--------")
# print(os.getcwd())
# print("--------")
# print(os.listdir)
# print("--------")
# print(os.listdir("../"))

"""time✅"""
import time

# print(time.asctime())
# print(time.time())
# print(time.localtime())
# print(*time.localtime())
# print(time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime()))

# # 计算两天前时间
# now_timestamp = time.time()
# print(now_timestamp)
# two_day_before = now_timestamp - 2*24*60*60
# time_tuple = time.localtime(two_day_before)
# print(time_tuple)
# print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))

"""urllib✅"""
# import urllib.request
# r = urllib.request.urlopen("http://www.baidu.com")
# print(r.status)
# print(r.headers)
# print(r.getheaders())
# # print(r.read())
# print(r.getcode())

"""math✅"""
# import math
#
# print(math.ceil(5.1))
# print(math.floor(5.1))
# print(math.sqrt(9))

"""_thread✅"""
# 9_2Thread/method_thread.py

"""threading✅"""
# 9_2Thread/method_threading.py

"""threading重构✅"""
# 9_2Thread/m_threading_run.py

"""request.encoding✅"""
# import requests
# r = requests.get("http://www.baidu.com")
# print(r.encoding)
# print(r.apparent_encoding)
# print(r.status_code)
# print(r.text)

"""env✅"""
# python3.8 -m venv envname
# source envname/bin/activate
# deactivate

"""unittest✅"""
# 9_5Unittest

"""pytest✅"""
# 9_6-9Pytest

"""参数化✅"""
# 同上
"""数据驱动✅"""
# 同上
"""测试报告✅"""
# pytest --alluredir ./result
# 1
# allure serve ./result
# 2
# allure generata ./result -o ./report --clean
