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


class AndroidManager(DriverFactory):

    def create_driver(self):
        return webdriver.Remote(command_executor="http://hub-cloud.browserstack.com/wd/hub",
                                desired_capabilities=self.init_android_options())

    def init_android_options(self):
        return {
            # Set your access credentials
            "browserstack.user": "rostislavtsiapur1",
            "browserstack.key": "sYAXtqzAiwrQSGpwfRxC",

            # Set URL of the application under test
            "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",

            # Specify device and os_version for testing
            "device": "Google Pixel 3",
            "os_version": "9.0",

            # Set other BrowserStack capabilities
            "project": "First Python project",
            "build": "Python Android",
            "name": "first_test"
        }


class DriverManager:

    def return_driver(self, driver):
        if driver.lower() == 'chrome':
            return ChromeManager().create_driver()
        elif driver.lower() == 'android':
            return AndroidManager().create_driver()

