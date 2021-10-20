import pytest

from constants import *
from functions import *


@pytest.mark.auth
class TestAuthorizationClass:

    @pytest.mark.smoke
    def test_login_positive(self, browser):
        browser.maximize_window()
        browser.get(Links.login)
        login_ui(browser, **POSITIVE_LOGIN_CREDENTIALS)
        wait_for_url_to_be(browser, Links.profile)
        assert browser.get_cookie('session')

    @pytest.mark.parametrize('email, password', NEGATIVE_LOGIN_CREDENTIALS,
                             ids=['empty email', 'empty password', 'invalid email', 'unregistered email'])
    def test_login_negative(self, browser, email, password):
        browser.maximize_window()
        browser.get(Links.login)
        login_ui(browser, email, password)
        wait_for_url_to_be(browser, Links.login)
