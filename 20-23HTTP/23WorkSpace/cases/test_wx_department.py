import allure
import pytest
import sys
sys.path.append("/Users/lusi/PycharmProjects/Sencond/20-23HTTP/23WorkSpace/apis")
sys.path.append("/Users/lusi/PycharmProjects/Sencond/20-23HTTP/23WorkSpace/datas")
sys.path.append("/Users/lusi/PycharmProjects/Sencond/20-23HTTP/23WorkSpace/utils")

from department import Department
from utils import Utils


@allure.feature("企业微信-部门")
class TestWxApi:
    def setup_class(self):
        token_data = Utils.get_data("../datas/token.yaml")
        corpid = token_data["corpid"]["Rose"]
        corpsecret = token_data["corpsecret"]["contact"]
        self.department = Department(corpid, corpsecret)
        self.department.clear_departments()

    def setup(self):
        self.create_data = {
            "name": "北京研发中心",
            "name_en": "RDBJ",
            "parentid": 1,
            "order": 1,
            "id": 4
        }

        self.update_data = {
            "id": 4,
            "name": "上海研发中心",
            "name_en": "RDSH",
            "parentid": 1,
            "order": 1
        }

        self.id = 4

    @allure.story("业务场景测试案例")
    @allure.title("创建-更新-删除部门")
    def test_departments(self):
        with allure.step("创建部门"):
            r = self.department.create_department(self.create_data)
            self.department.logging(self.create_data)
            assert r["errcode"] == 0
            r = self.department.get_departments_list()
            assert "北京研发中心" in self.department.jpath(r, "$..name")

        with allure.step("更新部门"):
            r = self.department.update_department(self.update_data)
            self.department.logging(self.update_data)
            assert r["errcode"] == 0
            r = self.department.get_departments_list()
            assert "上海研发中心" in self.department.jpath(r, "$..name")

        with allure.step("删除部门"):
            r = self.department.delete_department(self.id)
            self.department.logging(self.id)
            assert r["errcode"] == 0
            r = self.department.get_departments_list()
            assert self.id not in self.department.jpath(r, "$..id")

    @pytest.mark.parametrize(
        "data, expected_code", [
            [{"name": "北京研发中心", "name_en": "BJLN", "parentid": 1, "order": 1, "id": 4}, 0],
            [{"name": "辽宁研发中心#@@WSAFDVBGFNHJK<$%^&*(IUHGVCXZX", "name_en": "RDLN", "parentid": 1, "order": 1, "id": 3}, 60009],
            [{"name": "辽宁研发中心", "name_en": "RDLN", "parentid": 1, "order": 1, "id": 3}, 60008]
        ]
    )
    @allure.story("功能测试案例：创建部门")
    @allure.title("返回码为{expected_code}")
    def test_create_department_sample(self, data, expected_code):
        r = self.department.create_department(data)
        self.department.logging(r)
        assert r['errcode'] == expected_code
