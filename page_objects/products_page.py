from selenium.webdriver.common.by import By

from lib.element import Element
from lib.page import PageModel


class ProductsPage(PageModel):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.page_title = Element(self.driver, (By.CSS_SELECTOR, '.title'))
        self.robot_image = Element(self.driver, (By.CSS_SELECTOR, '.peek'))
        self.cart_badge = Element(self.driver, (By.CSS_SELECTOR, '.shopping_cart_badge'))
        self.add_jacket_button = Element(self.driver, (By.ID, 'add-to-cart-sauce-labs-fleece-jacket'))
        self.remove_jacket_button = Element(self.driver, (By.ID, 'remove-sauce-labs-fleece-jacket'))
        self.add_bike_light_button = Element(self.driver, (By.ID, 'add-to-cart-sauce-labs-bike-light'))

    def get_cart_number_of_items(self):
        return self.cart_badge.get_text()

    def add_jacket_to_cart(self):
        self.add_jacket_button.click()

    def add_bike_light_to_cart(self):
        self.add_bike_light_button.click()

    def remove_jacket_from_cart(self):
        self.remove_jacket_button.click()
