from locators.locators import InventoryLocators as il


class InventoryPageKate:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(*il.ADD_BUTTON).click()

    def button_text_before_adding(self):
        assert (
            'ADD TO CART' in self.driver.find_element(*il.ADD_BUTTON).text
        ), "Incorrect text"

    def button_text_after_adding(self):
        assert (
            'REMOVE' in self.driver.find_element(*il.REMOVE_BUTTON).text
        ), "Incorrect text"

    def bage_has_changed(self):
        cart_bage = self.driver.find_element(*il.CART_BAGE).text
        assert '1' in cart_bage, "Incorrect count"

    def sort_by_AZ(self):
        self.driver.find_element(*il.AZ_BUTTON).click()

    def sort_by_ZA(self):
        self.driver.find_element(*il.ZA_BUTTON).click()

    def sort_by_ASC(self):
        self.driver.find_element(*il.ASC_BUTTON).click()

    def sort_by_DESC(self):
        self.driver.find_element(*il.DESC_BUTTON).click()

    def show_sorted_elements(self):
        sorted_list = []
        for option in self.driver.find_elements(*il.ALL_PRODUCTS):
            sorted_list.append(option.text)
        return sorted_list
