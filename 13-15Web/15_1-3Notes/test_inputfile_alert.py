from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

from main import Main


class TestImage:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="datas/chromedriver")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_input_image(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("stfile").send_keys("/Users/lusi/PycharmProjects/Sencond/13-15Web/datas/1.png")
        sleep(3)

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        action = ActionChains(self.driver)
        ele1 = self.driver.find_element_by_id("draggable")
        ele2 = self.driver.find_element_by_id("droppable")
        action.drag_and_drop(ele1, ele2).perform()
        sleep(3)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)

    def test_main(self):
        m = Main()
        m.get_first_link().get_text()
