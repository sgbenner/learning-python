import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = os.environ.get("CHROME_DRIVER_PATH")

service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

url = "https://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
signup = driver.find_element(By.XPATH, '/html/body/form/button')

first_name.send_keys("Me")
last_name.send_keys("Myself")
email.send_keys("and@i.com")

time.sleep(1)


signup.click()

time.sleep(10)
