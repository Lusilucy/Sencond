from selenium.webdriver.common.by import By

from page.contact import Contact
from page.base import Base


class AddMember(Base):
    def add_member(self, name, id, phone):
        self.find_and_send(By.ID, "username", name)
        self.find_and_send(By.ID, "memberAdd_acctid", id)
        self.find_and_send(By.ID, "memberAdd_phone", phone)
        self.find_and_click(By.CSS_SELECTOR, ".ww_operationBar .js_btn_save")
        return Contact(self.driver)
