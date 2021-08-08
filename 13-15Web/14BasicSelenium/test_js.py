from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestJS:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_js(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("你好")
        self.driver.find_element_by_id("su").click()

        commands = [
            "return JSON.stringify(performance.timing)",
            "a = document.getElementById('kw').value;window.alert(a)"
        ]

        for command in commands:
            print(self.driver.execute_script(command))

        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(2)
        self.driver.execute_script("document.documentElement.scrollTop = 10000")
        self.driver.find_element_by_css_selector(".page-inner a:nth-last-child(1)").click()
        sleep(3)

    def test_12306_js(self):
        self.driver.get("https://www.12306.cn/index/")
        command = "document.getElementById('train_date')"
        print(self.driver.execute_script(f"return {command}.value"))
        self.driver.execute_script(f"{command}.removeAttribute('readonly')")
        self.driver.execute_script(f"{command}.value = '1992-10-11'")
        print(self.driver.execute_script(f"return {command}.value"))
        sleep(5)

    def test_12306_stream(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.find_element_by_id("fromStationText").click()
        self.driver.find_element(By.XPATH, "//*[@id='ul_list1']/li[1]").click()
        self.driver.find_element(By.XPATH, "//*[@id='ul_list1']/li[3]").click()
        command = "document.getElementById('train_date')"
        self.driver.execute_script(f"{command}.removeAttribute('readonly')")
        self.driver.execute_script(f"{command}.value = '2021-7-20'")

        sleep(2)

        self.driver.find_element_by_id("search_one").click()
        sleep(5)

    def test_12306_action(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.find_element_by_id("fromStationText").click()
        action1 = ActionChains(self.driver)
        action1.send_keys("北京").pause(0.5)
        action1.send_keys(Keys.ENTER).pause(0.5)
        action1.send_keys("厦门").pause(0.5)
        action1.send_keys(Keys.ENTER).pause(0.5)
        action1.send_keys(Keys.TAB)
        action1.perform()
        action2 = ActionChains(self.driver)
        action2.click(self.driver.find_element(By.CSS_SELECTOR, ".cell:nth-child(20)")).pause(0.5)
        action2.click(self.driver.find_element_by_id("search_one")).pause(0.5)
        action2.perform()
        sleep(5)

    def test_copy(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("你好")
        action = ActionChains(self.driver)
        action.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).pause(2)
        action.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.COMMAND).pause(2)
        action.send_keys(Keys.BACKSPACE).pause(2)
        action.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).pause(2)
        action.perform()
        sleep(2)

    def test_drag_and_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        action = ActionChains(self.driver)
        ele1 = self.driver.find_element_by_id("dragger")
        ele2 = self.driver.find_element_by_xpath("//div[3]")
        action.drag_and_drop(ele1, ele2).perform()
        sleep(3)