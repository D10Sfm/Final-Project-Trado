import allure
from selenium.webdriver.remote.webdriver import WebDriver




def assertAndAttached(driver:WebDriver,expected,actual,name):
    try:
        assert expected == actual
    finally:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(),
                          name=name,
                          attachment_type=allure.attachment_type.PNG)
        else:
            pass


