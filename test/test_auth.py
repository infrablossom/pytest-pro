import pytest

from constants import *
from pages.auth_page import AuthPage
from pages.blog_pages.main_page import MainPage
from pages.blog_pages.main_page import BasePage


@pytest.mark.auth
class TestAuthorizationClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.auth_page = AuthPage(browser, url + Links.login)
        self.auth_page.open_page()

    @pytest.mark.smoke
    def test_login_positive(self, url):
        self.auth_page.login_ui(**POSITIVE_LOGIN_CREDENTIALS)
        self.auth_page.check_successful_auth(url)

    @pytest.mark.parametrize('email, password', NEGATIVE_LOGIN_CREDENTIALS,
                             ids=['empty email', 'empty password', 'invalid email', 'unregistered email'])
    def test_login_negative(self, url, email, password):
        self.auth_page.login_ui(email, password)
        self.auth_page.check_unsuccessful_auth(url)


@pytest.mark.usefixtures('login')
class TestLogoutClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.blog_page = MainPage(browser, url + Links.blog)
        self.base_page = BasePage(browser, url + Links.login)

    def test_logout(self):
        self.blog_page.open_page()
        self.base_page.logout()
        self.blog_page.open_page()
        self.blog_page.check_create_post_button_is_missing()
