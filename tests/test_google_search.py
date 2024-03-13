import pytest


from selenium import webdriver
from selene import browser, be, have


@pytest.fixture(scope='function', autouse=True)
def browser_managment():
    """Фикстура для браузера"""
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://school.qa.guru'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument("--start-maximized")
    driver_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser.config.driver_options = driver_options

def test_search_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
    browser.quit()

def test_search_not_found():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('ds12e12-e0#@#@#$E$#@fdsklskdfdsf').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    browser.quit()
