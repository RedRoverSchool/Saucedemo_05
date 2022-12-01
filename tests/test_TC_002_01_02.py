import time
from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.locators import link


def test_sort_items_az_za_lowhigh_highlow(d):
    page = LoginPage(d, link)
    page.open_page()
    time.sleep(2)
    page.signin_4_username("standard_user", "secret_sauce")
    page.should_go_on_product_page()
    page = InventoryPage(d, link)
    page.sort_items_on_inventory_page_az_za()
    page.sort_items_on_inventory_page_lowhigh_highlow()
