from pytube import Playlist
from pytube import exceptions
import re

playlist_link = input("Enter playlist link: ")
p = Playlist(playlist_link)


print(f'********* Downloading: {p.title} ***********')


for video in p.videos:
    try:
        video.bypass_age_gate()
        video.streams.first().download('C:/Users/rohaa/Downloads')
        print("Downloaded Succesfully")
    except exceptions.AgeRestrictedError:
        print(f"Age restricted error on {video.title}, moving on")
    except:
        print("Error occurred way down bruh")
        

# checks if the user inputted string is a valid playlist string or not        
def isPlaylistvalid(link):
    regex = r"^(https://)?(www\.)?(youtube\.com|youtu\.be)/playlist\?list=([a-zA-Z0-0]+)"
    match = re.match(regex, link)
    if match:
        return True
    else:
        return False