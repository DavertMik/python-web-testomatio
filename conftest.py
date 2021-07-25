from pytest import fixture
from selenium.webdriver import Chrome

from page_objects.login_page import LoginPage
from page_objects.products_page import ProductsPage


@fixture(scope='session')
def driver():
    driver = Chrome('./drivers/chromedriver.exe')
    yield driver
    driver.quit()


@fixture(scope='session')
def login_page(driver):
    return LoginPage(driver, 'https://www.saucedemo.com/')


@fixture(scope='session')
def products_page(driver):
    return ProductsPage(driver, 'https://www.saucedemo.com/inventory.html')


@fixture(scope='function')
def perform_login(login_page):
    login_page.open()
    login_page.login('standard_user', 'secret_sauce')
