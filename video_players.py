import vlc
import tempfile
import os

def hdplayers_player(m3u_content):
    # Create a temporary file to store M3U content
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(m3u_content)

    # Get the path of the temporary file
    m3u_file_path = temp_file.name

    # Creating VLC instance
    vlc_instance = vlc.Instance('--input-repeat=-1', '--fullscreen', '--intf', 'skins2')

    # Creating media list player
    media_list_player = vlc_instance.media_list_player_new()

    # Creating media list
    media_list = vlc_instance.media_list_new([m3u_file_path])

    # Setting media list to media list player
    media_list_player.set_media_list(media_list)

    # Start playing
    media_list_player.play()

    # Loop to keep the script running while the media is playing
    while True:
        try:
            continue
        except KeyboardInterrupt:
            media_list_player.stop()
            break

    # Delete the temporary file
    temp_file.close()

def vidmoly_player(url):
    os.system(f'mpv "{url}" --http-header-fields="Referer: vidmoly.to"')

def youtube_okru_videoseyredin_player(url):
    os.system(f"mpv {url}")
