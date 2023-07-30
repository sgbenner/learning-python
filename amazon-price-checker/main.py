import requests
from bs4 import BeautifulSoup

with open("item_urls.txt", "r") as file:
    urls_to_check = file.readlines()

def get_amazon_product_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-ch-ua-platform": "macOS",
        "Accept-Encoding": "gzip, deflate, br"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_title = soup.find(id="productTitle")

    price_whole_html = soup.find("span", class_="a-price-whole")
    price_fraction_html = soup.find("span", class_="a-price-fraction")

    item_title = str(product_title.text).strip()
    price = price_whole_html.text + price_fraction_html.text

    return item_title, price


for url in urls_to_check:
    item_title, price = get_amazon_product_price(url)

    print(item_title)
    print(price)

