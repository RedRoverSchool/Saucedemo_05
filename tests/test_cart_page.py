import time

import pytest
import allure
from pages.login_page.login_page import LoginPage
from pages.inventory_page.inventory_page import InventoryPage
from pages.cart_page.cart_page import CartPage
from conf.website_config import WebSiteConfig


class TestCartPage:
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