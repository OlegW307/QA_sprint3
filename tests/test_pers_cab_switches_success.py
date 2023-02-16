import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#  проверяем переход в личный кабинет
@pytest.mark.usefixtures('driver', 'test_user')
def test_pers_cab_switch_success(driver, test_user):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, ".//p[contains(text(), 'персональные данные')]")))
    assert driver.find_element(By.XPATH, ".//a[contains(text(), 'Профиль')]")


# проверяем переход в личный кабинет и возвращение в Конструктор по кнопке Конструктор
@pytest.mark.usefixtures('driver', 'test_user')
def test_constructor_button_switch_success(driver, test_user):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, ".//p[contains(text(), 'персональные данные')]")))
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, ".//p[contains(text(), 'Конструктор')]"))).click()
    assert driver.find_element(By.XPATH, ".//h1[contains(text(), 'Соберите')]")


# проверяем переход в личный кабинет и возвращение в Конструктор по нажатию на лого
@pytest.mark.usefixtures('driver', 'test_user')
def test_constructor_logo_switch_success(driver, test_user):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, ".//p[contains(text(), 'персональные данные')]")))
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2"))).click()
    assert driver.find_element(By.XPATH, ".//h1[contains(text(), 'Соберите')]")


# проверяем переход в личный кабинет и выход из него
@pytest.mark.usefixtures('driver', 'test_user')
def test_exit_switch_success(driver, test_user):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, ".//p[contains(text(), 'персональные данные')]")))
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, ".//button[contains(text(), 'Выход')]"))).click()
    assert WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, ".//h2[contains(text(), 'Вход')]")))
