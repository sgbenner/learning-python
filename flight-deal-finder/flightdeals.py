import requests
import os

SHEETY_URL = os.environ.get("SHEETY_URL")


class FlightDeal:
    def __init__(self, id, city, iata_code, current_price, lowest_price):
        self.id = id
        self.city = city
        self.iata_code = iata_code
        self.current_price = current_price
        self.lowest_price = lowest_price

    def update(self):
        url = f"{SHEETY_URL}/{self.id}"

        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "price": {
                "currentPrice": self.current_price
            }
        }

        response = requests.put(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()


class FlightDeals:
    def __init__(self):
        self.deals = self.get()

    def get(self):
        response = requests.get(SHEETY_URL)
        response.raise_for_status()

        flight_deals = []

        for city in response.json()["prices"]:
            city_dict = dict(city)

            id = city_dict.get("id")
            city = city_dict.get("city")
            iata_code = city_dict.get("iataCode")
            current_price = city_dict.get("currentPrice")
            lowest_price = city_dict.get("lowestPrice")

            flight_deal = FlightDeal(id, city, iata_code, current_price, lowest_price)

            flight_deals.append(flight_deal)

        return flight_deals
