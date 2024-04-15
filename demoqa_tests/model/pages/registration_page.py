import os
import tests

from selene import browser, have, command


class RegistrationPage:
    def __init__(self):
        self.state = browser.element('#state')

    def open(self):
        browser.open('/automation-practice-form')

    def should_open_page_with_title(self, name):
        browser.should(have.title(name))

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def choose_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_phone_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def fill_subjects(self, *args):
        for sub in args:
            browser.element('#subjectsInput').type(sub).press_enter()

    def choose_hobbies(self, *args):
        for hob in args:
            browser.all('.custom-checkbox').element_by(have.exact_text(hob)).click()

    def fill_photo(self, file):
        browser.element('#uploadPicture').set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), f'resources/{file}')
            )
        )

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, value):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()

    def submit(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_open_form_with_text(self, value):
        browser.element('.modal-title').should(have.text(value))

    def should_registered_user_with(self, full_name, email, gender, phone_number, birthday, subjects, hobbies, photo,
                                    address, city):
        browser.element('.table').all('td').even.should(have.exact_texts(
            full_name,
            email,
            gender,
            phone_number,
            birthday,
            subjects,
            hobbies,
            photo,
            address,
            city
        )
        )