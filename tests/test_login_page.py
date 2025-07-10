from pytest_bdd import given, when, then, parsers, scenarios

from pages.login_page import LoginPage
from pages.trading_page import TradingPage

scenarios('../features/login_page.feature')

@given('the user navigates to the login page')
def navigate_to_login(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.click_accept_cookies()

@when(parsers.parse('the user logs in with email "{email}" and password "{password}"'))
def login_user(browser, email, password):
    login_page = LoginPage(browser)
    login_page.find_input_email()
    login_page.input_email(email)
    login_page.input_password(password)
    login_page.click_submit_button()

@then('the login should be successful')
def verify_login(browser):
    trading_page = TradingPage(browser)
    assert trading_page.balance_replenishment_label().is_displayed()