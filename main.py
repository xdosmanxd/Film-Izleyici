from m3u_scrapers import *
from video_players import *

url1 = "https://hdplayersystem.live/player/index.php?data=a1d7311f2a312426d710e1c617fcbc8c"
url2 = "https://vidmoly.to/embed-l7ha3gxw0iy0.html"
url3 = "https://www.youtube.com/embed/JJ7Jkx5Koqs"
url4 = "https://ok.ru/videoembed/3060596542006"
url5 = "https://videoseyred.in/embed/380205?hideTitle=1"

x = hdplayers_getter(url1)
hdplayers_player(x)