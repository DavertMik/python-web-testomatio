from selenium.webdriver.common.by import By

from lib.element import Element
from lib.page import PageModel


class LoginPage(PageModel):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.username_field = Element(self.driver, (By.ID, 'user-name'))
        self.password_field = Element(self.driver, (By.ID, 'password'))
        self.login_button = Element(self.driver, (By.ID, 'login-button'))
        self.error_container = Element(self.driver, (By.CSS_SELECTOR, '.error-message-container'))

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_container.get_text()
