import tempfile
import os

def hdplayers_player(m3u_content):
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding="utf-8") as temp_file:
        temp_file.write(m3u_content)
   
    m3u_file_path = temp_file.name
    os.system(f"mpv {m3u_file_path}")

    temp_file.close()

def others_player(url):
    os.system(f"mpv {url}")
