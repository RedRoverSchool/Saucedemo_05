import time
from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.locators import link


def test_return_from_itempage(d):
    page = LoginPage(d, link)
    page.open_page()
    time.sleep(2)
    page.signin_4_username("standard_user", "secret_sauce")
    time.sleep(2)
    page.should_go_on_product_page()
    page = InventoryPage(d, link)
    page.go_to_backpack_item_page()
    time.sleep(2)
    page.go_back_from_itempage_to_inventorypage()
