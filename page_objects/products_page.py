from selenium.webdriver.common.by import By

from lib.element import Element
from lib.page import PageModel


class ProductsPage(PageModel):
    page_title = Element((By.CSS_SELECTOR, '.title'))
    robot_image = Element((By.CSS_SELECTOR, '.peek'))
    cart_badge = Element((By.CSS_SELECTOR, '.shopping_cart_badge'))
    add_jacket_button = Element((By.ID, 'add-to-cart-sauce-labs-fleece-jacket'))
    remove_jacket_button = Element((By.ID, 'remove-sauce-labs-fleece-jacket'))
    add_bike_light_button = Element((By.ID, 'add-to-cart-sauce-labs-bike-light'))

    def get_cart_number_of_items(self):
        return self.cart_badge.get_text()

    def add_jacket_to_cart(self):
        self.add_jacket_button.click()

    def add_bike_light_to_cart(self):
        self.add_bike_light_button.click()

    def remove_jacket_from_cart(self):
        self.remove_jacket_button.click()
