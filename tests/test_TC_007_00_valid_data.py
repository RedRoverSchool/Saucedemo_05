import time

import pytest
from ..pages.inventory_page import *
from ..pages.cart_page import *
from ..pages.checkout_page import *


link_inv = "https://www.saucedemo.com/inventory.html"
link_Cart = "https://www.saucedemo.com/cart.html"
link_checkout = "https://www.saucedemo.com/checkout-step-one.html"


@pytest.mark.elina_abramova
@pytest.mark.xfail
def test_checkout(d, login_from_list):
    page = InventoryPage(d, link_inv)
    page.add_to_cart_backpack_inventory_item()
    page.add_to_cart_bike_lite_inventory_item()
    page.add_to_cart_onesie_inventory_item()

    page = CartPage(d, link_Cart)
    # d.implicitly_wait(2)
    page.go_to_the_cart()
    # assert (
    #     len(d.find_elements(By.CLASS_NAME, "cart_item")) == 3
    # ), "---WRONG NUMBER OF ELEMENTS---"
    assert (
        "Sauce Labs Backpack"
        and "Sauce Labs Bike Light"
        and "Sauce Labs Onesie" in d.find_element(By.CLASS_NAME, "cart_list").text
    )
    d.find_element(*CartPageLocators.BT_CHECKOUT).click()
    assert "checkout-step-one" in d.current_url, "---WRONG URL---"

    page = CheckoutPage(d, link_checkout)
    page.enter_checkout_info("Alice", "Smith", 78717)
    assert "checkout-step-two" in d.current_url, "---WRONG URL---"
