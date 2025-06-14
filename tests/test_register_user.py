import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time



def test_register_user():
    service = Service()  # Mac
    driver = webdriver.Chrome(service=service)  # Mac

    random_number = random.randint(1000, 9999)
    unique_email = f"test{random_number}@test.pl"

    driver.get("http://seleniumdemo.com")

    driver.find_element(By.XPATH, '//*[@id="menu-item-22"]/a').click()
    time.sleep(2)

    driver.find_element(By.ID, "reg_email").send_keys(unique_email)
    driver.find_element(By.ID, "reg_password").send_keys("somePassword243%&")
    driver.find_element(By.NAME, "register").click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "entry-header-inner")


