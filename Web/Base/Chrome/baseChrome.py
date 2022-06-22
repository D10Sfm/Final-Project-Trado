import pytest
from selenium import webdriver

from selenium.webdriver.remote.errorhandler import *

class DriverInit:

    @pytest.fixture(autouse=True)
    def setup_chrome(self):
            print("Initiating Chrome driver")
            self.driver = webdriver.Chrome()
            print("-----------------------------------------")
            print("Test is started")
            self.driver.implicitly_wait(15)
            self.driver.maximize_window()
            yield self.driver
            if self.driver is not None:
                print("-----------------------------------------")
                print("Tests is finished")
                self.driver.quit()
