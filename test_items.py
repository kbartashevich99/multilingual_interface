import pytest
from selenium import webdriver
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestBasketButton():

    def test_find_basket_button(self, browser):
        browser.get(link)
        time.sleep(10)
        button = browser.find_elements_by_css_selector('.btn-add ')
        assert len(button) > 0, 'Button is not found'

