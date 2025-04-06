import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import CredentialsLocators
from urls import Urls
from credentials_for_authorization import CredentialForAuthorization

class TestPersonalAccount:

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True) # запускаем тест в двух браузерах по очереди
    def test_redirect_to_personal_account(self, driver): # тест перехода в личный кабинет

        driver.get(Urls.home_page) # получаем главную страницу
        driver.find_element(*CredentialsLocators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*CredentialsLocators.EMAIL_AUTHORIZATION).send_keys(CredentialForAuthorization.LOGIN_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.PASS_AUTHORIZATION).send_keys(CredentialForAuthorization.PASS_FOR_AUTHORIZATION)
        driver.find_element(*CredentialsLocators.ENTER_AUTHORIZATION).click()
        # заполняем поля пароля и почты заведомо существующими данными и кликаем по кнопке войти
        driver.find_element(*CredentialsLocators.PERSONAL_ACCOUNT).click()
        # открываем личный кабинет

        assert WebDriverWait(driver, 10).until(EC.url_to_be(Urls.personal_account_page))
        # проверяем что произошел редирект на страницу личного кабинета и возвращаем true в случае успеха