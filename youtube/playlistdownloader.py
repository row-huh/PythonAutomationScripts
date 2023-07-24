from pytube import Playlist

p = Playlist("https://youtube.com/playlist?list=PLrolabKNtdOIrGLzdwcVVQkm1XgA-dZ4m")

print(f'Downloading: {p.title}')


for video in p.videos:
    try:    
        video.bypass_age_gate()
        video.streams().first().download()
        print("Downloaded Succesfully")
    except:
        print(f"something went wrong with {video.title}")
