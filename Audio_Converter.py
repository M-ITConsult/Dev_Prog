from pydub import AudioSegment

# open the webm file
webm_file = AudioSegment.from_file(str(input('File name .webm: ')), format='webm')

print('1. Convert to .wav')
print('2. Convert to .mp3')
choice = int(input('Select your choice: '))

if (choice == 1):
    # Save the wav file
    webm_file.export(str(input('File name .wav: ')), format='wav')

if (choice == 2):
    # Save the mp3 file
    webm_file.export(str(input('File name .mp3: ')), format='mp3')