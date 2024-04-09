import requests
import json
from bs4 import BeautifulSoup

base_url = "https://www.wfilmizle.de/wfilmizle-film-arsivi/page/"
movie_list = {}

for i in range(1, 357):
    url = base_url + str(i) + "/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="lxml")
    movies = soup.find_all("span", class_="movie-title")

    for i in movies:
        title = i.find("a")["title"]
        movie_list[title] = i.find("a")["href"]

with open("initial_data.json", "w", encoding="utf-8") as file:
    json.dump(movie_list, file, indent=4, ensure_ascii=False)
