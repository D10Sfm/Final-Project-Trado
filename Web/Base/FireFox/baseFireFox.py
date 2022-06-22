import pytest
from selenium import webdriver


class DriverFireFox:

    @pytest.fixture(autouse=True)
    def setup_fire_fox(self):
        print("Initiating FireFox driver")
        self.driver = webdriver.Firefox()
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()