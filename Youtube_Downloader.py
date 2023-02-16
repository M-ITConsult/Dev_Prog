# Pytube doc
# https://pytube.io/en/latest/user/streams.html#filtering-for-mp4-streams

from pytube import YouTube
print('1. Video')
print('2. Audio')
choice = int(input('Select your choice: '))

if (choice == 1):
    link = str(input('Link: '))
    yt = YouTube(link)
    streams = yt.streams
    stream = yt.streams.get_by_itag(22) # The itag 22 = .mp4 720p founded into the pytube doc
    stream.download()

if (choice == 2):
    link = str(input('Link: '))
    yt = YouTube(link)
    stream = yt.streams.get_by_itag(251) # The itag 251 = .webm founded into the pytube doc
    stream.download()