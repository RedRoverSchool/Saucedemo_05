from pages.base_page.base_page import BasePage
from pages.login_page.login_page import LoginPage
from pages.detailed_page.detailed_page_locator import DetailedPageLocators
from pages.inventory_page.inventory_page_locators import InventoryPageLocators


class DetailedPage(LoginPage, BasePage):
    def open_first_item(self):
        self.click_button(InventoryPageLocators.ITEM_NAME)

    def click_add_to_cart(self):  # кликнуть Add to cart на странице продукта
        self.click_button(DetailedPageLocators.ADD_TO_CART_BUTTON)
