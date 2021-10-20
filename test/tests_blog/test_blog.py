from constants import Links
from functions import *


class TestBlog:
    def test_open_post(self, browser):
        browser.get(Links.author_page)
        post_heading = wait_until_clickable(browser, (By.XPATH, '//*[@href="/blog/page/1/test-post/"]'))
        post_heading.click()
        text = wait_until_visible(browser, (By.XPATH, '//p[2]')).text
        assert text == 'Hello world!', f'Текст не совпадает с заданным, неверный текст: {text}'
