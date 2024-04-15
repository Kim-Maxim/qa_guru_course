from demoqa_tests.model.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import User


def test_fill_and_send():
    test_user = User(
        first_name='Ivan',
        last_name='Ivanov',
        email='ivanivanov@gmail.com',
        gender='Male',
        phone_number='8005553535',
        month='April',
        year='1997',
        day='15',
        subjects='Maths, Physics',
        hobbies='Sports, Reading',
        photo='file.png',
        address='14, Ashoka Rd, Sansad Marg Area',
        state='NCR',
        city='Delhi'
    )

    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register_user(test_user)
    registration_page.should_registered_user_with(test_user)
    