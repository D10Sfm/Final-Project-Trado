import allure
import pytest
from selenium.webdriver.common.by import By
import Web.Pages.loginFeatures as feature
from Web.Utilitis.preConditions import PreConditionsInit



class TestUI(PreConditionsInit):
    def test_upper_bur_ui(self):
        driver = self.driver
        collection = self.collection
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        Upper = self.driver.find_element(By.CSS_SELECTOR,'div[class="login_loginregister"]').get_attribute("innerText")
        assert Upper == "signInsignUp"


    def test_title_ui(self):
        driver = self.driver
        collection = self.collection
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        title = self.driver.find_element(By.CSS_SELECTOR,'div [class="login_titleContainer"]').get_attribute("innerText")
        assert title == "ברוכים השבים! מתרגשים לראות אתכם כאן\nבחרו את אפשרות ההתחברות המועדפת עליכם"

    def test_logo_ui(self):
        driver = self.driver
        collection = self.collection
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        Logo = self.driver.find_element(By.CSS_SELECTOR, 'div[class="login_socialLoginButtons"]').get_attribute("innerText")
        assert Logo == ""

    def test_OR_ui(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        Or = self.driver.find_element(By.CSS_SELECTOR, 'div[class="login_or"]').get_attribute("innerText")
        assert Or == "או"

    def test_phone_ui(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        phone = self.driver.find_element(By.CSS_SELECTOR,'div[class="form_formItem  undefined undefined false undefined"]').get_attribute("innerText")
        assert phone == "* מס' הטלפון שלך"

    def test_remmemberMe(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        rememberMe = self.driver.find_element(By.CSS_SELECTOR,'div[class="form_formItem  form_checkbox undefined false undefined"]').get_attribute("innerText")
        assert rememberMe == "זכור אותי לפעם הבאה :)"

    def test_Login_ui(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        Login = self.driver.find_element(By.CSS_SELECTOR,'input[class="form_submitBtn"]').get_attribute("defaultValue")
        assert Login == "התחברות"


    def test_title_page2(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0525086651')
        login_feature.clickOnLoginBtn()
        verify = self.driver.find_element(By.CSS_SELECTOR,'div[class="login_titleContainer"]').get_attribute("innerText")
        assert verify == "רק מוודאים שאנחנו מכירים\nיש להזין את הקוד שקיבלת בהודעת SMS"

    def test_elemnts_logo(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0525086651')
        login_feature.clickOnLoginBtn()
        logo = self.driver.find_element(By.CSS_SELECTOR,'div[class="login_socialLoginButtons"]').get_attribute("innerText")
        assert logo == ""

    def test_OR_page2(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0525086651')
        login_feature.clickOnLoginBtn()
        OR = self.driver.find_element(By.CSS_SELECTOR, 'div[class="login_or"]').get_attribute("innerText")
        assert OR == "או"

    def test_code(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0525086651')
        login_feature.clickOnLoginBtn()
        code = self.driver.find_element(By.CSS_SELECTOR, 'div[class="form_loginCode"]').get_attribute("innerText")
        assert code == ""

    def test_verify_page2(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0525086651')
        login_feature.clickOnLoginBtn()
        code = self.driver.find_element(By.CSS_SELECTOR, 'input[class="form_submitBtn"]').get_attribute("defaultValue")
        assert code == "בצע אימות"


    def test_ageinSMS(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0525086651')
        login_feature.clickOnLoginBtn()
        agein_SMS = self.driver.find_element(By.CSS_SELECTOR, 'input[class="form_submitBtn"]').get_attribute("innerText")
        assert agein_SMS == "שלחו לי שוב, SMS לא קיבלתי"


    def test_securing(self):
        driver = self.driver
        login_feature = feature.LoginFeature(driver)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0525086651')
        login_feature.clickOnLoginBtn()
        Securing = self.driver.find_element(By.CSS_SELECTOR, 'div[class="login_securityBanner"]').get_attribute("innerText")
        assert Securing =="אימות באבטחה מוגברת\n\nהפרטיות שלכם חשובה לנו. אנו מבקשים לבצע אימות באמצעות בכדי להיות בטוחים שאלו אתם והפרטים שלכם מוגנים SMS"