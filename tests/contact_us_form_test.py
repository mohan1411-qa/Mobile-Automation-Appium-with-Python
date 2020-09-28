from AutomationDemoApp.pages.contact_us_form_page import ContactUsPage
import AutomationDemoApp.utilities.custom_logger as cl
import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup")
class ContactFormTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_obj(self):
        self.cp = ContactUsPage(self.driver)

    @pytest.mark.run(order=3)
    def test_contact_us_button(self):
        cl.allureLogs("App Launch")
        self.cp.click_contact_us_form_button()
        result = self.cp.page_title()
        assert True == result

    @pytest.mark.run(order=4)
    def test_contact_us_page(self):
        self.cp.enter_name("")
        self.cp.enter_email("mohan@gmail.com")
        self.cp.enter_mobile("998765443")
        self.cp.enter_address("26 F Baker Street")
        self.cp.click_submit_button()











