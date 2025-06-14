from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert


class BasePage:
    """
    Base class for each page
    """
    def __init__(self, driver):
        # service = webdriver.ChromeService(executable_path="/usr/bin/chromedriver")
        self.driver = driver
        self.wait_5s = WebDriverWait(self.driver, 5)
        self.alert = Alert(self.driver)
        self._verify_page()

    def _verify_page(self):
        return