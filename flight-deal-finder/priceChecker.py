import os
import requests

RESULTS_LIMIT = 5

API_KEY = os.environ.get("API_KEY")


class FlightResult():
    def __init__(self, id, nights_in_destination, price):
        self.id = id
        self.nights_in_destination = nights_in_destination
        self.price = price


def get_prices(fly_from, fly_to, date_from, date_to, price_to, nights_in_dst_from, nights_in_dst_to):
    url = "https://api.tequila.kiwi.com/v2/search"
    params = {
        "fly_from": fly_from,
        "fly_to": fly_to,
        "date_from": date_from,
        "date_to": date_to,
        "curr": "USD",
        "price_to": price_to,
        "nights_in_dst_from": nights_in_dst_from,
        "nights_in_dst_to": nights_in_dst_to,
        "limit": RESULTS_LIMIT
    }

    headers = {
        "apikey": API_KEY,
        "accept": "application/json"
    }

    response = requests.get(url=url, params=params, headers=headers)
    response.raise_for_status()

    flights = response.json()["data"]
    flight_results = []

    for flight in flights:
        flight_results.append(FlightResult(flight["id"], flight["nightsInDest"], flight["price"]))

    return flight_results
