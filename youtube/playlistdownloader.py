from pytube import Playlist
from pytube import exceptions
import re
from moviepy.editor import AudioFileClip

def main():
    playlist_link = getPlaylistlink()
    p = Playlist(playlist_link)


    print(f'********* Downloading: {p.title} ***********')


    for video in p.videos:
        ...
        

# checks if the user inputted string is a valid playlist string or not        
def getPlaylistlink():
    link = input("Enter Playlist link: ")
    regex = r"^(https://)?(www\.)?(youtube\.com|youtu\.be)/playlist\?list=([a-zA-Z0-0]+)"
    match = re.match(regex, link)
    while not match:
        link = input("Invalid link, Enter again: ")
        match = re.match(regex, link)
    return link


def download_video(video):
    try:
            video.bypass_age_gate()
            video.streams.first().download('C:/Users/rohaa/Downloads')
            print("Downloaded Succesfully")
    except exceptions.AgeRestrictedError:
        print(f"Age restricted error on {video.title}, moving on")
    except:
        print("Error occurred way down bruh")




# convert to mp3
def convertToMp3(video):
    ...
    
    
    
    
    
if __name__ == "__main__":
    main()