import pytest
from ..pages.inventory_page import *

link_inv = "https://www.saucedemo.com/inventory.html"


@pytest.mark.elina_abramova
@pytest.mark.xfail
def test_add_items_all_users(d, login_from_list):
    page = InventoryPage(d, link_inv)
    d.implicitly_wait(2)
    page.add_to_cart_backpack_inventory()
