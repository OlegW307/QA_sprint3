import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# переход к разделу Начинки
@pytest.mark.parametrize("driver_param", ['https://stellarburgers.nomoreparties.site/'], indirect=True)
def test_fillings_switch_success(driver_param):
    driver_param.find_element(By.XPATH, ".//span[contains(text(), 'Начинки')]").click()
    WebDriverWait(driver_param, 3).until(EC.visibility_of_element_located(
        (By.XPATH, ".//h2[contains(text(), 'Начинки')]")))
    assert driver_param.find_element(By.XPATH, ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and contains("
                                               "text(), 'Мясо')]")


# переход к разделу Соусы
@pytest.mark.parametrize("driver_param", ['https://stellarburgers.nomoreparties.site/'], indirect=True)
def test_salsas_switch_success(driver_param):
    driver_param.find_element(By.XPATH, ".//span[contains(text(), 'Соусы')]").click()
    WebDriverWait(driver_param, 3).until(EC.visibility_of_element_located(
        (By.XPATH, ".//h2[contains(text(), 'Соусы')]")))
    assert driver_param.find_element(By.XPATH, ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and contains("
                                               "text(), 'Соус')]")


# переход к разделу Булки (сначала прыгаем на другую вкладку)
@pytest.mark.parametrize("driver_param", ['https://stellarburgers.nomoreparties.site/'], indirect=True)
def test_rolls_switch_success(driver_param):
    driver_param.find_element(By.XPATH, ".//span[contains(text(), 'Начинки')]").click()
    driver_param.find_element(By.XPATH, ".//span[contains(text(), 'Булки')]").click()
    WebDriverWait(driver_param, 3).until(EC.visibility_of_element_located(
        (By.XPATH, ".//h2[contains(text(), 'Булки')]")))
    assert driver_param.find_element(By.XPATH, ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and contains("
                                               "text(), 'булка')]")
