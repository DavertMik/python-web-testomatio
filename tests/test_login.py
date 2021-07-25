class TestLogin:
    def test_login_with_valid_credentials(self, login_page, products_page):
        login_page.open()
        login_page.login('standard_user', 'secret_sauce')
        assert products_page.page_title.is_visible()
        assert products_page.robot_image.is_visible()

    def test_login_with_invalid_credentials(self, login_page):
        login_page.open()
        login_page.login('bad_username', 'bad_password')
        expected_error = 'Epic sadface: Username and password do not match any user in this service'
        assert login_page.error_container.get_text() == expected_error

    def test_login_without_username(self, login_page):
        login_page.open()
        login_page.login('', 'bad_password')
        expected_error = 'Epic sadface: Username is required'
        assert login_page.error_container.get_text() == expected_error

    def test_login_without_password(self, login_page):
        login_page.open()
        login_page.login('bad_username', '')
        expected_error = 'Epic sadface: Password is required'
        assert login_page.error_container.get_text() == expected_error
