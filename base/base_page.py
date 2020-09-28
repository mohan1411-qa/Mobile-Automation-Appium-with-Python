"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from AutomationDemoApp.base.appium_driver import AppiumDriver
from traceback import print_stack


class BasePage(AppiumDriver):
    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver

    # def verify_page_title(self, title_to_verify):
    #     """
    #     Verify the page Title
    #
    #     Parameters:
    #         title_to_verify: Title on the page that needs to be verified
    #     """
    #     # try:
    #     #     actualTitle = self.get_title()
    #     #     return self.util.verifyTextContains(actualTitle, title_to_verify)
    #     # except:
    #     #     self.log.error("Failed to get page title")
    #     #     print_stack()
    #     #     return False
    #     pass
    # def verify_text(self, locator, locator_type, text_to_verify):
    #     """
    #     Verify the text
    #
    #     Parameters:
    #     titleToVerify: Text on the page that needs to be verified
    #     """
    #     try:
    #         actual_text = self.get_text(locator, locator_type)
    #         return self.util.verifyTextMatch(actual_text, text_to_verify)
    #     except:
    #         self.log.info("Failed to get the text")
    #         print_stack()
    #         return False
    #
    # def modify_result(self, expected_result, actual_result):
    #     return self.util.verifyTestResult(expected_result, actual_result)





