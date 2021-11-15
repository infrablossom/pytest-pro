import random

import pytest

from constants import Links, BROWSERS


def pytest_configure(config):
    config.addinivalue_line(
        'markers', 'smoke: tests for smoke testing'
    )
    config.addinivalue_line(
        'markers', 'auth: tests for auth'
    )


@pytest.fixture
def browser(request):
    my_browser = request.config.getoption('--browser')
    browser = BROWSERS[my_browser]()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def url(request):
    """Фикстура для получения заданного из командной строки окружения"""
    env = request.config.getoption('--env')
    url = Links.base_url.get(env)
    if not url:
        raise Exception('Передано неверное окружение')
    return url


def pytest_addoption(parser):
    parser.addoption(
        '--env', default='prod'
    )
    parser.addoption(
        '--browser', default='chrome', choices=["chrome", "opera", "safari"]
    )


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return random.randint(0, 9999)
