from pages.base_page import BasePage
from selenium.webdriver.common.by import By

login_page_link = 'https://stockstrader.roboforex.com/trading'

balance_replenishment_label = (By.XPATH, '//ion-label[@translate="accounts.operations.deposit"]')

class TradingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def balance_replenishment_label(self):
        self.wait_until_clickable(balance_replenishment_label)
        return self.find_element(balance_replenishment_label)