from pydub import AudioSegment

# open the webm file
print('1. Webm')
print('2. Mp4')
choice = int(input('Make your choice: '))

if (choice == 1):
    webm_file = AudioSegment.from_file(str(input('File name .webm: ')), format='webm')

if (choice == 2):
    mp4_file = AudioSegment.from_file(str(input('File name .mp4: ')), format='mp4')


print('1. Convert to .wav')
print('2. Convert to .mp3')
choice = int(input('Make your choice: '))

if (choice == 1):
    # Save the wav file
    webm_file.export(str(input('File name .wav: ')), format='wav')

if (choice == 2):
    # Save the mp3 file
    webm_file.export(str(input('File name .mp3: ')), format='mp3')