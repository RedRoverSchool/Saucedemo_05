from pages.base_page.base_page import BasePage
from pages.login_page.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url=url)
        super().open()

    def login_user(self, username="", password=""):
        username_input = self.browser.find_element(*LoginPageLocators.INPUT_USER_NAME)
        username_input.click()
        username_input.clear()
        username_input.send_keys(username)
        password_input = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        password_input.click()
        password_input.clear()
        password_input.send_keys(password)
        self.browser.find_element(*LoginPageLocators.BTN_LOGIN).click()
