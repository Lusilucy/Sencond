import os
from time import sleep

from base import Base


class TestBrowser(Base):
    def test_browser(self):
        print(os.environ)
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("霍格沃滋测试学院")
        self.driver.find_element_by_id("su").click()
        sleep(3)
