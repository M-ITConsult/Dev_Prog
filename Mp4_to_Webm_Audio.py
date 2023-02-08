from pydub import AudioSegment

# Load MP4 file
mp4_file = AudioSegment.from_file(str(input('File name .mp4: ')), format="mp4")

# Export as WebM audio
mp4_file.export(str(input('File name .webm: ')), format="webm", codec="libvorbis")