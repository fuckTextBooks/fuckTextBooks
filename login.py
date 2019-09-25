from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def login(user: str, passw: str):
    browser = webdriver.Firefox()

    # Open UofT bookstore course material UTORID redirect login
    browser.get('https://www.utpshop.com/secure/')
    # Grab needed login elements
    login_user = browser.find_element_by_id('username')
    login_pass = browser.find_element_by_id('password')
    login_button = browser.find_element_by_name('_eventId_proceed')
    # Fill credentials
    login_user.send_keys(user)
    login_pass.send_keys(passw)
    # Click login
    login_button.click()

    # Wait for new page to finish loading
    browser.implicitly_wait(15)
    browser.find_element_by_id('buybackForm')

    # Return html
    return browser.page_source
