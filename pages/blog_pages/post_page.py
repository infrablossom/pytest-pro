from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# класс для работы со страницей отображения поста (пример URL — /blog/page/1/test-post/ или /blog/page/1)
class PostPage(BasePage):
    POST_TEXT = (By.CSS_SELECTOR, ".container p+p")
    EDIT_BUTTON = (By.ID, 'edit')
    DELETE_BUTTON = (By.ID, 'delete')
    CONFIRM_DELETE_BUTTON = (By.ID, 'confirmedDelete')

    def check_post_text(self, text):
        post_text = self.wait_until_visible(self.POST_TEXT)
        assert post_text.text == text, "Неверный текст"

    def click_edit_post_button(self):
        self.wait_until_clickable(self.EDIT_BUTTON).click()

    def click_delete_post_button(self):
        self.wait_until_clickable(self.DELETE_BUTTON).click()

    def press_confirm_to_delete(self):
        self.wait_until_clickable(self.CONFIRM_DELETE_BUTTON).click()
