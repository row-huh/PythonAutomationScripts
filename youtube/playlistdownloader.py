from pytube import Playlist
from pytube import exceptions
import re
from moviepy.editor import AudioFileClip

def main():
    # ask the user if they want to download video or a playlist
    
    # if they say video then ask them for a video link
        # call a download video function
        
    
    # if they say playlist, ask them for a playlist link
        # call a download playlist function
    # 
    playlist_link = getPlaylistlink()
    p = Playlist(playlist_link)

        

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
        print(f"Some error occurred on {video.title}, moving on")




# convert to mp3
def convertToMp3(video):
    ...
    

    
if __name__ == "__main__":
    main()