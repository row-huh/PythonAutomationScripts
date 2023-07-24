from pytube import Playlist

p = Playlist("https://youtube.com/playlist?list=PLrolabKNtdOIrGLzdwcVVQkm1XgA-dZ4m")

print(f'Downloading: {p.title}')


for video in p.videos:
    video.bypass_age_gate()
    video.streams().first().download()
