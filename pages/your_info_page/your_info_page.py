from pages.your_info_page.your_info_page_locators import YourInfoLocators
from pages.cart_page.cart_page import CartPage


class YourInfoPage(CartPage):
    def click_cancel(self):
        self.click_button(YourInfoLocators.BTN_CANCEL)

    def click_continue(self):
        self.click_button(YourInfoLocators.BTN_CONTINUE)

    def get_error_msg_text(self):
        err_container = self.element_is_present(YourInfoLocators.ERR_MSG)
        return err_container.text
