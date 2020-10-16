import logging
from time import time, sleep
from page_objects import PageObject
from traceback2 import print_stack
import utilities.custom_logger as cl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(PageObject):

    '''
    This class will be inherited by all Page classes
    '''
    # logger for any test run
    log = cl.customLogger(logging.DEBUG)

    def get_element(self, locator, locatorType="css"):
        element = None
        try:
            locatorType = locatorType.lower()
            if locatorType == "id":
                element = self.w.find_element_by_id(locator)
            elif locatorType == "name":
                element = self.w.find_element_by_name(locator)
            elif locatorType == "xpath":
                element = self.w.find_element_by_xpath(locator)
            elif locatorType == "css":
                element = self.w.find_element_by_css_selector(locator)
            elif locatorType == "class":
                element = self.w.find_element_by_class(locator)
            elif locatorType == "link":
                element = self.w.find_element_by_link_text(locator)
            elif locatorType == "tag":
                element = self.w.find_element_by_tag_name(locator)
            else:
                self.log.info("Locator type: " + locatorType +
                              "is not correct/supported")
        except:
            self.log.info("Element not found with locator: " + locator +
                          "and locatorType: " + locatorType)
        return element

    def click_element(self, locator, locatorType="css"):
        element = None
        try:
            if locator:
                element = self.get_element(locator, locatorType)

            element.click()
            self.log.info("Clicked on element with locator:" + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          "locatorType: " + locatorType)
            print_stack()

    def send_keys(self, data, locator="", locatorType="css", element=None):
        try:
            if locator:
                element = self.get_element(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          "locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on element with locator: " + locator +
                          "locatorType: " + locatorType)
            print_stack()

    def wait_for_element_clickable(self, locator, wait_time=10, poll_frequency=1, ignored_exceptions=None, xpath=False):
        sleep(1) # this sleep is for animations that make clicking tricky
        if xpath == True:
            try:
                WebDriverWait(self.w, wait_time, poll_frequency, ignored_exceptions).until(
                    EC.element_to_be_clickable((By.XPATH, locator)))
            except Exception as e:
                self.log.info("Element not clickable " + locator)
                print_stack()
                raise e
        else:
            try:
                WebDriverWait(self.w, wait_time, poll_frequency, ignored_exceptions).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
            except Exception as e:
                self.log.info("Element not clickable " + locator)
                print_stack()
                raise e

    def is_element_present(self, locator, locatorType="css", element=None):
        try:
            if locator:
                element = self.get_element(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              "locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False