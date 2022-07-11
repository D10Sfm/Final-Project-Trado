class Root:
    # urls
    base_url = 'https://qa.trado.co.il/'

    # main page pre condition locators
    div_store_interests_css = 'div[class="store_interests"]'
    div_store_interests_saveBt_xpath = "//button[contains(text(),'Save')]"

    # main page pre condition login user locators
    login_link_css =  'a[class="header_userAreaLink"]'
    phone_field_css = 'input[type="tel"]'
    check_in_css = 'i[class="micon-check icon_icon "]'
    login_btn_css = 'input[type="submit"]'
    sms_div_css = 'div[class="form_loginCode"]'
    verification_btn_css = 'input[class="form_submitBtn"]'
    login_div_css = 'div[class="modal_modal modal_login_modal login_modal"]'
    active_check_box_css = 'span[class=" checkbox_checkbox "]'
    user_area_link_css = 'a[class="header_userAreaLink"]'
