from pydub import AudioSegment
import os

# function to convert Webm files to Wav
def webm_to_wav(file):
    # open the Webm file using Pydub
    sound = AudioSegment.from_file(file, format='webm')

    # create a new file name for the Wav file
    wav_file = os.path.splitext(file)[0] + '.wav'

    # save the Wav file using Pytdub
    sound.export(wav_file, format='wav')

# prompt user for input directory and output directory
input_dir = input('Enter the directory containing the Webm files: ')
output_dir = input('Enter the directory where you want to save the Wav files: ')

# get a list of all the WAV files in the input directory
webm_files = [f for f in os.listdir(input_dir) if f.endswith('.webm')]

# convert each WAV file to MP3 and save in the output directory
for file in webm_files:
    webm_file_path = os.path.join(input_dir, file)
    webm_to_wav(webm_file_path)

print("Conversion complete!")