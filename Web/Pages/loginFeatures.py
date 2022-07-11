from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from Web.Utilitis.functions import assertAndAttached
from Web.Utilitis.Constants.loginLocetor import LoginLocators


class LoginFeature(LoginLocators):
    def __init__(self,driver:WebDriver):
        self.driver = driver

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

    def click_on_facebookBtn(self):
        driver = self.driver
        facebook_link = driver.find_element(By.CSS_SELECTOR, self.facebook_link_css)
        facebook_link.click()
        x = driver.window_handles
        driver.switch_to.window(x[1])
        assert driver.title == 'Facebook'

    def click_on_googelBtn(self):
        driver = self.driver
        google_link = driver.find_element(By.CSS_SELECTOR, self.google_link_css)
        google_link.click()
        x = driver.window_handles
        driver.switch_to.window(x[1])
        assert driver.title == 'כניסה - חשבונות Google'

    def click_on_twitterBtn(self):
        driver = self.driver
        twitter_link = driver.find_element(By.CSS_SELECTOR, self.twitter_link_css)
        twitter_link.click()
        x = driver.window_handles
        driver.switch_to.window(x[1])
        assert driver.title == 'twitter'


    def click_on_logout_btn(self):
        driver = self.driver
        logout_button = driver.find_element(By.XPATH,self.logout_link_xpath)
        logout_button.click()
        WebDriverWait(driver,15).until(
            driver.find_element(By.XPATH,self.login_span_xpath)
        )


