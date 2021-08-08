import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class Base:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def swip_and_find(self, text, n=5):
        logging.info(f"swip:{text}")
        window = self.driver.get_window_rect()
        height = window['height']
        width = window['width']
        start_x = width / 2
        start_y = height * 0.8
        end_x = start_x
        end_y = height * 0.2
        self.driver.implicitly_wait(0)
        for i in range(n):
            try:
                ele = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(10)
                return ele
            except Exception as e:
                print(e)
                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def find(self, by, locator):
        logging.info(f"find:{by},{locator}")
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        logging.info("find_and_click")
        return self.find(by, locator).click()

    def find_and_send(self, by, locator, value):
        logging.info("find_and_sendkeys")
        return self.find(by, locator).send_keys(value)

    def finds(self, by, locator):
        logging.info(f"finds:{by},{locator}")
        return self.driver.find_elements(by, locator)

    def find_xtext_ele(self, text):
        logging.info("find_by_xpath")
        return self.find(MobileBy.XPATH, f"//*[@text='{text}']")

    def find_xtext_click(self, text):
        logging.info("find_by_xpath_and_click")
        return self.find_xtext_ele(text).click()

    def find_x_send(self, text, value):
        logging.info(f"find_by_xpath_and_sendkeys:{value}")
        return self.find_xtext_ele(text).send_keys(value)
