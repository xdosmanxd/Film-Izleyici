import json
import sys
from m3u_scrapers import *
from video_players import *

sys.stdout.reconfigure(encoding="utf-8")

def source_checker(url):
    pass


with open("data_with_sources.json", "r", encoding="utf-8") as file:
    data = json.load(file)

#Data with index numbers
new_data = {}


for index, movie in enumerate(data):
    new_data[f"#{index} {movie}"] = data[movie]

while True:
    x = input("What movie do you want watch: ")
    for i in new_data:
        if x in i or x.capitalize() in i:
            print(i)
    t = input("Do you see your movie in here? (y, n)")
    if t == "y":
        number = input("Please write the movie id (without the hashtag): ")
        is_available = False
        for movie in new_data:
            if movie.startswith(f"#{number}"):
                is_available = True
                will_watch = new_data[movie]

        if not is_available:
            print("Couldn't find a movie with that id please try again") 

        for index, source in enumerate(will_watch):
            print(f"#{index} {source}")

        index_wewant = int(input("Please select the source (without the hashtag): "))         
        
        source_wewant = (will_watch[list(will_watch)[index_wewant]])
        source_without_http = source_wewant.removeprefix("https://")

        if source_without_http.startswith("www.youtube.com") or source_without_http.startswith("www.vidmoly") or source_without_http.startswith("www.ok.ru") or source_without_http.startswith("www.odnoklassniki"):
            others_player(source_wewant)

        elif source_without_http.startswith("videoseyred"):
            final = videoseyredin_getter(source_wewant)
            others_player(final)

        else:
            final = hdplayers_getter(source_wewant)
            hdplayers_player(final)
