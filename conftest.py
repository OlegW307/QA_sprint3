import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import gen_login, gen_pass


# фикстура для передачи адреса страницы сайта для использования в тесте
@pytest.fixture(scope='function')
def driver_param(request):
    browser_driver = webdriver.Chrome(executable_path='./chromedriver')
    browser_driver.get(request.param)
    yield browser_driver
    browser_driver.quit()


# фикстура для разных браузеров Хром и Firefox
@pytest.fixture(params=['chrome', 'firefox'])
def driver_two(request):
    if request.param == 'chrome':
        driver_two = webdriver.Chrome()
    elif request.param == 'firefox':
        driver_two = webdriver.Firefox()
    else:
        raise ValueError('Invalid browser selection')
    yield driver_two
    driver_two.quit()


# простая фикстура драйвера Хрома
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# фикстура для регистрации и входа на сайт
@pytest.fixture
def test_user(driver):
    login_test = gen_login()
    pass_test = gen_pass(8)
    driver.get('https://stellarburgers.nomoreparties.site/register')
    #  регистрация пользователя
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys('UserConstructor')
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(login_test)
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(pass_test)
    #  кнопка регистрация
    driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/form/button').click()
    # ждем когда отрисутеся страница и можно будет вводить данные
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, ".//h2[contains(text(), 'Вход')]")))
    # ввод данных после регистрации для входа
    driver.find_element(By.XPATH, ".//input[@type='text']").send_keys(login_test)
    driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(pass_test)
    #   кнопка Войти
    driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/form/button').click()
