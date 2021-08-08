import yaml
from selenium import webdriver


class TestCookie:
    def test_get_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        cookies = self.driver.get_cookies()
        with open("data/cookie.yaml", "w") as d:
            yaml.safe_dump(cookies, d)

