import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import CredentialsLocators
from urls import Urls
from credentials_for_authorization import CredentialForAuthorization

class TestSignOut:

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True) # запускаем тест в двух браузерах по очереди
    def test_sing_out(self, driver): # тест авторизации и последующего выхода из аккаунта

        driver.get(Urls.home_page) # получаем главную страницу
        driver.find_element(*CredentialsLocators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*CredentialsLocators.EMAIL_AUTHORIZATION).send_keys(CredentialForAuthorization.LOGIN_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.PASS_AUTHORIZATION).send_keys(CredentialForAuthorization.PASS_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.ENTER_AUTHORIZATION).click()
        # заполняем поля пароля и почты заведомо существующими данными и кликаем по кнопке войти
        driver.find_element(*CredentialsLocators.PERSONAL_ACCOUNT).click()
        # открываем личный кабинет
        driver.find_element(*CredentialsLocators.SIGN_OUT).click()
        # клик по кнопке выйти
        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.login_page))
        # проверяем что произошел редирект на страницу авторизации и возвращаем true в случае успеха