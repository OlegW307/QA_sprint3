from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import gen_login, gen_pass


class TestGoodEntry:
    @classmethod
    def setup_class(cls):
        cls.login_test = gen_login()
        cls.password = gen_pass(8)
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://stellarburgers.nomoreparties.site/register')
        cls.driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys('ClassUser')
        cls.driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(cls.login_test)
        cls.driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys(cls.password)
        cls.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/form/button').click()

    def setup_method(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/')
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()

    # успешный вход на сайт чере кнопку войти в Аккаунт
    def test_enter_account_success(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]"))).click()
        self.driver.find_element(By.XPATH, ".//input[@type='text']").send_keys(self.login_test)
        self.driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(self.password)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/form/button').click()
        assert WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")))

    # успешный вход через Личный кабинет
    def test_enter_pers_cab_success(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]"))).click()
        self.driver.find_element(By.XPATH, ".//input[@type='text']").send_keys(self.login_test)
        self.driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(self.password)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/form/button').click()
        assert WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")))

    # успешный вход через форму восстановления пароля
    def test_enter_recovery_success(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, ".//a[@class='Auth_link__1fOlj']"))).click()
        self.driver.find_element(By.XPATH, ".//input[@type='text']").send_keys(self.login_test)
        self.driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(self.password)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/form/button').click()
        assert WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")))
