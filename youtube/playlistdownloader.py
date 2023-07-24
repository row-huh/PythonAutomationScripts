from pytube import Playlist
from pytube import exceptions


playlist_link = input("Enter playlist link: ")

p = Playlist(playlist_link)

print(f'Downloading: {p.title}')


for video in p.videos:
    try:
        video.bypass_age_gate()
        video.streams.first().download('C:/Users/rohaa/Downloads')
        print("Downloaded Succesfully")
    except exceptions.AgeRestrictedError:
        print(f"Age restricted error on {video.title}, moving on")
        
