from pages.login_page import LoginPage
import pytest
from locators.login_locators import LoginLocators as ll


class TestSample:
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.parametrize(
        'username, password',
        [('standard_user', 'secret_sauce'), ('problem_user', 'secret_sauce')],
    )
    def test_sample(self, d, username, password):
        lp = LoginPage(d)
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
    def test_login_invalid(self):
        pass
