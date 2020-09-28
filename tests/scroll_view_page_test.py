from AutomationDemoApp.pages.scroll_view_page import ScrollViewPage
import unittest
import pytest
import time


@pytest.mark.usefixtures("one_time_setup")
class ScrollViewTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def cls_obj(self):
        self.sv = ScrollViewPage(self.driver)

    @pytest.mark.run(order=9)
    def test_button1(self):
        self.sv.click_scroll_view_button()
        result = self.sv.verify_page_title()
        assert True == result
        self.sv.click_button_1()
        self.sv.click_alert_no()
        result_1 = self.sv.verify_page_title()
        assert True == result_1
        self.sv.click_button_1()
        self.sv.click_alert_yes()
        result_2 = self.sv.verify_home_page()
        assert True == result_2
        time.sleep(3)

    @pytest.mark.run(order=11)
    def test_scroll_view_button16(self):
        self.sv.click_scroll_view_button()
        self.sv.verify_scroll(1)
        self.sv.click_button_16()
        self.sv.click_alert_yes()
        result_1 = self.sv.verify_home_page()
        assert True == result_1

    @pytest.mark.run(order=10)
    def test_scroll_view_button15(self):
        self.sv.click_scroll_view_button()
        self.sv.verify_scroll(1)
        self.sv.click_button_15()
        self.sv.click_alert_yes()
        result_1 = self.sv.verify_home_page()
        assert True == result_1
        time.sleep(3)

