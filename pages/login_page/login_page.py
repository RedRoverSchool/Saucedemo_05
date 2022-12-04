from pages.base_page.base_page import BasePage
from pages.login_page.login_page_locators import LoginPageLocators
from conf.users import users
from conf.website_config import WebSiteConfig
from selenium.webdriver.chrome.webdriver import WebDriver


class LoginPage(BasePage):
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = WebSiteConfig.LOGIN_PAGE_URL
        super().__init__(browser=self.browser, url=self.url)

    def login_user(self, username="", password=""):
        # self.highlight_web_element(LoginPageLocators.INPUT_USER_NAME)
        self.send_keys_to_input(LoginPageLocators.INPUT_USER_NAME, username)
        # self.highlight_web_element(LoginPageLocators.INPUT_PASSWORD)
        self.send_keys_to_input(LoginPageLocators.INPUT_PASSWORD, password)
        # self.move_to_element(LoginPageLocators.BTN_LOGIN)
        self.click_button(LoginPageLocators.BTN_LOGIN)

    def login_standard_user(self):
        self.login_user(
            username=users["standard_user"]["username"],
            password=users["standard_user"]["password"],
        )

    def get_alert_text(self):
        err_container = self.element_is_present(
            LoginPageLocators.ERR_CONTAINER
        )
        return err_container.text
