import random
from pages.inventory_page.inventory_page import InventoryPage
from pages.detailed_page.detailed_page_locator import DetailedPageLocators
from pages.inventory_page.inventory_page_locators import InventoryPageLocators


class DetailedPage(InventoryPage):
    def open_first_item(self):
        self.click_button(InventoryPageLocators.ITEM_NAME)

    def click_add_to_cart(self):  # кликнуть Add to cart на странице продукта
        self.click_button(DetailedPageLocators.ADD_TO_CART_BUTTON)

    def click_remove_button(self):
        self.click_button(DetailedPageLocators.REMOVE_BUTTON)

    def click_back_to_products(self):
        self.click_button(DetailedPageLocators.BACK_TO_PRODUCTS)

    def get_random_item_properties_and_click(self, browser):
        # get the list of all products on the page
        products_list = browser.find_elements(*InventoryPageLocators.ITEMS_CARDS)

        # select random product from product_list
        item_for_compare = random.randint(0, len(products_list) - 1)

        # get values of all parameters
        item_for_click = products_list[item_for_compare].find_element(
            *InventoryPageLocators.ITEM_NAME
        )
        inventory_description = (
            products_list[item_for_compare]
            .find_element(*InventoryPageLocators.ITEM_DESC)
            .text
        )
        inventory_price = (
            products_list[item_for_compare]
            .find_element(*InventoryPageLocators.ITEM_PRICE)
            .text
        )
        inventory_name = (
            products_list[item_for_compare]
            .find_element(*InventoryPageLocators.ITEM_NAME)
            .text
        )
        inventory_image = (
            products_list[item_for_compare]
            .find_element(*InventoryPageLocators.ITEM_IMAGE)
            .get_attribute("src")
        )

        return (
            inventory_name,
            inventory_description,
            inventory_price,
            inventory_image,
            item_for_click,
        )
