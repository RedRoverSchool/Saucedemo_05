import pytest

from ..pages.locators import LoginPageLocators
from ..pages.login_page import LoginPage

link = "https://www.saucedemo.com/"


# вариант теста когда мы проверяем наличие окна об ошибке
#
def test_correct_username_wrong_password(d):
    page = LoginPage(d, link)
    page.should_be_login_form()
    page.should_be_login_box()
    page.should_be_login_btn()
    page.signin_standart_user(login="standard_user", password="secret_sauce1")
    d.find_element(*LoginPageLocators.MESSAGE_EPIC_SADFACE).is_displayed()


# вариант теста когда мы проверяем что тест упал потому что неправильный пароль
# и используем маркер xfail для этого
# @pytest.mark.xfail()
# def test_correct_username_wrong_password(d):
#     page = LoginPage(d,link)
#     page.should_be_login_form()
#     page.should_be_login_box()
#     page.should_be_login_btn()
#     page.signin_standart_user(login="standard_user", password="secret_sauce1")
