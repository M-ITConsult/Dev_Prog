'''Download link list'''
# Pytube doc
# https://pytube.io/en/latest/user/streams.html#filtering-for-mp4-streams

from pytube import YouTube
import csv

' Many Links '

links = []
with open('links.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        links.append(row[0])

for link in links:
    try:
        yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        stream = yt.streams.get_by_itag(251) # The itag 251 = .webm founded into the pytube doc
        stream.download()
    except:
        print(f'Error downloading {link}')
