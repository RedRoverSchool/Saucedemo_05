from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import conf
from pages.locators import LoginPageLocators
from pages.locators import BurgerMenuLocators


class TestLoginPage:
    def test_login(self, d):

        assert d.current_url == conf.URL

        # login
        d.find_element(*LoginPageLocators.LOGIN_FORM).send_keys("standard_user")
        d.find_element(*LoginPageLocators.PASSWORD_FORM).send_keys("secret_sauce")
        d.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert d.current_url == "https://www.saucedemo.com/inventory.html"

        # logout
        d.find_element(*BurgerMenuLocators.BURGER_MENU).click()

        wait = WebDriverWait(d, 5)
        wait.until(
            EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
        ).click()
        assert d.current_url == "https://www.saucedemo.com/"
