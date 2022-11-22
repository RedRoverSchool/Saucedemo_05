from selenium.webdriver.common.by import By


class DetailedPageLocators:
    # button "add to cart" on detailed page
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[text()='Add to cart']")

    # button "add to cart" on detailed page
    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")
