import time
import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = os.environ.get("CHROME_DRIVER_PATH")

service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

url = "https://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(service=service, options=options)
driver.get(url)


def get_best_available_item():
    items = driver.find_element(By.ID, "store").find_elements(By.TAG_NAME, "div")

    available_items_list = []

    print(len(items))

    for item in items:
        # item_name_tag = item.find_element(By.TAG_NAME, "b").text
        available = True if str(item.get_attribute("class")).strip() == "" else False
        # item_name_desc_split = item_name_tag.split(" - ")

        # if len(item_name_desc_split) == 2:
        #     item_name = item_name_desc_split[0]
        #     cost = item_name_desc_split[1]

        if available:
            # available_items_list.append([item, item_name, available, cost])
            available_items_list.append([item, available])

    if len(available_items_list) != 0:
        # return available_items_list[-1]  # return the last item that's available
        return available_items_list[-1]  # return the last item that's available

    else:
        return None


# get the cookie to click on it
cookie = driver.find_element(By.ID, "cookie")

five_second_start = datetime.now()

while True:
    cookie.click()

    if (datetime.now() - five_second_start).total_seconds() >= 120:
        five_second_start = datetime.now()
        best_avail_item = get_best_available_item()

        if best_avail_item is not None:
            # print(f"Clicking item: {best_avail_item[1]}")
            best_avail_item[0].click()

