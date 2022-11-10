from pages.base_page.base_page import BasePage
from pages.login_page.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def login_user(self, username="", password=""):
        # self.highlight_web_element(LoginPageLocators.INPUT_USER_NAME)
        self.send_keys_to_input(LoginPageLocators.INPUT_USER_NAME, username)
        # self.highlight_web_element(LoginPageLocators.INPUT_PASSWORD)
        self.send_keys_to_input(LoginPageLocators.INPUT_PASSWORD, password)
        # self.hover(LoginPageLocators.BTN_LOGIN)
        self.click_button(LoginPageLocators.BTN_LOGIN)
