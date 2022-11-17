import allure
import time
import random
from selenium.webdriver.common.by import By
from pages.inventory_page.inventory_page import InventoryPage

LOGIN_PAGE_URL = "https://www.saucedemo.com/"
CART_URL = "https://www.saucedemo.com/cart.html"


class TestCartEdit:
    @allure.epic("Cart Page Test")
    @allure.story("TC_004.00 Cart | URL")
    def test_cart_url(self, browser):
        page = InventoryPage(browser, url=LOGIN_PAGE_URL)
        page.open()
        page.login_standard_user()
        browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        assert browser.current_url == CART_URL

    @allure.epic("Cart Page Test")
    @allure.story(
        "TC_004.00.__ Cart | Edit Cart Items"
        "Add to Cart from inventory Page > Go To Cart > Dell"
    )
    def test_cart_del_items_all(self, browser):
        page = InventoryPage(browser, url=LOGIN_PAGE_URL)
        page.open()
        page.login_standard_user()
        inventory_items = page.find_items_cards()
        items_in_cart = 0
        for item in inventory_items:
            page.click_item_cart_button(item)
            items_in_cart += 1
        browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        while items_in_cart != 0:
            browser.find_element(By.CLASS_NAME, "cart_button").click()
            items_in_cart -= 1
            assert items_in_cart == page.get_cart_counter()

    @allure.epic("Cart Page Test")
    @allure.story(
        "TC_004.00.02 Cart | Edit Cart Items"
        "Add to Cart from inventory Page > Go To Cart > Dell"
    )
    def test_cart_del_items_random(self, browser):
        page = InventoryPage(browser, url=LOGIN_PAGE_URL)
        page.open()
        page.login_standard_user()
        inventory_items = page.find_items_cards()
        items_in_cart = 0
        for item in random.sample(inventory_items, 3):
            page.click_item_cart_button(item)
            items_in_cart += 1
        browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        while items_in_cart != random.randint(1, items_in_cart):
            browser.find_element(By.CLASS_NAME, "cart_button").click()
            items_in_cart -= 1
            assert items_in_cart == page.get_cart_counter()
