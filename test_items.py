import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_exist_button_add_to_cart(browser):
    browser.get(link)
    time.sleep(10)
    button_text = browser.find_element(By.CLASS_NAME, "btn-add-to-basket").text
    assert len(button_text) != 0, "Button is not exist"

