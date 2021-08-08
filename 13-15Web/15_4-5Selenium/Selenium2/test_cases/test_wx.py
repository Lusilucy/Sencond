import sys
import pytest

sys.path.append("/Users/lusi/PycharmProjects/Sencond/13-15Web/15_4-5Selenium/Selenium2")
from page.main import Main
from utils import Utils


class TestWX:
    data = Utils().get_data("../datas/add_member_data.yaml")

    def setup(self):
        self.main = Main()

    def teardown(self):
        self.main.quit()

    @pytest.mark.parametrize(
        "name,id,phone",
        data
    )
    def test_add_member(self, name, id, phone):
        mem_phone = self.main.goto_contact().click_add_member2().add_member(name, id, phone).check_members()
        assert str(phone) in mem_phone
