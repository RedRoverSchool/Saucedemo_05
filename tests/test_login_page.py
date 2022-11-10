import time
import pytest
import allure
from conf.users import users
from pages.login_page.login_page import LoginPage
from pages.inventory_page.inventory_page import InventoryPage

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
        login_page.login_user(
            username=users["standard_user"]["username"],
            password=users["standard_user"]["password"],
        )
        # print(f"Navigated to {login_page.get_current_url()}")
        inventory_page = InventoryPage(browser, url=INVENTORY_URL)
        inventor_items = inventory_page.find_items_cards()
        inventory_page.open_burger_menu()
        time.sleep(1)
        inventory_page.click_logout_from_burger_menu()
        # print(f"Navigated to {inventory_page.get_current_url()}")
        assert len(inventor_items) == 6, "The number of items cards is not equal to 6"

    @allure.epic("Login Page Test")
    @allure.story("US_001.00 | Login Page > Login (Login Locked Out User)")
    def test_login_locked_out_user(self, browser):
        login_page = LoginPage(browser, url=LOGIN_PAGE_URL)
        login_page.open()
        login_page.login_user(
            username=users["locked_out_user"]["username"],
            password=users["locked_out_user"]["password"],
        )
        assert (
            login_page.get_alert_text()
            == "Epic sadface: Sorry, this user has been locked out."
        )

    @allure.epic("Login Page Test")
    @allure.story(
        "TC_001.00.02 | Try to login unregistered user (incorrect login, correct pass)"
    )
    @pytest.mark.smoke
    def test_login_unregistered_user(self, browser):
        login_page = LoginPage(browser, url=LOGIN_PAGE_URL)
        login_page.open()
        login_page.login_user(
            username="unregistered_user",
            password="secret_sauce",
        )
        assert (
            login_page.get_alert_text()
            == "Epic sadface: Username and password do not match any user in this service"
        )

    @allure.epic("Login Page Test")
    @allure.story("Try to navigate to inventory page while logged out")
    def test_inventory_logout_user(self, browser):
        login_page = LoginPage(browser, url=LOGIN_PAGE_URL)
        login_page.open()
        login_page.navigate_to(INVENTORY_URL)
        assert (
            login_page.get_alert_text()
            == "Epic sadface: You can only access '/inventory.html' when you are logged in."
        )
