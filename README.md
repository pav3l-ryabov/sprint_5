Проект Sprint_5

Установите зависимости:
pip install pytest selenium
Запустите тесты:
pytest

conftest.py – фикстуры для настройки WebDriver

test_registration.py - проверки регистрации

test_authorization.py - проверки входа

test_personal_account.py - переход в личный кабинет

test_constructor_page.py - переход в конструктор и редирект после клика по лого

test_sign_out.py - выход из аккаунта

test_tabs.py - тесты перехода между разделами в конструкторе

locators.py – локаторы для элементов страницы

urls.py – URL-адреса страниц

generator_credentials.py – генерация тестовых данных

credentials_for_authorization.py – данные для авторизации