from locators.login_locators import LoginLocators as ll


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_title(self):
        return self.driver.title

    def action_login(self, username, password):
        self.driver.find_element(*ll.input_username).send_keys(username)
        self.driver.find_element(*ll.input_password).send_keys(password)
        self.driver.find_element(*ll.login_btn).click()

    def action_logout(self):
        self.driver.find_element(*ll.hamburger_btn).click()
        self.driver.find_element(*ll.logout_btn).click()
