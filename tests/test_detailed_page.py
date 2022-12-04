import allure
from pages.detailed_page.detailed_page import DetailedPage
from pages.detailed_page.detailed_page_locator import DetailedPageLocators


class TestDetailedPage:
    def open_page(self, browser):
        page = DetailedPage(browser)
        page.open()
        page.login_standard_user()
        return page

    @allure.epic("Detailed Page Test")
    @allure.story("TC_003.00.01 | Detailed item description")
    def test_add_to_cart(self, browser):
        page = self.open_page(browser)
        page.open_first_item()
        page.click_add_to_cart()

        assert (
            page.element_is_not_visible(
                DetailedPageLocators.ADD_TO_CART_BUTTON
            ),
            "there is add button",
        )

        assert (
            page.element_is_visible(DetailedPageLocators.REMOVE_BUTTON),
            "there is no remove button",
        )
