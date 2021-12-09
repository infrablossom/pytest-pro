from selenium.webdriver import Chrome, Opera, Safari, Remote


NEGATIVE_LOGIN_CREDENTIALS = [
    ("", "!QAZ2wsx"),
    ("qa_test@test.ru", ""),
    ("qa_test", "!QAZ2wsx"),
    ("test@test.ru", "1QAZ2wsx")
]

POSITIVE_LOGIN_CREDENTIALS = {"email": "api_user_13@test.ru",
                              "password": "q13w13e13"}

BROWSERS = {"opera": Opera,
            "chrome": Chrome,
            "safari": Safari}

VALID_BROWSERS = {
   "chrome": Chrome,
   "opera": Opera,
   "remote": Remote
}

BROWSER_REMOTE_CAPABILITIES = {
      "browserName": "chrome",
      "version": "95.0",
      "enableVNC": True,
  }

COMMAND_EXECUTOR = 'http://localhost:4444/wd/hub'


class Links:
    base_url = {'prod': 'https://qastand.valhalla.pw/',
                'stage': 'https://qastand-dev.valhalla.pw/'}
    login = "login"
    profile = "profile"
    blog = "blog"
    author_page = "blog/author/2/"
