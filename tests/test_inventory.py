import allure
import pytest
from pages.inventory_page.inventory_page import InventoryPage
from pages.login_page.login_page import LoginPage


class TestCartClass:
    @allure.epic('US_002.00')
    @allure.story('TC_002.00.01')
    @allure.title("Bage change when adding")
    def test_change_bage_when_adding(
        self, driver, username='standard_user', password='secret_sauce'
    ):
        login_page = LoginPage(driver)
        with allure.step('step1 login user'):
            login_page.action_login(username, password)
        inventory_page = InventoryPage(driver)
        with allure.step('step2 click on add'):
            inventory_page.add_to_cart()
        with allure.step('step3 bage has changed'):
            inventory_page.bage_has_changed()

    @allure.epic('US_002.00')
    @allure.story('TC_002.00.02')
    @allure.title("Button text after remove")
    @pytest.mark.debug
    def test_change_add_button_text(
        self, driver, username='standard_user', password='secret_sauce'
    ):
        login_page = LoginPage(driver)
        with allure.step('step1 login user'):
            login_page.action_login(username, password)
        inventory_page = InventoryPage(driver)
        with allure.step('step2 text before adding'):
            inventory_page.button_text_before_adding()
        with allure.step('step3 click on button'):
            inventory_page.add_to_cart()
        with allure.step('step4 text after adding'):
            inventory_page.button_text_after_adding()
