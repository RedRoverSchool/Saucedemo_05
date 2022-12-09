from pages.inventory_page.inventory_page import InventoryPage
from pages.detailed_page.detailed_page_locators import DetailedPageLocators
from pages.inventory_page.inventory_page_locators import InventoryPageLocators


class DetailedPage(InventoryPage):
    def open_first_item(self):
        self.click_button(InventoryPageLocators.ITEM_NAME)

    def click_add_to_cart(self):  # click Add to cart on the product page
        self.click_button(DetailedPageLocators.ADD_TO_CART_BUTTON)
