from selenium.webdriver.common.by import By


class CartPageLocators:
    ITEM_CARD = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_QTY = (By.CSS_SELECTOR, ".cart_quantity")
    ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    ITEM_BTN = (By.CSS_SELECTOR, ".cart_button")
    ITEM_DESC = (By.CSS_SELECTOR, ".inventory_item_desc")

    TITLE = (By.CLASS_NAME, "title")
    DESCR = (By.CSS_SELECTOR, ".cart_desc_label")
    BTN_CHECKOUT = (By.CSS_SELECTOR, ".checkout_button")
    BTN_CONTINUE_SHOPPING = (By.ID, "continue-shopping")