import time
import pytest
from ..pages.locators import InventoryPageLocators
from ..pages.locators import link
from ..pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
    ],
)
def test_logout(d, username, password):
    page = LoginPage(d, link)
    page.should_be_login_form()
    page.signin_4_username(username, password)
    time.sleep(1)
    page.should_go_on_product_page()

    d.find_element(*InventoryPageLocators.BURGER_BTN).click()
    time.sleep(2)
    d.find_element(*InventoryPageLocators.BURGER_MENU_LOGOUT_BTN).click()
    assert d.current_url == link
