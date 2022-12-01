import pytest
from ..pages.inventory_page import *
from ..pages.cart_page import *

link_inv = "https://www.saucedemo.com/inventory.html"
link_Cart = "https://www.saucedemo.com/cart.html"


@pytest.mark.elina_abramova
@pytest.mark.xfail
def test_remove_items_from_cart_on_cart_page(d, login_from_list):
    page = InventoryPage(d, link_inv)
    page.add_to_cart_backpack_inventory()
    page = CartPage(d, link_Cart)
    d.implicitly_wait(2)
    page.backpack_can_be_removed()
    page.cart_is_empty()
