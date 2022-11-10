from pages.base_page.base_page import BasePage
from pages.inventory_page.inventory_page_locators import InventoryPageLocators


class InventoryPage(BasePage):
    def open_burger_menu(self):
        self.click_button(InventoryPageLocators.BTN_BURGER_MENU)

    def close_burger_menu(self):
        self.click_button(InventoryPageLocators.BTN_BURGER_MENU_CLOSE)

    def click_side_menu_item(self, locator):
        self.open_burger_menu()
        self.click_button(locator)
