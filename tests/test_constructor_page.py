import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import CredentialsLocators
from urls import Urls
from credentials_for_authorization import CredentialForAuthorization


class TestConstructor:

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True) # запускаем тест в двух браузерах по очереди
    def test_redirect_to_constructor_from_personal_page(self, driver): # тест перехода в конструктор из личного кабинет

        driver.get(Urls.home_page) # получаем главную страницу
        driver.find_element(*CredentialsLocators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*CredentialsLocators.EMAIL_AUTHORIZATION).send_keys(CredentialForAuthorization.LOGIN_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.PASS_AUTHORIZATION).send_keys(CredentialForAuthorization.PASS_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.ENTER_AUTHORIZATION).click()
        # заполняем поля пароля и почты заведомо существующими данными и кликаем по кнопке войти
        driver.find_element(*CredentialsLocators.PERSONAL_ACCOUNT).click()
        # открываем личный кабинет
        driver.find_element(*CredentialsLocators.CONSTRUCTOR).click()
        # открываем конструктор
        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.home_page))
        # проверяем что произошел редирект на страницу конструктора и возвращаем true в случае успеха

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True) # запускаем тест в двух браузерах по очереди
    def test_redirect_to_logo_from_personal_page(self, driver): # тест перехода на домашнюю страницу из личного кабинета

        driver.get(Urls.home_page) # получаем главную страницу
        driver.find_element(*CredentialsLocators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*CredentialsLocators.EMAIL_AUTHORIZATION).send_keys(CredentialForAuthorization.LOGIN_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.PASS_AUTHORIZATION).send_keys(CredentialForAuthorization.PASS_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.ENTER_AUTHORIZATION).click()
        # заполняем поля пароля и почты заведомо существующими данными и кликаем по кнопке войти
        driver.find_element(*CredentialsLocators.PERSONAL_ACCOUNT).click()
        # открываем личный кабинет
        driver.find_element(*CredentialsLocators.LOGO).click()
        # открываем домашнюю страницу через кнопку логотипа
        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.home_page))
        # проверяем что произошел редирект на домашнюю страницу и возвращаем true в случае успеха