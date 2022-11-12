from pages.base_page.base_page import BasePage
from pages.login_page.login_page import LoginPage
from pages.detailed_page.detailed_page_locator import DetailedPageLocators


class DetailedPage(LoginPage, BasePage):

    def open_first_item(self):                                  #кликнуть первый элемент в списке
        self.click_button(DetailedPageLocators.ITEM_TITLE)

    def click_add_to_cart(self):                                #кликнуть Add to cart на странице продукта
        self.click_button(DetailedPageLocators.ADD_TO_CART_BUTTON)


