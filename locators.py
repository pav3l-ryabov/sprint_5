from selenium.webdriver.common.by import By


class CredentialsLocators: # класс с локаторами

    NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']") # поле ввода Имя на странице регистрации
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']") # поле ввода "Email" на странице регистрации
    PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input[@name='Пароль']") # поле ввода "Пароль" на странице регистрации
    REGISTRATION = (By.XPATH, "//button[text()='Зарегистрироваться']") # кнопка "Зарегистрироваться" на странице регистрации
    INVALID_PASS = (By.XPATH, "//p[text()='Некорректный пароль']") # Всплывающая подсказка "Некорректный пароль" на странице регистрации
    ENTER = (By.XPATH, "//a[text()='Войти']") # Кнопка "Войти" на странице регистрации

    LOGIN_TO_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт" на главной странице
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']") # Кнопка "Личный кабинет" на главной странице

    EMAIL_AUTHORIZATION = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']") # поле ввода "Email" на странице авторизации
    PASS_AUTHORIZATION = (By.XPATH, "//label[text()='Пароль']/following-sibling::input[@name='Пароль']") # поле ввода "Пароль" на странице авторизации
    ENTER_AUTHORIZATION = (By.XPATH, "//button[text()='Войти']") # кнопка "Войти" на странице авторизации

    ENTER_FORGOT_PASS = (By.XPATH, "//a[text()='Войти']") # кнопка "Войти" на странице восстановления пароля

    CONSTRUCTOR = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/']") # кнопка "Конструктор"

    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") # кнопка логотипа

    SIGN_OUT = (By.XPATH, "//button[contains(text(), 'Выход')]") # кнопка "выйти" на странице личного кабинета

    # локаторы для таба "Булки"
    TAB_BULKI = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]")
    TAB_BULKI_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current') and .//span[text()='Булки']]")

    # локаторы для таба "Соусы"
    TAB_SOUSY = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]")
    TAB_SOUSY_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current') and .//span[text()='Соусы']]")

    # локаторы для таба "Начинки"
    TAB_NACHINKI = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]")
    TAB_NACHINKI_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current') and .//span[text()='Начинки']]")