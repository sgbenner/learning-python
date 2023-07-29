import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

soup = BeautifulSoup(response.content, features="html.parser")

movies = soup.select("h3")

movies_list = [n.text for n in reversed(movies)]

movies_df = pd.DataFrame(movies_list)

movies_df.to_csv("movies.txt")

# for movie in reversed(movies):
#     print(movie.text)
