from selenium.webdriver.common.by import By


class BasePageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_FORM = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")

class ProductPageLocators():
    INVENTORY_LIST = (By.CSS_SELECTOR, '.inventory_item')
    INVENTORY_ITEM_NAME = (By.CSS_SELECTOR, '.inventory_item_name')
    INVENTORY_ITEM_DESC = (By.CSS_SELECTOR, '.inventory_item_desc')
    INVENTORY_ITEM_PRICE = (By.CSS_SELECTOR, '.inventory_item_price')
    INVENTORY_ITEM_LINK = (By.CSS_SELECTOR, '.inventory_item_img .inventory_item_img')
