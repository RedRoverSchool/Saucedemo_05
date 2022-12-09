from typing import List
import logging
import conf
from selenium.webdriver.remote.webelement import WebElement
from pages.inventory_page.inventory_page import InventoryPage
from pages.inventory_page.inventory_page_locators import InventoryPageLocators
from pages.cart_page.cart_page_locators import CartPageLocators


class CartPage(InventoryPage):
    def __init__(self, browser):
        self.browser = browser
        self.url = conf.CART_PAGE_URL
        super().__init__(browser=self.browser)

    def navigate_to_cart_page(self):
        self.navigate_to(url=conf.CART_PAGE_URL)

    def click_continue_shopping(self):
        self.click_button(CartPageLocators.BTN_CONTINUE_SHOPPING)

    def click_checkout(self):
        self.click_button(CartPageLocators.BTN_CHECKOUT)

    def get_cart_counter(self) -> int:
        try:
            cart_items_counter = self.element_is_present(
                InventoryPageLocators.CART_BADGE
            )
            return int(cart_items_counter.text)
        except Exception as e:
            logging.error(f"Counter for cart is 0, {e}")
            return 0

    def find_items_cart_cards(self) -> List[WebElement]:
        return self.elements_are_present(CartPageLocators.ITEM_CARD)

    def click_item_remove(self, element: WebElement) -> None:
        element.find_element(*CartPageLocators.ITEM_BTN).click()
