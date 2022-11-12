import pytest
import allure
from pages.detailed_page.detailed_page import DetailedPage

LOGIN_PAGE_URL = "https://www.saucedemo.com/"


class TestDetailedPage:
    def test_add_to_cart(self, browser):
        page = DetailedPage(browser, url=LOGIN_PAGE_URL)
        page.open()
        page.login_standard_user()
        page.open_first_item()
        page.click_add_to_cart()

