import logging
from jsonpath import jsonpath
import requests


class Base:
    fileHandler = logging.FileHandler(filename="../logs/apitest.log", encoding="utf-8")
    logging.getLogger().setLevel(0)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    fileHandler.setFormatter(formatter)
    logging.getLogger().addHandler(fileHandler)

    def logging(self, msg):
        return logging.info(msg)

    def request(self, kwargs):
        return requests.request(**kwargs)

    def jpath(self, obj, expr):
        return jsonpath(obj, expr)
