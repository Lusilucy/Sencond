from appium.webdriver.common.mobileby import MobileBy

from app import App
from add_member_page import AddMember


class EditMember(App):
    def edit_member(self, name, tel):
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']", name)
        self.find_and_send(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']", tel)
        self.find_xtext_click("保存后自动发送邀请通知")
        self.find_xtext_click("保存")
        return AddMember(self.driver)
