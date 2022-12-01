import time
from .base_page import BasePage
from .locators import *


class CheckoutPage(BasePage):
    def enter_checkout_info(self, firstname, lastname, zip):
        self.d.find_element(*CheckoutPageLocators.FIRS_NAME).send_keys(firstname)
        self.d.find_element(*CheckoutPageLocators.LAST_NAME).send_keys(lastname)
        self.d.find_element(*CheckoutPageLocators.ZIP_P_CODE).send_keys(zip)
        self.d.find_element(*CheckoutPageLocators.CONTINUE).click()
