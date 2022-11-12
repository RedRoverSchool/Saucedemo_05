from selenium.webdriver.common.by import By


class DetailedPageLocators:
    ITEM_TITLE = (By.CSS_SELECTOR, ".inventory_item")       #first item on inventory page
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")    #button "add to cart" on detailed page
    CART_ICON = (By.CSS_SELECTOR, ".shopping_cart_link")     #иконка корзины
