from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":

    website = requests.get("https://news.ycombinator.com/")
    soup = BeautifulSoup(website.content, 'html.parser')

    links = soup.find_all(class_="athing")
    subtexts = soup.find_all(class_="subtext")

    results = []

    for index, link in enumerate(links):
        # link_url = link.find("a")
        titleline = link.find(class_="titleline")
        title = titleline.text
        url = titleline.select_one("a").get("href")

        subtext = subtexts[index]
        scores = subtext.find_all(class_="score")

        if scores:
            score = str(scores[0].text).replace(" points", "")
        else:
            score = "0"

        results.append({
            "title": title,
            "url": url,
            "score": score
        })

    print(results[0]["title"])
