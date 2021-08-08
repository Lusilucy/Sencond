from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestMusic:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_music(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("你好音乐")
        self.driver.find_element_by_id("su").click()
        self.driver.find_element_by_link_text("你好音乐 - 歌曲").click()

        def wait(x):
            return len(self.driver.window_handles) > 1

        WebDriverWait(self.driver, 10).until(wait)

        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.switch_to.frame("g_iframe")
        self.driver.find_element(By.XPATH, "//*[@datas-res-id='122526'][1]").click()
        # ele = self.driver.find_element_by_css_selector("[datas-res-id='122526']")
        # self.driver.execute_script("arguments[0].click();", ele)
        sleep(5)
