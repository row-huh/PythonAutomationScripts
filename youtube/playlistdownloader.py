import re
import subprocess



# main function
def main():
    # ask the user if they want to download video or a playlist
    choice = input("Enter the number adjacent to: \n[1] MP3\n[2] MP4\nEnter: ")
    while choice != "1" and choice != "2":
        choice = input("Enter the number adjacent to: \n[1] MP3\n[2] MP4\nEnter: ")
    
    link = getLink()
    if choice == "1":
        downloadMP3(link)
    elif choice == "2":
        downloadMP4(link)        
 

# checks if the user inputted string is a valid playlist string or not        
def getLink():
    link = input("Enter Playlist link: ")
    regex = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/(watch\?v=|playlist\?list=)([a-zA-Z0-9_-]+)'
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