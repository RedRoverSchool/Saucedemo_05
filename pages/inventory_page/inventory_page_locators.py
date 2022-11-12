from typing import Tuple

from selenium.webdriver.common.by import By


class InventoryPageLocators:
    BTN_BURGER_MENU = (By.CSS_SELECTOR, "button#react-burger-menu-btn")
    BTN_BURGER_MENU_CLOSE = (By.CSS_SELECTOR, "button#react-burger-cross-btn")
    BURGER_MENU_ALL_ITEMS = (By.CSS_SELECTOR, "a#inventory_sidebar_link")
    BURGER_MENU_ABOUT = (By.CSS_SELECTOR, "a#about_sidebar_link")
    BURGER_MENU_LOGOUT = (By.CSS_SELECTOR, "a#logout_sidebar_link")
    BURGER_MENU_RESET = (By.CSS_SELECTOR, "a#reset_sidebar_link")
    ITEMS_CARDS = (By.CSS_SELECTOR, ".inventory_item")                  #first item on inventory page
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")                #cart icon, work with empty cart
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")              #quantity of items in cart, does not work with empty cart
    CART_COUNTER = (By.CSS_SELECTOR, "div#shopping_cart_container span")
    DROPDOWN_SORTING = (By.CSS_SELECTOR, "div#header_container select")
    PRODUCTS_CARDS = (By.CSS_SELECTOR, ".inventory_list > div")
    FOOTER_LINKS = (By.CSS_SELECTOR, "div#page_wrapper li")

    ITEM_NAME = ".inventory_item_name"
    ITEM_DESC = ".inventory_item_desc"
    ITEM_PRICE = ".inventory_item_price"
    ITEM_IMAGE = ".inventory_item_img a img"
    ITEM_BUTTON = ".btn_inventory"
