import allure
import random
from conf.website_config import WebSiteConfig
from pages.inventory_page.inventory_page_locators import InventoryPageLocators
from pages.your_info_page.your_info_page import YourInfoPage
from pages.cart_page.cart_page_locators import CartPageLocators
from pages.your_info_page.your_info_page_locators import YourInfoLocators


class TestYourInfoPage:
    def open_page(self, browser):
        page = YourInfoPage(browser)
        page.open()
        page.login_standard_user()
        return page

    @allure.epic("Checkout: Your Information Page Test")
    @allure.story("TC_005_ checkout  URL & header")
    def test_checkout_layout(self, browser):

        page = self.open_page(browser)
        inventory_items = page.find_items_cards()
        randon_num = random.randint(1, WebSiteConfig.ITEMS_COUNTER)
        for item in random.sample(inventory_items, randon_num):
            page.click_item_cart_button(item)
        items_in_cart_cnt = page.get_cart_counter()
        page.click_cart_button()
        page.click_button(CartPageLocators.BTN_CHECKOUT)
        assert browser.current_url == WebSiteConfig.YOUR_INFO_URL
        assert page.element_is_present(InventoryPageLocators.BTN_BURGER_MENU)
        assert page.element_is_present(InventoryPageLocators.LOGIN_LOGO)
        assert page.element_is_present(InventoryPageLocators.CART_LINK)
        assert items_in_cart_cnt == page.get_cart_counter()

    @allure.epic("Checkout: Your Information Page Test")
    @allure.story("TC_005_ checkout layout")
    def test_checkout_layout(self, browser):

        page = self.open_page(browser)
        inventory_items = page.find_items_cards()
        randon_num = random.randint(1, WebSiteConfig.ITEMS_COUNTER)
        for item in random.sample(inventory_items, randon_num):
            page.click_item_cart_button(item)
        page.click_cart_button()
        page.click_button(CartPageLocators.BTN_CHECKOUT)
        assert page.element_is_present(YourInfoLocators.INPUT_FIRST_NAME)
        assert page.element_is_present(YourInfoLocators.INPUT_LAST_NAME)
        assert page.element_is_present(YourInfoLocators.INPUT_ZIP_CODE)
        assert page.element_is_present(YourInfoLocators.BTN_CANCEL)
        assert page.element_is_present(YourInfoLocators.BTN_CONTINUE)
        assert (
            page.get_element_text(YourInfoLocators.TITLE)
            == "CHECKOUT: YOUR INFORMATION"
        )
        assert (
            page.get_attribute(
                YourInfoLocators.INPUT_FIRST_NAME, "placeholder"
            )
            == "First Name"
        )
        assert (
            page.get_attribute(YourInfoLocators.INPUT_LAST_NAME, "placeholder")
            == "Last Name"
        )
        assert (
            page.get_attribute(YourInfoLocators.INPUT_ZIP_CODE, "placeholder")
            == "Zip/Postal Code"
        )
        assert page.get_element_text(YourInfoLocators.BTN_CANCEL) == "CANCEL"
        assert (
            page.get_attribute(YourInfoLocators.BTN_CONTINUE, "value")
            == "Continue"
        )

    @allure.epic("Checkout: Your Information Page Test")
    @allure.story("TC_005.00.01 all fields are filled")
    def test_checkout_all_fields_are_filled(self, browser):

        page = self.open_page(browser)
        inventory_items = page.find_items_cards()
        randon_num = random.randint(1, WebSiteConfig.ITEMS_COUNTER)
        for item in random.sample(inventory_items, randon_num):
            page.click_item_cart_button(item)
        page.click_cart_button()
        page.click_button(CartPageLocators.BTN_CHECKOUT)
        page.send_keys_to_input(YourInfoLocators.INPUT_FIRST_NAME, "Petr")
        page.send_keys_to_input(YourInfoLocators.INPUT_LAST_NAME, "Smirnov")
        page.send_keys_to_input(YourInfoLocators.INPUT_ZIP_CODE, "234589")
        page.click_continue()
        assert browser.current_url == WebSiteConfig.OVERVIEW_URL

    @allure.epic("Checkout: Your Information Page Test")
    @allure.story("TC_005._ all fields are empty")
    def test_checkout_fields_are_empty(self, browser):

        page = self.open_page(browser)
        inventory_items = page.find_items_cards()
        randon_num = random.randint(1, WebSiteConfig.ITEMS_COUNTER)
        for item in random.sample(inventory_items, randon_num):
            page.click_item_cart_button(item)
        page.click_cart_button()
        page.click_button(CartPageLocators.BTN_CHECKOUT)
        page.click_continue()
        assert page.get_error_msg_text() == "Error: First Name is required"

    @allure.epic("Checkout: Your Information Page Test")
    @allure.story("TC_005.00.02 First Name is empty")
    def test_checkout_fields_are_empty(self, browser):

        page = self.open_page(browser)
        inventory_items = page.find_items_cards()
        randon_num = random.randint(1, WebSiteConfig.ITEMS_COUNTER)
        for item in random.sample(inventory_items, randon_num):
            page.click_item_cart_button(item)
        page.click_cart_button()
        page.click_button(CartPageLocators.BTN_CHECKOUT)
        page.send_keys_to_input(
            YourInfoLocators.INPUT_LAST_NAME, page.random_word()
        )
        page.send_keys_to_input(
            YourInfoLocators.INPUT_ZIP_CODE, page.random_word()
        )
        page.click_continue()
        assert page.get_error_msg_text() == "Error: First Name is required"

    @allure.epic("Checkout: Your Information Page Test")
    @allure.story("TC_005.00.02 Last Name is empty")
    def test_checkout_fields_are_empty(self, browser):

        page = self.open_page(browser)
        inventory_items = page.find_items_cards()
        randon_num = random.randint(1, WebSiteConfig.ITEMS_COUNTER)
        for item in random.sample(inventory_items, randon_num):
            page.click_item_cart_button(item)
        page.click_cart_button()
        page.click_button(CartPageLocators.BTN_CHECKOUT)
        page.send_keys_to_input(
            YourInfoLocators.INPUT_FIRST_NAME, page.random_word()
        )
        page.send_keys_to_input(
            YourInfoLocators.INPUT_ZIP_CODE, page.random_word()
        )
        page.click_continue()
        assert page.get_error_msg_text() == "Error: Last Name is required"

    @allure.epic("Checkout: Your Information Page Test")
    @allure.story("TC_005.00.02 Zip/Postal Code is empty")
    def test_checkout_fields_are_empty(self, browser):

        page = self.open_page(browser)
        inventory_items = page.find_items_cards()
        randon_num = random.randint(1, WebSiteConfig.ITEMS_COUNTER)
        for item in random.sample(inventory_items, randon_num):
            page.click_item_cart_button(item)
        page.click_cart_button()
        page.click_button(CartPageLocators.BTN_CHECKOUT)
        page.send_keys_to_input(
            YourInfoLocators.INPUT_FIRST_NAME, page.random_word()
        )
        page.send_keys_to_input(
            YourInfoLocators.INPUT_LAST_NAME, page.random_word()
        )
        page.click_continue()
        assert page.get_error_msg_text() == "Error: Postal Code is required"
