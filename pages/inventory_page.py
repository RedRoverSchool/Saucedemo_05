import time
from .base_page import BasePage
from .locators import *


class InventoryPage(BasePage):
    def add_to_cart_backpack_inventory_item(self):
        self.d.find_element(*InventoryPageLocators.BACKPACK_ADD_BTN).click()
        # assert "id=4" in self.d.current_url

    def add_to_cart_bike_lite_inventory_item(self):
        self.d.find_element(*InventoryPageLocators.BIKELIGHT_ADD_BTN).click()

    def add_to_cart_onesie_inventory_item(self):
        self.d.find_element(*InventoryPageLocators.ONESIE_ADD_BTN).click()

    def add_to_cart_backpack_inventory(self):
        self.d.find_element(*InventoryPageLocators.BACKPACK_ADD_BTN).click()
        self.d.find_element(*InventoryPageLocators.CART_BTN).click()
        assert "cart" in self.d.current_url
        assert (
            "Sauce Labs Backpack"
            in self.d.find_element(*InventoryPageLocators.BACKPACK_LABEL).text
        )

    def change_quantity_in_cart(self):
        self.add_to_cart_backpack_inventory()

    def add_to_cart_backpack(self):
        self.d.find_element(*InventoryPageLocators.BACKPACK_ADD_BTN).click()

    def item_added_to_cart(self):
        assert self.element_is_present(*InventoryPageLocators.CART_BADGE)
        assert self.element_is_present(*InventoryPageLocators.BACKPACK_REMOVE_BTN)

    def no_item_in_cart(self):
        assert self.element_is_NOT_present(*InventoryPageLocators.CART_BADGE)
        assert self.element_is_NOT_present(*InventoryPageLocators.BACKPACK_REMOVE_BTN)

    def remove_backpack_from_cart(self):
        self.d.find_element(*InventoryPageLocators.BACKPACK_REMOVE_BTN).click()

    def user_on_inventory_page(self):
        assert "inventory" in self.d.current_url

    def sort_items_on_inventory_page_az_za(self):
        unsortedlist = self.d.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
        unsortedfinal = []
        for x in unsortedlist:
            unsortedfinal.append(x.text)
        unsortedfinal.sort()
        print(unsortedfinal)
        self.d.find_element(*InventoryPageLocators.SORT_MENU_BUTTON).click()
        time.sleep(2)
        self.d.find_element(*InventoryPageLocators.SORT_OPTION_BUTTON_AZ).click()
        time.sleep(2)
        sortedlistaz = self.d.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
        sortedazfinal = []
        for i in sortedlistaz:
            sortedazfinal.append(i.text)
        print(sortedazfinal)
        self.d.find_element(*InventoryPageLocators.SORT_MENU_BUTTON).click()
        time.sleep(2)
        self.d.find_element(*InventoryPageLocators.SORT_OPTION_BUTTON_ZA).click()
        time.sleep(2)
        sortedlistza = self.d.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
        sortedzafinal = []
        for p in sortedlistza:
            sortedzafinal.append(p.text)
        print(sortedzafinal)
        sortedzafinal.reverse()
        print(sortedzafinal)
        assert sortedazfinal == unsortedfinal
        assert sortedazfinal == sortedzafinal

    def sort_items_on_inventory_page_lowhigh_highlow(self):
        self.d.find_element(*InventoryPageLocators.SORT_MENU_BUTTON).click()
        self.d.find_element(*InventoryPageLocators.SORT_OPTION_BUTTON_LOWHIGH).click()
        time.sleep(2)
        sortedlist = self.d.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
        self.d.find_element(*InventoryPageLocators.SORT_MENU_BUTTON).click()
        self.d.find_element(*InventoryPageLocators.SORT_OPTION_BUTTON_HIGHLOW).click()
        time.sleep(2)
        sortedlist1 = self.d.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
        assert sortedlist[0] == sortedlist1[-1]

    def go_to_backpack_item_page(self):
        self.d.find_element(*InventoryPageLocators.BACKPACK_LABEL).click()
        assert self.element_is_present(*InventoryItemPageLocator.BACK_TO_PRODUCKS_BTN)

    def go_back_from_itempage_to_inventorypage(self):
        self.d.find_element(*InventoryItemPageLocator.BACK_TO_PRODUCKS_BTN).click()
        assert self.element_is_present(*InventoryPageLocators.CART_BTN)

    def add_item_to_cart(self, *args):
        count = 0
        for item in args:
            self.d.find_element(*item).click()
            count += 1
        assert str(count) in self.d.find_element(*InventoryPageLocators.CART_BADGE).text
