import allure
from allure_commons.types import Severity

def test_no_labels():
    pass

def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Issue in repo')
    allure.dynamic.story('Unauthorized user cannot create task in the repository')
    allure.dynamic.link('https://github.com', name='Testing')
    pass

@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'eroshenkoam')
@allure.feature('Issue in repo')
@allure.story('Authorized user can create task in the repository')
@allure.link('https://github.com', name='Testing')
def test_decorator_labels():
    pass
