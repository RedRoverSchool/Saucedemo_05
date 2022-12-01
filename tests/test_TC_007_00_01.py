from selenium.webdriver.common.by import By
from ..pages.login_page import LoginPage
from ..pages.inventory_page import InventoryPage
from ..pages.cart_page import CartPage
from ..pages.locators import (
    link,
    InventoryPageLocators,
    CartPageLocators,
    CheckoutPageLocators,
)


def test_checkout_info_active(d):
    page = LoginPage(d, link)
    page.signin_standart_user(login="standard_user", password="secret_sauce")
    page = InventoryPage(d, link)

    first_item = d.find_element(*InventoryPageLocators.BACKPACK_LABEL)
    second_item = d.find_element(*InventoryPageLocators.FLEECE_JACKET_LABEL)
    third_item = d.find_element(*InventoryPageLocators.ONESIE_LABEL)
    item = InventoryPageLocators()
    page.add_item_to_cart(
        item.BACKPACK_ADD_BTN, item.FLEECE_JACKET_ADD_BTN, item.ONESIE_ADD_BTN
    )
    page = CartPage(d, link)
    page.click_icon_cart()
    assert first_item
    assert second_item
    assert third_item
    d.find_element(*CartPageLocators.BT_CHECKOUT).click()
    assert (
        d.find_element(By.XPATH, '//*[text()="Checkout: Your Information"]')
        and d.current_url == "https://www.saucedemo.com/checkout-step-one.html"
    )
    d.find_element(*CheckoutPageLocators.FIRS_NAME).send_keys("Alice")
    d.find_element(*CheckoutPageLocators.LAST_NAME).send_keys("Smith")
    d.find_element(*CheckoutPageLocators.ZIP_P_CODE).send_keys(85001)

    d.find_element(*CheckoutPageLocators.CONTINUE).click()
    assert (
        d.find_element(By.XPATH, '//*[text()="Checkout: Overview"]')
        and d.current_url == "https://www.saucedemo.com/checkout-step-two.html"
    )
