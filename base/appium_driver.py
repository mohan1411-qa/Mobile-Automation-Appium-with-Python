from traceback import print_stack
import time
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from AutomationDemoApp.utilities.custom_logger import CustomLogger
from appium.webdriver.common.touch_action import TouchAction
import os
import allure


class AppiumDriver():
    log = CustomLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locator_value, locator_type="id"):
        locator_type = locator_type.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locator_type == "id":
            element = wait.until(lambda x: x.find_element_by_id(locator_value))
            return element
        elif locator_type == "class":
            element = wait.until(lambda x: x.find_element_by_class_name(locator_value))
            return element
        elif locator_type == "des":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().description("%s")' % (locator_value)))
            return element
        elif locator_type == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator("UiSelector().index(%d)" % int(locator_value)))
            return element
        elif locator_type == "text":
            element = wait.until(lambda x: x.find_element_by_android_uiautomator('text("%s")' % locator_value))
            return element
        elif locator_type == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath('%s' % (locator_value)))
            return element
        else:
            self.log.info("Locator value " + locator_value + "not found")

        return element

    def get_element(self, locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.waitForElement(locator_value, locator_type)
            self.log.info("Element found with LocatorType: {} "
                          "with the locator_value : {} ".format(locator_type, locator_value))
        except:
            allure.attach(self.screen_shot(locator_type))
            self.log.info(
                "Element not found with LocatorType: {}  and "
                "with the locator_value : {}".format(locator_type, locator_value))

        return element

    def click_element(self, locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.click()
            self.log.info("Clicked on element with LocatorType: {} "
                          "the locator_value : {} ".format(locator_type, locator_value))
        except:
            allure.attach(self.screen_shot(locator_type))
            self.log.info(
                "Cannot clicked on element with LocatorType: {}  and "
                "the locator_value : {}".format(locator_type, locator_value))

    def send_text(self,data, locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.send_keys(data)
            self.log.info("Send data on element with LocatorType: {} and "
                          "the locator_value : {} ".format(locator_type, locator_value))
        except:
            allure.attach(self.screen_shot(locator_type))
            self.log.info(
                "Cannot send data with LocatorType: {}  and "
                "the locator_value : {}".format(locator_type, locator_value))

    def clear_field(self, locator_value="", locator_type="id", element=None):
        try:
            if locator_value:
                element = self.get_element(locator_value, locator_type)
            element.clear()
            self.log.info("Cleared data on element with locator: {} and "
                          "locator_type: {}".format(locator_value, locator_type))
        except:
            allure.attach(self.screen_shot(locator_type))
            self.log.info(
                "Cannot clear data on element with locator: {} "
                "and locator_type: {}".format(locator_value, locator_type))

    def is_element_displayed(self, locator_value="", locator_type="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locator_type
        """
        isDisplayed = False
        try:
            if locator_value:  # This means if locator is not empty
                element = self.get_element(locator_value, locator_type)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator_value +
                              " locator_type: " + locator_type)
            else:
                allure.attach(self.screen_shot(locator_type))
                self.log.info("Element not displayed with locator: " + locator_value +
                              " locator_type: " + locator_type)
            return isDisplayed
        except:
            print("Element not found")
            allure.attach(self.driver.get_screenshot_as_png(), name=locator_type)
            return False

    def screen_shot(self, screenshot_name):
        """
        Takes screenshot of the current open web page
        """
        file_name = screenshot_name + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        file_path = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, file_path)
        destination_directory = os.path.join(current_directory, screenshot_directory)
        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot save to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def get_text(self,locator_value="", locator_type="id", element=None):
        data = None
        try:
            if locator_value:
                element = self.get_element(locator_value, locator_type)
            data = element.text
            self.log.info("Text found on element with locator: {} and "
                          "locator_type: {}".format(locator_value, locator_type))
        except:
            allure.attach(self.screen_shot(locator_type))
            self.log.info(
                "No text found on element with locator: {} "
                "and locator_type: {}".format(locator_value, locator_type))

        return data

    def scroll_screen(self, scroll_number):
        touch = TouchAction(self.driver)
        for i in range(scroll_number):
            touch.press(x=976, y=1968).move_to(x=996, y=321).release().perform()
            self.log.info("Screen scrolled {}".format(scroll_number))

    def drag_and_drop_element(self, locator_value="", locator_type="id", drop_locator_value="", drop_locator_type="id"):
        actions = TouchAction(self.driver)
        if locator_value:
            element = self.get_element(locator_value, locator_type)
            drop_loc = self.get_element(drop_locator_value, drop_locator_type)
            actions.long_press(element).move_to(drop_loc).release().perform()
            self.log.info("Dragged and dropped into {}".format(drop_loc))
        else:
            self.log.info("Locator value is not given")

    def get_location(self,locator_value="", locator_type="id"):
        element = self.get_element(locator_value, locator_type)
        loc = element.location
        return loc





