# QA_sprint3 "Финальный проект 3го спринта" 

##Описание тестов и локаторов

ВНИМАНИЕ: в связи с плохим Интернет соединением и как следствие долгим временем открытия страниц в тестах применяется избыточное количество ожидания.

###**0. conftest.py**

- фикстура для передачи адреса страницы в тест @pytest.fixture(scope='function')
def driver_param(request):
- фикстура для разных браузеров 
@pytest.fixture(params=['chrome', 'firefox']) 
def browser(request):
- простая фикстура драйвера хрома
@pytest.fixture 
def driver(request):
- фикстура для регистрации и входа на сайт
@pytest.fixture 
def test_user(driver)


###**1. test_first_reg_entry_sucсess.py**
Проверка успешной регистрации и входа на сайт.
Регистрация и вход осуществляется через фикстуру.

В тесте проверяется наличие на странице https://stellarburgers.nomoreparties.site/ 
кнопки "Оформить заказ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                   "button_button_size_large__G21Vg']"
                   или
                   ".//button[contains(text(), 'Оформить заказ')]"


###**2. test_alt_entry_success.py**
В тестах этого файла проверяются альтернативные способы входа на сайт.
Тесты сгрупированы в класс. Регистрация пароля осуществляется в предусловиях для всего класса.

Локаторы для полей ввода полей  
- ".//input[@type='text']")
- ".//input[@type='password']")
- '/html/body/div[1]/div/main/div/form/button'

https://stellarburgers.nomoreparties.site/ 

2.1.Успешный вход по кнопке «Войти в аккаунт» на главной

**def test_enter_account_success(self):** 
- заходим через кнопку 'Войти в аккаунт' ".//button[contains(text(), 'Войти в аккаунт')]"
- проверка через кнопку оформить заказ ".//button[contains(text(), 'Оформить заказ')]"
        
2.2.Успешный вход через кнопку «Личный кабинет»

**def test_enter_pers_cab_success(self):**
- заходим через кнопку 'Личный кабинет' ".//p[contains(text(), 'Личный Кабинет')]"
- проверка через кнопку оформить заказ ".//button[contains(text(), 'Оформить заказ')]"

'https://stellarburgers.nomoreparties.site/forgot-password'

2.3.Успешный вход через кнопку в форме восстановления пароля

**def test_enter_recovery_success(self):**
- переход в форму входа по локатору ".//a[@class='Auth_link__1fOlj']"
- проверка через кнопку оформить заказ ".//button[contains(text(), 'Оформить заказ')]"
  
        
##**3. test_constructor_switches_success.py**
Проверяем переходы внутри конструктора заказов.
Все тесты однотипные.

Тестироание  https://stellarburgers.nomoreparties.site/

Регистрация и вход в фикстурах. @pytest.mark.parametrize("driver_param", ['https://stellarburgers.nomoreparties.site/'], indirect=True)
Фикстура для передачи страницы исключительно в образовательных целях.

3.1. Переход к разделу Начинки

**def test_fillings_switch_success(driver_param):**
- переходим по кнопке Начинки ".//span[contains(text(), 'Начинки')]"
- ждем когда появится раздел Начинки ".//h2[contains(text(), 'Начинки')]"
- проверяем по наличию характерной позиции ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and contains("
                                            "text(), 'Мясо')]")

3.2. переход к разделу Соусы

**def test_salsas_switch_success(driver_param):**
- переходим по кнопке Соусы ".//span[contains(text(), 'Соусы')]"
- ждем когда появится раздел Соусы ".//h2[contains(text(), 'Соусы')]"
- проверяем по наличию характерной позиции ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and contains("
                                         "text(), 'Соус')]"
                                            
3.3.переход к разделу Булки (сначала прыгаем на другую вкладку)

**def test_rolls_switch_success(driver_param):**
- переходим по кнопке Начинки ".//span[contains(text(), 'Начинки')]" что бы кнопка Булки стала стала активной
- переходим по кнопке Булки ".//span[contains(text(), 'Булки')]"
- ждем когда появится раздел Булки ".//h2[contains(text(), 'Булки')]"
- проверяем по наличию характерной позиции "".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and contains("
                                         "text(), 'булка')]""


##**4. test_pers_cab_switches_success.py**
Проверяем переходы в личный кабинет и обратно.
Использовались фикстуры @pytest.mark.usefixtures('driver', 'test_user')

Тестироание на странице  https://stellarburgers.nomoreparties.site/
                                       
4.1. проверяем переход в личный кабинет

**def test_pers_cab_switch_success(driver, test_user):**
- Нажмаем кнопку личнй кабинет ".//p[contains(text(), 'Личный Кабинет')]"     
- Ждем когда появится надпись персональные данные ".//p[contains(text(), 'персональные данные')]"
- Проверяем по надписи Профиль ".//a[contains(text(), 'Профиль')]"
                                  
                                                                          
4.2. проверяем переход в личный кабинет и возвращение в Конструктор по кнопке Конструктор

**def test_constructor_button_switch_success(driver, test_user):**
- Нажмаем кнопку личнй кабинет ".//p[contains(text(), 'Личный Кабинет')]"     
- Ждем когда появится надпись персональные данные ".//p[contains(text(), 'персональные данные')]"
- Нажимаем на кнопку Конструктор ".//p[contains(text(), 'Конструктор')]"
- Проверяем наличие элемента Соберите ".//h1[contains(text(), 'Соберите')]" 
   
                                         
4.3. проверяем переход в личный кабинет и возвращение в Конструктор по нажатию на лого

**def test_constructor_button_switch_success(driver, test_user):**
- Нажмаем кнопку личнй кабинет ".//p[contains(text(), 'Личный Кабинет')]"     
- Ждем когда появится надпись персональные данные ".//p[contains(text(), 'персональные данные')]"
- Нажимаем на Лого ".AppHeader_header__logo__2D0X2"
- Проверяем наличие элемента Соберите ".//h1[contains(text(), 'Соберите')]"


4.4. проверяем переход в личный кабинет и выход из него  

**def test_exit_switch_success(driver, test_user):**
- Нажмаем кнопку личнй кабинет ".//p[contains(text(), 'Личный Кабинет')]"     
- Ждем когда появится надпись персональные данные ".//p[contains(text(), 'персональные данные')]"
- Выходим по кнопке ".//button[contains(text(), 'Выход')]"
- Проверяем по наличию элемента ".//h2[contains(text(), 'Вход')]"

                                             
##**5. test_reg_errors.py**
Используем фикстуру для 2 браузеров

5.1. проверка, что пустое поле "Имя" не позволяет зарегестрироваться

**def test_reg_null_name_failure(driver):**
- при регистрации вводим пустое имя './/fieldset[1]/div/div/input').send_keys('')
проверям что регистрация не произошла и кнопка Регистрации осталась на месте
".//button[contains(text(), 'Зарегистрироваться')]"

5.2. ошибка на короткий пароль

**def test_reg_short_pass_failure(driver):**
- генерируем пароль из 3 символов pass_test = gen_pass(3)
- проверяем что пояаилось сообщение об ошибке ".//p[contains(text(), 'Некорректный пароль')]"



