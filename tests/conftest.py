import pytest

from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    browser.config.driver_options = options
    yield
    browser.quit()
    