from pytest import fixture
from selenium.webdriver import Chrome

from config.base_config import BaseConfig
from page_objects.login_page import LoginPage
from page_objects.menu_page import MenuPage
from page_objects.products_page import ProductsPage


@fixture(scope='session')
def driver():
    driver = Chrome(BaseConfig.CHROME_EXECUTABLE_PATH)
    yield driver
    driver.quit()


@fixture(scope='session')
def login_page(driver):
    return LoginPage(driver, BaseConfig.BASE_URL)


@fixture(scope='session')
def products_page(driver):
    return ProductsPage(driver, BaseConfig.BASE_URL)


@fixture(scope='session')
def menu_page(driver):
    return MenuPage(driver, BaseConfig.BASE_URL)


@fixture(scope='class')
def perform_login(login_page):
    login_page.open()
    login_page.login(BaseConfig.USERNAME, BaseConfig.PASSWORD)


@fixture
def reset_app_state(menu_page):
    menu_page.menu_button.click()
    menu_page.reset_state.click()
    menu_page.driver.refresh()
