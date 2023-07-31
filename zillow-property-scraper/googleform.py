import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = os.environ.get("CHROME_DRIVER_PATH")
GOOGLE_SHEET_URL = os.environ.get("GOOGLE_SHEET_URL")

service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()

class GoogleForm():
    def __init__(self, address, price_per_month, link_to_property):
        self.address = address
        self.price_per_month = price_per_month
        self.link_to_property = link_to_property


    def upload(self):
        #TODO: Use selenium to input data on form
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(GOOGLE_SHEET_URL)

        time.sleep(2)

        # get fields
        address_text_box = driver.find_element(By.XPATH,         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_per_month_text_box = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_text_box = driver.find_element(By.XPATH,            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

        # input data
        address_text_box.send_keys(self.address)
        price_per_month_text_box.send_keys(self.price_per_month)
        link_text_box.send_keys(self.link_to_property)

        time.sleep(.5)

        # click submit
        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_button.click()

        time.sleep(.5)
