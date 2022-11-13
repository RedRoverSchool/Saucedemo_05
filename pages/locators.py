from selenium.webdriver.common.by import By


class HeaderLocators:

    APP_LOGO = (By.CLASS_NAME, ".app_logo")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")


class BurgerMenuLocators:
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    ALL_ITEMS = (By.ID, "inventory_sidebar_link")
    ABOUT = (By.ID, "about_sidebar_link")
    LOGAUT = (By.ID, "logout_sidebar_link")
    RESET_APP_STATE = (By.ID, "reset_sidebar_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "user-name")
    PASSWORD_FORM = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    LOGIN_LOGO = (By.CLASS_NAME, ".login_logo")
    USERNAME_CROSS = (By.CSS_SELECTOR, "div:nth-child(1) > svg")
    PASSWORD_CROSS = (By.CSS_SELECTOR, "div:nth-child(2) > svg")
    ERROR_MESSAGE = (By.CLASS_NAME, ".error-message-container.error")
    BOT_COLUMN = (By.CLASS_NAME, "bot_column")
    LOGIN_CREDENTIALS = (By.CLASS_NAME, ".login_credentials")


class ProductPageLocators:
    INVENTORY_LIST = (By.CSS_SELECTOR, ".inventory_item")
    INVENTORY_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    INVENTORY_ITEM_DESC = (By.CSS_SELECTOR, ".inventory_item_desc")
    INVENTORY_ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    INVENTORY_ITEM_LINK = (By.CSS_SELECTOR, ".inventory_item_img .inventory_item_img")

    SAUCE_LABS_BACKPACK_ADD_TO_CART = (
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-backpack",
    )
    SAUCE_LABS_BACKPACK_REMOVE_FROM_CART = (
        By.CSS_SELECTOR,
        "#remove-sauce-labs-backpack",
    )
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "select_container")
    PRICE_LOW_TO_HIGH = (By.CSS_SELECTOR, "[value='lohi']")
