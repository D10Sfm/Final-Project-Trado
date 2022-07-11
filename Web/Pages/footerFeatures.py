import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from Web.Utilitis.functions import assertAndAttached
from Web.Utilitis.Constants import FooterLocators


@allure.title("footer chat box actions")
class FooterCheckBox(FooterLocators):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def clickOnChatBoxBtn(self):
        driver = self.driver
        chat_box_bt = driver.find_element(By.CSS_SELECTOR, self.footer_chatBox_button_css)
        chat_box_bt.click()

    def enterFirstName(self, firstName):
        driver = self.driver
        first_name_field = driver.find_element(By.CSS_SELECTOR, self.footer_chatBox_iframe_firstName_input_css)
        first_name_field.send_keys(firstName)
        assertAndAttached(driver, firstName, first_name_field.get_attribute('value'), "firstNameNotInfield")

    def enterEmail(self, email):
        driver = self.driver
        email_field = driver.find_element(By.CSS_SELECTOR, self.footer_chatBox_iframe_email_input_css)
        email_field.send_keys(email)
        assertAndAttached(driver, email, email_field.get_attribute('value'), "emailNotInfield")

    def enterText(self, text):
        driver = self.driver
        text_area = driver.find_element(By.CSS_SELECTOR, self.footer_chatBox_iframe_textarea_css)
        text_area.send_keys(text)
        assertAndAttached(driver, text, text_area.get_attribute('value'), "textNotInfield")

    def validClickSendBtn(self):
        driver = self.driver
        send_button = driver.find_element(By.CSS_SELECTOR, self.footer_chatBox_iframe_send_btn_css)
        send_button.click()
        sent_approval = driver.find_element(By.XPATH, self.footer_chatBox_approval_text_css).text
        assertAndAttached(driver, "Email Sent!", sent_approval, "EmailSentDontApproved")

    def clickSendBtn(self):
        driver = self.driver
        send_button = driver.find_element(By.CSS_SELECTOR, self.footer_chatBox_iframe_send_btn_css)
        send_button.click()

    def closeChatBox(self):
        driver = self.driver
        close_btn = driver.find_element(By.CSS_SELECTOR, self.footer_chatBox_close_iframe_button_css)
        div = driver.find_element(By.CSS_SELECTOR, self.footer_chatBox_iframe_css_selector)
        close_btn.click()
        try:
            WebDriverWait(driver, 15).until(
                EC.invisibility_of_element(div))
        finally:
            if (Exception):
                allure.attach(driver.get_screenshot_as_png(),
                              name='ChatBoxIframeNotClosed',
                              attachment_type=allure.attachment_type.PNG)


class FooterStayInTouch(FooterLocators):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def clickOnContactLinks(self):
        driver = self.driver
        contact_div = driver.find_element(By.CSS_SELECTOR, self.footer_contact_div_xpath)
        contact_link = contact_div.find_elements(By.TAG_NAME, 'a')
        title_list = ['Facebook - log in or sign up', 'Instagram', 'טוויטר \ טוויטר. זה מה שקורה.']
        names = ['Facebook', 'Instagram', 'Twitter']
        for link, expected, name in zip(contact_link, title_list, names):
            link.click()
            tabs = driver.window_handles
            tab = tabs[1]
            driver.switch_to.window(tab)
            title = driver.title
            assertAndAttached(driver, expected, title, f"{name}TabNotOpend")
            driver.close()
            driver.switch_to.window(tabs[0])


class FooterAdditionals(FooterLocators):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def clickOnAdditionalsLinks(self):
        driver = self.driver
        additional_div = driver.find_element(By.XPATH, self.footer_additionals_div_xpath)
        links = additional_div.find_elements(By.TAG_NAME, 'a')
        expect_title = 'כרטיס אשראי עסקי Trado Business - שלל הטבות לעסקים - max'
        expect_urls = [self.base_url + 'questions', self.base_url + 'shipment']
        for link, url in zip(links[0:2], expect_urls):
            link.click()
            assertAndAttached(driver, url, driver.current_url, "NotMatchingUrls")
        for link in links[2:]:
            link.click()
            tabs = driver.window_handles
            tab = tabs[1]
            driver.switch_to.window(tab)
            title = driver.title
            assertAndAttached(driver, expect_title, title, 'TitlesDontMatch')
            driver.close()
            driver.switch_to.window(tabs[0])


class FooterImportants(FooterLocators):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def clickOnImportantsLinks(self):
        driver = self.driver
        importants_div = driver.find_element(By.XPATH, self.footer_importants_div_xpath)
        importants_link = importants_div.find_elements(By.TAG_NAME, 'a')
        who_us_url = 'https://www.trado.co.il/page'
        urls = ['https://qa.trado.co.il/user/personalArea', 'https://www.trado.co.il/etrado',
                'https://www.trado.co.il/contact', 'https://www.trado.co.il/joinUs']
        importants_link[0].click()
        x = driver.window_handles
        driver.switch_to.window(x[1])
        assert driver.current_url == who_us_url
        driver.close()
        driver.switch_to.window(x[0])
        importants_link[1].click()
        assert urls[0] == driver.current_url
        exit = driver.find_element(By.CSS_SELECTOR, self.exit_bt_login_div)
        exit.click()
        driver.back()
        for link, expected in zip(importants_link[2:], urls[1:]):
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(link)
            )
            link.click()
            url = driver.current_url
            assertAndAttached(driver, expected, url, f"abNotOpend")
            driver.back()


class FooterImportants_who_us(FooterLocators):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def clickOn_who_us(self):
        driver = self.driver
        who_us_div = driver.find_element(By.XPATH, self.footer_importants_who_us_link_xpath).click()

    def clickOn_More_details_button(self):
        driver = self.driver
        additional_div = driver.find_element(By.XPATH, self.footer_additionals_div_xpath)
        links = additional_div.find_elements(By.TAG_NAME, 'a')
        expect_title = 'כרטיס אשראי עסקי Trado Business - שלל הטבות לעסקים - max'
        expect_urls = [self.base_url + 'questions', self.base_url + 'shipment']
        for link, url in zip(links[0:2], expect_urls):
            link.click()
            assertAndAttached(driver, url, driver.current_url, "NotMatchingUrls")
        for link in links[2:]:
            link.click()
            tabs = driver.window_handles
            tab = tabs[1]
            driver.switch_to.window(tab)
            title = driver.title
            assertAndAttached(driver, expect_title, title, 'TitlesDontMatch')
            driver.close()
            driver.switch_to.window(tabs[0])

    def clickOn_To_the_trading_arena_button(self):
        driver = self.driver
        To_the_trading_arena = driver.find_element(By.XPATH, self.To_the_trading_arena).click()


class FooterUi(FooterLocators):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def test_test(self):
        driver = self.driver
        x = driver.find_element(By.CSS_SELECTOR, 'div[class="footer_chatBox"]').get_attribute('clientHeight')
        y = driver.find_element(By.CSS_SELECTOR, 'div[class="footer_chatBox"]').get_attribute('scrollWidth')
        print(x, y)
        assert x == 165
        assert y == 313
