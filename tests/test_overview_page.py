import allure
from pages.overview_page.overview_page import OverviewPage
from pages.overview_page.overview_page_locators import OverviewPageLocator
from pages.inventory_page.inventory_page_locators import InventoryPageLocators
from conf.website_config import WebSiteConfig


class TestOverviewPage:
    @allure.epic("Checkout: Overview")
    @allure.story("TC_005_ Checkout: Overview  URL & header")
    def test_checkout_layout_url_header(self, browser):
        page = OverviewPage(browser)
        page.go_to_overview_page()
        assert browser.current_url == WebSiteConfig.OVERVIEW_URL
        assert page.element_is_present(InventoryPageLocators.BTN_BURGER_MENU)
        assert page.element_is_present(InventoryPageLocators.LOGIN_LOGO)
        assert page.element_is_present(InventoryPageLocators.CART_LINK)

    def test_checkout_layout(self, browser):
        page = OverviewPage(browser)
        page.go_to_overview_page()
        assert page.get_element_text(OverviewPageLocator.TITLE) == "CHECKOUT: OVERVIEW"
        assert page.get_element_text(OverviewPageLocator.QTY) == "QTY"
        assert page.get_element_text(OverviewPageLocator.DESCR) == "DESCRIPTION"
