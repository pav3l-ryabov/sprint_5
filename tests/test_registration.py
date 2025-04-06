import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from generator_credentials import GeneratorCredentials
from locators import CredentialsLocators
from urls import Urls


class TestRegistration:

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True) # запускаем тест в двух браузерах по очереди
    def test_success_reg(self, driver): # успешная регистрация

        driver.get(Urls.reg_page) # получаем страницу регистрации

        driver.find_element(*CredentialsLocators.NAME).send_keys(GeneratorCredentials.generate_valid_name())
        driver.find_element(*CredentialsLocators.EMAIL).send_keys(GeneratorCredentials.generate_valid_email())
        driver.find_element(*CredentialsLocators.PASSWORD).send_keys(GeneratorCredentials.generate_valid_pass())
        driver.find_element(*CredentialsLocators.REGISTRATION).click()
        # ищем поля и заполняем сгенерированными данными, ищем и кликаем кнопку регистрации

        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.login_page))
        # без wait проверка падает, поэтому одновременно проверяем что произошел редирект на страницу логина и возвращаем true в случае успеха

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True) # запускаем тест в двух браузерах по очереди
    def test_not_success_reg_short_pass(self, driver): # невалидный короткий пароль

        driver.get(Urls.reg_page) # получаем страницу регистрации

        driver.find_element(*CredentialsLocators.NAME).send_keys(GeneratorCredentials.generate_valid_name())
        driver.find_element(*CredentialsLocators.EMAIL).send_keys(GeneratorCredentials.generate_valid_email())
        driver.find_element(*CredentialsLocators.PASSWORD).send_keys(GeneratorCredentials.generate_invalid_short_pass())
        driver.find_element(*CredentialsLocators.REGISTRATION).click()
        # ищем поля и заполняем сгенерированными данными, ищем и кликаем кнопку регистрации

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((CredentialsLocators.INVALID_PASS))
        )
        # ждем отобразится ли всплывающая подсказка "Некорректный пароль"?

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True) # запускаем тест в двух браузерах по очереди
    def test_not_success_reg_null_pass(self, driver): # пустой пароль

        driver.get(Urls.reg_page) # получаем страницу регистрации

        driver.find_element(*CredentialsLocators.NAME).send_keys(GeneratorCredentials.generate_valid_name())
        driver.find_element(*CredentialsLocators.EMAIL).send_keys(GeneratorCredentials.generate_valid_email())
        driver.find_element(*CredentialsLocators.PASSWORD).send_keys('')
        driver.find_element(*CredentialsLocators.REGISTRATION).click()
        # ищем поля и заполняем сгенерированными данными, ищем и кликаем кнопку регистрации

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((CredentialsLocators.INVALID_PASS))
        ),
        # ждем отобразится ли всплывающая подсказка "Некорректный пароль"?
        # всплывашка не появляется - нашли баг

