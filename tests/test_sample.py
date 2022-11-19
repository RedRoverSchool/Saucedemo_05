import pytest

from constants import NEGATIVE_LOGIN_CREDENTIALS
from locators.login_locators import LoginLocators as ll
from pages.login_page import LoginPage


class TestSample:
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.parametrize(
        'username, password',
        [('standard_user', 'secret_sauce'), ('problem_user', 'secret_sauce')],
    )
    def test_sample(self, browser, username, password):
        lp = LoginPage(browser)
        assert lp.login_title() == ll.title
        lp.action_login(username, password)
        lp.action_logout()

    '''
    Example of skipped test
    '''

    @pytest.mark.skip(reason="test is skipped because, ")
    def test_login_skip(self):
        pass

    '''
    Example of xfail test
    '''

    @pytest.mark.regression
    @pytest.mark.xfail
    def test_login_invalid(self, browser):
        lp = LoginPage(browser)
        assert lp.login_title() == ll.title
        lp.action_login(NEGATIVE_LOGIN_CREDENTIALS['user'], NEGATIVE_LOGIN_CREDENTIALS['password'])

        pass
