from AutomationDemoApp.base.base_page import BasePage
import time

class ScrollViewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    scroll_view_button = "com.code2lead.kwad:id/ScrollView"
    page_title = "ScrollView"  #text
    button_1 = "BUTTON1"
    button_15 = "BUTTON15"
    button_16 = "BUTTON16"
    yes_button = "YES"
    no_button = "NO"
    home_page = "Appium Demo"

    def click_scroll_view_button(self):
        self.click_element(self.scroll_view_button)
        time.sleep(5)

    def click_button_1(self):
        self.click_element(self.button_1, "text")
        time.sleep(3)

    def click_button_15(self):
        self.click_element(self.button_15, "text")
        time.sleep(3)

    def click_button_16(self):
        self.click_element(self.button_16, "text")
        time.sleep(3)

    def verify_page_title(self):
        result = self.is_element_displayed(self.page_title, "text")
        return result

    def verify_scroll(self, scroll_count):
        self.scroll_screen(scroll_count)

    def click_alert_yes(self):
        self.click_element(self.yes_button, "text")
        time.sleep(2)

    def click_alert_no(self):
        self.click_element(self.no_button, "text")
        time.sleep(2)

    def verify_home_page(self):
        result = self.is_element_displayed(self.home_page, "text")
        return result






