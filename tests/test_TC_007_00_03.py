import time

import pytest
from ..pages.inventory_page import *
from ..pages.cart_page import *
from ..pages.checkout_page import *


link_inv = "https://www.saucedemo.com/inventory.html"
link_Cart = "https://www.saucedemo.com/cart.html"
link_checkout = "https://www.saucedemo.com/checkout-step-one.html"


@pytest.mark.elina_abramova
# @pytest.mark.xfail
def test_checkout(d, login_from_list):
    page = InventoryPage(d, link_inv)
    page.add_to_cart_backpack_inventory_item()
    page.add_to_cart_bike_lite_inventory_item()
    page.add_to_cart_onesie_inventory_item()

    """создаем словарь ['name':'price'] из товаров, которые добавляем в корзину"""

    items = d.find_elements(
        By.XPATH,
        "//*[@class='btn btn_secondary btn_small btn_inventory']/../../div[@class='inventory_item_label']/a",
    )
    keys_inventory = []
    for k in items:
        keys_inventory.append(k.text)
    prices = d.find_elements(
        By.XPATH, "//*[@class='btn btn_secondary btn_small btn_inventory']/../div"
    )
    values_inventory = []
    for v in prices:
        values_inventory.append(v.text)
    dict_inventory = {
        keys_inventory[i]: values_inventory[i] for i in range(len(keys_inventory))
    }

    """go to cart page, then to chechout page"""

    d.find_element(*InventoryPageLocators.CART_BTN).click()
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

    """создаем словарь из товаров, которые указаны на странице checkout:overview"""

    items_ov = d.find_elements(
        By.XPATH,
        "//div[@class='cart_item_label']/a",
    )
    keys_overview = []
    for k in items_ov:
        keys_overview.append(k.text)
    prices_ov = d.find_elements(
        By.XPATH, "//div[@class='cart_item_label']//div[@class='inventory_item_price']"
    )
    values_overview = []
    for v in prices_ov:
        values_overview.append(v.text)
    dict_overview = {
        keys_overview[i]: values_overview[i] for i in range(len(keys_overview))
    }
    assert dict_inventory == dict_overview, "---LISTS ARE NOT THE SAME---"

    """Проверем наличие: Payment, Shipping and Price information (Item total, Tax, Total)"""

    assert (
        d.find_element(
            By.XPATH, "//div[@class='summary_info']/div[@class='summary_info_label'][1]"
        ).text
        == "Payment Information:"
    )
    assert (
        d.find_element(
            By.XPATH, "//div[@class='summary_info']/div[@class='summary_info_label'][2]"
        ).text
        == "Shipping Information:"
    )

    """сравниваем сумму цены товаров с графой Item total"""

    item_total = d.find_element(By.CLASS_NAME, "summary_subtotal_label").text
    item_total_ = float(item_total.replace("Item total: $", ""))

    ammount_ = list(" ".join(values_overview).replace("$", "").split(" "))
    ammount = 0
    for x in ammount_:
        ammount += float(x)

    assert item_total_ == ammount
