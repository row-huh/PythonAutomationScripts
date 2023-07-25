from pytube import Playlist
from pytube import exceptions
import re
from moviepy.editor import AudioFileClip

def main():
    # ask the user if they want to download video or a playlist
    choice = input("Enter the number adjacent to: \n[1] Download a YouTube video\n[2] Download a YouTube playlist\nEnter: ")
    while choice != "1" and choice != "2":
        choice = input("\n\nInvalid choice!!\n[1] Download a YouTube video\n[2] Download a YouTube playlist\nEnter: ")
        
    if choice == "1":
        ...     # call youtube downloader
    elif choice == "2":
        ...     # call playlist downloader
        

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