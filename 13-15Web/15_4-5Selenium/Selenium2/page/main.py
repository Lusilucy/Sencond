from time import sleep

from selenium.webdriver.common.by import By

from page.base import Base


class Main(Base):
    _url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contact(self):
        self.find_and_click(By.ID, "menu_contacts")
        from page.contact import Contact
        return Contact(self.driver)

    def click_add_member1(self):

        while True:
            self.find_and_click(By.CSS_SELECTOR, ".js_service_list>a:nth-child(1)")
            if len(self.finds(By.ID, "username")) > 0:
                break

        from page.add_member import AddMember
        return AddMember(self.driver)
