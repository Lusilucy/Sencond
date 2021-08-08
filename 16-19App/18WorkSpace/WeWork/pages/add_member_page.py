from app import App


class AddMember(App):
    def click_manual_add(self):
        self.find_xtext_click("手动输入添加")
        from edit_member_page import EditMember
        return EditMember(self.driver)

    def check(self):
        return self.find_xtext_ele("添加成功").text
