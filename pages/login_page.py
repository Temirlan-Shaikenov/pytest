from pages.base_page import BasePage
from selenium.webdriver.common.by import By

login_page_link = 'https://stockstrader.roboforex.com/login'

accept_cookies_button = (By.XPATH, '//ion-button[@translate="cookies.allow"]')

email_input = (By.XPATH, '//ion-input[@type="email"]//input')
password_input = (By.XPATH, '//input[@inputmode="text"]')
submit_button = (By.XPATH, '//ion-button[contains(@class,"button-large")]')

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.open_page(login_page_link)

    def find_input_email(self):
        self.wait_until_presence(email_input)
        self.find_element(email_input)

    def input_email(self, email):
        self.click_element(email_input)
        self.input_text(email_input, email)

    def input_password(self, password):
        self.click_element(password_input)
        self.input_text(password_input, password)

    def click_submit_button(self):
        self.click_element(submit_button)

    def click_accept_cookies(self):
        self.wait_until_presence(accept_cookies_button)
        self.click_element(accept_cookies_button)
