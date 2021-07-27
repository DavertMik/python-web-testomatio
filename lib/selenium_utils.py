from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from config.base_config import BaseConfig


class SeleniumUtils:
    def find_element(self, locator, timeout=BaseConfig.DEFAULT_TIMEOUT):
        self.wait_element_is_visible(locator, timeout)
        return self.driver.find_element(*locator)

    def find_elements(self, locator, timeout=BaseConfig.DEFAULT_TIMEOUT):
        self.wait_element_is_visible(locator, timeout)
        return self.driver.find_elements(*locator)

    def wait_element_is_visible(self, locator, timeout=BaseConfig.DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def wait_element_is_not_visible(self, locator, timeout=BaseConfig.DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element(locator))

    def wait_element_has_text(self, locator, text, timeout=BaseConfig.DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(ec.text_to_be_present_in_element(locator, text))
