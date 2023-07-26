from datetime import datetime, timedelta
from flightdeals import FlightDeals, FlightDeal
from priceChecker import get_prices
import os

FLY_FROM = os.environ.get("FLY_FROM")

today = datetime.today()

DATE_FROM = (today + timedelta(days=7)).strftime("%d/%m/%Y")
DATE_TO = (today + timedelta(days=180)).strftime("%d/%m/%Y")
NIGHTS_IN_DST_FROM = 4
NIGHTS_IN_DST_TO = 7
RESULTS_LIMIT = 5

flight_deals = FlightDeals().deals

for row in flight_deals:
    iata_code = row.iata_code
    lowest_price = row.lowest_price

    print(iata_code, lowest_price)

    flight_prices = get_prices(fly_from=FLY_FROM, fly_to=iata_code, date_from=DATE_FROM, date_to=DATE_TO,
                               price_to=lowest_price, nights_in_dst_from=NIGHTS_IN_DST_FROM,
                               nights_in_dst_to=NIGHTS_IN_DST_TO)

    if len(flight_prices) == 0:
        row.current_price = "No flights found"
    else:
        # update with the first price returned
        row.current_price = flight_prices[0].price

    # update row
    row.update()
