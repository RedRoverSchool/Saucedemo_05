import pytest

from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.locators import link


@pytest.mark.xfail
def test_sort_items_az_za_lowhigh_highlow_all_users(d, login_from_list):
    page = LoginPage(d, link)
    page.should_go_on_product_page()
    page = InventoryPage(d, link)
    page.sort_items_on_inventory_page_az_za()
    page.sort_items_on_inventory_page_lowhigh_highlow()
