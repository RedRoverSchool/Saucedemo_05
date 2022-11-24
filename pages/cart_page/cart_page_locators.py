from selenium.webdriver.common.by import By


class CartPageLocators:
    ITEM_CARD = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = ".inventory_item_name"
    ITEM_QTY = (By.CSS_SELECTOR, ".cart_quantity")
    DESCR = (By.CSS_SELECTOR, ".cart_desc_label")
    ITEM_PRICE = ".inventory_item_price"
    ITEM_BTN = ".cart_button"
    ITEM_DESC = ".inventory_item_desc"

    BTN_CHECKOUT = (By.CSS_SELECTOR, ".checkout_button")
    BTN_CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    TITLE = (By.CLASS_NAME, "title")
