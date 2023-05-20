import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_guest_should_see_login_link(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    assert browser.find_elements(By.CLASS_NAME, 'btn.btn-default'), "корзинка не найдена"