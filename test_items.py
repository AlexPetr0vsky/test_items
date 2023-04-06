import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_is_button_add_to_basket_displayed(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    # time.sleep(30)
    button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")))
    assert button.is_displayed() is True, 'There is no "Add to basket" button on the page'
