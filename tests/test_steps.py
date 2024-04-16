import allure

from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


allure.dynamic.tag("web")
allure.dynamic.severity(Severity.CRITICAL)
allure.dynamic.feature("Checking issue")
allure.dynamic.story("Checking issue in repo")
allure.dynamic.link("https://github.com", name="eroshenkoam")
def test_steps_issue():
    with allure.step("Open browser"):
        browser.open("https://github.com")

    with allure.step("Search repo"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Go to link of repo"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Open issue"):
        s("#issues-tab").click()

    with allure.step("Check number 76 of issue"):
        s(by.partial_text("#76")).should(be.visible)
