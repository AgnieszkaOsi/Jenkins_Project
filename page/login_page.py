from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginpageLocators:
    REG_EMAIL_OF_USER = (By.ID, "reg_email")
    REG_PASSWORD_OF_A_USER = (By.ID, "reg_password")
    REG_BUTTON = (By.NAME, "register")

    NAME_OF_USER = (By.ID, "username")
    PASSWORD_OF_A_USER = (By.ID, "username")
    LOG_IN_BUTTON = (By.NAME, "login")



class RegPage(BasePage):
    def enter_reg_email(self, email):
        self.driver.find_element(*LoginpageLocators.REG_EMAIL_OF_USER).send_keys(email)

    def enter_reg_password(self, password):
        self.driver.find_element(*LoginpageLocators.REG_PASSWORD_OF_A_USER).send_keys(password)

    def click_reg_button(self):
        self.driver.find_element(*LoginpageLocators.REG_BUTTON).click()




class LoginPage(BasePage):
    """
    Login Page object
    """
    def enter_username(self, username):
        """
        Enters username
        :param username:
        """
        el = self.driver.find_element(*LoginpageLocators.NAME_OF_USER)
        el.send_keys(username)


    def enter_password(self, password):
        """
        Enters password
        :param password:
        """
        self.driver.find_element(*LoginpageLocators.PASSWORD_OF_A_USER).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginpageLocators.LOG_IN_BUTTON).click()

