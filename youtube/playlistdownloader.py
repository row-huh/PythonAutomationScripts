from pytube import Playlist, YouTube
from pytube import exceptions
import re
from moviepy.editor import AudioFileClip
import subprocess



# main function
def main():
    # ask the user if they want to download video or a playlist
    choice = input("Enter the number adjacent to: \n[1] Download a YouTube video\n[2] Download a YouTube playlist\nEnter: ")
    while choice != "1" and choice != "2":
        choice = input("\n\nInvalid choice!!\n[1] Download a YouTube video\n[2] Download a YouTube playlist\nEnter: ")
        
    if choice == "1":
        v = getVideolink()
        download_video(v)
    elif choice == "2":
        p = getPlaylistlink()
        downloadPlaylist(p)
        



# checks if the user inputted string is a valid playlist string or not        
def getPlaylistlink():
    link = input("Enter Playlist link: ")
    regex = r"^(https://)?(www\.)?(youtube\.com|youtu\.be)/playlist\?list=([a-zA-Z0-0]+)"
    match = re.match(regex, link)
    while not match:
        link = input("Invalid link, Enter again: ")
        match = re.match(regex, link)
    return link




def downloadPlaylist(playlistlink):
    p = Playlist(playlistlink)
    
    for video in p.videos:
        download_video(video.watch_url)
        


    

def download_video(videolink):
    video = YouTube (
        videolink,
        use_oauth=True,
        allow_oauth_cache=True
    )
    video.streams.first().download("C:/Users/rohaa/Downloads")



def getVideolink():
    link = input("Enter Video link: ")
    regex = r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/(watch\?v=)?([a-zA-Z0-9_-]+)"
    match = re.match(regex, link)
    while not match:
        link = input("Invalid link, Enter again: ")
        match = re.match(regex, link)
    return link
    
    
# convert to mp3
def convertToMp3(video):
    ...
    

    
if __name__ == "__main__":
    main()
