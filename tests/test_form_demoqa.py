import allure
import os


from selene import have, be
        

def test_fill_all_fields(setup_browser):
    browser = setup_browser
    with allure.step("Open registrations form"):
        browser.open('https://demoqa.com/automation-practice-form')
    with allure.step("Fill form"):
        browser.element('#firstName').should(be.blank).type('Ivan')
        browser.element('#lastName').should(be.blank).type('Ivanov')
        browser.element('#userEmail').type('ivan.ivanov@gmail.com')
        browser.element('[for="gender-radio-1"]').click()
        browser.element('#userNumber').type('8005553535')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click().element('option[value="1991"]').click()
        browser.element('.react-datepicker__month-select').click().element('option[value="11"]').click()
        browser.element('.react-datepicker__day--026').click()
        browser.element('#subjectsInput').type('Maths').press_enter()
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('#uploadPicture').send_keys(os.path.abspath('tests/image.png'))
        browser.element('#currentAddress').type('Russia')
        browser.element('#react-select-3-input').type('hary').press_enter()
        browser.element('#react-select-4-input').type('karn').press_enter()
        browser.element('#submit').click()
        browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    with allure.step("Check form results"):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
