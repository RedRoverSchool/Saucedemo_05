import pytest
from ..pages.login_page import *

link_Main = "https://www.saucedemo.com/"


@pytest.mark.elina_abramova
def test_signin_using_a_list_of_credentials(d, login_from_list):
    assert d.title == "Swag Labs"
    assert "inventory" in d.current_url


# @pytest.mark.parametrize(
#     "username,password",
#     [
#         ("standard_user", "secret_sauce"),
#         ("problem_user", "secret_sauce"),
#         ("performance_glitch_user", "secret_sauce"),
#         pytest.param("locked_out_user", "secret_sauce", marks=pytest.mark.xfail),
#     ],
# )
# @pytest.mark.elina_abramova
# def test_signin_4_username(d, username, password):
#     page = LoginPage(d, link_Main)
#     page.should_be_login_form()
#     page.signin_4_username(username, password)
#     page.should_go_on_product_page()
