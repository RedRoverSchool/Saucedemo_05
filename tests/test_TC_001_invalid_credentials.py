import pytest
from ..pages.login_page import *

link_Main = "https://www.saucedemo.com/"


@pytest.mark.parametrize(
    "username,password",
    [
        ("", ""),
        ("standartUser", "secret_sauce"),
        ("standard_user", "secretsauce"),
        ("standard_user", ""),
        ("", "secret_sauce"),
        ("locked_out_user", "secret_sauce"),
    ],
)
@pytest.mark.elina_abramova
def test_negativ_signin(d, username, password):
    page = LoginPage(d, link_Main)
    page.should_be_login_form()
    page.signin_4_username(username, password)
    assert d.find_element(By.XPATH, "//*[contains(text(), 'Epic sadface')]")
