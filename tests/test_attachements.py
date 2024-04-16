import json
import allure

from allure import attachment_type
from selene import browser


def test_attachments():
    allure.attach("Text", name="Text", attachment_type=attachment_type.TEXT)
    allure.attach("<h1>Hello</h1>", name="Html", attachment_type=attachment_type.HTML)
    allure.attach(
        json.dumps({"first": 1, "second": 2}),
        name="Json",
        attachment_type=attachment_type.JSON,
    )
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name="Screenshot",
        attachment_type=attachment_type.PNG,
    )
