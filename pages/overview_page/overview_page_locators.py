from selenium.webdriver.common.by import By


class OverviewPageLocator:
    TITLE = (By.CLASS_NAME, "title")
    QTY = (By.CLASS_NAME, "cart_quantity_label")
    DESCR = (By.CLASS_NAME, "cart_desc_label")

    ITEM_CARD = (By.CLASS_NAME, "cart_item_label")
    ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_QTY = (By.CSS_SELECTOR, ".cart_quantity")
    ITEM_DESC = (By.CSS_SELECTOR, ".inventory_item_desc")
    ITEM_PRICE = (By.CSS_SELECTOR, ".item_pricebar")

    PAY_INFO = (By.XPATH, "//*[@id='checkout_summary_container']/div[1]/div[2]/div[1]")
    SAUCE_CARD = (
        By.XPATH,
        "//*[@id='checkout_summary_container']/div[1]/div[2]/div[2]",
    )
    SHIPPING_INFO = (
        By.XPATH,
        "//*[@id='checkout_summary_container']/div[1]/div[2]/div[3]",
    )
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    BTN_CANCEL = (By.ID, "cancel")
    BTN_FINISH = (By.ID, "finish")
