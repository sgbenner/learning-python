import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = set()
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and not href.startswith('#'):  # Exclude anchor links
            absolute_url = urljoin(url, href)
            links.add(absolute_url)

    return links

def scrape_all_links(url):
    all_links = set()
    visited_links = set()
    queue = [url]

    while queue:
        current_url = queue.pop(0)
        if current_url in visited_links:
            continue

        visited_links.add(current_url)
        links = get_links(current_url)
        all_links.update(links)

        queue.extend(links - visited_links)

    return all_links

if __name__ == "__main__":
    base_url = "https://books.toscrape.com/"
    all_links = scrape_all_links(base_url)

    # Write links to a CSV file
    with open('all_links.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Links"])
        for link in all_links:
            csv_writer.writerow([link])

    print("All Links have been written to all_links.csv file.")
