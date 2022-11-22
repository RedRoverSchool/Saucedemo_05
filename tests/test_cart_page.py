import allure
import pytest
import time
import random
from selenium.webdriver.common.by import By
from pages.login_page.login_page import LoginPage
from pages.inventory_page.inventory_page import InventoryPage
from pages.cart_page.cart_page_locators import CartPageLocators
from pages.cart_page.cart_page import CartPage
from conf.website_config import WebSiteConfig


class TestCartPage:
    @allure.epic("Cart Page Test")
    @allure.story("TC_004.00 Cart | URL")
    def test_cart_url_btn(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login_standard_user()
        page = InventoryPage(browser)
        page.click_cart_button()
        assert browser.current_url == WebSiteConfig.CART_PAGE_URL
        assert page.element_is_clickable(CartPageLocators.BTN_CHECKOUT)
        assert page.element_is_clickable(CartPageLocators.BTN_CONTINUE_SHOPPING)

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
        "TC_004.00.02 Cart | Edit Cart Items"
        "Add to Cart from inventory Page > Go To Cart > Dell"
    )
    def test_cart_page_remove_items_random(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login_standard_user()
        page = InventoryPage(browser)
        inventory_items = page.find_items_cards()
        for item in random.sample(inventory_items, 4):
            page.click_item_cart_button(item)
        items_in_cart_cnt = page.get_cart_counter()
        page.click_cart_button()
        page = CartPage(browser)
        items_in_cart = page.find_items_cart_cards()
        for item in random.sample(items_in_cart, 2):
            page.click_item_remove(item)
            items_in_cart_cnt -= 1
            assert items_in_cart_cnt == page.get_cart_counter()

    @allure.epic("Cart Page Test")
    @allure.story(
        "TC_004.00.02 Cart | Edit Cart Items"
        "Add to Cart from inventory Page > Go To Cart > Dell > Continue Shopping"
    )
    def test_cart_page_remove_items_random_btn_cont_shopping(self, browser):
        page = LoginPage(browser)
        page.open()
        page.login_standard_user()
        page = InventoryPage(browser)
        inventory_items = page.find_items_cards()
        for item in random.sample(inventory_items, 5):
            page.click_item_cart_button(item)
        items_in_cart_cnt = page.get_cart_counter()
        page.click_cart_button()
        page = CartPage(browser)
        items_in_cart = page.find_items_cart_cards()
        for item in random.sample(items_in_cart, 3):
            page.click_item_remove(item)
            items_in_cart_cnt -= 1
        page.click_button(CartPageLocators.BTN_CONTINUE_SHOPPING)
        assert browser.current_url == WebSiteConfig.INVENTORY_PAGE_URL
