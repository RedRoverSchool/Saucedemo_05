from typing import List

from pages.base_page.base_page import BasePage
from pages.login_page.login_page import LoginPage
from pages.inventory_page.inventory_page import InventoryPage
from pages.inventory_page.inventory_page_locators import InventoryPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class CartPage(InventoryPage, LoginPage, BasePage):
