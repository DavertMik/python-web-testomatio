def test_add_item_to_cart(perform_login, products_page):
    products_page.add_item_to_cart(products_page.add_jacket_button)
    assert products_page.get_cart_number_of_items() == '1'


def test_remove_button_appears_after_adding_item_to_cart(perform_login, products_page):
    products_page.add_item_to_cart(products_page.add_jacket_button)
    assert products_page.is_displayed(products_page.remove_jacket_button)


def test_remove_item_from_cart(perform_login, products_page):
    products_page.add_item_to_cart(products_page.add_jacket_button)
    products_page.add_item_to_cart(products_page.add_bike_light_button)
    assert products_page.get_cart_number_of_items() == '2'
    products_page.remove_item_from_cart(products_page.remove_jacket_button)
    assert products_page.get_cart_number_of_items() == '1'
