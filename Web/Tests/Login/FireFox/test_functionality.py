import allure
import pytest
from Web.Utilitis.preConditions import PreConditionFireFox
from Db.Utilitis.preConditions import UsersCollection
import Web.Pages.loginFeatures as feature
import Db.trado_qa_db.collections as records

@allure.description("This class is set of functional tests for login feature[firefox]")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sanity
@pytest.mark.usefixtures('preConditionMain')
@pytest.mark.usefixtures('setUpUsersCollection')
class TestLoginFeature(PreConditionFireFox,UsersCollection):

    @allure.description("This test is sending valid message via chat box[firefox]")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_registration(self):
        driver = self.driver
        collection = self.collection
        login_feature = feature.LoginFeature(driver)
        users = records.UsersCollections(collection)
        login_feature.clickOnLoginLink()
        login_feature.enterPhoneNumber('0525393079')
        login_feature.checkRememberBox()
        login_feature.clickOnLoginBtn()
        code = users.getSmsCode('phone','0525393079')
        login_feature.enterCodeSms(code)
        login_feature.clickOnVerificationBtn()