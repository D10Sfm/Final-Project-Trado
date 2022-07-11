import allure
import pytest
from Web.Utilitis.functions import assertAndAttached
from selenium.webdriver.common.by import By
from Web.Utilitis.preConditions import PreConditionsInit
from Db.Utilitis.preConditions import UsersCollection
import Web.Pages.loginFeatures as feature
import Db.trado_qa_db.collections as collections

import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)



@allure.description("This class is set of functional tests for login feature[chrome]")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures('setUpUsersCollection')
@pytest.mark.usefixtures('preConMainGuest')
@pytest.mark.xfail(str(IPAddr) != '172.24.176.1',reason='No connection to DB in this ip')
class TestLoginFeature(PreConditionsInit, UsersCollection):

    @allure.description("This test is valid login to the system[chrome]")
    @pytest.mark.sanity
    @pytest.mark.usefixtures('preConMainLoginUser')
    def test_valid_login(self,preConMainLoginUser):
        driver = self.driver
        return driver

    def test_valid_login_null_rememberBox(self):
        driver = self.driver
        collection = self.collection
        login_feature = feature.LoginFeature(driver)
        users = collections.UsersCollections(collection)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0525086651')
        login_feature.clickOnLoginBtn()
        code = users.getSmsCode('phone', '0525086651')
        login_feature.enterCodeSms(code)
        login_feature.clickOnVerificationBtn()

    @pytest.mark.sanity
    def test_login_invalid_phone_under_10_digits(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('05250866')
        login_feature.checkRememberBox()
        login_feature.clickOnLoginBtn(valid=False)
        message = driver.find_element(By.CSS_SELECTOR,'div[class="form_note "]').text
        assertAndAttached(driver,"מס׳ טלפון לא תקין",message,'Wrong/NotInMessage')

    @pytest.mark.sanity
    def test_login_invalid_phone_over_10_digits(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0525086651111')
        login_feature.checkRememberBox()
        login_feature.clickOnLoginBtn(valid=False)
        message = driver.find_element(By.CSS_SELECTOR,'div[class="form_note "]')
        assertAndAttached(driver,message.text,"מס׳ טלפון לא תקין",'Wrong/NotInMessage')

    def test_login_null_phone_and_null_remember_box(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('')
        login_feature.clickOnLoginBtn(valid=False)
        message = driver.find_element(By.CSS_SELECTOR,'div[class="form_note "]')
        assertAndAttached(driver,message.text,"נא למלא שדה זה",'Wrong/NotInMessage')

    @pytest.mark.sanity
    def test_invalid_login_null_phone(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('')
        login_feature.checkRememberBox()
        login_feature.clickOnLoginBtn(valid=False)
        message = driver.find_element(By.CSS_SELECTOR,'div[class="form_note "]')
        assertAndAttached(driver,message.text,"נא למלא שדה זה",'Wrong/NotInMessage')

    @pytest.mark.sanity
    def test_login_not_existent_number(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0595236541')
        login_feature.checkRememberBox()
        login_feature.clickOnLoginBtn(valid=False)
        message = driver.find_element(By.CSS_SELECTOR,'div[class="form_message"]')
        assertAndAttached(driver,message.text,'no such user please register','Wrong/NotInMessage')


    def test_link_facebook(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.click_on_facebookBtn()

    def test_link_google(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.click_on_googelBtn()
    @pytest.mark.regression
    @pytest.mark.xfail(reason="Twitter intgration still in developing")
    def test_link_twitter(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.click_on_twitterBtn()

    @pytest.mark.sanity
    def test_login_invalid_smsCode(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0525086651')
        login_feature.checkRememberBox()
        login_feature.clickOnLoginBtn()
        code = '14656'
        login_feature.enterCodeSms(code)
        login_feature.clickOnVerificationBtn(valid=False)
        message = driver.find_element(By.CSS_SELECTOR,'div[class="form_message"]').get_attribute('innerText')
        assertAndAttached(driver,'Faild To Login',message,'Wrong/NotInMessage')

    @pytest.mark.sanity
    def test_login_invalid_sms_code_under_5_digits(self):
        driver = self.driver
        collection = self.collection
        login_feature = feature.LoginFeature(driver)
        collections.UsersCollections(collection)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0525086651')
        login_feature.checkRememberBox()
        login_feature.clickOnLoginBtn()
        code = '146'
        login_feature.enterCodeSms(code)
        login_feature.clickOnVerificationBtn(valid=False)
        message = driver.find_element(By.CSS_SELECTOR,'div[class="form_message"]').text
        print(message)
        # assertAndAttached(driver,'Faild To Login',message,'Wrong/NotInMessage')

    @pytest.mark.sanity
    def test_login_invalid_code_charcters(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0525086651')
        login_feature.checkRememberBox()
        login_feature.clickOnLoginBtn()
        code = '147$@'
        login_feature.enterCodeSms(code,valid=False)
        login_feature.clickOnVerificationBtn(valid=False)
        message = driver.find_element(By.CSS_SELECTOR,'div[class="form_message"]').get_attribute('innerHTML')
        assertAndAttached(driver,'Faild To Login',message,'Wrong/NotInMessage')
    @pytest.mark.sanity
    def test_valid_logout(self):
        driver = self.test_valid_login()
        login_feature = feature.LoginFeature(driver)
        login_feature.click_on_logout_btn()



