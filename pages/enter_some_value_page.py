from AutomationDemoApp.base.base_page import BasePage
import AutomationDemoApp.utilities.custom_logger as cl


class EnterSomeValuePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    esm_button = "com.code2lead.kwad:id/EnterValue"
    esm_title = "Enter some Value" #text
    esm_text_field = "com.code2lead.kwad:id/Et1"
    submit_button = "com.code2lead.kwad:id/Btn1"
    text_preview = "com.code2lead.kwad:id/Tv1"

    def click_esm_button(self):
        self.click_element(self.esm_button)
        cl.allureLogs("Clicked on esm button")

    def enter_data(self, data):
        self.send_text(data, self.esm_text_field)
        cl.allureLogs("Entered text")

    def verify_page_title(self):
        self.is_element_displayed(self.esm_title, "text")
        cl.allureLogs("Verified Page Title")

    def click_submit_button(self):
        self.click_element(self.submit_button)
        cl.allureLogs("Clicked on submit button")

    def verify_text(self, text):
        result = self.get_text(self.text_preview)
        if result == text:
            cl.allureLogs("Verified Text")
            return True
        else:
            return False
