import pytest
from selenium.webdriver.common.by import By
from generators import gen_login, gen_pass


# проверка, что пустое поле "Имя" не позволяет зарегестрироваться
@pytest.mark.usefixtures('browser')
def test_reg_null_name_failure(driver):
    login_test = gen_login()
    pass_test = gen_pass(8)
    driver.get('https://stellarburgers.nomoreparties.site/register')
    #  регистрация пользователя c пустым именем
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys('')
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(login_test)
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(pass_test)
    #  кнопка регистрация
    driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/form/button').click()
    # проверям что регистрация не произошла и кнопка Регистрации осталась на месте
    assert driver.find_element(By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]")


# ошибка на короткий пароль
@pytest.mark.usefixtures('browser')
def test_reg_short_pass_failure(driver):
    login_test = gen_login()
    # генерируем пароль из 3 символов
    pass_test = gen_pass(3)
    driver.get('https://stellarburgers.nomoreparties.site/register')
    #  регистрация пользователя c
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys('ShortPassword')
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(login_test)
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(pass_test)
    #  кнопка регистрация
    driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/form/button').click()
    #  проверяем что пояаилось сообщение об ошибке
    assert driver.find_element(By.XPATH, ".//p[contains(text(), 'Некорректный пароль')]")
