import pytest

from ..pages.cart_page import CartPage

link = "https://www.saucedemo.com/inventory.html"


@pytest.mark.xfail
def test_chackout_with_empty_cart(d, correct_login):
    page = CartPage(d, link)
    page.go_to_the_cart()
    page.cart_is_empty()
    page.chackout_order_with_empty_cart()
