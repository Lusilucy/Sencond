import os

from selenium import webdriver


class Base:
    def setup(self):
        browser = os.getenv("browser")
        if browser == "safari":
            self.driver = webdriver.Safari()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
