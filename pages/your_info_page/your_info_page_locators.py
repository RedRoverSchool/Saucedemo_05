from selenium.webdriver.common.by import By


class YourInfoLocators:
    TITLE = (By.CLASS_NAME, "title")

    INPUT_FIRST_NAME = (By.ID, "first-name")
    INPUT_LAST_NAME = (By.ID, "last-name")
    INPUT_ZIP_CODE = (By.ID, "postal-code")

    BTN_CANCEL = (By.ID, "cancel")
    BTN_CONTINUE = (By.ID, "continue")

    ERR_MSG = (By.XPATH, '//*[contains(@data-test, "error")]')
