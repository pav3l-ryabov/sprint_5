import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import CredentialsLocators
from urls import Urls
from credentials_for_authorization import CredentialForAuthorization


class TestAuthorization:

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True) # запускаем тест в двух браузерах по очереди
    def test_authorization_login_to_account(self,driver): # авторизация через кнопку "Войти в аккаунт"

        driver.get(Urls.home_page) # получаем главную страницу
        driver.find_element(*CredentialsLocators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*CredentialsLocators.EMAIL_AUTHORIZATION).send_keys(CredentialForAuthorization.LOGIN_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.PASS_AUTHORIZATION).send_keys(CredentialForAuthorization.PASS_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.ENTER_AUTHORIZATION).click()
        # заполняем поля пароля и почты заведомо существующими данными и кликаем по кнопке войти

        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.home_page))
        # проверяем что произошел редирект на главную страницу и возвращаем true в случае успеха

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True) # запускаем тест в двух браузерах по очереди
    def test_authorization_personal_account(self, driver): # авторизация через кнопку "Личный кабинет"

        driver.get(Urls.home_page) # получаем главную страницу
        driver.find_element(*CredentialsLocators.PERSONAL_ACCOUNT).click()
        driver.find_element(*CredentialsLocators.EMAIL_AUTHORIZATION).send_keys(CredentialForAuthorization.LOGIN_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.PASS_AUTHORIZATION).send_keys(CredentialForAuthorization.PASS_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.ENTER_AUTHORIZATION).click()
        # заполняем поля пароля и почты заведомо существующими данными и кликаем по кнопке войти

        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.home_page))
        # проверяем что произошел редирект на главную страницу и возвращаем true в случае успеха

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True) # запускаем тест в двух браузерах по очереди
    def test_authorization_in_register_page(self, driver): # авторизация через кнопку "Войти" на странице авторизации

        driver.get(Urls.reg_page) # получаем страницу регистрации
        driver.find_element(*CredentialsLocators.ENTER).click()
        driver.find_element(*CredentialsLocators.EMAIL_AUTHORIZATION).send_keys(CredentialForAuthorization.LOGIN_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.PASS_AUTHORIZATION).send_keys(CredentialForAuthorization.PASS_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.ENTER_AUTHORIZATION).click()
        # заполняем поля пароля и почты заведомо существующими данными и кликаем по кнопке войти

        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.home_page))
        # проверяем что произошел редирект на главную страницу и возвращаем true в случае успеха

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True) # запускаем тест в двух браузерах по очереди
    def test_authorization_in_forgot_pass_page(self, driver): # авторизация через кнопку "Войти" на странице восстановления пароля

        driver.get(Urls.forgot_pass_page) # получаем страницу восстановления пароля
        driver.find_element(*CredentialsLocators.ENTER_FORGOT_PASS).click()
        driver.find_element(*CredentialsLocators.EMAIL_AUTHORIZATION).send_keys(CredentialForAuthorization.LOGIN_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.PASS_AUTHORIZATION).send_keys(CredentialForAuthorization.PASS_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.ENTER_AUTHORIZATION).click()
        # заполняем поля пароля и почты заведомо существующими данными и кликаем по кнопке войти

        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.home_page))
        # проверяем что произошел редирект на главную страницу и возвращаем true в случае успеха

