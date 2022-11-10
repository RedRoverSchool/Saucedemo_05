import pytest
import allure
from conf.users import users
from pages.login_page.login_page import LoginPage


LOGIN_PAGE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = "https://www.saucedemo.com/inventory.html"


class TestLoginPage:
    @allure.epic("Login Page Test")
    @allure.story("US_001.00 | Login Page > Login")
    @pytest.mark.smoke
    def test_login_registered_user(self, browser):
        """Login using registered user credentials."""
        login_page = LoginPage(browser, url=LOGIN_PAGE_URL)
        login_page.open()
        print(login_page.get_page_title())
        login_page.login_user(
            username=users["standard_user"]["username"],
            password=users["standard_user"]["password"],
        )
        print(login_page.get_page_title())


