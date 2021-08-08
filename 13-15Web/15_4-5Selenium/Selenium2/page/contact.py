from selenium.webdriver.common.by import By

from page.base import Base


class Contact(Base):
    def click_add_member2(self):
        self.wait((By.CSS_SELECTOR, ".ww_operationBar .js_add_member"))

        while True:
            self.find_and_click(By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
            if len(self.finds(By.ID, "username")) > 0:
                break

        from page.add_member import AddMember
        return AddMember(self.driver)

    def check_members(self):
        self.wait((By.XPATH, "//*[@id='member_list']/tr/td[5]"))
        members = []
        eles = self.finds(By.XPATH, "//*[@id='member_list']/tr/td[5]")
        for member in eles:
            members.append(member.get_attribute("title"))
        return members
