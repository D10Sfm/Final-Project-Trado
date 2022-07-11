from Web.Utilitis.Constants.rootConstants import Root

class LoginLocators(Root):
    facebook_link_css = 'button[class="login_facebook metro"]'
    google_link_css = 'button[class="login_google"]'
    logout_link_xpath = '//a[contains(@class,"header_logOut")]'
    twitter_link_css = 'div[class="login_twitter"]'
    login_span_xpath = "//span[contains(text(),'התחברות')]"

