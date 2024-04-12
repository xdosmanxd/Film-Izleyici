import vlc
import tempfile
import os

def hdplayers_player(m3u_content):
    # Create a temporary file to store M3U content
    with tempfile.NamedTemporaryFile(mode='w', delete=False,encoding="utf-8") as temp_file:
        temp_file.write(m3u_content)

    # Get the path of the temporary file
    m3u_file_path = temp_file.name

    os.system(f"mpv {m3u_file_path}")
    # Delete the temporary file
    temp_file.close()

def others_player(url):
    os.system(f"mpv {url}")
