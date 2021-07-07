import pytest
import yaml

from calculator import Calculator


# 获取yaml数据
def get_data():
    with open("./cal.yml") as d:
        return yaml.safe_load(d)


# setup_class,实例Calculator()
@pytest.fixture(scope="class")
def cal():
    return Calculator()


# setup,teardown
@pytest.fixture(autouse=True)
def up_and_down():
    print("开始计算")
    yield
    print("计算结束")


# 加法int传参
@pytest.fixture(params=get_data()["add_i"][0], ids=get_data()["add_i"][1])
def get_add_i(request):
    return request.param


# 加法float传参
@pytest.fixture(params=get_data()["add_f"])
def get_add_f(request):
    return request.param


# 除法传参（包含除数为0）
@pytest.fixture(params=get_data()["div"][0], ids=get_data()["div"][1])
def get_div(request):
    return request.param
