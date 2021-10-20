import pytest
from constants import *


@pytest.fixture(autouse=True)
def login(browser):
    browser.get(Links.login)
    browser.add_cookie(SESSION_COOKIE)
    browser.maximize_window()
