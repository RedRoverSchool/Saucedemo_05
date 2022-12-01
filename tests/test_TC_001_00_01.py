import pytest
from ..pages.login_page import *

# from .pages.cart_page import *

link_Main = "https://www.saucedemo.com/"


@pytest.mark.elina_abramova
def test_standart_user_can_signin(d):
    assert d.title == "Swag Labs"
    page = LoginPage(d, link_Main)
    page.should_be_login_form()
    page.signin_standart_user(login="standard_user", password="secret_sauce")
    page.should_go_on_product_page()
