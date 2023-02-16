import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures('driver', 'test_user')
def test_reg_pers_cabs_success(driver, test_user):
    assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
        (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx "
                   "button_button_size_large__G21Vg']")))
