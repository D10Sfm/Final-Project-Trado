from Web.Utilitis.preConditions import PreConditionFireFox
import allure
import pytest
import Web.Pages.footerFeatures as feature



@allure.description("This class is set of functional tests for Footer Chat box[chrome]")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures('preConditionMain')
class TestFooterChatBox(PreConditionFireFox):



    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_send_message_valid(self):
        driver = self.driver
        footer_feature = feature.FooterCheckBox(driver)
        footer_feature.clickOnChatBoxBtn()
        footer_feature.enterFirstName('Fasil')
        footer_feature.enterEmail('fasileos12@gmail.com')
        footer_feature.enterText('Messi IS! the best player in football history')
        footer_feature.validClickSendBtn()
        footer_feature.closeChatBox()

    @allure.severity(allure.severity_level.MINOR)
    def test_send_message_nullName(self):
        driver = self.driver
        footer_feature = feature.FooterCheckBox(driver)
        footer_feature.clickOnChatBoxBtn()
        footer_feature.enterEmail('fasileos12@gmail.com')
        footer_feature.enterText('Messi IS! the best player in football history')
        footer_feature.clickSendBtn()

    @allure.severity(allure.severity_level.MINOR)
    def test_send_message_nullEmail(self):
        driver = self.driver
        footer_feature = feature.FooterCheckBox(driver)
        footer_feature.clickOnChatBoxBtn()
        footer_feature.enterFirstName('Fasil')
        footer_feature.enterText('Messi IS! the best player in football history')
        footer_feature.clickSendBtn()

    @allure.severity(allure.severity_level.MINOR)
    def test_send_message_nullText(self):
        driver = self.driver
        footer_feature = feature.FooterCheckBox(driver)
        footer_feature.clickOnChatBoxBtn()
        footer_feature.enterFirstName('Fasil')
        footer_feature.enterEmail('fasileos12@gmail.com')
        footer_feature.clickSendBtn()


    def test_send_message_invalid_email(self):
        driver = self.driver
        footer_feature = feature.FooterCheckBox(driver)
        footer_feature.clickOnChatBoxBtn()
        footer_feature.enterFirstName('Fasil')
        footer_feature.enterEmail('fasileos.@gmail..com')
        footer_feature.clickSendBtn()


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures('preConditionMain')
class TestFooterStayInTouch(PreConditionFireFox):
    @pytest.mark.sanity
    def test_contact_link(self):
        driver = self.driver
        stay_in_touch = feature.FooterStayInTouch(driver)
        stay_in_touch.clickOnContactLinks()

@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.usefixtures('preConditionMain')
class TestFooterAdditionals(PreConditionFireFox):
    @pytest.mark.sanity
    def test_links(self):
        driver = self.driver
        additionals = feature.FooterAdditionals(driver)
        additionals.clickOnAdditionalsLinks()



@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.sanity
@pytest.mark.usefixtures('preConditionMain')
class TestFooterImportants(PreConditionFireFox):
    def test_importants_link(self):
        driver = self.driver
        stay_in_touch = feature.FooterImportants(driver)
        stay_in_touch.clickOnImportantsLinks()


@pytest.mark.sanity
@pytest.mark.usefixtures('preConditionMain')
class TestFooterImportants_who_us(PreConditionFireFox):
    def test_Importants_who_us_links(self):
        driver = self.driver
        Importants_who_us = feature.FooterImportants_who_us(driver)
        Importants_who_us.clickOn_who_us()

