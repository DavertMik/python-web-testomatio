from abc import ABC

from lib.element import Element
from lib.selenium_utils import SeleniumUtils


class PageModel(ABC, SeleniumUtils):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.__set_elements_driver()

    def open(self):
        self.driver.get(self.url)

    def __set_elements_driver(self):
        for attr in dir(self):
            real_attr = getattr(self, attr)
            if isinstance(real_attr, Element):
                real_attr.driver = self.driver
