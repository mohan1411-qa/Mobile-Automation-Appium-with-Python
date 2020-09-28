from AutomationDemoApp.base.base_page import BasePage
import AutomationDemoApp.utilities.custom_logger as cl


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    login_button_locator = "com.code2lead.kwad:id/Login"
    email_field_locator = "com.code2lead.kwad:id/Et4"
    password_field_locator = "com.code2lead.kwad:id/Et5"
    login_button = "com.code2lead.kwad:id/Btn3"
    page_title_locator = "Login Page"  #text
    app_page_locator = "Enter Admin"  #text
    admin_field_locator = "com.code2lead.kwad:id/Edt_admin"
    submit_button_locator = "com.code2lead.kwad:id/Btn_admin_sub"
    admin_text_locator = "com.code2lead.kwad:id/Tv_admin"
    error_message_locator = "Wrong Credentials" #text

    def click_login_button(self):
        self.click_element(self.login_button_locator)
        cl.allureLogs("Clicked on Login button")

    def enter_email(self, data):
        self.send_text(data, self.email_field_locator)
        cl.allureLogs("Entered the email")

    def enter_password(self, data):
        self.send_text(data, self.password_field_locator)
        cl.allureLogs("Entered the password")

    def click_sign_in_button(self):
        self.click_element(self.login_button)
        cl.allureLogs("Clicked on sign-in button to login")

    def login_page_verification(self):
        cl.allureLogs("Verified tha Login page")
        return self.is_element_displayed(self.page_title_locator, "text")

    def app_page_verification(self):
        cl.allureLogs("Verified the app page")
        return self.is_element_displayed(self.app_page_locator, "text")

    def enter_admin_text(self, data):
        self.send_text(data, self.admin_field_locator)
        cl.allureLogs("Entered text in admin field")

    def click_submit_button(self):
        self.click_element(self.submit_button_locator)
        cl.allureLogs("Clicked on submit button")

    def verify_admin_text(self):
        cl.allureLogs("Verified the admin text")
        return self.is_element_displayed(self.admin_text_locator)

    def verify_error_message(self):
        cl.allureLogs("Verified error message")
        return self.is_element_displayed(self.error_message_locator, "text")

