from selenium.webdriver.common.by import By

from lib.element import Element
from lib.page import PageModel


class MenuPage(PageModel):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.menu_button = Element(self.driver, (By.ID, 'react-burger-menu-btn'))
        self.reset_state = Element(self.driver, (By.ID, 'reset_sidebar_link'))
