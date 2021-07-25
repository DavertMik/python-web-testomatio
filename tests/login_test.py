def test_login_with_valid_credentials(login_page, products_page):
    login_page.open()
    login_page.login('standard_user', 'secret_sauce')
    assert products_page.is_displayed(products_page.page_title)
    assert products_page.is_displayed(products_page.robot_image)


def test_login_with_invalid_credentials(login_page):
    login_page.open()
    login_page.login('bad_username', 'bad_password')
    assert login_page.get_error_message() == 'Epic sadface: Username and password do not match any user in this service'


def test_login_without_username(login_page):
    login_page.open()
    login_page.login('', 'bad_password')
    assert login_page.get_error_message() == 'Epic sadface: Username is required'


def test_login_without_password(login_page):
    login_page.open()
    login_page.login('bad_username', '')
    assert login_page.get_error_message() == 'Epic sadface: Password is required'
