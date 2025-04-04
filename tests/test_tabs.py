import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import Urls
from locators import CredentialsLocators

class TestTabs:

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    def test_tabs_scroll(self, driver):

        driver.get(Urls.home_page)
        wait = WebDriverWait(driver, 10)

        # Нажимаем на таб "Соусы" и проверяем, что он становится активным
        wait.until(EC.element_to_be_clickable(CredentialsLocators.TAB_SOUSY)).click()
        active_sousy = wait.until(EC.visibility_of_element_located(CredentialsLocators.TAB_SOUSY_ACTIVE))
        assert active_sousy.is_displayed()

        # Нажимаем на таб "Булки" и проверяем, что он становится активным
        wait.until(EC.element_to_be_clickable(CredentialsLocators.TAB_BULKI)).click()
        active_bulki = wait.until(EC.visibility_of_element_located(CredentialsLocators.TAB_BULKI_ACTIVE))
        assert active_bulki.is_displayed()

        # Нажимаем на таб "Начинки" и проверяем, что он становится активным
        wait.until(EC.element_to_be_clickable(CredentialsLocators.TAB_NACHINKI)).click()
        active_nachinki = wait.until(EC.visibility_of_element_located(CredentialsLocators.TAB_NACHINKI_ACTIVE))
        assert active_nachinki.is_displayed()
