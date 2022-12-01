from ..pages.inventory_page import InventoryPage
from ..pages.checkout_page import CheckoutPage
from ..pages.locators import CheckoutPageLocators


def test_widgets_inventory_page(d, correct_login):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(d, link)
    page.open_page()
    page.all_widgets_on_page()


def test_widgets_inventory_item_page(d, correct_login):
    link = "https://www.saucedemo.com/inventory-item.html?id=4"
    page = InventoryPage(d, link)
    page.open_page()
    page.all_widgets_on_page()


def test_widgets_cart_page(d, correct_login):
    link = "https://www.saucedemo.com/cart.html"
    page = InventoryPage(d, link)
    page.open_page()
    page.all_widgets_on_page()


def test_widgets_checkout_step_one_page(d, correct_login):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(d, link)
    page.add_to_cart_backpack()
    link = "https://www.saucedemo.com/checkout-step-one.html"
    page = CheckoutPage(d, link)
    page.open_page()
    page.all_widgets_on_page()


def test_widgets_checkout_step_two_page(d, correct_login):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(d, link)
    page.add_to_cart_backpack()
    link = "https://www.saucedemo.com/checkout-step-one.html"
    page = CheckoutPage(d, link)
    page.open_page()
    page.enter_checkout_info("Elena", "Precrasnaya", "11100")
    page.all_widgets_on_page()


def test_widgets_checkout_complete_page(d, correct_login):
    link = "https://www.saucedemo.com/inventory.html"
    page = InventoryPage(d, link)
    page.add_to_cart_backpack()
    link = "https://www.saucedemo.com/checkout-step-one.html"
    page = CheckoutPage(d, link)
    page.open_page()
    page.enter_checkout_info("Elena", "Precrasnaya", "11100")
    page.d.find_element(*CheckoutPageLocators.FINISH).click()
    page.all_widgets_on_page()
