from locators.locators import LoginLocators as ll
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.core import Core


class LoginPageMy(Core):
    def __init__(self, driver):
        Core.__init__(self, driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def login_title(self):
        return self.driver.title

    def action_login(self, username, password):
        Core.send_keys(self, ll.input_username, username)
        Core.send_keys(self, ll.input_password, password)
        Core.click(self, ll.login_btn)

    def action_logout(self):
        self.driver.find_element(*ll.hamburger_btn).click()
        self.wait.until(EC.element_to_be_clickable(ll.logout_btn)).click()
