from selenium.common.exceptions import NoSuchElementException
from .locators import *


class BasePage:
    def __init__(self, d, link):
        self.d = d
        self.link = link

    def open_page(self):
        self.d.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.d.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def should_be_autorized_user(self):
        assert self.element_is_present(*InventoryPageLocators.CART_BTN)

    def element_is_NOT_present(self, method, locator):
        try:
            self.d.find_element(method, locator)
        except NoSuchElementException:
            return True
        return False

    def all_widgets_on_page(self):
        self.widgets = [
            (Widgets.FB_WIDGET_ALL_PAGES, "https://www.facebook.com/", "saucelabs"),
            (Widgets.TWITTER_WIDGET_ALL_PAGES, "https://twitter.com/", "saucelabs"),
            (
                Widgets.LINKEDIN_WIDGET_ALL_PAGES,
                "https://www.linkedin.com/",
                "sauce-labs",
            ),
        ]
        n = 1
        for loc, urls, urle in self.widgets:
            self.d.find_element(*loc).click()
            handles = self.d.window_handles
            self.d.switch_to.window(handles[n])
            assert (
                urls in self.d.current_url and urle in self.d.current_url
            ), "you are NOT on correct widget page"
            self.d.switch_to.window(handles[0])
            n += 1
