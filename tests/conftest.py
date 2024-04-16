import pytest

from selenium import webdriver
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    browser.config.driver_options = chrome_options
    yield
    browser.quit()
