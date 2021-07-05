from time import sleep

import allure
import pytest
from selenium import webdriver


@allure.testcase("https://www.baidu.com/", "百度的搜索功能")
@allure.feature("百度搜索功能")
class TestBaiDu:
    @allure.story("搜索词条")
    @allure.title("{data}")
    @pytest.mark.parametrize("data", ["allure", "selenium", "appium"])
    def test_demo(self, data):
        with allure.step("1）打开浏览器进入百度"):
            driver = webdriver.Chrome(executable_path="/Users/lusi/Downloads/chromedriver")
            driver.implicitly_wait(5)
            driver.get("https://www.baidu.com")
        with allure.step(f"2）在搜索栏输入{data}并点击'百度一下'"):
            driver.find_element_by_id("kw").send_keys(data)
            driver.find_element_by_id("su").click()
        with allure.step("3）截图保存搜索页面内容"):
            driver.save_screenshot(f"./result2/{data}.jpg")
            allure.attach.file(f"./result2/{data}.jpg", f"{data}.jpg", allure.attachment_type.JPG)
            allure.attach('<head></head><body>首页</body>', "HTMLAttach", allure.attachment_type.HTML)
        with allure.step("关闭浏览器"):
            sleep(3)
            driver.quit()
