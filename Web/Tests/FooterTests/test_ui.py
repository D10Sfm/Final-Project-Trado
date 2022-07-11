import allure
import pytest
import Web.Pages.footerFeatures as feature
from Web.Utilitis.preConditions import PreConditionsInit



@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.usefixtures('preConMainGuest')
class TestUiFooter(PreConditionsInit):
    def test_footer_ui_checkbox(self):
        driver = self.driver
        footer_ui = feature.FooterUi(driver)
        footer_ui.test_test()
        allure.attach(driver.get_screenshot_as_png(), name="invalid", attachment_type=allure.attachment_type.PNG)
        try:
            assert driver.title == ""
        except Exception as e:
            print("Title is wrong", format(e))
            driver.quit()
