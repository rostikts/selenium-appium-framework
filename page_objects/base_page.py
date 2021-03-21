import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def enter_query(self):
        self.driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys('lol')
