import allure

from selene import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_decorator_steps():
    open_main_page()
    search_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue()
    should_see_issue_with_number('#76')

@allure.step('Open browser')
def open_main_page():
    browser.open('https://github.com')

@allure.step('Search repo {repo}')
def search_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repo)
    s('#query-builder-test').submit()

@allure.step('Go to link of repo {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step('Open issue')
def open_issue():
    s('#issues-tab').click()

@allure.step('Check number 76 of issue {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
    