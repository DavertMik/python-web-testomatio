import pytest


@pytest.mark.usefixtures('perform_login', 'reset_app_state')
class TestProducts:
    def test_add_item_to_cart(self, products_page):
        products_page.add_jacket_to_cart()
        assert products_page.get_cart_number_of_items() == '1'

    def test_remove_button_appears_after_adding_item_to_cart(self, products_page):
        products_page.add_jacket_to_cart()
        assert products_page.remove_jacket_button.is_visible()

    def test_remove_item_from_cart(self, products_page):
        products_page.add_jacket_to_cart()
        products_page.add_bike_light_to_cart()
        assert products_page.get_cart_number_of_items() == '2'
        products_page.remove_jacket_from_cart()
        assert products_page.get_cart_number_of_items() == '1'
