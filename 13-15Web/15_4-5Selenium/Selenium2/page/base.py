import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    _url = ""

    def __init__(self, _driver: WebDriver = None):
        if _driver is None:
            # opt = webdriver.ChromeOptions()
            # opt.debugger_address = "127.0.0.1:9222"
            # self.driver = webdriver.Chrome(options=opt)
            # self.driver.implicitly_wait(5)
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
            with open("../../Selenium1/data/cookie.yaml") as d:
                cookies = yaml.safe_load(d)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
        else:
            self.driver = _driver

        self.driver.implicitly_wait(5)

        if self._url != "":
            self.driver.get(self._url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        return self.find(by, locator).click()

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_send(self, by, locator, value):
        return self.find(by, locator).send_keys(value)

    def wait(self, ele):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))

    def quit(self):
        self.driver.quit()