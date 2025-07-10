from selenium import webdriver
import pytest

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.maximize_window()
    chrome_browser.implicitly_wait(5)
    yield chrome_browser
    chrome_browser.close()
    chrome_browser.quit()