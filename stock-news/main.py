import requests
import datetime
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

TODAY = datetime.date.today()
YESTERDAY = str(TODAY - datetime.timedelta(days=1))
DAY_BEFORE = str(TODAY - datetime.timedelta(days=2))


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_close_price_by_day(stock: str, day: str):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "interval": "5min",
        "apikey": os.environ.get("ALPHAVANTAGE_API_KEY")
    }

    url = "https://www.alphavantage.co/query"
    r = requests.get(url, params)
    r.raise_for_status()
    data = r.json()

    time_series_daily = data["Time Series (Daily)"]

    return float(time_series_daily[day]["4. close"])


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

def get_top_news_articles(company_name: str, n_articles: int):
    # GET https://newsapi.org/v2/everything?q=Apple&from=2023-07-21&sortBy=popularity&apiKey=API_KEY

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": company_name,
        "from": "2023-07-20",
        "sortBy": "popularity",
        "apiKey": os.environ.get("NEWS_API_KEY")
    }

    r = requests.get(url, params)
    r.raise_for_status()

    return r.json()["articles"][0:n_articles]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_ssms(text_message_body):
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


# Get stock price % calc difference
yesterday_close, day_before_close = get_close_price_by_day(STOCK, YESTERDAY), get_close_price_by_day(STOCK, DAY_BEFORE)
price_change_pct = round(((yesterday_close - day_before_close) / day_before_close) * 100, 1)

# get latest news articles
articles = get_top_news_articles(COMPANY_NAME, 3)

# send message w/ stock price update and latest news articles
ssms_message = f"{STOCK} {price_change_pct}%\n"

for article in articles:
    ssms_message += f"{article['title']}\nLink: {article['url']}\n"

print(ssms_message)

send_ssms(ssms_message)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
