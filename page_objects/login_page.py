from selenium.webdriver.common.by import By

from lib.element import Element
from lib.page import PageModel


class LoginPage(PageModel):
    username_field = Element((By.ID, 'user-name'))
    password_field = Element((By.ID, 'password'))
    login_button = Element((By.ID, 'login-button'))
    error_container = Element((By.CSS_SELECTOR, '.error-message-container'))

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_container.get_text()
