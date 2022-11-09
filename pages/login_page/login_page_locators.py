from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_USER_NAME = (By.CSS_SELECTOR, 'input#user-name')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input#password')
    BTN_LOGIN = (By.CSS_SELECTOR, 'input#login-button')
