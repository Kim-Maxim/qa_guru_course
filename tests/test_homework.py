from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_fill_and_send():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.should_open_page_with_title('DEMOQA')
    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Ivanov')
    registration_page.fill_email('ivanivanov@gmail.com')
    registration_page.choose_gender('Male')
    registration_page.fill_phone_number('8005553535')
    registration_page.fill_birthday('1997', 'April', '15')
    registration_page.fill_subjects('Maths', 'Physics')
    registration_page.choose_hobbies('Sports', 'Reading')
    registration_page.fill_photo('file.png')
    registration_page.fill_address('14, Ashoka Rd, Sansad Marg Area')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')
    registration_page.submit()
    registration_page.should_open_form_with_text('Thanks for submitting the form')
    registration_page.should_registered_user_with(
        'Ivan Ivanov',
        'ivanivanov@gmail.com',
        'Male',
        '8005553535',
        '15 April,1997',
        'Maths, Physics',
        'Sports, Reading',
        'file.png',
        '14, Ashoka Rd, Sansad Marg Area',
        'NCR Delhi'
    )
