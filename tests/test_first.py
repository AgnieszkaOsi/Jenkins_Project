import unittest
from selenium import webdriver
from page.home_page import HomePage
from page.login_page import LoginPage, RegPage
from page.login_page import LoginpageLocators


def test_setup():
    service = webdriver.ChromeService()  # Mac
    driver = webdriver.Chrome(service=service)  # Mac
    driver.maximize_window()
    driver.get("http://seleniumdemo.com")
    home_page = HomePage(driver)
    login_page = RegPage(driver)
    # login_page = LoginPage(driver)



def tearDown(self):
         self.driver.quit()