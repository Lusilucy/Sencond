from app import App


class Contact(App):
    def click_add_member(self):
        self.swip_and_find("添加成员").click()
        from add_member_page import AddMember
        return AddMember(self.driver)
