from selenium.webdriver.common.by import By

from lib.element import Element
from lib.page import PageModel


class MenuPage(PageModel):
    menu_button = Element((By.ID, 'react-burger-menu-btn'))
    reset_state = Element((By.ID, 'reset_sidebar_link'))
