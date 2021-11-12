import pytest
from selenium.webdriver.common.by import By

from api.api_helpers import delete_all_posts
from api.blog_api import BlogApi
from constants import Links
from functions import wait_until_visible, wait_until_clickable


@pytest.fixture()
def delete_user_posts(url):
    yield
    delete_all_posts(url)


@pytest.fixture()
def create_new_post(url, faker):
    api = BlogApi(url)
    title = faker.text(7)
    text = faker.text(50)
    api.create_post(title=title, text=text, tags=[faker.text(5)])
    return title, text


@pytest.mark.usefixtures('delete_user_posts')
class TestBlogOpen:
    def test_open_post(self, browser, url, create_new_post):
        title, text = create_new_post
        browser.get(url + Links.blog)
        wait_until_clickable(browser, (By.XPATH, f'//h1[text()="{title}"]')).click()
        post_text = wait_until_visible(browser, (By.CSS_SELECTOR, '.container p+p'))

        assert post_text.text == text


@pytest.mark.usefixtures('delete_user_posts')
class TestsBlogModify:
    def test_create_post(self, browser, url, faker):
        browser.get(url + Links.blog)
        wait_until_clickable(browser, (By.ID, 'new')).click()
        title = faker.text(10)
        text = faker.text(100)
        wait_until_clickable(browser, (By.ID, 'title')).send_keys(title)
        wait_until_clickable(browser, (By.ID, 'text')).send_keys(text)
        wait_until_clickable(browser, (By.ID, 'tags')).send_keys(faker.text(5))
        wait_until_clickable(browser, (By.ID, 'submit')).click()

        assert 'Blog posted successfully!' in wait_until_visible(browser, (
            By.ID, 'alert_div')).text, 'Не отобразилось сообщение об успехе'
        assert wait_until_visible(browser, (By.TAG_NAME, 'h1')).text == title, 'Пост не опубликовался'

