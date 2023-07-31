import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = os.environ.get("CHROME_DRIVER_PATH")

service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

url = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome(service=service, options=options)
driver.get(url)

search = driver.find_element(By.NAME, 'search')
search.send_keys("Python ")
time.sleep(1)
search.send_keys(Keys.ENTER)
