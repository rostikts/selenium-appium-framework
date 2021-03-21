import os
from abc import ABC, abstractmethod

from selenium import webdriver


class DriverFactory(ABC):

    @abstractmethod
    def create_driver(self):
        pass


class ChromeManager(DriverFactory):
    DRIVER_PATH = os.path.abspath('drivers/chromedriver')

    def create_driver(self):
        return webdriver.Chrome(executable_path=self.DRIVER_PATH, options=self.init_chrome_options())


    def init_chrome_options(self):
        chrome_ops = webdriver.ChromeOptions()
        if os.environ.get('EXECUTOR') == 'local':
            chrome_ops.add_argument('--headless')
            chrome_ops.add_argument('--window-size=1920,1080')
        chrome_ops.add_argument('--no-sandbox')
        chrome_ops.add_argument('--disable-infobars')
        chrome_ops.add_argument('--disable-dev-shm-usage')

        return chrome_ops


class DriverManager:

    def return_driver(self, driver):
        if driver.lower() == 'chrome':
            return ChromeManager().create_driver()
