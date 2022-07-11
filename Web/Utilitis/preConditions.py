import allure
import pytest
from Web.Base.baseChrome import DriverInit
from Web.Utilitis.Constants.rootConstants import Root
from selenium.webdriver.remote.webdriver import WebDriver
from Web.Utilitis.functions import assertAndAttached
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Db.trado_qa_db.collections import UsersCollections
from Db.Utilitis.preConditions import UsersCollection

class MainPreCondition(Root):
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

    def clickOnLoginLink(self):
        driver = self.driver
        login_link = driver.find_element(By.CSS_SELECTOR,self.login_link_css)
        login_link.click()
        div = driver.find_element(By.CSS_SELECTOR,self.login_div_css)
        WebDriverWait(driver,15).until(
            EC.visibility_of(div)
        )
    def enterPhoneNumber(self,phone):
        driver = self.driver
        phone_field = driver.find_element(By.CSS_SELECTOR,self.phone_field_css)
        phone_field.send_keys(phone)
        actual = phone_field.get_attribute('value')
        assertAndAttached(driver,phone,actual,'PhoneNotInField')

    def checkRememberBox(self):
        driver = self.driver
        check_box = driver.find_element(By.CSS_SELECTOR,self.check_in_css)
        active = driver.find_element(By.CSS_SELECTOR,self.active_check_box_css)
        check_box.click()
        actual = active.get_attribute('class')
        assertAndAttached(driver," checkbox_checkbox checkbox_checked",actual,"CheckBoxDontChecked")

    def clickOnLoginBtn(self,valid=True):
        driver = self.driver
        login_btn = driver.find_element(By.CSS_SELECTOR,self.login_btn_css)
        login_btn.click()
        if valid:
            div = driver.find_element(By.CSS_SELECTOR,self.sms_div_css)
            WebDriverWait(driver,15).until(
                EC.visibility_of(div)
            )
        else:
            pass
    def enterCodeSms(self,code,valid=True):
        driver = self.driver
        login_div = driver.find_element(By.CSS_SELECTOR,self.sms_div_css)
        inputs = login_div.find_elements(By.TAG_NAME,'input')
        for digit,place in zip(code,inputs):
            place.send_keys(digit)
            if valid:
                assertAndAttached(driver,digit,place.get_attribute('value'),"DigitNotEnterdToPlace")
            else:
                pass
    def clickOnVerificationBtn(self,valid=True,name='יונתן אליאס'):
        driver = self.driver
        verification_btn = driver.find_element(By.CSS_SELECTOR,self.verification_btn_css)
        verification_btn.click()
        if valid:
            WebDriverWait(driver,15).until(
                EC.invisibility_of_element((By.CSS_SELECTOR,self.login_div_css))
            )
            user_name = driver.find_element(By.CSS_SELECTOR,self.user_area_link_css).get_attribute('innerText')
            assertAndAttached(driver,f"שלום {name},\nמעבר לאיזור אישי",user_name,"UserNameDontShowingInHeader")
        else:
            pass


@allure.description("This is precondition to all the footer check box tests[chrome]")
@pytest.mark.usefixtures('setup_chrome')
class PreConditionsInit(DriverInit,UsersCollection):
    @pytest.fixture(autouse=True)
    def preConMainGuest(self, setup_chrome):
        driver = self.driver
        main = MainPreCondition(driver)
        main.landOnPage()
        main.clickOnStoreInterest()
        main.clickOnSaveBtStoreInterest()

    # @pytest.mark.usefixtures('preConMainGuest')
    # @pytest.mark.usefixtures('setUpUsersCollection')
    @pytest.fixture(autouse=True)
    def preConMainLoginUser(self,preConMainGuest,setUpUsersCollection):
        driver = self.driver
        main = MainPreCondition(driver)
        collection = self.collection
        users = UsersCollections(collection)
        main.clickOnLoginLink()
        main.enterPhoneNumber('0525086651')
        code = users.getSmsCode('phone','0525086651')
        main.enterCodeSms(code)
        main.clickOnVerificationBtn()




# @pytest.mark.usefixtures('setup_chrome')
# @pytest.mark.usefixtures('setUpUsersCollection')
# class PaymentsPreCondition(DriverInit,UsersCollection):
#     @pytest.fixture(autouse=True)
#     def preConditionPayments(self,setup_chrome,setUpUsersCollection):
#         driver = self.driver
#         collection = self.collection
#         users = UsersCollections(collection)
#         payments = MainPreCondition(driver)
#         payments.landOnPage()
#         payments.clickOnStoreInterest()
#         payments.clickOnSaveBtStoreInterest()
#         driver.find_element(By.CSS_SELECTOR,
#                              "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > a:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
#         driver.find_element(By.XPATH,
#                              "//div[contains(@class,'fullProduct_productsHedaer')]//i[contains(@class,'micon-plus icon_icon')]").click()
#         checkout = driver.find_element(By.XPATH, "//button[contains(text(),'תשלום')]")
#         checkout.click()
#         phone = driver.find_element(By.XPATH, "//input[contains(@type,'tel')]")
#         phone.click()
#         phone.send_keys("0549767689")
#         signin = driver.find_element(By.XPATH, "//input[@value='התחברות']")
#         signin.click()
#         code = users.getSmsCode('phone','0549767689')
#         login_div = driver.find_element(By.CSS_SELECTOR,'div[class="form_loginCode"]')
#         inputs = login_div.find_elements(By.TAG_NAME,'input')
#         for digit,place in zip(code,inputs):
#             place.send_keys(digit)
#             assertAndAttached(driver,digit,place.get_attribute('value'),"DigitNotEnterdToPlace")
#         # OTP HERE
#         login_bt = driver.find_element(By.CSS_SELECTOR,'input[type="submit"]')
#         login_bt.click()
#         payment_checkout = driver.find_element(By.XPATH, "//button[contains(text(),'תשלום')]")
#         payment_checkout.click()

