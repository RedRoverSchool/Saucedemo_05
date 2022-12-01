from ..pages.cart_page import *
from ..pages.locators import CheckoutPageLocators


def test_finish_shopping(d, correct_login):
    d.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    cart = CartPage(d, link)
    cart.click_icon_cart()
    d.find_element(
        By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]",
    ).click()
    d.find_element(*CartPageLocators.BT_CHECKOUT).click()
    page_ch_you_inf = d.find_element(
        By.XPATH, "//span[contains(text(),'Checkout: Your Information')]"
    )
    assert page_ch_you_inf.text == "CHECKOUT: YOUR INFORMATION", "Page not found!!!"
    d.find_element(*CheckoutPageLocators.FIRS_NAME).send_keys("Test_user")
    d.find_element(*CheckoutPageLocators.LAST_NAME).send_keys("Test_password")
    d.find_element(*CheckoutPageLocators.ZIP_P_CODE).send_keys("43250")
    d.find_element(*CheckoutPageLocators.CONTINUE).click()
    assert (
        d.current_url == "https://www.saucedemo.com/checkout-step-two.html"
    ), "Not Found"
    d.find_element(*CheckoutPageLocators.FINISH).click()
    complete_message_text = d.find_element(
        By.XPATH, '//*[@id="checkout_complete_container"]/h2'
    ).text
    expected_complete_message = "THANK YOU FOR YOUR ORDER"
    assert complete_message_text == expected_complete_message
    print("______THANKS FOR YOUR ORDER_____")
    d.find_element(By.ID, "back-to-products").click()
    assert (
        d.current_url == "https://www.saucedemo.com/inventory.html"
    ), "Page Not Found!!!"
