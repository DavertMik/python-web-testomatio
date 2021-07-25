from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from lib.page_model import PageModel


class ProductsPage(PageModel):
    page_title = (By.CSS_SELECTOR, '.title')
    robot_image = (By.CSS_SELECTOR, '.peek')
    cart_badge = (By.CSS_SELECTOR, '.shopping_cart_badge')
    add_jacket_button = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    remove_jacket_button = (By.ID, 'remove-sauce-labs-fleece-jacket')
    add_bike_light_button = (By.ID, 'add-to-cart-sauce-labs-bike-light')

    def add_item_to_cart(self, add_item_button):
        self.driver.find_element(*add_item_button).click()

    def remove_item_from_cart(self, remove_item_button):
        self.driver.find_element(*remove_item_button).click()

    def get_cart_number_of_items(self):
        try:
            return self.driver.find_element(*self.cart_badge).text
        except NoSuchElementException:
            return '0'
