# todo fixture

import pytest
import yaml

from calculator import Calculator


class TestCal:
    with open("./cal.yml") as f:
        data = yaml.safe_load(f)

    # def setup_class(self):
    #     self.cal = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b,c", data["add_i"][0], ids=data["add_i"][1])
    def test_add_int(self, cal, a, b, c):
        assert cal.add(a, b) == c

    @pytest.mark.parametrize("a,b,c", data["add_f"][0], ids=data["add_f"][1])
    def test_add_float(self, a, b, c):
        assert round(self.cal.add(a, b), 2) == c

    @pytest.mark.parametrize("a,b,c", data["div"][0], ids=data["div"][1])
    def test_div(self, a, b, c):
        try:
            assert self.cal.div(a, b) == c
        except ZeroDivisionError as z:
            print(z)
