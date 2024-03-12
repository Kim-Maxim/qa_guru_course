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


def test_valid_login():
    """Проверка успешной авторизации"""
    browser.open('/')
    browser.element('[name="email"]').should(be.blank).type('qagurubot@gmail.com')
    browser.element('[name="password"]').should(be.blank).type('somepasshere').press_enter()
    browser.element('[class="page-header"]').should(have.text('Список тренингов'))
    browser.open('/cms/system/login')
    browser.element('.logined-form').should(have.text('Здравствуйте, QA_GURU_BOT'))
    browser.quit()


def test_invalid_login_with_wrong_password():
    """Проверка неуспешной авторизации"""
    browser.open('/')
    browser.element('[name="email"]').should(be.blank).type('qagurubot@gmail.com')
    browser.element('[name="password"]').should(be.blank).type('somepassher').press_enter()
    browser.element('.btn-success').should(have.text('Неверный пароль'))
    browser.quit()
    