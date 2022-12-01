from ..pages.base_page import BasePage
import pytest
from selenium.webdriver.common.by import By
import time

link_inv = "https://www.saucedemo.com/inventory.html"
link_Cart = "https://www.saucedemo.com/cart.html"


class CartPage(BasePage):
    def backpack_can_be_removed(self):
        self.d.find_element(By.ID, "remove-sauce-labs-backpack").click()

    def cart_is_empty(self):
        assert self.element_is_NOT_present(*CART_ITEM)


CART_ITEM = (By.CLASS_NAME, "cart_item")
CART_BTN = (By.ID, "shopping_cart_container")
BACKPACK_ADD_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")


@pytest.fixture(
    params=["standard_user", "problem_user", "performance_glitch_user"],
    scope="function",
)
def login_from_list(d, request):
    d.get("https://www.saucedemo.com/")
    d.find_element(By.ID, "user-name").send_keys(request.param)
    d.find_element(By.ID, "password").send_keys("secret_sauce")
    d.find_element(By.ID, "login-button").click()


class InventoryPage(BasePage):
    def add_to_cart_backpack_inventory(self):
        # self.d.implicitly_wait(10)
        add_item = self.d.find_element(*BACKPACK_ADD_BTN)
        add_item.click()
        go_to_cart = self.d.find_element(*CART_BTN)
        go_to_cart.click()
        assert "cart" in self.d.current_url
        assert (
            "Sauce Labs Backpack"
            in self.d.find_element(By.ID, "item_4_title_link").text
        )


def test_add_items(d, login_from_list):
    page = InventoryPage(d, link_inv)
    page.add_to_cart_backpack_inventory()


# poetry run pytest tests/test_saucedemo_POM.py::test_add_items -v -n auto
# def test_remove_items_from_cart_on_cart_page(d):
#     page = BasePage(d, link_Main)
#     page.open_page()
#     page = LoginPage(d, link_Main)
#     page.signin_standart_user(login="standard_user", password="secret_sauce")
#     page = InventoryPage(d, link_inv)
#     page.add_to_cart_backpack_inventory()
#     time.sleep(2)
#     page = CartPage(d, link_Cart)
#     page.backpack_can_be_removed()
#     page.cart_is_empty()
@pytest.mark.order(3)
def test_remove_items_from_cart_on_cart_page(d, login_from_list):
    page = InventoryPage(d, link_inv)
    page.add_to_cart_backpack_inventory()
    page = CartPage(d, link_Cart)
    # d.implicitly_wait(2)
    page.backpack_can_be_removed()
    page.cart_is_empty()
