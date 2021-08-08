'''
企业微信打卡案例
前提条件
已登录状态（ noReset=True）
打卡用例：
1、打开【企业微信】应用
2、进入【工作台】
3、点击【打卡】
4、选择【外出打卡】tab
5、点击【第N次打卡】
6、验证【外出打卡成功】
7、退出【企业微信】应用
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeWork:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "Rose"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # caps["ensureWebviewsHavePages"] = True
        caps["noReset"] = "True"
        # caps["settings[waitForIdleTimeout]"] = 0
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_wework_daka(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        for i in range(3):
            try:
                self.driver.find_element(MobileBy.XPATH, "//*[@text='打卡']").click()
                break
            except Exception as e:
                print(e)
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().text("打卡")'
        #                          '.instance(0));').click()
        self.driver.update_settings({'waitForIdleTimeout': 1})
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        assert self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']").text == '外出打卡成功'
