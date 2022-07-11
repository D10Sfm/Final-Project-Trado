import allure
from Web.Utilitis.Constants import RegistrationLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from Web.Utilitis.functions import assertAndAttached


class RegistrationFeature(RegistrationLocators):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('go to registration')
    def click_on_registration_btn(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)
        driver.find_element(By.XPATH,self.registrationHomePage).click()
        div = driver.find_element(By.CSS_SELECTOR,self.registardiv)
        wait.until(EC.visibility_of(div))
        driver.find_element(By.XPATH,self.signup).click()
        register_h2 = driver.find_element(By.XPATH,self.h2_registration_window).text
        assertAndAttached(driver,'כיף שבאתם! כבר יוצרים לכם מקום בזירה',register_h2,"NotMoveToRegiister")

    @allure.step('registration with facebook')
    def click_on_facebook_link(self):
        driver = self.driver
        facebook = driver.find_element(By.XPATH,self.facebookButton)
        facebook.click()
        windoes = self.driver.window_handles
        driver.switch_to.window(windoes[1])
        title = driver.title
        assertAndAttached(driver,"facebook",title,"Notopen")

    @allure.step('registration with google')
    def click_on_google_link(self):
        driver = self.driver
        google = driver.find_element(By.XPATH,self.googleButton)
        google.click()
        windoes = driver.window_handles
        driver.switch_to.window(windoes[1])
        title = driver.title
        assertAndAttached(driver, "PASSED [100%]כניסה - חשבונות Google", title, "Notopen")

    @allure.step('registration with twitter')
    def click_on_twitter_link(self):
        driver = self.driver
        twitter = driver.find_element(By.XPATH,self.twitterButton)
        twitter.click()
        windoes = driver.window_handles
        driver.switch_to.window(windoes[1])
        title = driver.title
        assertAndAttached(driver, "twitter", title, "Notopen")
    @allure.step('inserting phone number')
    def insert_phoneNumber(self,number):
        driver = self.driver
        phone_field = self.driver.find_element(By.XPATH, self.phone_field_xpath)
        phone_field.send_keys(number)
        field_value = phone_field.get_attribute('value')
        assertAndAttached(driver,number,field_value,"NumberNotInField")

    @allure.step('marked policy box')
    def mark_policy_chick_box(self):
        driver = self.driver
        chickbox = driver.find_element(By.XPATH,self.policyBox)
        chickbox.click()
        valid = chickbox.get_attribute('class')
        assertAndAttached(driver," checkbox_checkbox checkbox_checked",valid,"NotMarked")



    @allure.step('unmarked mailing box')
    def unmark_mailing_chick_box(self):
        driver = self.driver
        chickbox = driver.find_element(By.XPATH,self.mailingList)
        chickbox.click()
        valid = chickbox.get_attribute('class')
        assertAndAttached(driver," checkbox_checkbox checkbox_checked",valid,"Unmarked")

    @allure.step('click on registration button')
    def click_on_registration_button(self):
        driver = self.driver
        reg = driver.find_element(By.XPATH,self.registarButton)
        reg.click()
        h5 = driver.find_element(By.XPATH,self.h5)
        h5.get_attribute('innerText')
        assertAndAttached(driver, "יש להזין את הקוד שקיבלת בהודעת SMS", h5, "NotValidat")


    @allure.step('enter Code sms')
    def enterCodeSms(self,code):
        driver = self.driver
        registration_div = driver.find_element(By.XPATH,self.sms_div_xpath)
        inputs = registration_div.find_elements(By.TAG_NAME,'input')
        for digit,place in zip(code,inputs):
            place.send_keys(digit)
            assertAndAttached(driver,digit,place.get_attribute('value'),"DigitNotEnterdToPlace")



    @allure.step('click on authentication')
    def click_on_authentication(self):
        driver = self.driver
        driver.find_element(By.XPATH,self.authentication_button).click()
        interests = driver.find_element(By.XPATH,self.h4)
        interests.get_attribute('innerText')
        assertAndAttached(driver,"יש לבחור לפחות תחום עניין 1 מתוך הרשימה",interests,"Interestsnotopen")


    @allure.step('click on interests')
    def click_on_interests(self):
        driver = self.driver
        driver.find_element(By.XPATH,self.cocltail).click()
        driver.find_element(By.XPATH,self.restaurants).click()
        driver.find_element(By.XPATH,self.create_account).click()
        account = driver.find_element(By.XPATH,self.personal_area)
        account.get_attribute('innerText')
        assertAndAttached(driver," מעבר לאיזור אישי ",account,"No account created")








