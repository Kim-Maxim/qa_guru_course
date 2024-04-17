import pytest

from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    # browser.config.type_by_js = True
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.page_load_strategy = 'eager'
    browser.config.driver_options = chrome_options
    yield
    browser.quit()
