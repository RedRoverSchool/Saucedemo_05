from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page.base_page import BasePage
from pages.inventory_page.inventory_page_locators import InventoryPageLocators
from conf.website_config import WebSiteConfig
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.cart_page.cart_page_locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = WebSiteConfig.CART_PAGE_URL
        super().__init__(browser=self.browser, url=self.url)

    def navigate_to_cart_page(self):
        self.navigate_to(url=WebSiteConfig.CART_PAGE_URL)

    def click_continue_shopping(self):
        self.click_button(CartPageLocators.BTN_CONTINUE_SHOPPING)

    def click_checkout(self):
        self.click_button(CartPageLocators.BTN_CHECKOUT)

    def get_cart_counter(self) -> int:
        try:
            cart_items_counter = self.element_is_present(
                InventoryPageLocators.CART_BADGE
            )
            return int(cart_items_counter.text)
        except:
            return 0

    def find_items_cart_cards(self) -> List[WebElement]:
        return self.elements_are_present(CartPageLocators.ITEM_CARD)

    def click_item_remove(self, element: WebElement) -> None:
        element.find_element(By.CSS_SELECTOR, CartPageLocators.ITEM_BTN).click()
