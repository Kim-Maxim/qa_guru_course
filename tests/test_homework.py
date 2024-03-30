from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    if 6 <= current_time.hour < 22:
        is_dark_theme = False
    else:
        is_dark_theme = True
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    if dark_theme_enabled_by_user is True:
        is_dark_theme = True
    elif dark_theme_enabled_by_user is False:
        is_dark_theme = False
    elif 6 <= current_time.hour < 22 and dark_theme_enabled_by_user is None:
        is_dark_theme = False
    else:
        is_dark_theme = True
    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    for user in users:
        if user['name'] == "Olga":
            suitable_users = user
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []
    for user in users:
        if user['age'] < 20:
            suitable_users.append(user)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def print_name(func_name, **kwargs):
    result_name = func_name.replace('_', ' ').title()
    result_args = ', '.join([f"{key}={value}" for key, value in kwargs.items()])
    res = f'{result_name} [{result_args}]'
    print(res)


def open_browser(browser_name):
    actual_result = f"Open Browser [{browser_name}]"
    assert actual_result == f"Open Browser [Chrome]"
    print_name(open_browser.__name__, browser_name=browser_name)


def go_to_companyname_homepage(page_url):
    actual_result = f"Go To Companyname Homepage [{page_url}]"
    assert actual_result == f"Go To Companyname Homepage [https://companyname.com]"
    print_name(go_to_companyname_homepage.__name__, page_url=page_url)


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = f"Find Registration Button On Login Page [{page_url}, {button_text}]"
    assert actual_result == f"Find Registration Button On Login Page [https://companyname.com/login, Register]"
    print_name(find_registration_button_on_login_page.__name__, page_url=page_url, button_text=button_text)
