import pytest
import allure
from pages.inventory_page.inventory_page import InventoryPage

LOGIN_PAGE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

sorting_price_cases = (
    ("Price (low to high)", ("$7.99", "$9.99", "$15.99", "$15.99", "$29.99", "$49.99")),
    ("Price (high to low)", ("$49.99", "$29.99", "$15.99", "$15.99", "$9.99", "$7.99")),
)

sorting_name_cases = (
    (
        "Name (Z to A)",
        (
            "Test.allTheThings() T-Shirt (Red)",
            "Sauce Labs Onesie",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Bike Light",
            "Sauce Labs Backpack",
        ),
    ),
    (
        "Name (A to Z)",
        (
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)",
        ),
    ),
)


class TestInventoryPage:
    @allure.epic("Inventory Page Test")
    @allure.story("TC_002.00.01 | Test Inventory Page content")
    def test_inventory_page_content(self, browser):
        page = InventoryPage(browser, url=LOGIN_PAGE_URL)
        page.open()
        page.login_standard_user()
        inventory_items = page.find_items_cards()
        inventory_item_names_count = len(set(page.extract_items_names(inventory_items)))
        inventory_item_descs_count = len(set(page.extract_items_descs(inventory_items)))
        inventory_item_img_lnk_count = len(
            set(page.extract_items_links(inventory_items))
        )
        assert (
            inventory_item_names_count == 6
            and inventory_item_descs_count == 6
            and inventory_item_img_lnk_count == 6
            # and not page.check_js_errors()
            # and not page.wait_page_loaded(check_images=True)
        ), "Some Items are not unique!"

    @allure.epic("Inventory Page Test")
    @allure.story("TC_002.00.02.01 | Test Inventory Page Sorting by price")
    @pytest.mark.parametrize("sorting, prices", sorting_price_cases)
    def test_inventory_page_sorting_by_price(self, browser, sorting, prices):
        page = InventoryPage(browser, url=LOGIN_PAGE_URL)
        page.open()
        page.login_standard_user()
        page.set_sorting_order(sorting)
        inventory_items = page.find_items_cards()
        assert page.extract_items_prices(inventory_items) == list(
            prices
        ), "Sorting by price works incorrect"

    @allure.epic("Inventory Page Test")
    @allure.story("TC_002.00.02.02 | Test Inventory Page Sorting by name")
    @pytest.mark.parametrize("sorting, names", sorting_name_cases)
    def test_inventory_page_sorting_by_name(self, browser, sorting, names):
        page = InventoryPage(browser, url=LOGIN_PAGE_URL)
        page.open()
        page.login_standard_user()
        page.set_sorting_order(sorting)
        inventory_items = page.find_items_cards()
        assert page.extract_items_names(inventory_items) == list(
            names
        ), "Sorting by name works incorrect"
