import unittest
from AutomationDemoApp.pages.login_page import LoginPage
import pytest
import AutomationDemoApp.utilities.custom_logger as cl


@pytest.mark.usefixtures("one_time_setup")
class LoginPageTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def cls_obj(self):
        self.cp = LoginPage(self.driver)

    @pytest.mark.run(order=5)
    def test_login_button(self):
        self.cp.click_login_button()
        result = self.cp.login_page_verification()
        assert True == result
        cl.allureLogs("Login Button Verification")

    @pytest.mark.run(order=7)
    def test_valid_login(self):
        self.cp.enter_email("admin@gmail.com")
        self.cp.enter_password("admin123")
        self.cp.click_sign_in_button()
        result = self.cp.app_page_verification()
        assert True == result

    @pytest.mark.run(order=8)
    def test_verify_admin_text(self):
        self.cp.enter_admin_text("Hello")
        self.cp.click_submit_button()
        result = self.cp.verify_admin_text()
        assert True == result

    @pytest.mark.run(order=6)
    def test_invalid_login(self):
        self.cp.enter_email("admin@gmail.com")
        self.cp.enter_password("admin12345")
        self.cp.click_sign_in_button()
        result = self.cp.verify_error_message()
        assert True == result



