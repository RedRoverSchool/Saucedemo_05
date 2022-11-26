from pages.inventory_page.inventory_page_locators import InventoryPageLocators
from pages.cart_page.cart_page_locators import CartPageLocators
from pages.your_info_page.your_info_page_locators import YourInfoLocators
from conf.website_config import WebSiteConfig
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.cart_page.cart_page import CartPage


class YourInfoPage(CartPage):
    def click_cancel(self):
        self.click_button(YourInfoLocators.BTN_CANCEL)

    def click_continue(self):
        self.click_button(YourInfoLocators.BTN_CONTINUE)
