import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from generator_credentials import GeneratorCredentials
from locators import CredentialsLocators
from urls import Urls
from credentials_for_authorization import CredentialForAuthorization


@pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)  # запускаем тест в двух браузерах по очереди
def test_tabs_scroll(driver):
    driver.get(Urls.home_page)  # открываем страницу с табами и списками продуктов


    tab_bulki = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]"))
    )
    # Прокручиваем элемент в видимую область
    driver.execute_script("arguments[0].scrollIntoView(true);", tab_bulki)

    driver.execute_script("arguments[0].click();", tab_bulki)

    # Проверяем, что первый продукт из списка булок отображается
    product_bulki = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[1]/a[1]"))
    )
    assert product_bulki.is_displayed()

    # Повторяем для таба "Соусы"
    tab_sousy = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", tab_sousy)
    driver.execute_script("arguments[0].click();", tab_sousy)

    product_sousy = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[2]/a[1]"))
    )
    assert product_sousy.is_displayed()

    # Повторяем для таба "Начинки"
    tab_nachinki = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", tab_nachinki)
    driver.execute_script("arguments[0].click();", tab_nachinki)

    product_nachinki = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/section[1]/div[2]/ul[3]/a[1]"))
    )
    assert product_nachinki.is_displayed()