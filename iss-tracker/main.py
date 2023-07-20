import time
import os
import requests
from datetime import datetime
from smtplib import SMTP

MY_LAT = float(os.environ["my_lat"])  # Your latitude
MY_LONG = float(os.environ["my_long"])  # Your longitude
FROM_EMAIL = os.environ["from_email"]
TO_EMAIL = os.environ["to_email"]
MY_PASSWORD = os.environ["my_password"]

SLEEP_TIME = 60

def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_latitude, iss_longitude)

    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True

    return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if sunset < hour_now < sunrise:
        print("Its dark...")
        return True

    return False


def send_email():
    with SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Look up!\n\nThe ISS is nearby..."
        )


while True:

    time_now = datetime.utcnow()
    hour_now = time_now.hour

    # if ISS is close
    if is_iss_close():
        print(f"{time_now} -- Its close...")
        if is_dark():
            print(f"{time_now} - Its close and its dark...")
            send_email()

    time.sleep(SLEEP_TIME)
