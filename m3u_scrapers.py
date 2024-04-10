import requests
import re


def hdplayers_getter(base_url):
    url = base_url + "&do=getVideo"
    hash = base_url.split("=")[1]

    r = requests.post(url, data={"hash": hash, "r": "https://www.wfilmizle.de" }, headers={"X-Requested-With": "XMLHttpRequest"})
    source_data = r.json()

    new_url = (source_data["videoSource"])
    r = requests.get(new_url)

    lines = r.text.split("\n")
    last_url = (lines[-1])

    r = requests.get(last_url, headers={"Accept": "*/*"})
    m3u_content = r.text

    return(m3u_content)

def videoseyredin_getter(url):
    video_id = url.split("/")[-1]
    m3u_url = "https://videoseyred.in/playlist/" + video_id + ".json"
    r = requests.get(m3u_url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}).json()
    final_url = r[0]["sources"][0]["file"]

    return(final_url)
    