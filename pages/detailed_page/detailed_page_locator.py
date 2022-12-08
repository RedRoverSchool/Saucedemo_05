from selenium.webdriver.common.by import By


class DetailedPageLocators:
    # button "add to cart" on detailed page
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Add to cart']")

    # button "add to cart" on detailed page
    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")

    DETAILS_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_details_name")
    DETAILS_ITEM_DESC = (By.CSS_SELECTOR, ".inventory_details_desc")
    DETAILS_ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_details_price")
    DETAILS_ITEM_IMAGE = (By.CSS_SELECTOR, ".inventory_details_img")

    BACK_TO_PRODUCTS = (By.CSS_SELECTOR, "#back-to-products")

    PRODUCTS_LABEL = (By.XPATH, "// span[text() = 'Products']")
