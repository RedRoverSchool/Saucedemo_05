from ..pages.locators import link
from ..pages.login_page import LoginPage
import time


def test_login_page_with_empty_password(d):
    page = LoginPage(d, link)
    page.open_page()
    time.sleep(2)
    page.signin_4_username("standard_user", "")
    time.sleep(2)
    page.user_is_not_authorized()
