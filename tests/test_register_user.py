import random

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


def test_register_user():
    service = webdriver.ChromeService()  # Mac
    driver = webdriver.Chrome(service=service)  # Mac

    random_number = random.randint(1000, 9999)
    unique_email = f"test{random_number}@test.pl"

    driver.get("http://seleniumdemo.com")
    driver.find_element(By.CLASS_NAME, "nav__title")
    driver.find_element(By.ID, "reg_email")
    driver.find_element(By.ID, "reg_password")
    driver.find_element(By.NAME, "register")


