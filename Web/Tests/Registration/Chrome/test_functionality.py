import allure
import pytest
from Web.Utilitis.preConditions import PreConditionsInit
from Db.Utilitis.preConditions import UsersCollection
import Db.trado_qa_db.collections as collections
from Web.Pages.registrationFeatures import RegistrationFeature


@allure.description("This class is set of functional tests for registration feature[chrome]")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sanity
@pytest.mark.usefixtures('preConditionMain')
@pytest.mark.usefixtures('setUpUsersCollection')


class TestRegistrationFeatures(PreConditionsInit,UsersCollection):

    @allure.description("This test checks a valid registration with facebook[chrome]")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_registration_with_facebook(self):
        driver = self.driver
        register = RegistrationFeature(driver)
        register.click_on_registration_btn()
        register.click_on_facebook_link()

    @allure.description("This test checks a valid registration with google[chrome]")
    def test_valid_registration_with_google(self):
        driver = self.driver
        register = RegistrationFeature(driver)
        register.click_on_registration_btn()
        register.click_on_google_link()

    @allure.description("This test checks a valid registration with twitter[chrome]")
    def test_valid_registration_with_twitter(self):
        driver = self.driver
        register = RegistrationFeature(driver)
        register.click_on_registration_btn()
        register.click_on_twitter_link()

    @allure.description("This test checks a valid registration with phone_field_xpath[chrome]")
    def test_valid_registration_with_phoneNumber(self):
        driver = self.driver
        collection = self.collection
        register = RegistrationFeature(driver)
        users = collections.UsersCollections(collection)
        register.click_on_registration_btn()
        register.insert_phoneNumber("0525346456")
        register.mark_policy_chick_box()
        register.click_on_registration_button()
        code = users.getSmsCode('phone','0525346456')
        register.enterCodeSms(code)
        register.click_on_authentication()
        register.click_on_interests()


    @allure.description("This test checks a valid registration with phone_field_xpath When the mailbox is unmarked[chrome]")
    def test_valid_registration_with_phoneNumber_unmarked_mailing(self):
        driver = self.driver
        collection = self.collection
        register = RegistrationFeature(driver)
        users = collections.UsersCollections(collection)
        register.click_on_registration_btn()
        register.insert_phoneNumber("0525346459")
        register.mark_policy_chick_box()
        register.unmark_mailing_chick_box()
        register.click_on_registration_button()
        code = users.getSmsCode('phone', '0525346459')
        register.enterCodeSms(code)
        register.click_on_authentication()
        register.click_on_interests()


    @allure.description("This test checks a invalid registration with phone_field_xpath over ten digits[chrome]")
    def test_invalid_registration_with_phoneNumber_12_digits(self):
        driver = self.driver
        register = RegistrationFeature(driver)
        register.click_on_registration_btn()
        register.insert_phoneNumber("052534645988")
        register.mark_policy_chick_box()
        register.click_on_registration_button()

    @allure.description("This test checks a invalid registration with phone_field_xpath under ten digits[chrome]")
    def test_invalid_registration_with_phoneNumber_9_digits(self):
        driver = self.driver
        register = RegistrationFeature(driver)
        register.click_on_registration_btn()
        register.insert_phoneNumber("052534645")
        register.mark_policy_chick_box()
        register.click_on_registration_button()

    @allure.description("This test checks a invalid registration with phone_field_xpath over ten digits and unmarked policy[chrome]")
    def test_invalid_registration_with_phoneNumber_12_digits_and_unmarked_policy(self):
        driver = self.driver
        
        register = RegistrationFeature(driver)
        register.click_on_registration_btn()
        register.insert_phoneNumber("052534645")
        register.click_on_registration_button()

    @allure.description("This test checks a invalid registration with phone_field_xpath under ten digits and unmarked policy[chrome]")
    def test_invalid_registration_with_phoneNumber_9_digits_and_unmarked_policy(self):
        driver = self.driver
        register = RegistrationFeature(driver)
        register.click_on_registration_btn()
        register.insert_phoneNumber("052534645")
        register.click_on_registration_button()

    @allure.description("This test checks a invalid registration with phone_field_xpath (marks)[chrome]")
    def test_invalid_registration_with_phoneNumber_marks(self):
        driver = self.driver
        register = RegistrationFeature(driver)
        register.click_on_registration_btn()
        register.insert_phoneNumber(")%@%#$^$%^")
        register.mark_policy_chick_box()
        register.click_on_registration_button()

    @allure.description("This test checks a invalid registration with phone_field_xpath (marks) and unmarked policy[chrome]")
    def test_invalid_registration_with_phoneNumber_marks_unmarked_policy(self):
        driver = self.driver
        register = RegistrationFeature(driver)
        register.click_on_registration_btn()
        register.insert_phoneNumber(")%@%#$^$%^")
        register.click_on_registration_button()

    @allure.description("This test checks a invalid registration with phone_field_xpath (null)[chrome]")
    def test_invalid_registration_with_null_phoneNumber(self):
        driver = self.driver
        register = RegistrationFeature(driver)
        register.click_on_registration_btn()
        register.insert_phoneNumber("")
        register.mark_policy_chick_box()
        register.click_on_registration_button()

    @allure.description("This test checks a invalid registration with phone_field_xpath (null) and unmarked policy[chrome]")
    def test_invalid_registration_with_null_phoneNumber_unmarked_policy(self):
        driver = self.driver
        register = RegistrationFeature(driver)
        register.click_on_registration_btn()
        register.insert_phoneNumber("")
        register.click_on_registration_button()