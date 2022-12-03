import pytest
import allure
from pages.inventory_page.inventory_page import InventoryPage
from conf.website_config import WebSiteConfig


sorting_price_cases = ("Price (low to high)", "Price (high to low)")
sorting_name_cases = ("Name (Z to A)", "Name (A to Z)")


class TestInventoryPage:
    def login_standard_user(self, browser):
        page = InventoryPage(browser)
        page.open()
        page.login_standard_user()
        return page

    @allure.epic("Inventory Page Test")
    @allure.story("TC_002.00.01 | Test Inventory Page content")
    def test_inventory_page_content(self, browser):
        page = self.login_standard_user(browser)
        page.wait_page_loaded(check_images=True)
        if page.check_js_errors():
            raise Exception
        inventory_items = page.find_items_cards()
        inventory_item_names_count = len(set(page.extract_items_names(inventory_items)))
        inventory_item_descs_count = len(set(page.extract_items_descs(inventory_items)))
        inventory_item_img_lnk_count = len(
            set(page.extract_items_links(inventory_items))
        )
        assert (
            inventory_item_names_count == WebSiteConfig.ITEMS_COUNTER
            and inventory_item_descs_count == WebSiteConfig.ITEMS_COUNTER
            and inventory_item_img_lnk_count == WebSiteConfig.ITEMS_COUNTER
        ), "Some Items are not unique!"

    @allure.epic("Inventory Page Test")
    @allure.story("TC_002.00.02.01 | Test Inventory Page Sorting by price")
    @pytest.mark.parametrize("sorting", sorting_price_cases)
    def test_inventory_page_sorting_by_price(self, browser, sorting):
        page = self.login_standard_user(browser)
        page.set_sorting_order(sorting)
        inventory_items = page.find_items_cards()
        prices_list = page.extract_items_prices(inventory_items)
        expected_list = sorted(
            prices_list, reverse=True if sorting == "Price (high to low)" else False
        )
        assert expected_list == prices_list, "Sorting by price works incorrect"

    @allure.epic("Inventory Page Test")
    @allure.story("TC_002.00.02.02 | Test Inventory Page Sorting by name")
    @pytest.mark.parametrize("sorting", sorting_name_cases)
    def test_inventory_page_sorting_by_name(self, browser, sorting):
        page = self.login_standard_user(browser)
        page.set_sorting_order(sorting)
        inventory_items = page.find_items_cards()
        names_list = page.extract_items_names(inventory_items)
        expected_list = sorted(
            names_list, reverse=True if sorting == "Name (Z to A)" else False
        )
        assert expected_list == names_list, "Sorting by name works incorrect"

    @allure.epic("Inventory Page Test")
    @allure.story(
        "TC_002.01.01 | Add to Cart from inventory Page > button text changed"
    )
    def test_add_item_to_cart(self, browser):
        page = self.login_standard_user(browser)
        page.reset_page_state()
        inventory_items = page.find_items_cards()
        items_in_cart = page.get_cart_counter()
        for item in inventory_items:
            button_text = page.click_item_cart_button(item).upper()
            items_in_cart += 1
            assert button_text == "REMOVE"
            assert items_in_cart == page.get_cart_counter()
        items_in_cart = page.get_cart_counter()
        for item in inventory_items:
            button_text = page.click_item_cart_button(item).upper()
            items_in_cart -= 1
            assert button_text == "ADD TO CART"
            assert items_in_cart == page.get_cart_counter()
