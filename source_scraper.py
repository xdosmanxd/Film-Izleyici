import requests
import json
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')
new_data = {}


with open("initial_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="lxml")
    return soup

for movie_name in data:
    url = data[movie_name]
    soup = get_soup(url)
    new_data[movie_name] = {}
    sources = soup.find("div", {"id": "action-parts"}).find_all("span")
    
    if len(sources) == 0:
        try:
            video_link = soup.find("iframe")["src"]
            new_data[movie_name]["In-Site"] = video_link 
        except:
            print(f"Couldn't find a video source for {movie_name} in {url}")    
            
    else:
        try:
            i = 1
            for source in sources:
                modified_url = url + str(i)
                soup = get_soup(modified_url)     
                video_link = soup.find("iframe")["src"]
                new_data[movie_name][source.text] = video_link
                i += 1
        except:
            print(f"Couldn't find a video source for {movie_name} in {url}")

with open("data_with_sources.json", "w", encoding="utf-8") as file:
    json.dump(new_data, file, indent=4, ensure_ascii=False)