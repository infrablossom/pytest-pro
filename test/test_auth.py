import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from functions import wait_until_clickable
from functions import wait_for_url_to_be
from data import credentials


@pytest.mark.auth
class TestAuthorizationClass:

    @pytest.mark.smoke
    def test_login_positive(self):
        with Chrome() as browser:
            browser.maximize_window()
            browser.get('https://qastand.valhalla.pw/login')
            wait_until_clickable(browser, (By.NAME, 'email')).send_keys('qa_test@test.ru')
            wait_until_clickable(browser, (By.NAME, 'password')).send_keys('!QAZ2wsx')
            wait_until_clickable(browser, (By.XPATH, '//*[@type="checkbox"]')).click()
            wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()
            wait_for_url_to_be(browser, 'https://qastand.valhalla.pw/profile')
            browser.get_cookie('session')

    @pytest.mark.parametrize('email, password', credentials,
                             ids=['empty email', 'empty password', 'invalid email', 'unregistered email'])
    def test_login_negative(self, email, password):
        with Chrome() as browser:
            browser.maximize_window()
            browser.get('https://qastand.valhalla.pw/login')
            wait_until_clickable(browser, (By.NAME, 'email')).send_keys(email)
            wait_until_clickable(browser, (By.NAME, 'password')).send_keys(password)
            wait_until_clickable(browser, (By.CLASS_NAME, 'button')).click()
            wait_for_url_to_be(browser, 'https://qastand.valhalla.pw/login')
