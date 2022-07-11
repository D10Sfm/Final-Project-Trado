from Web.Utilitis.Constants.rootConstants import Root

class PaymentsLocators(Root):
    # By.XPATH
    og_kush_xpath = "//div[contains(@class,'fullProduct_productsHedaer')]//i[contains(@class,'micon-plus icon_icon')]"
    move_to_payment_xpath = "//button[contains(@class,'button_button')]"
    name_xpath = "//input[@name='store']"
    ltd_xpath = "//input[@name='userId']"
    email_xpath = "//input[@name='email']"
    # By.NAME
    city_name = "address.city"
    street_name = "address.street"
    building_name = "address.building"
    enterance_name = "address.enterance"
    address_floor_name = "address.floor"
    # shipping address
    first_name = "firstName"
    last_name = "lastName"
    cellephone = "phone"
    # By.XPATH
    confirm_ship = "//button[@class='checkout-form_submitBtn']"
    # Wallet section
    # credit_card
    # By.XPATH
    new_card = "//div[normalize-space()='+']"
    # By.ID
    credit_card_num = "credit-card-input"
    credit_card_id = "userId-input"
    credit_card_exp = "expmonth"
    credit_card_year = "expyear"
    credit_card_cvv = "cvv"
    credit_card_submit = "btnSubmit"

    # B2B Option
    # By.XPATH
    choose_b2b = ".userCardsList_addCardBtn"
    b2b_input_id = "//input[@id='b2b']"
    b2b_user_id = "//input[@name_xpath='userId']"
    b2b_customer_id = "//input[@name_xpath='userCustomerId']"
    b2b_confirm_transfer = "//button[contains(text(),'אישור ההעברה')]"

    # cheque Option
    cheque_option = "etrado"
    cheque_branch = "//input[@name_xpath='branch']"
    account_number = "//input[@name_xpath='acountNumber']"
    cheque_sign = "//button[contains(text(),'חתימה + הוספת הצ')]"

    # finTrado
    choose_finTrado = "//input[@id='finTrado']"
    finTrado_next = "//button[contains(text(),'הבא')]"
    finish_finTrado = "//button[contains(text(),'סיים הזמנה')]"

    # return_to_homepage
    return_homePage = "// button[contains(text(), 'חזור לדף הבית')]"

    # Finish order
    finish_order_button = "input[value='בצע תשלום']"
