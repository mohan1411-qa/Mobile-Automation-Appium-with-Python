import unittest
from AutomationDemoApp.pages.enter_some_value_page import EnterSomeValuePage
import AutomationDemoApp.utilities.custom_logger as cl
import pytest
import time

@pytest.mark.usefixtures("one_time_setup")
class EnterSomeValueTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def cls_obj(self):
        self.ep = EnterSomeValuePage(self.driver)

    @pytest.mark.run(order=1)
    def test_esm_button(self):
        cl.allureLogs("App Launched")
        self.ep.click_esm_button()
        self.ep.verify_page_title()

    @pytest.mark.run(order=2)
    def test_text_field(self):
        self.ep.enter_data("Appium Automation")
        self.ep.click_submit_button()
        time.sleep(10)
        result = self.ep.verify_text("Appium Automation")
        assert True == result
        cl.allureLogs("Test Case Passed")



