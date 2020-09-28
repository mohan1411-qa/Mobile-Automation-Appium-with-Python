from AutomationDemoApp.base.base_page import BasePage
import AutomationDemoApp.utilities.custom_logger as cl


class ContactUsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    enter_name_field = "com.code2lead.kwad:id/Et2"  #id
    enter_email_field = "com.code2lead.kwad:id/Et3"  #id
    enter_address_field = "com.code2lead.kwad:id/Et6"  #id
    enter_mobile_no_field = "com.code2lead.kwad:id/Et7"  #id
    contact_us_button = "com.code2lead.kwad:id/ContactUs"  #id
    page_name = "Contact Us form"  #text
    submit_button_locator = "com.code2lead.kwad:id/Btn2"  #id

    def enter_name(self, name=""):
        self.send_text(name, self.enter_name_field)
        cl.allureLogs("Enter the name")

    def enter_email(self, email=""):
        self.send_text(email, self.enter_email_field)
        cl.allureLogs("Enter the email ID")

    def enter_address(self, address=""):
        self.send_text(address, self.enter_address_field)
        cl.allureLogs("Enter the address")

    def enter_mobile(self, mobile_no=""):
        self.send_text(mobile_no, self.enter_mobile_no_field)
        cl.allureLogs("Enter the mobile number")

    def click_contact_us_form_button(self):
        self.click_element(self.contact_us_button)
        cl.allureLogs("Click on Contact Us Form Button")

    def page_title(self):
        cl.allureLogs("Verify the page")
        return self.is_element_displayed(self.page_name, "text")

    def click_submit_button(self):
        self.click_element(self.submit_button_locator)
        cl.allureLogs("Click on submit button")




