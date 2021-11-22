from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from constants import Links


# класс для работы со страницей авторизации (/login)
class AuthPage(BasePage):
    EMAIL_FIELD = (By.NAME, 'email')
    PASS_FIELD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'button')

    def login_ui(self, email, password):
        """Функция логина на стенде через UI"""
        self.wait_until_clickable(self.EMAIL_FIELD).send_keys(email)
        self.wait_until_clickable(self.PASS_FIELD).send_keys(password)
        self.wait_until_clickable(self.LOGIN_BUTTON).click()

    def check_successful_auth(self, url):
        self.wait_for_url_to_be(url + Links.profile)
        assert self.browser.get_cookie('session')

    def check_unsuccessful_auth(self, url):
        self.wait_for_url_to_be(url + Links.login)



