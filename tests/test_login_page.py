import pytest
import allure
from conf.users import users
from pages.login_page.login_page import LoginPage
import time

LOGIN_PAGE_URL = "https://www.saucedemo.com/"


class TestLoginPage:
    @allure.epic("Login Page Test")
    @pytest.mark.smoke
    def test_login_registered_user(self, browser):
        login_page = LoginPage(browser, url=LOGIN_PAGE_URL)
        login_page.login_user(
            username=users["standard_user"]["username"],
            password=users["standard_user"]["password"],
        )
