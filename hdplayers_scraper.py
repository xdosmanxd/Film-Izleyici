import requests

def source_getter(base_url):
    url = base_url + "&do=getVideo"
    hash = base_url.split("=")[1]

    r = requests.post(url, data={"hash": hash, "r": "https://www.wfilmizle.de" }, headers={"X-Requested-With": "XMLHttpRequest"})
    source_data = r.json()

    new_url = (source_data["videoSource"])
    r = requests.get(new_url)

    lines = r.text.split("\n")
    last_url = (lines[-1])

    r = requests.get(last_url, headers={"Accept": "*/*"})
    m3u_file = r.text

    return(m3u_file)