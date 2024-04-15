Провести рефакторинг своего теста на регистрацию студента по форме https://demoqa.com/automation-practice-form, используя инструменты объектно-ориентированной парадигмы для инкапсуляции деталей реализации бизнес-шагов пользователя, таким образом реализовав идеи шаблона PageObject.

Задание состоит из нескольких частей, каждую из которых следует сдавать в виде отдельной ссылки на соответствующую бренчу в репозитории с тестами на приложение demoqa (все ссылки в одном сообщении в комментариях ниже).

ЧАСТЬ I (реализовать в бренче mid-level-step-objects)

В этой части мы рассматриваем как ценный c точки зрения бизнеса шаг пользователя – «заполнение отдельных данных о пользователе» или «подтверждение результата проделанной работы» (как например, подтверждение что регистрация прошла успешно).

Финальный тест должен иметь структуру вида:

registration_page.open() registration_page.fill_first_name('Yasha') registration_page.fill_last_name('Kramarenko') ... registration_page.submit() registration_page.should_have_registered(yasha) ... или использовав идеи шаблона Fluent PageObject: registration_page.open() registration_page
.fill_first_name('Yasha')
.fill_last_name('Kramarenko')
.fill_email('yashaka@gmail.com')
...
.submit() registration_page.should_have_registered('Yasha Kramarenko', 'yashaka@gmail.com', ...) ... или использовав форматирование через круглые скобки вместо \

registration_page.open() (
registration_page .fill_first_name('Yasha') .fill_last_name('Kramarenko') .fill_email('yashaka@gmail.com') ... .submit() ) registration_page.should_have_registered('Yasha Kramarenko', 'yashaka@gmail.com', ...) Другие варианты реализации проверки:

registration_page.should_have_registered( student_name='Yasha Kramarenko', student_email='yashaka@gmail.com', ... ) registration_page.should_have_registered( ('Student Name', 'Yasha Kramarenko'), ('Student Email', 'yashaka@gmail.com'), ... )

Дополнительные условия и подсказки:

Все элементы выносить в отдельные поля объекта класса не обязательно, но стоит это сделать с теми элементами, которые будут повторяться.

Класс для PageObject должен лежать в выделенном модуле в выделенном пакете внутри проекта, как было показано на уроке 😉

ЧАСТЬ II (реализовать в бренче high-level-step-objects)

В этой части мы рассматриваем как ценный c точки зрения бизнеса шаг пользователя – «отправить форму с данными» или другими словами «провести регистрацию через форму». Также шагом считаем подтверждение результата проделанной работы (как например, подтверждение, что регистрация прошла успешно).

Также в этой части следует провести рефакторинг работы с данными пользователя, представив их в виде объекта датакласса, используя уже имеющиеся знания из предыдущих уроков.

Финальный тест должен выглядеть примерно так:

yasha = User(first_name='yasha', last_name='kramarenko', email='yashaka@gmail.com', ...) registration_page.open() registration_page.register(yasha) registration_page.should_have_registered(yasha) Допустимо реализовать шаг вида:

registration_page.fill(yasha).submit() Допустимо предопределить пользователя для тестов в отдельном модуле users.py и в тесте либо использовать напрямую: registration_page.open() registration_page.register(users.student) registration_page.should_have_registered(users.student) ... либо через переменную:

student = users.student registration_page.open() registration_page.register(student) registration_page.should_have_registered(student)

Дополнительные условия и подсказки:

Не обязательно на уровне с высокоуровневыми шагами типа .register(user) добавлять в PageObject средне-уровневые шаги типа .fill_email(user.email), но можно

если их добавлять – это будет сделать не сложно, просто скопировав из предыдущей версии решения из Часть I, – то возможно их стоит сделать "приватными" (добавив перед именем подчеркивание), чтобы не дать возможность в тесте – миксовать подход, а использовать только высокоуровневые шаги, но можно и не вводить такое ограничение.

вероятно, проще вместо добавления таких средне-уровневых шагов из Часть I – добавить в init поля объекта для всех элементов и переиспользовать их внутри реализации .register(user). Таким образом реализация будет более лаконичная и все еще достаточно гибкая, чтобы в будущем иметь доступ к элементам в контексте других "бизнес задач" на этой странице.

Классы для PageObject и модели данных должны лежать в выделенных модулях в выделенных пакетах внутри проекта, как было показано на уроке 😉

При реализации модели данных для реализации тех или иных полей будет неплохо использовать специальные типы данных, например, для даты использовать datetime.date, а для хобби использовать Enum 😉 Если пока не хватает знаний, сделай как можешь, или посмотри разбор этого домашнего задания.

Часть III – ДОПОЛНИТЕЛЬНО/НЕ-ОБЯЗАТЕЛЬНО (реализовать в бренче application-manager)

добавить в проект тест на упрощенную регистрацию через форму https://demoqa.com/text-box и соответствующий PageObject.

Реализовать шаблон ApplicationManager для предсоздания всех объектов для пейдж-обджектов.

в тесте загрузить форму не через simple_registration_form.open(), а через app.left_panel.open_simple_registration_form(), который должен быть шорткатом (методом, вызывающим под капотом другой метод этого же объекта) на app.left_panel.open('Elements', 'Text Box')

cоответственно добавить пейджобджект для LeftPanel и создать его объект в виде поля обьекта апликейшен-менеджера