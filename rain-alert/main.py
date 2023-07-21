import os
import requests
from datetime import datetime
from twilio.rest import Client

API_KEY = os.environ["weather_api_key"]
MY_LONG: float = os.environ["my_long"]
MY_LAT: float = os.environ["my_lat"]


def get_weather():
    params = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": API_KEY,
        "units": "imperial"
    }

    URL: str = "https://api.openweathermap.org/data/2.5/forecast"

    response = requests.get(url=URL, params=params)
    response.raise_for_status()

    results_json = response.json()

    return results_json["list"]


def get_24hr_forecast_description():
    weather_forecasts = get_weather()

    forecast_description: str = "24 Hr Forecast\n"

    for forecast in weather_forecasts[0:8]:
        # print(forecast)
        dt = forecast["dt"]
        timestamp = datetime.fromtimestamp(dt).time()
        main = forecast["main"]
        temp = main["temp"]
        feels_like = main["feels_like"]
        temp_min = main["temp_min"]
        temp_max = main["temp_max"]
        humidity = main["humidity"]
        weather_description = forecast["weather"][0]["description"]

        forecast_description += f"{timestamp}: temp: {temp_max} | feels like: {feels_like} | humidity: {humidity} | weather: {weather_description}\n"

    return forecast_description


def send_message(text_message_body):
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    from_phone_num = os.environ['TWILIO_FROM_PHONE_NUM']
    to_phone_num = os.environ['TO_PHONE_NUM']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=text_message_body,
        from_=from_phone_num,
        to=to_phone_num
    )

    print(message.status)


forecast = get_24hr_forecast_description()

send_message(forecast)
