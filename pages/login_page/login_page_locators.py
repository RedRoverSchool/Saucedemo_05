from selenium.webdriver.common.by import By


class LoginPageLocators:
    INPUT_USER_NAME = (By.CSS_SELECTOR, "input#user-name")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input#password")
    BTN_LOGIN = (By.CSS_SELECTOR, "input#login-button")
    ERR_CONTAINER = (By.CSS_SELECTOR, "h3")
    ERR_TEXT = (
        By.XPATH,
        '//*[@id="login_button_container"]/div/form/div[3]/h3/text()',
    )
    BTN_ERR_CLOSE = (By.CSS_SELECTOR, ".error-button")