from typing import List
from pages.inventory_page.inventory_page_locators import InventoryPageLocators
from selenium.webdriver.remote.webelement import WebElement
from conf.website_config import WebSiteConfig
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page.login_page import LoginPage
import logging


class InventoryPage(LoginPage):
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = WebSiteConfig.INVENTORY_PAGE_URL
        super().__init__(browser=self.browser)

    def navigate_to_inventory_page(self):
        self.navigate_to(url=WebSiteConfig.INVENTORY_PAGE_URL)

    def open_burger_menu(self):
        self.click_button(InventoryPageLocators.BTN_BURGER_MENU)

    def close_burger_menu(self):
        self.click_button(InventoryPageLocators.BTN_BURGER_MENU_CLOSE)

    def click_side_menu_item(self, locator):
        self.open_burger_menu()
        self.click_button(locator)

    def click_logout_from_burger_menu(self):
        self.click_button(InventoryPageLocators.BURGER_MENU_LOGOUT)

    def do_logout(self):
        self.click_button(InventoryPageLocators.BTN_BURGER_MENU)
        self.click_logout_from_burger_menu()

    def reset_page_state(self):
        self.open_burger_menu()
        self.click_button(InventoryPageLocators.BURGER_MENU_RESET)
        self.close_burger_menu()
        self.refresh_page()

    def find_items_cards(self) -> List[WebElement]:
        return self.elements_are_present(InventoryPageLocators.ITEMS_CARDS)

    def extract_item_name(self, element: WebElement) -> str:
        return element.find_element(*InventoryPageLocators.ITEM_NAME).text

    def extract_items_names(self, we_list: List[WebElement]) -> List:
        names = []
        for item in we_list:
            names.append(self.extract_item_name(item))
        return names

    def extract_item_desc(self, element: WebElement) -> str:
        return element.find_element(*InventoryPageLocators.ITEM_DESC).text

    def extract_items_descs(self, we_list: List[WebElement]) -> List:
        descs = []
        for item in we_list:
            descs.append(self.extract_item_desc(item))
        return descs

    def extract_item_price(self, element: WebElement) -> str:
        return element.find_element(*InventoryPageLocators.ITEM_PRICE).text

    def extract_items_prices(self, we_list: List[WebElement]) -> List:
        prices = []
        for item in we_list:
            prices.append(float(self.extract_item_price(item).strip("$")))
        return prices

    def extract_item_img_link(self, element: WebElement) -> str:
        return element.find_element(
            *InventoryPageLocators.ITEM_IMAGE
        ).get_property("src")

    def extract_items_links(self, we_list: List[WebElement]) -> List:
        links = []
        for item in we_list:
            links.append(self.extract_item_img_link(item))
        return links

    def set_sorting_order(self, sorting: str):
        self.select_dropdown_option(
            InventoryPageLocators.DROPDOWN_SORTING, sorting
        )

    def click_item_cart_button(self, element: WebElement) -> str:
        element.find_element(*InventoryPageLocators.ITEM_BUTTON).click()
        return element.find_element(*InventoryPageLocators.ITEM_BUTTON).text

    def click_cart_button(self):
        self.click_button(InventoryPageLocators.CART_LINK)

    def get_cart_counter(self) -> int:
        try:
            cart_items_counter = self.element_is_present(
                InventoryPageLocators.CART_BADGE
            )
            return int(cart_items_counter.text)
        except Exception as e:
            logging.error(f"Counter for cart is 0, {e}")
            return 0
