import pytest
from selenium.webdriver.common.by import By
from Web.Utilitis.preConditions import PaymentsPreCondition
from Web.Utilitis.Constants.paymentLoacators import PaymentsLocators
from selenium.webdriver.common.keys import Keys
from time import sleep

@pytest.mark.usefixtures('preConditionPayments')
class Testpayments(PaymentsPreCondition, PaymentsLocators):
    def test_b2b(self):
        browser = self.driver
        choose_b2b = browser.find_element(By.CSS_SELECTOR, PaymentsLocators.choose_b2b).click()
        choose_b2b.click()
        b2b = browser.find_element(By.XPATH, PaymentsLocators.b2b_user_id).click()
        b2b.send_keys("12345")
        finish_order = browser.find_element(By.CSS_SELECTOR, PaymentsLocators.finish_order_button)
        finish_order.click()

    def test_invalid_b2b_id(self):
        browser = self.driver
        choose_b2b = browser.find_element(By.CSS_SELECTOR, PaymentsLocators.choose_b2b).click()
        choose_b2b.click()
        b2b = browser.find_element(By.XPATH, PaymentsLocators.b2b_user_id).click()
        b2b.send_keys("$%$%$")
        finish_order = browser.find_element(By.CSS_SELECTOR, PaymentsLocators.finish_order_button)
        finish_order.click()

    def test_Add_new_credit_card(self):
        browser = self.driver
        choose_credit_card = browser.find_element(By.XPATH, PaymentsLocators.new_card)
        choose_credit_card.click()
        credit_card_num = browser.find_element(By.ID, PaymentsLocators.credit_card_num)
        credit_card_num.click()
        credit_card_num.send_keys("12345678901112")
        sleep(2)
        id_num = browser.find_element(By.ID, PaymentsLocators.credit_card_id)
        id_num.click()
        id_num.send_keys("12345678")
        exp_month = browser.find_element(By.ID, PaymentsLocators.credit_card_exp)
        exp_month.click()
        exp_year = browser.find_element(By.ID, PaymentsLocators.credit_card_year)
        exp_year.click()
        cvv = browser.find_element(By.ID, PaymentsLocators.credit_card_cvv)
        cvv.send_keys("123")
        submit = browser.find_element(By.ID, PaymentsLocators.credit_card_submit)
        submit.send_keys(Keys.ENTER)
        finish_order = browser.find_element(By.CSS_SELECTOR, PaymentsLocators.finish_order_button)
        finish_order.click()

    def test_invalid_credit_card(self):
        browser = self.driver
        choose_credit_card = browser.find_element(By.XPATH, PaymentsLocators.new_card)
        choose_credit_card.click()
        credit_card_number = browser.find_element(By.ID, PaymentsLocators.credit_card_num)
        credit_card_number.click()
        credit_card_number.send_keys("#@$##%%##")
        id_num = browser.find_element(By.ID, PaymentsLocators.credit_card_id)
        id_num.click()
        id_num.send_keys("$$$$")
        exp_month = browser.find_element(By.ID, PaymentsLocators.credit_card_exp)
        exp_month.click()
        exp_year = browser.find_element(By.ID, PaymentsLocators.credit_card_year)
        exp_year.click()
        cvv = browser.find_element(By.ID, PaymentsLocators.credit_card_cvv)
        cvv.send_keys("$$$")
        submit = browser.find_element(By.ID, PaymentsLocators.credit_card_submit)
        submit.send_keys(Keys.ENTER)
        finish_order = browser.find_element(By.CSS_SELECTOR, PaymentsLocators.finish_order_button)
        finish_order.click()


    def test_cheque(self):
        browser = self.driver
        choose_cheque = browser.find_element(By.ID, PaymentsLocators.cheque_option)
        choose_cheque.click()
        bank_branch = browser.find_element(By.XPATH, PaymentsLocators.cheque_branch)
        bank_branch.send_keys("123")
        bank_number = browser.find_element(By.XPATH, PaymentsLocators.account_number)
        bank_number.send_keys("123456")
        signup = browser.find_element(By.XPATH, PaymentsLocators.cheque_sign)
        signup.click()
        finish_order = browser.find_element(By.CSS_SELECTOR, PaymentsLocators.finish_order_button)
        finish_order.click()

    def test_invalid_cheque(self):
        browser = self.driver
        choose_cheque = browser.find_element(By.ID, PaymentsLocators.cheque_option)
        choose_cheque.click()
        bank_branch = browser.find_element(By.XPATH, PaymentsLocators.cheque_branch)
        bank_branch.send_keys("$$$")
        bank_number = browser.find_element(By.XPATH, PaymentsLocators.account_number)
        bank_number.send_keys("$$$$$")
        signup = browser.find_element(By.XPATH, PaymentsLocators.cheque_sign)
        signup.click()
        finish_order = browser.find_element(By.CSS_SELECTOR, PaymentsLocators.finish_order_button)
        finish_order.click()

    def test_finTrado(self):
        browser = self.driver
        choose_finTrado = browser.find_element(By.XPATH, PaymentsLocators.choose_finTrado)
        choose_finTrado.click()
        confirm_fin = browser.find_element(By.XPATH, PaymentsLocators.finTrado_next)
        confirm_fin.click()
        confirm_fin = browser.find_element(By.XPATH, PaymentsLocators.finTrado_next)
        confirm_fin.click()
        finish = browser.find_element(By.XPATH, PaymentsLocators.finish_finTrado)
        finish.click()