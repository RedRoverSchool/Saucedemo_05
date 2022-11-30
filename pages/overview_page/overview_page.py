import random
from conf.website_config import WebSiteConfig
from pages.your_info_page.your_info_page import YourInfoPage
from pages.overview_page.overview_page_locators import OverviewPageLocator
from pages.cart_page.cart_page_locators import CartPageLocators
from pages.your_info_page.your_info_page_locators import YourInfoLocators


class OverviewPage(YourInfoPage):
    def go_to_overview_page(self):
        self.open()
        self.login_standard_user()
        inventory_items = self.find_items_cards()
        randon_num = random.randint(1, WebSiteConfig.ITEMS_COUNTER)
        for item in random.sample(inventory_items, randon_num):
            self.click_item_cart_button(item)
        self.click_cart_button()
        self.click_button(CartPageLocators.BTN_CHECKOUT)
        self.send_keys_to_input(YourInfoLocators.INPUT_FIRST_NAME, self.random_word())
        self.send_keys_to_input(YourInfoLocators.INPUT_LAST_NAME, self.random_word())
        self.send_keys_to_input(YourInfoLocators.INPUT_ZIP_CODE, self.random_word())
        self.click_continue()

    def click_cancel(self):
        self.click_button(OverviewPageLocator.BTN_CANCEL)

    def click_finish(self):
        self.click_button(OverviewPageLocator.BTN_FINISH)
