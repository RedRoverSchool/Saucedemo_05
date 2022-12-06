import pytest
import allure
from pages.detailed_page.detailed_page import DetailedPage
from pages.detailed_page.detailed_page_locator import DetailedPageLocators


class TestDetailedPage:
    def open_page(self, browser):
        page = DetailedPage(browser)
        page.open()
        page.login_standard_user()
        return page

    @allure.epic("Detailed Page Test")
    @allure.story("TC_003.00.01 | Detailed item description")
    def test_add_to_cart(self, browser):
        page = self.open_page(browser)
        page.open_first_item()
        page.click_add_to_cart()

        assert (
            page.element_is_visible(DetailedPageLocators.REMOVE_BUTTON),
            "there is no remove button",
        )
        assert page.get_cart_counter() == 1

    @allure.epic("Detailed item description")
    @allure.story("TC_003.00.02 | Test Inventory Page")
    def test_compare_inventory_and_detailed(self, browser):
        page = self.open_page(browser)
        (
            inventory_name,
            inventory_description,
            inventory_price,
            inventory_image,
            item,
        ) = page.get_random_item_properties_and_click(browser)
        item.click()

        details_name = browser.find_element(
            *DetailedPageLocators.DETAILS_ITEM_NAME
        ).text
        # # сверяю 1 элемент из списка продуктов с name на detailed page
        assert inventory_name == details_name

        details_description = browser.find_element(
            *DetailedPageLocators.DETAILS_ITEM_DESC
        ).text
        assert inventory_description == details_description

        details_price = browser.find_element(
            *DetailedPageLocators.DETAILS_ITEM_PRICE
        ).text
        assert inventory_price == details_price

        details_image = browser.find_element(
            *DetailedPageLocators.DETAILS_ITEM_IMAGE
        ).get_attribute("src")
        assert inventory_image == details_image

    @allure.epic("Detailed item description")
    @allure.story("TC_003.00.04 | Remove Button")
    def test_remove_button(self, browser):
        page = self.open_page(browser)
        page.open_first_item()
        page.click_add_to_cart()
        page.click_remove_button()

        assert (
            page.element_is_visible(DetailedPageLocators.ADD_TO_CART_BUTTON),
            "there is no add button",
        )
        assert page.get_cart_counter() == 0

    @allure.epic("Detailed item description")
    @allure.story("TC_003.00.03 | Back to Product")
    def test_back_to_product(self, browser):
        page = self.open_page(browser)
        page.open_first_item()
        page.click_add_to_cart()
        page.click_back_to_products()

        assert page.get_cart_counter() == 1
        assert page.element_is_visible(DetailedPageLocators.PRODUCTS_LABEL)
