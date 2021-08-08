from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestSelennium:
    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("w3c", False)
        self.driver = webdriver.Chrome(options=opt)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element_by_link_text("所有分类").click()

        def wait(x):
            return len(self.driver.find_elements_by_link_text("最新")) >= 1

        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element_by_link_text("开源项目").click()
        sleep(3)

    def test_move_to_element(self):
        self.driver.get("https://www.baidu.com")
        action = ActionChains(self.driver)
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action.move_to_element(ele).perform()
        sleep(3)

    def test_touchactions(self):
        self.driver.get("https://www.baidu.com")
        ele = self.driver.find_element_by_id("kw")
        ele.send_keys("selenium测试")
        self.driver.find_element_by_id("su").click()
        sleep(3)
        action = TouchActions(self.driver)
        action.scroll_from_element(ele, 0, 10000).perform()
        self.driver.find_element_by_css_selector("#page .n").click()
        sleep(3)

    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("霍格沃滋测试学院")
        self.driver.find_element_by_id("su").click()
        sleep(3)
        self.driver.find_element_by_link_text("霍格沃兹测试学院-软件自动化测试开发培训_接口性能测试").click()
        windows = self.driver.window_handles
        print(windows)
        print(self.driver.current_window_handle)
        self.driver.switch_to.window(windows[-1])
        print(self.driver.current_window_handle)
        sleep(5)
        print(self.driver.title)
