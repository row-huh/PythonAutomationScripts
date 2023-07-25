import re
import subprocess



# main function
def main():
    # ask the user if they want to download video or a playlist
    choice = input("Enter the number adjacent to: \n[1] MP3\n[2] MP4\nEnter: ")
    while choice != "1" and choice != "2":
        choice = input("\n\nInvalid choice!!\n[1] Download a YouTube video\n[2] Download a YouTube playlist\nEnter: ")
    if choice == "1":
        
    elif choice == "2":
        ...        
 



# checks if the user inputted string is a valid playlist string or not        
def getPlaylistlink():
    link = input("Enter Playlist link: ")
    regex1 = r"^(https://)?(www\.)?(youtube\.com|youtu\.be)/playlist\?list=([a-zA-Z0-0]+)"
    regex2 = r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/(watch\?v=)?([a-zA-Z0-9_-]+)"
    match = re.match(regex1, link)
    while not match:
        link = input("Invalid link, Enter again: ")
        match = re.match(regex, link)
    return link



def getVideolink():
    link = input("Enter Video link: ")
    regex = 
    match = re.match(regex, link)
    while not match:
        link = input("Invalid link, Enter again: ")
        match = re.match(regex, link)
    return link
    
    

def downloadMP3(link):
    subprocess.run(['youtube-dl', '--extract-audio', '--audio-format', 'mp3', link])
    
    
def downloadMP4(link):
    subprocess.run(['youtube-dl', link])

if __name__ == "__main__":
    main()