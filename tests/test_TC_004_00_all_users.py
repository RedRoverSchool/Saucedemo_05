from ..pages.locators import *


def test_open_cart_all_users(d, login_from_list):
    assert d.title == "Swag Labs", "NOT ENTER"
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    assert d.current_url == "https://www.saucedemo.com/cart.html"
    d.find_element(*CartPageLocators.CONTINUE_SHOPPING).click()
    assert d.title == "Swag Labs", "____You NOT LEFT_____"
