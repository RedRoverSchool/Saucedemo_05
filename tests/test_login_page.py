import pytest
import allure
from pages.login_page.login_page import LoginPage
from pages.inventory_page.inventory_page import InventoryPage
import conf

failed_users_test_cases = (
    ("locked_out_user", "Epic sadface: Sorry, this user has been locked out."),
    (
        "unregistered_user",
        "Epic sadface: Username and password do not match any user in this service",
    ),
    ("empty_username_user", "Epic sadface: Username is required"),
    ("empty_password_user", "Epic sadface: Password is required"),
)


class TestLoginPage:
    @allure.epic("Login Page Test")
    @allure.story("US_001.00 | Login Page > Login")
    def test_login_registered_user(self, driver):
        """Login using registered user credentials."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login_standard_user()
        inventory_page = InventoryPage(driver)
        inventor_items = inventory_page.find_items_cards()
        inventory_page.do_logout()
        assert (
            len(inventor_items) == conf.ITEMS_COUNTER
        ), f"The number of items cards is not equal to {conf.ITEMS_COUNTER}"

    @allure.epic("Login Page Test")
    @allure.story("TC_001.00.02 | Try to login unregistered/locked out user")
    @pytest.mark.parametrize("user, msg", failed_users_test_cases)
    def test_unsuccessful_login(self, driver, user, msg):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login_user(
            username=conf.USERS[user]["username"],
            password=conf.USERS[user]["password"],
        )
        assert login_page.get_alert_text() == msg

    @allure.epic("Login Page Test")
    @allure.story("TC_001.00.02 | Try to login unregistered/locked out user")
    @allure.story("Try to navigate to inventory page while logged out")
    def test_inventory_logout_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.navigate_to(conf.INVENTORY_PAGE_URL)
        assert (
            login_page.get_alert_text()
            == "Epic sadface: You can only access '/inventory.html' when you are logged in."
        )