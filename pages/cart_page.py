from .locators import *
from .base_page import *


class CartPage(BasePage):
    def backpack_can_be_removed(self):
        self.d.find_element(*CartPageLocators.REMOVE_ITEM_BTN).click()

    def cart_is_empty(self):
        assert self.element_is_NOT_present(*CartPageLocators.CART_ITEM_BLOCK)

    def click_icon_cart(self):
        self.d.find_element(*CartPageLocators.CART_ICON).click()

    def go_to_the_cart(self):
        self.d.find_element(*InventoryPageLocators.CART_BTN).click()
        assert "cart" in self.d.current_url

    def chackout_order_with_empty_cart(self):
        self.d.find_element(*CartPageLocators.BT_CHECKOUT).click()
        assert (
            "checkout-step-one" not in self.d.current_url
        ), "You on Checkout page with EMPTY CART"
