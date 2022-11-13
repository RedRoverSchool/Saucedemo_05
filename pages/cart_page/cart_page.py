from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base_page.base_page import BasePage
from pages.login_page.login_page import LoginPage
from pages.inventory_page.inventory_page import InventoryPage
from pages.inventory_page.inventory_page_locators import InventoryPageLocators
from pages.cart_page.cart_page_locators import CartPageLocators


class CartPage(InventoryPage, LoginPage, BasePage):
    pass
