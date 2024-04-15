import os
import tests


from selene import browser, have, command


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def register_user(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.all('[name=gender]').element_by(have.value(user.gender)).element('..').click()
        browser.element('#userNumber').type(user.phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(user.month)
        browser.element('.react-datepicker__year-select').type(user.year)
        browser.element(
            f'.react-datepicker__day--0{user.day}:not(.react-datepicker__day--outside-month)'
        ).click()
        for sub in user.subjects.split(", "):
            browser.element('#subjectsInput').type(sub).press_enter()
        for hob in user.hobbies.split(", "):
            browser.all('.custom-checkbox').element_by(have.exact_text(hob)).click()

        browser.element('#uploadPicture').set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), f'resources/{user.photo}')
            )
        )
        browser.element('#currentAddress').type(user.address)
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(user.state)
        ).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(user.city)
        ).click()
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_registered_user_with(self, user):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.day} {user.month},{user.year}',
            user.subjects,
            user.hobbies,
            user.photo,
            user.address,
            f'{user.state} {user.city}'
        )
        )
