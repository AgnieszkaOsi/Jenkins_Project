from page.base_page import BasePage
# from page.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePageLocators:
    """
    Home Page locators
    """
    MY_ACCOUNT_BUTTON = (By.CLASS_NAME, "nav__title")


class HomePage(BasePage):
    """
    Home Page object
    """
    def click_my_account(self):
        """
        Clicks log in link
        :return: LoginPage instance
        """
        # 1. Znajdź przycisk My account
        # 2. Kliknij w niego
        self.driver.find_element(*HomePageLocators.MY_ACCOUNT_BUTTON).click()
        # Zwróć stronę logowania
        # return LoginPage(self.driver)
