import pytest
from locators.locators import LoginLocators as ll
from pages.login_page_my import LoginPageMy


class TestSample1:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_sample1(self, driver):
        lp = LoginPageMy(driver)
        assert lp.login_title() == ll.title
