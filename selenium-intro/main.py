from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

chrome_driver_path = os.environ.get("CHROME_DRIVER_PATH")

service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()

url = "https://www.python.org/"

driver = webdriver.Chrome(service=service, options=options)
driver.get(url)
# events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

events_list_item = events.find_elements(By.TAG_NAME, "li")

events_dict = {}

for index, event in enumerate(events_list_item):
    event_name = event.find_element(By.TAG_NAME, "a").text
    event_time = event.find_element(By.TAG_NAME, "time").text

    events_dict.update({
        index: {
            "time": event_time,
            "name": event_name
        }
    })

print(events_dict)
