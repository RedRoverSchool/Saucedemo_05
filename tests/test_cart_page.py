import allure
import random
from pages.cart_page.cart_page import CartPage
from pages.cart_page.cart_page_locators import CartPageLocators
from conf.website_config import WebSiteConfig


class TestCartPage:
    def open_page(self, browser):
        page = CartPage(browser)
        page.open()
        page.login_standard_user()
        return page

    @allure.epic("Cart Page Test")
    @allure.story("TC_004.00 Cart | layout")
    def test_cart_url_btn(self, browser):
        page = self.open_page(browser)
        page.click_cart_button()
        assert browser.current_url == WebSiteConfig.CART_PAGE_URL
        assert page.get_element_text(CartPageLocators.TITLE) == "YOUR CART"
        assert page.get_element_text(CartPageLocators.DESCR) == "DESCRIPTION"
        assert page.element_is_present(CartPageLocators.BTN_CHECKOUT)
        assert page.get_element_text(CartPageLocators.BTN_CHECKOUT) == "CHECKOUT"
        assert page.get_element_text(CartPageLocators.BTN_CONTINUE_SHOPPING) == "CONTINUE SHOPPING"

    @allure.epic("Cart Page Test")
    @allure.story("TC_")
    def test_cart_page_remove_items(self, browser):
        page = self.open_page(browser)
        page.reset_page_state()
        inventory_items = page.find_items_cards()
        for item in inventory_items:
            page.click_item_cart_button(item)
        items_in_cart_cnt = page.get_cart_counter()
        page.click_cart_button()
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
        page = self.open_page(browser)
        inventory_items = page.find_items_cards()
        random_num = random.randint(1, 6)
        for item in random.sample(inventory_items, random_num):
            page.click_item_cart_button(item)
        items_in_cart_cnt = page.get_cart_counter()
        page.click_cart_button()
        items_in_cart = page.find_items_cart_cards()
        random_num_2 = random.randint(1, random_num)
        for item in random.sample(items_in_cart, random_num_2):
            page.click_item_remove(item)
            items_in_cart_cnt -= 1
            assert items_in_cart_cnt == page.get_cart_counter()

    @allure.epic("Cart Page Test")
    @allure.story(
        "TC_004.00.02 Cart | Edit Cart Items"
        "Add to Cart from inventory Page > Go To Cart > Dell > Continue Shopping"
    )
    def test_cart_page_remove_items_random_btn_cont_shopping(self, browser):
        page = self.open_page(browser)
        inventory_items = page.find_items_cards()
        randon_num = random.randint(1, 6)
        for item in random.sample(inventory_items, randon_num):
            page.click_item_cart_button(item)
        items_in_cart_cnt = page.get_cart_counter()
        page.click_cart_button()
        items_in_cart = page.find_items_cart_cards()
        randon_num_2 = random.randint(1, randon_num)
        for item in random.sample(items_in_cart, randon_num_2):
            page.click_item_remove(item)
            items_in_cart_cnt -= 1
        page.click_button(CartPageLocators.BTN_CONTINUE_SHOPPING)
        assert browser.current_url == WebSiteConfig.INVENTORY_PAGE_URL
