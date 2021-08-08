from app import App


class MainPage(App):
    def click_contact(self):
        self.find_xtext_click("通讯录")
        from contact_page import Contact
        return Contact(self.driver)
