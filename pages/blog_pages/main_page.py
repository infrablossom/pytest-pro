from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# класс для работы с главной страницей блога (/blog)
class MainPage(BasePage):
    POST_TITLE = '//h1[text()="{}"]'
    CREATE_POST_BUTTON = (By.ID, "new")
    SUCCESS_MESSAGE = (By.ID, "alert_div")
    FIRST_POST_TITLE = (By.TAG_NAME, "h1")

    def click_on_post_title(self, title):
        self.wait_until_clickable((By.XPATH, self.POST_TITLE.format(title))).click()

    def click_create_post_button(self):
        self.wait_until_clickable(self.CREATE_POST_BUTTON).click()

    def check_post_created_successfully_message(self):
        assert "Blog posted successfully!" in self.wait_until_visible(
            self.SUCCESS_MESSAGE).text, \
            "Не отобразилось сообщение об успехе"

    def check_post_deleted_successfully_message(self):
        assert 'Your post was successfully deleted' in self.wait_until_visible(
            self.SUCCESS_MESSAGE).text, 'Не отобразилось сообщение об успехе'

    def check_post_exists(self, title):
        assert self.element_is_present((By.XPATH, self.POST_TITLE.format(title))), "Пост не опубликовался"

    def check_post_is_missing(self, title):
        assert not self.element_is_present((By.XPATH, self.POST_TITLE.format(title))), 'Пост не удалился'

    def check_title_edited(self, edited_title):
        assert self.element_is_present((By.XPATH, self.POST_TITLE.format(edited_title))), 'Текст заголовка не ' \
                                                                                                  'поменялся на нужный'

    def check_create_post_button_is_missing(self):
        self.wait_until_not_present(self.CREATE_POST_BUTTON)
