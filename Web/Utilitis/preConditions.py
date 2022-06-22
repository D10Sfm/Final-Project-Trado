import allure
import pytest
from Web.Base.Chrome.baseChrome import DriverInit
from Web.Base.FireFox.baseFireFox import DriverFireFox
from Web.Constants.footerLocators import FooterLocators
from selenium.webdriver.remote.webdriver import WebDriver
from Web.Utilitis.functions import assertAndAttached
from selenium.webdriver.common.by import By
from Db.trado_qa_db.collections import UsersCollections
from Db.Utilitis.preConditions import UsersCollection

class MainPreCondition(FooterLocators):
    def __init__(self,driver:WebDriver):
        self.driver = driver
    def landOnPage(self):
        driver = self.driver
        driver.get(self.base_url)
        assertAndAttached(driver, self.base_url, driver.current_url, "Url's not matching!")
        assertAndAttached(driver, 'trado', driver.title, "Title's not matching! ")


    def clickOnStoreInterest(self):
        driver = self.driver
        interest_div = driver.find_element(By.CSS_SELECTOR, self.div_store_interests_css)
        interests = interest_div.find_elements(By.TAG_NAME, 'div')
        for i in interests:
            i.click()
            class_value = i.get_attribute('class')
            assertAndAttached(driver, 'store_intrerstItem store_activeItem', class_value, "InterestNotActivated")


    def clickOnSaveBtStoreInterest(self):
        driver = self.driver
        save_bt = driver.find_element(By.XPATH, self.div_store_interests_saveBt_xpath)
        save_bt.click()


@pytest.mark.usefixtures('setup_chrome')
@pytest.mark.usefixtures('setUpUsersCollection')
class PaymentsPreCondition(DriverInit,UsersCollection):
    @pytest.fixture(autouse=True)
    def preConditionPayments(self,setup_chrome,setUpUsersCollection):
        driver = self.driver
        collection = self.collection
        users = UsersCollections(collection)
        payments = MainPreCondition(driver)
        payments.landOnPage()
        payments.clickOnStoreInterest()
        payments.clickOnSaveBtStoreInterest()
        driver.find_element(By.CSS_SELECTOR,
                             "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > a:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
        driver.find_element(By.XPATH,
                             "//div[contains(@class,'fullProduct_productsHedaer')]//i[contains(@class,'micon-plus icon_icon')]").click()
        checkout = driver.find_element(By.XPATH, "//button[contains(text(),'תשלום')]")
        checkout.click()
        phone = driver.find_element(By.XPATH, "//input[contains(@type,'tel')]")
        phone.click()
        phone.send_keys("0549767689")
        signin = driver.find_element(By.XPATH, "//input[@value='התחברות']")
        signin.click()
        code = users.getSmsCode('phone','0549767689')
        login_div = driver.find_element(By.CSS_SELECTOR,'div[class="form_loginCode"]')
        inputs = login_div.find_elements(By.TAG_NAME,'input')
        for digit,place in zip(code,inputs):
            place.send_keys(digit)
            assertAndAttached(driver,digit,place.get_attribute('value'),"DigitNotEnterdToPlace")
        # OTP HERE
        login_bt = driver.find_element(By.CSS_SELECTOR,'input[type="submit"]')
        login_bt.click()
        payment_checkout = driver.find_element(By.XPATH, "//button[contains(text(),'תשלום')]")
        payment_checkout.click()


@allure.description("This is precondition to all the footer check box tests[chrome]")
@pytest.mark.usefixtures('setup_chrome')
class PreConditionsInit(DriverInit):
    @pytest.fixture(autouse=True)
    def preConditionMain(self, setup_chrome):
        driver = self.driver
        footer_feature = MainPreCondition(driver)
        footer_feature.landOnPage()
        footer_feature.clickOnStoreInterest()
        footer_feature.clickOnSaveBtStoreInterest()

@allure.description("This is precondition to all the footer check box tests[firefox]")
@pytest.mark.usefixtures('setup_fire_fox')
class PreConditionFireFox(DriverFireFox):
    @pytest.fixture(autouse=True)
    def preConditionMain(self,setup_fire_fox):
        driver = self.driver
        footer_feature = MainPreCondition(driver)
        footer_feature.landOnPage()
        footer_feature.clickOnStoreInterest()
        footer_feature.clickOnSaveBtStoreInterest()


