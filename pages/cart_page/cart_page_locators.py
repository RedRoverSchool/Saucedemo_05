from selenium.webdriver.common.by import By


class CartPageLocators:
    ITEM_CARD = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = ".inventory_item_name"
    ITEM_QTY = ".cart_quantity"
    ITEM_PRICE = ".inventory_item_price"
    ITEM_BTN = ".cart_button"
    ITEM_DESC = ".inventory_item_desc"

    BTN_CHECKOUT = (By.CLASS_NAME, "checkout_button")
    BTN_CONTINUE_SHOPPING = (By.ID, "continue-shopping")
