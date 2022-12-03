import allure
from pages.overview_page.overview_page import OverviewPage
from pages.overview_page.overview_page_locators import OverviewPageLocator
from pages.inventory_page.inventory_page_locators import InventoryPageLocators
from conf.website_config import WebSiteConfig
import math


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

    @allure.epic("Checkout: Overview")
    @allure.story("TC_005_ Checkout: Overview  layout")
    def test_checkout_layout(self, browser):
        page = OverviewPage(browser)
        page.go_to_overview_page()
        assert page.get_element_text(OverviewPageLocator.TITLE) == "CHECKOUT: OVERVIEW"
        assert page.get_element_text(OverviewPageLocator.QTY) == "QTY"
        assert page.get_element_text(OverviewPageLocator.DESCR) == "DESCRIPTION"
        assert (
            page.get_element_text(OverviewPageLocator.PAY_INFO)
            == "Payment Information:"
        )
        assert (
            page.get_element_text(OverviewPageLocator.SAUCE_CARD) == "SauceCard #31337"
        )
        assert (
            page.get_element_text(OverviewPageLocator.SHIPPING_INFO)
            == "Shipping Information:"
        )

        assert page.get_element_text(OverviewPageLocator.ITEM_TOTAL).startswith(
            "Item total: $"
        )
        assert page.get_element_text(OverviewPageLocator.TAX).startswith("Tax: $")
        assert page.get_element_text(OverviewPageLocator.TOTAL).startswith("Total: $")

        assert page.get_element_text(OverviewPageLocator.BTN_CANCEL) == "CANCEL"
        assert page.get_element_text(OverviewPageLocator.BTN_FINISH) == "FINISH"

    @allure.epic("Checkout: Overview")
    @allure.story("TC_005_ Checkout: Overview  Sum Total For One Item In Cart")
    def test_checkout_item_total_for_one_item_in_cart(self, browser):
        page = OverviewPage(browser)
        page.go_to_overview_page_one_item()
        assert page.get_price_num(OverviewPageLocator.ITEM_PRICE) == page.get_price_num(
            OverviewPageLocator.ITEM_TOTAL
        )
        assert page.get_price_num(OverviewPageLocator.ITEM_TOTAL), page.get_price_num(
            OverviewPageLocator.TAX
        ) == page.get_price_num(OverviewPageLocator.TOTAL)
