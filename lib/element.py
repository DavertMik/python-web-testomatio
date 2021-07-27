from lib.selenium_utils import SeleniumUtils


class Element(SeleniumUtils):
    def __init__(self, locator):
        self.driver = None
        self.locator = locator

    def click(self):
        self.find_element(self.locator).click()

    def send_keys(self, text):
        self.find_element(self.locator).send_keys(text)

    def is_visible(self):
        return bool(self.wait_element_is_visible(self.locator))

    def get_text(self):
        return self.find_element(self.locator).text
