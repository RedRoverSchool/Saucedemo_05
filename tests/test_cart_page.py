import allure
import pytest
import time
import random
from selenium.webdriver.common.by import By
from pages.login_page.login_page import LoginPage
from pages.inventory_page.inventory_page import InventoryPage
from pages.cart_page.cart_page import CartPage
from conf.website_config import WebSiteConfig

CART_URL = "https://www.saucedemo.com/cart.html"


class TestCartPage:
    @allure.epic("Cart Page Test")
    @allure.story("TC_004.00 Cart | URL")
    def test_cart_url(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login_standard_user()
        browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        assert browser.current_url == CART_URL

    @allure.epic("Cart Page Test")
    @allure.story("TC_")
    def test_cart_page_remove_items(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login_standard_user()
        page = InventoryPage(browser)
        page.reset_page_state()
        inventory_items = page.find_items_cards()
        for item in inventory_items:
            page.click_item_cart_button(item)
        items_in_cart_cnt = page.get_cart_counter()
        page.click_cart_button()
        page = CartPage(browser)
        items_in_cart = page.find_items_cart_cards()
        assert items_in_cart_cnt == len(items_in_cart)
        for item in items_in_cart:
            page.click_item_remove(item)
            items_in_cart_cnt -= 1
            assert items_in_cart_cnt == page.get_cart_counter()
        assert page.get_cart_counter() == 0

    @allure.epic("Cart Page Test")
    @allure.story(
        "TC_004.00.__ Cart | Edit Cart Items"
        "Add to Cart from inventory Page > Go To Cart > Dell"
    )
    def test_cart_del_items_all(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login_standard_user()
        page = InventoryPage(browser)
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
        page = LoginPage(browser)
        page.open()
        page.login_standard_user()
        page = InventoryPage(browser)
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
