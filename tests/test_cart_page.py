import conf
from pages.locators import LoginPageLocators
from pages.locators import ProductPageLocators


class TestAddToCart:
    def test_add_to_cart(self, d):

        assert d.current_url == conf.URL

        # login
        d.find_element(*LoginPageLocators.LOGIN_FORM).send_keys("standard_user")
        d.find_element(*LoginPageLocators.PASSWORD_FORM).send_keys("secret_sauce")
        d.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert d.current_url == "https://www.saucedemo.com/inventory.html"

        add_to_cart_button = d.find_element(
            *ProductPageLocators.SAUCE_LABS_BACKPACK_ADD_TO_CART
        ).text

        assert add_to_cart_button == "ADD TO CART"
        d.find_element(*ProductPageLocators.SAUCE_LABS_BACKPACK_ADD_TO_CART).click()

        shopping_cart = d.find_element(*ProductPageLocators.SHOPPING_CART_LINK).text
        assert shopping_cart == "1"

        remove_from_cart_button = d.find_element(
            *ProductPageLocators.SAUCE_LABS_BACKPACK_REMOVE_FROM_CART
        ).text
        assert remove_from_cart_button == "REMOVE"

        d.find_element(
            *ProductPageLocators.SAUCE_LABS_BACKPACK_REMOVE_FROM_CART
        ).click()

        shopping_cart = d.find_element(*ProductPageLocators.SHOPPING_CART_LINK).text
        assert shopping_cart == ""
