from typing import Tuple

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from conf import URL


class BasePage:
    CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')

    def __init__(self, driver):
        self.driver = driver
        self.url = URL

    def open_page(self):
        self.driver.get(self)

    def wait_for_url_to_be(self, url: str, timeout: int = 5) -> bool:
        return WebDriverWait(self.driver, timeout).until(ec.url_to_be(url))

    def page_title_is(self, title: str, timeout: int = 5) -> bool:
        return WebDriverWait(self.driver, timeout).until(ec.title_is(title))

    def wait_until_clickable(self, locator: Tuple, timeout: int = 5) -> WebElement:
        return WebDriverWait(self.driver,  timeout).until(
            ec.element_to_be_clickable(locator)
        )

    def wait_until_present(self, locator: Tuple, timeout: int = 5) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(locator)
        )

    def wait_until_not_present(self, locator: Tuple, timeout=5) -> WebElement:
        return WebDriverWait(self.driver, timeout).until_not(
            ec.presence_of_element_located(locator)
        )

    def wait_until_visible(self, locator: Tuple, timeout: int = 5) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator)
        )

    def element_is_present(self, locator: Tuple, timeout: int = 5) -> bool:
        try:
            self.wait_until_visible(locator, timeout)
            return True
        except TimeoutException:
            return False


    def page_is_open(self, url):
        try:
            self.wait_for_url_to_be(url)
            return True
        except TimeoutException:
            return False

    def elements_are_present(self, locator, timeout: int = 5):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    def go_to_cart(self, locator):
        self.wait_until_clickable(self.CART_BUTTON).click()
