from ..pages.locators import *


def test_checkout_fields_empty(d, correct_login):
    d.find_element(*InventoryPageLocators.FLEECE_JACKET_ADD_BTN).click()
    d.find_element(*InventoryPageLocators.CART_BTN).click()
    d.find_element(*CartPageLocators.BT_CHECKOUT).click()
    d.find_element(*CheckoutPageLocators.CONTINUE).click()
    assert (
        d.find_element(
            By.XPATH,
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[4]",
        ).text
        == "Error: First Name is required"
    ), "Message not founded"
