import time

import pytest

from ..pages.locators import InventoryPageLocators
from ..pages.locators import link
from ..pages.login_page import LoginPage


@pytest.mark.xfail
def test_about_page_all_users(d, login_from_list):
    d.find_element(*InventoryPageLocators.BURGER_BTN).click()
    time.sleep(2)
    d.find_element(*InventoryPageLocators.BURGER_MENU_ABOUT_BTN).click()
    assert d.current_url == "https://saucelabs.com/"
