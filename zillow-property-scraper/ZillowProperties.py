from bs4 import BeautifulSoup
import requests
from fake_headers import Headers

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.44127939556881%2C%22east%22%3A-122.05401132916256%2C%22south%22%3A37.68725355211447%2C%22north%22%3A37.91701919813141%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"


class ZillowProperties():
    def __init__(self):
        self.properties_for_rent = self.get_properties()

    def get_properties(self):
        headers = {
            "Content-Type": "text/html;charset=UTF-8",
            "Transfer-Encoding": "chunked",
            "connection": "closed",
            "Server": "Apache-Coyote/1.1",
            "X-Internal-Host": "030",
            "Cache-Control": "no-cache",
            "X-Frame-Options": "deny",
            "Vary": "Accept-Encoding",
            "Z-Using-Act": "2",
            "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US;en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }

        response = requests.get(ZILLOW_URL, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        listing_result = soup.select_one("#grid-search-results").find("ul")

        listings = listing_result.select("li")

        for_rent_properties = []

        for listing in listings:
            link = listing.find("a", href=True)
            address = listing.find("address")
            price = listing.find("span")

            if link and address and price:
                link_url = f"https://www.zillow.com{link['href']}"

                for_rent_properties.append({"link": link_url, "address": address.text, "price": price.text})

        return for_rent_properties
