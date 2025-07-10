from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def click_element(self, locator):
        return self.browser.find_element(*locator).click()

    def input_text(self, locator, text):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator)).send_keys(text)

    def open_page(self, link):
        return self.browser.get(link)

    def wait_until_presence(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))

    def wait_until_clickable(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))