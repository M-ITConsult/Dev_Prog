from pydub import AudioSegment
import os
# Replace 'Mp3' with others by example 'Webm'
# function to convert Mp3 files to Wav
def audiofiles_to_wav(file):
    # open the audio files using Pydub
    sound = AudioSegment.from_file(file, format='webm')
# 	sound = AudioSegment.from_file(file, format='mp3')

    # create a new file name for the Wav file
    wav_file = os.path.splitext(file)[0] + '.wav'

    # save the Wav file using Pytdub
    sound.export(wav_file, format='wav')

# prompt user for input directory and output directory
input_dir = input('Enter the directory containing the audio files: ')
output_dir = input('Enter the directory where you want to save the Wav files: ')

# get a list of all the audio files in the input directory
# audio_files = [f for f in os.listdir(input_dir) if f.endswith('.mp3')]
audio_files = [f for f in os.listdir(input_dir) if f.endswith('.webm')]

# convert each WAV file to MP3 and save in the output directory
for file in audio_files:
    audio_file_path = os.path.join(input_dir, file)
    audiofiles_to_wav(audio_file_path)

print("Conversion complete!")