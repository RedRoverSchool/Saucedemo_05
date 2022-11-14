from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page.base_page import BasePage
from conf.website_config import WebSiteConfig
from selenium.webdriver.chrome.webdriver import WebDriver


class CartPage(BasePage):
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = WebSiteConfig.CART_PAGE_URL
        super().__init__(browser=self.browser, url=self.url)
