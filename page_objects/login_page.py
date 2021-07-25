from selenium.webdriver.common.by import By

from lib.page_model import PageModel


class LoginPage(PageModel):
    username_field = (By.ID, 'user-name')
    password_field = (By.ID, 'password')
    login_button = (By.ID, 'login-button')
    error_container = (By.CSS_SELECTOR, '.error-message-container')

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_container).text
